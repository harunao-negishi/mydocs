"""
Heatmap of |G0(k, z)| on the 2D square-lattice BZ to illustrate Fermi surface.

Two modes:
  1) Retarded probe at omega = mu (eta>0):   G0(k, omega) = 1 / (omega + i*eta - eps(k))
  2) Matsubara at lowest fermionic frequency: G0(k, i*omega0) with omega0 = pi*T

We show three chemical potentials mu in {-2, 0, +2} (units of t>0), a=1.
Outputs:
  - ../figs/g0_heatmap_retarded_mu_grid.png
  - ../figs/g0_heatmap_matsubara_mu_grid.png
"""
from __future__ import annotations

from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

CFG = {
    "a": 1.0,
    "t": 1.0,
    "Nk": 401,
    "mu_list": [-2.0, 0.0, 2.0],
    # Retarded
    "eta": 0.05,  # small broadening in |t|
    # Matsubara
    "T": 0.05,  # kB T in units of |t|
    # Figure
    "figsize": (8.8, 3.2),
    "dpi": 110,
}


def eps_k(kx: np.ndarray, ky: np.ndarray, t: float) -> np.ndarray:
    return -2.0 * t * (np.cos(kx) + np.cos(ky))


def heatmap(ax: plt.Axes, Z: np.ndarray, title: str, vmax_pct: float = 98.0) -> None:
    # Clip vmax by percentile to avoid a few huge pixels dominating
    vmin, vmax = 0.0, np.percentile(Z, vmax_pct)
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
    ax.set_xlabel(r"$k_x a$")
    ax.set_ylabel(r"$k_y a$")
    ax.set_xticks([-np.pi, 0.0, np.pi], labels=[r"$-\pi$", r"$0$", r"$\pi$"])
    ax.set_yticks([-np.pi, 0.0, np.pi], labels=[r"$-\pi$", r"$0$", r"$\pi$"])
    ax.set_title(title)
    return im


def main() -> None:
    t = CFG["t"]
    Nk = int(CFG["Nk"])
    mu_list = [float(m) for m in CFG["mu_list"]]

    # BZ grid in k*a in [-pi, pi]
    k = np.linspace(-np.pi, np.pi, Nk)
    KX, KY = np.meshgrid(k, k, indexing="xy")
    E = eps_k(KX, KY, t=t)

    figs_dir = Path(__file__).resolve().parent.parent / "figs"
    figs_dir.mkdir(parents=True, exist_ok=True)

    # 1) Retarded at omega = mu (eta>0)
    fig1, axes1 = plt.subplots(1, 3, figsize=CFG["figsize"], dpi=CFG["dpi"], constrained_layout=True)
    for ax, mu in zip(axes1.flat, mu_list):
        omega = mu  # probe energy equals mu, highlights FS where eps ~ mu
        Z = 1.0 / np.sqrt((omega - E) ** 2 + (CFG["eta"]) ** 2)  # | 1/(omega + i*eta - eps) |
        im = heatmap(ax, Z, title=fr"retarded: $\mu={mu}$, $\omega=\mu$, $\eta={CFG['eta']}$")
    cbar1 = fig1.colorbar(im, ax=axes1.ravel().tolist(), shrink=0.9, pad=0.02)
    out1 = figs_dir / "g0_heatmap_retarded_mu_grid.png"
    fig1.savefig(out1, bbox_inches="tight")
    print("Saved:", out1)

    # 2) Matsubara at lowest frequency i*omega0 with omega0 = pi*T
    T = CFG["T"]
    omega0 = np.pi * T
    fig2, axes2 = plt.subplots(1, 3, figsize=CFG["figsize"], dpi=CFG["dpi"], constrained_layout=True)
    for ax, mu in zip(axes2.flat, mu_list):
        # |1/(i omega0 - (eps-mu))| = 1/sqrt(omega0^2 + (eps-mu)^2)
        Z = 1.0 / np.sqrt((omega0) ** 2 + (E - mu) ** 2)
        im = heatmap(ax, Z, title=fr"Matsubara: $\mu={mu}$, $\omega_0=\pi T={omega0:.3f}$")
    cbar2 = fig2.colorbar(im, ax=axes2.ravel().tolist(), shrink=0.9, pad=0.02)
    out2 = figs_dir / "g0_heatmap_matsubara_mu_grid.png"
    fig2.savefig(out2, bbox_inches="tight")
    print("Saved:", out2)


if __name__ == "__main__":
    main()
