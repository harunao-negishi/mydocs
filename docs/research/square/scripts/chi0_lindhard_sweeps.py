"""
Static chi0(q,0) heatmaps via Lindhard form for multiple mu and T on 2D square TB.

Model: eps(k) = -2 t (cos kx + cos ky), a=1, t=1
Definition (static, iOmega_0=0):
  chi0(q,0) = (g_s/Nk^2) * sum_k [ f(Ek-mu) - f(Ekq-mu) ] / (-(Ekq - Ek))
with the smooth limit at Ekq==Ek given by -df/dE.

Outputs:
  - ../figs/chi0_static_mu_grid.png   (vary mu at fixed T)
  - ../figs/chi0_static_T_grid.png    (vary T at fixed mu)
"""
from __future__ import annotations

from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

CFG = {
    "t": 1.0,
    "Nk": 81,
    "g_s": 2.0,
    # sweeps
    "mu_list": [-2.0, 0.0, 2.0],
    "T_for_mu": 0.05,
    "T_list": [0.02, 0.05, 0.10],
    "mu_for_T": 0.0,
    # fig
    "figsize_row": (8.8, 3.2),
    "dpi": 110,
    "vmax_pct": 98.0,
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


def chi0_static_map_lindhard(Nk: int, T: float, mu: float, t: float, g_s: float) -> np.ndarray:
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


def heatmap_row(Z_list, titles, outpath, vmax_pct=98.0):
    n = len(Z_list)
    fig, axes = plt.subplots(1, n, figsize=(CFG["figsize_row"][0], CFG["figsize_row"][1]), dpi=CFG["dpi"], constrained_layout=True)
    if n == 1:
        axes = [axes]
    im = None
    vmax = max(np.percentile(Z, vmax_pct) for Z in Z_list)
    for ax, Z, title in zip(axes, Z_list, titles):
        im = ax.imshow(
            Z,
            origin="lower",
            extent=[-np.pi, np.pi, -np.pi, np.pi],
            cmap="viridis",
            vmin=np.min(Z),
            vmax=vmax,
            interpolation="nearest",
            aspect="equal",
        )
        ax.set_xlabel(r"$q_x a$")
        ax.set_ylabel(r"$q_y a$")
        ax.set_xticks([-np.pi, 0.0, np.pi], labels=[r"$-\pi$", r"$0$", r"$\pi$"])
        ax.set_yticks([-np.pi, 0.0, np.pi], labels=[r"$-\pi$", r"$0$", r"$\pi$"])
        ax.set_title(title)
    fig.colorbar(im, ax=axes, shrink=0.9, pad=0.02)
    fig.savefig(outpath, bbox_inches="tight")
    print("Saved:", outpath)


def main():
    Nk = CFG["Nk"]
    t = CFG["t"]
    g_s = CFG["g_s"]

    figs_dir = Path(__file__).resolve().parent.parent / "figs"
    figs_dir.mkdir(parents=True, exist_ok=True)

    # Sweep mu at fixed T
    T0 = CFG["T_for_mu"]
    mu_list = CFG["mu_list"]
    Zs = []
    titles = []
    for mu in mu_list:
        Z = chi0_static_map_lindhard(Nk, T0, mu, t, g_s)
        Zs.append(Z)
        titles.append(fr"$\mu={mu}$, $T={T0}$")
    heatmap_row(Zs, titles, figs_dir / "chi0_static_mu_grid.png", vmax_pct=CFG["vmax_pct"])

    # Sweep T at fixed mu
    mu0 = CFG["mu_for_T"]
    T_list = CFG["T_list"]
    Zs = []
    titles = []
    for T in T_list:
        Z = chi0_static_map_lindhard(Nk, T, mu0, t, g_s)
        Zs.append(Z)
        titles.append(fr"$T={T}$, $\mu={mu0}$")
    heatmap_row(Zs, titles, figs_dir / "chi0_static_T_grid.png", vmax_pct=CFG["vmax_pct"])


if __name__ == "__main__":
    main()
