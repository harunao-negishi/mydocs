"""
Non-interacting susceptibility chi0(q, iOmega_m) on 2D square-lattice tight-binding.

Model: eps(k) = -2 t (cos kx + cos ky), a=1, t>0
Lindhard form after Matsubara sum:
    chi0(q, iOmega_m) = (g_s / N_k^2) * sum_k [ f(Ek-mu) - f(Ekq-mu) ] / (1j*Omega_m - (Ekq - Ek))
with spin degeneracy g_s=2.

This script produces ONLY the static map (bosonic lowest Matsubara: m=0, iOmega_0=0):
    - ../figs/chi0_static_heatmap.png

Implementation detail: for the static limit where Ekq-Ek≈0, the integrand is replaced
by the smooth limit -df/dE to avoid 0/0 instability.
"""
from __future__ import annotations

from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

CFG = {
    "a": 1.0,
    "t": 1.0,
    "Nk": 81,          # grid per axis for k and q
    "T": 0.05,         # temperature in |t|
    "mu": 0.0,         # half-filling
    "g_s": 2.0,        # spin degeneracy
    "eps_reg": 1e-8,   # small regularizer for static denominator
    # Figures
    "figsize_hm": (4.8, 4.2),
    "dpi": 110,
}


def eps_k(kx: np.ndarray, ky: np.ndarray, t: float) -> np.ndarray:
    return -2.0 * t * (np.cos(kx) + np.cos(ky))


def fermi(x: np.ndarray, T: float) -> np.ndarray:
    # f(x) = 1/(exp(x/T)+1); stable for small/large x
    xT = x / max(T, 1e-12)
    # clip to avoid overflow
    xT = np.clip(xT, -60.0, 60.0)
    return 1.0 / (np.exp(xT) + 1.0)


def fermi_deriv(x: np.ndarray, T: float) -> np.ndarray:
    # df/dE = -1/(4T) * sech^2((x)/(2T)) ; stable implementation
    T = max(T, 1e-12)
    y = np.clip(x / (2.0 * T), -60.0, 60.0)
    sech2 = 1.0 / (np.cosh(y) ** 2)
    return -0.25 / T * sech2


def make_k_grid(Nk: int):
    k = np.linspace(-np.pi, np.pi, Nk, endpoint=False)
    KX, KY = np.meshgrid(k, k, indexing="xy")
    return k, KX, KY


def chi0_map(Nk: int, T: float, mu: float, t: float, g_s: float, m: int) -> np.ndarray:
    # Precompute band and Fermi on k-grid
    k, KX, KY = make_k_grid(Nk)
    Ek = eps_k(KX, KY, t)
    fk = fermi(Ek - mu, T)

    if m == 0:
        Omega = 0.0
    else:
        Omega = 2.0 * np.pi * T * m

    chi = np.zeros((Nk, Nk), dtype=np.float64)

    for iqx in range(Nk):
        for iqy in range(Nk):
            # Shift by (iqx, iqy) in index space -> q ~ (iq) * dk
            Ekq = np.roll(np.roll(Ek, shift=iqx, axis=0), shift=iqy, axis=1)
            fkq = np.roll(np.roll(fk, shift=iqx, axis=0), shift=iqy, axis=1)
            dE = Ekq - Ek
            num = fk - fkq

            if m == 0:
                # Static limit: handle dE ~ 0 with derivative limit -> -f'(Ek)
                mask = np.abs(dE) < CFG["eps_reg"]
                denom = -dE
                integrand = np.zeros_like(denom, dtype=np.float64)
                # regular points
                safe = ~mask
                integrand[safe] = (num[safe] / denom[safe]).real
                # limiting points
                integrand[mask] = -fermi_deriv(Ek[mask] - mu, T)
                val = integrand.sum() * (g_s / (Nk * Nk))
            else:
                denom = 1j * Omega - dE
                # On imaginary axis, result should be real; take real part
                val = np.real((num / denom).sum() * (g_s / (Nk * Nk)))

            chi[iqx, iqy] = val

    # Center q=0 at the middle for imshow
    return np.fft.fftshift(chi)


def heatmap(ax, Z: np.ndarray, title: str, vmax_pct: float = 98.0):
    vmin, vmax = np.min(Z), np.percentile(Z, vmax_pct)
    im = ax.imshow(
        Z,
        origin="lower",
        extent=[-np.pi, np.pi, -np.pi, np.pi],
        cmap="viridis",
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


def main():
    Nk = int(CFG["Nk"])
    T = float(CFG["T"])
    mu = float(CFG["mu"])
    t = float(CFG["t"])
    g_s = float(CFG["g_s"])

    figs_dir = Path(__file__).resolve().parent.parent / "figs"
    figs_dir.mkdir(parents=True, exist_ok=True)

    # Compute map (static only)
    chi_static = chi0_map(Nk, T, mu, t, g_s, m=0)

    # Heatmaps
    fig1, ax1 = plt.subplots(1, 1, figsize=CFG["figsize_hm"], dpi=CFG["dpi"], constrained_layout=True)
    im1 = heatmap(ax1, chi_static, title=r"$\chi_0(\mathbf{q}, 0)$")
    fig1.colorbar(im1, ax=ax1, shrink=0.9, pad=0.02)
    out1 = figs_dir / "chi0_static_heatmap.png"
    fig1.savefig(out1, bbox_inches="tight")
    print("Saved:", out1)

    # No finite-frequency or path plots in this script


if __name__ == "__main__":
    main()
