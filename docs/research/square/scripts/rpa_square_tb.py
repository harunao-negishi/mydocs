"""
RPA charge/spin susceptibilities and a simple self-energy-dressed Green's function (static V) for 2D square TB.

Model: eps(k) = -2 t (cos kx + cos ky), a=1, t=1; Hubbard U > 0 (onsite).
Use precomputed Lindhard chi0 via the same grid; compute static chi_s(q,0) and chi_c(q,0):
  chi_s = chi0 / (1 - U * chi0)
  chi_c = chi0 / (1 + U * chi0)
Estimate Ucrit = 1 / max_q chi0(q,0) at given (mu,T) for spin channel (divergence threshold at q*).
Also compare G0(k,iω0) and a dressed G(k,iω0) with a static RPA potential V_eff = U^2 * chi_s(q*,0) (toy, momentum-averaged),
by adding a simple local static Σ ≈ Σ0 = V_eff * n (n from half-filling here -> set Σ0 phenomenologically).
This is illustrative rather than a conserving approximation; purpose: contrast lineshapes.

Outputs:
  - ../figs/chi_s_static_heatmap.png
  - ../figs/chi_c_static_heatmap.png
  - ../figs/chi_s_Uscan.png
  - ../figs/g0_vs_grpa_matsubara.png
"""
from __future__ import annotations

from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

# --- Config ---
CFG = {
    "t": 1.0,
    "Nk": 81,
    "T": 0.05,
    "mu": 0.0,
    "g_s": 2.0,
    "U": 0.8,           # choose U below Ucrit (we'll estimate)
    "eta": 0.05,        # small imaginary part for plots (if needed)
    "dpi": 110,
    "figsize_hm": (4.8, 4.2),
    "figsize_row": (8.8, 3.2),
}


def eps_k(kx: np.ndarray, ky: np.ndarray, t: float) -> np.ndarray:
    return -2.0 * t * (np.cos(kx) + np.cos(ky))


def fermi(x: np.ndarray, T: float) -> np.ndarray:
    T = max(T, 1e-12)
    y = np.clip(x / T, -60.0, 60.0)
    return 1.0 / (np.exp(y) + 1.0)


def fermi_deriv(x: np.ndarray, T: float) -> np.ndarray:
    T = max(T, 1e-12)
    y = np.clip(x / (2.0 * T), -60.0, 60.0)
    sech2 = 1.0 / (np.cosh(y) ** 2)
    return -0.25 / T * sech2


def make_k_grid(Nk: int):
    k = np.linspace(-np.pi, np.pi, Nk, endpoint=False)
    KX, KY = np.meshgrid(k, k, indexing="xy")
    return k, KX, KY


def chi0_static_map(Nk: int, T: float, mu: float, t: float, g_s: float) -> np.ndarray:
    # Lindhard static map with derivative fix at dE=0
    _, KX, KY = make_k_grid(Nk)
    Ek = eps_k(KX, KY, t)
    fk = fermi(Ek - mu, T)

    chi = np.zeros((Nk, Nk), dtype=np.float64)
    for iqx in range(Nk):
        for iqy in range(Nk):
            Ekq = np.roll(np.roll(Ek, shift=iqx, axis=0), shift=iqy, axis=1)
            fkq = np.roll(np.roll(fk, shift=iqx, axis=0), shift=iqy, axis=1)
            dE = Ekq - Ek
            num = fk - fkq
            mask = np.abs(dE) < 1e-10
            denom = -dE
            integrand = np.zeros_like(denom, dtype=np.float64)
            safe = ~mask
            integrand[safe] = (num[safe] / denom[safe]).real
            integrand[mask] = -fermi_deriv(Ek[mask] - mu, T)
            chi[iqx, iqy] = integrand.sum() * (g_s / (Nk * Nk))

    return np.fft.fftshift(chi)


def heatmap(ax, Z: np.ndarray, title: str, vmax_pct: float = 98.0):
    vmin, vmax = np.min(Z), np.percentile(Z, vmax_pct)
    im = ax.imshow(
        Z,
        origin="lower",
        extent=[-np.pi, np.pi, -np.pi, np.pi],
        cmap="inferno",
        vmin=vmin,
        vmax=vmax,
        interpolation="nearest",
        aspect="equal",
    )
    ax.set_xlabel(r"$q_x a$")
    ax.set_ylabel(r"$q_y a$")
    ax.set_xticks([-np.pi, 0.0, np.pi], labels=[r"$-\pi$", r"$0$", r"$\pi$"])
    ax.set_yticks([-np.pi, 0.0, np.pi], labels=[r"$-\pi$", r"$0$", r"$\pi$"])
    ax.set_title(title)
    return im


def estimate_Ucrit(chi0_shifted: np.ndarray) -> float:
    # chi_s diverges when 1 - U * max(chi0) = 0 -> Ucrit = 1/max(chi0)
    chi0_max = np.max(chi0_shifted)
    if chi0_max <= 0:
        return np.inf
    return 1.0 / chi0_max


def compute_chi_s_c(chi0_shifted: np.ndarray, U: float):
    chi_s = chi0_shifted / (1.0 - U * chi0_shifted)
    chi_c = chi0_shifted / (1.0 + U * chi0_shifted)
    return chi_s, chi_c


def matsubara_g0_vs_grpa_plot(Nk: int, T: float, mu: float, t: float, U: float, chi_s_shifted: np.ndarray, outpath):
    # Compare |G0(k, iω0)| vs |G(k, iω0)| with a toy static local self-energy Σ0.
    # Take Σ0 = alpha * U^2 * max_q chi_s(q,0), with small alpha to avoid overbroadening.
    alpha = 0.2
    Sigma0 = alpha * (U ** 2) * np.max(chi_s_shifted)

    # ω0 = πT, fermionic
    w0 = np.pi * T
    _, KX, KY = make_k_grid(Nk)
    Ek = eps_k(KX, KY, t)

    G0_abs = 1.0 / np.sqrt((w0) ** 2 + (Ek - mu) ** 2)
    G_abs = 1.0 / np.sqrt((w0) ** 2 + (Ek - (mu + Sigma0)) ** 2)

    # Show as two panels (G0, G) at ω0
    fig, axes = plt.subplots(1, 2, figsize=(8.8, 3.2), dpi=CFG["dpi"], constrained_layout=True)
    im1 = heatmap(axes[0], np.fft.fftshift(G0_abs), title=r"$|G_0(\mathbf{k}, i\omega_0)|$")
    im2 = heatmap(axes[1], np.fft.fftshift(G_abs), title=r"$|G_{\rm RPA}(\mathbf{k}, i\omega_0)|$ (static $\Sigma$)")
    fig.colorbar(im1, ax=axes[0], shrink=0.9, pad=0.02)
    fig.colorbar(im2, ax=axes[1], shrink=0.9, pad=0.02)
    fig.savefig(outpath, bbox_inches="tight")
    print("Saved:", outpath)


def main():
    Nk = CFG["Nk"]
    T = CFG["T"]
    mu = CFG["mu"]
    t = CFG["t"]
    g_s = CFG["g_s"]
    U = CFG["U"]

    figs_dir = Path(__file__).resolve().parent.parent / "figs"
    figs_dir.mkdir(parents=True, exist_ok=True)

    # chi0 (static)
    chi0 = chi0_static_map(Nk, T, mu, t, g_s)

    # Estimate Ucrit and ensure U below it for plotting
    Ucrit = estimate_Ucrit(chi0)
    print(f"Estimated Ucrit ~ {Ucrit:.3f} at (mu={mu}, T={T})")
    if not np.isinf(Ucrit) and U >= Ucrit:
        U = 0.9 * Ucrit
        print(f"Adjusted U -> {U:.3f} (< Ucrit) for stable RPA plots")

    # chi_s and chi_c heatmaps
    chi_s, chi_c = compute_chi_s_c(chi0, U)

    fig1, ax1 = plt.subplots(1, 1, figsize=CFG["figsize_hm"], dpi=CFG["dpi"], constrained_layout=True)
    im1 = heatmap(ax1, chi_s, title=rf"$\chi_s(\mathbf{{q}},0)$, $U={U:.2f}$")
    fig1.colorbar(im1, ax=ax1, shrink=0.9, pad=0.02)
    out1 = figs_dir / "chi_s_static_heatmap.png"
    fig1.savefig(out1, bbox_inches="tight")
    print("Saved:", out1)

    fig2, ax2 = plt.subplots(1, 1, figsize=CFG["figsize_hm"], dpi=CFG["dpi"], constrained_layout=True)
    im2 = heatmap(ax2, chi_c, title=rf"$\chi_c(\mathbf{{q}},0)$, $U={U:.2f}$")
    fig2.colorbar(im2, ax=ax2, shrink=0.9, pad=0.02)
    out2 = figs_dir / "chi_c_static_heatmap.png"
    fig2.savefig(out2, bbox_inches="tight")
    print("Saved:", out2)

    # U scan plot for max chi_s vs U (to illustrate divergence near Ucrit)
    Uvals = np.linspace(0.0, min(Ucrit*0.99 if np.isfinite(Ucrit) else 2.0, 2.0), 60)
    max_chi_s = []
    for Uv in Uvals:
        cs, _ = compute_chi_s_c(chi0, Uv)
        max_chi_s.append(np.max(cs))
    fig3, ax3 = plt.subplots(1, 1, figsize=(6.2, 3.2), dpi=CFG["dpi"], constrained_layout=True)
    ax3.plot(Uvals, max_chi_s, '-b')
    if np.isfinite(Ucrit):
        ax3.axvline(Ucrit, color='r', ls='--', label=rf"$U_{{crit}}\approx{Ucrit:.2f}$")
    ax3.set_xlabel(r"$U$")
    ax3.set_ylabel(r"$\max_\mathbf{q}\,\chi_s(\mathbf{q},0)$")
    ax3.legend(frameon=False)
    out3 = figs_dir / "chi_s_Uscan.png"
    fig3.savefig(out3, bbox_inches="tight")
    print("Saved:", out3)

    # Matsubara G0 vs dressed G (toy static Σ)
    matsubara_g0_vs_grpa_plot(Nk, T, mu, t, U, chi_s, figs_dir / "g0_vs_grpa_matsubara.png")


if __name__ == "__main__":
    main()
