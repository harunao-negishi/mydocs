"""
Compute DOS for 2D square-lattice tight-binding (nearest-neighbor only)
using a uniform k-grid histogram, and save a figure with guide lines at
E=-4t, 0, +4t. Intended for small PNG (~800px width) used via Markdown.
"""
from __future__ import annotations

from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

CONFIG = {
    "a": 1.0,
    "t": 1.0,          # use t>0 with epsilon = -2 t (cos kx + cos ky)
    "eps0": 0.0,
    "N": 801,          # k-grid per axis (N x N samples) for the main (fine) plot
    "bins": 401,
    "figsize": (6.4, 4.0),
    "dpi": 125,
}


def epsilon_k(kx: np.ndarray, ky: np.ndarray, a: float, t: float, eps0: float) -> np.ndarray:
    return eps0 - 2.0 * t * (np.cos(kx * a) + np.cos(ky * a))


def _one_hist(ax: plt.Axes, E: np.ndarray, bins: int, t: float) -> None:
    hist, edges, _ = ax.hist(E, bins=bins, density=True, color="#1f77b4", alpha=0.85, lw=0.0)
    # Guides at E=-4t, 0, +4t
    for xv, label in [(-4.0 * t, "-4t"), (0.0, "0"), (4.0 * t, "+4t")]:
        ax.axvline(xv, color="#444444", lw=1.0, ls="--")
        ax.text(xv, ax.get_ylim()[1] * 0.92, label, ha="center", va="top", fontsize=9,
                bbox=dict(boxstyle="round,pad=0.2", fc="white", ec="none", alpha=0.7))
    ax.set_xlabel("Energy E")
    ax.set_ylabel("DOS D(E)")
    ax.grid(True, ls=":", alpha=0.3)


def main() -> None:
    a = CONFIG["a"]
    t = CONFIG["t"]
    eps0 = CONFIG["eps0"]
    N = int(CONFIG["N"])
    bins = int(CONFIG["bins"])

    # k in [-pi/a, pi/a]
    kx = np.linspace(-np.pi / a, np.pi / a, N, dtype=float)
    ky = np.linspace(-np.pi / a, np.pi / a, N, dtype=float)
    KX, KY = np.meshgrid(kx, ky, indexing="xy")

    E = epsilon_k(KX, KY, a=a, t=t, eps0=eps0).ravel()

    # Main (fine) single-axes figure
    fig, ax = plt.subplots(figsize=CONFIG["figsize"], dpi=CONFIG["dpi"]) 
    _one_hist(ax, E, bins=bins, t=t)
    ax.set_title("2D square lattice TB DOS (fine)")
    fig.tight_layout()

    figs_dir = Path(__file__).resolve().parent.parent / "figs"
    figs_dir.mkdir(parents=True, exist_ok=True)
    out_fine = figs_dir / "dos_square_tb.png"
    fig.savefig(out_fine, bbox_inches="tight")
    print("Saved:", out_fine)

    # Comparison: coarse vs fine (two subplots)
    fig2, (ax1, ax2) = plt.subplots(1, 2, figsize=(8.8, 3.8), dpi=CONFIG["dpi"], sharey=True)

    # Coarse mesh
    Nc, bc = 96, 121
    kx_c = np.linspace(-np.pi / a, np.pi / a, Nc, dtype=float)
    ky_c = np.linspace(-np.pi / a, np.pi / a, Nc, dtype=float)
    KXc, KYc = np.meshgrid(kx_c, ky_c, indexing="xy")
    Ec = epsilon_k(KXc, KYc, a=a, t=t, eps0=eps0).ravel()
    _one_hist(ax1, Ec, bins=bc, t=t)
    ax1.set_title(f"coarse: N={Nc}×{Nc}, bins={bc}")

    # Fine mesh (same as main)
    _one_hist(ax2, E, bins=bins, t=t)
    ax2.set_title(f"fine: N={N}×{N}, bins={bins}")

    fig2.tight_layout()
    out_cmp = figs_dir / "dos_square_tb_mesh_compare.png"
    fig2.savefig(out_cmp, bbox_inches="tight")
    print("Saved:", out_cmp)


if __name__ == "__main__":
    main()
