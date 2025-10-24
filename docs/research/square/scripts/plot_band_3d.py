"""
3D band surface plot for a 2D square lattice dispersion.
Saves the figure next to this article under ../figs/band_square_3d.png
"""
from __future__ import annotations

from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

# Configuration: change here if needed
CONFIG = {
    "a": 1.0,          # lattice constant
    "t": -1.0,         # nearest-neighbor hopping
    "t_prime": 0.0,    # next-nearest (t')
    "t_doubleprime": 0.0,  # third-nearest (t'')
    "eps0": 0.0,       # onsite energy shift
    "grid_n": 121,     # grid size per axis (odd is nice for symmetry)
}


def epsilon_k(kx_a: np.ndarray, ky_a: np.ndarray, cfg: dict) -> np.ndarray:
    """
    Dispersion epsilon(k) on a square lattice using dimensionless variables
    kx_a = kx * a, ky_a = ky * a (both in [-pi, pi]).
    """
    a = cfg["a"]
    t = cfg["t"]
    tp = cfg["t_prime"]
    tpp = cfg["t_doubleprime"]
    eps0 = cfg["eps0"]

    # Using k*a (dimensionless)
    cx = np.cos(kx_a)
    cy = np.cos(ky_a)
    c2x = np.cos(2.0 * kx_a)
    c2y = np.cos(2.0 * ky_a)

    return (
        eps0
        + 2.0 * t * (cx + cy)
        + 4.0 * tp * (cx * cy)
        + 2.0 * tpp * (c2x + c2y)
    )


def main() -> None:
    cfg = CONFIG
    N = int(cfg["grid_n"])  # grid points along each axis

    # Dimensionless k*a in [-pi, pi]
    kx_a = np.linspace(-np.pi, np.pi, N)
    ky_a = np.linspace(-np.pi, np.pi, N)
    KX, KY = np.meshgrid(kx_a, ky_a, indexing="xy")

    E = epsilon_k(KX, KY, cfg)

    # Prepare figure (smaller size to match other figures)
    fig = plt.figure(figsize=(5.2, 3.6), dpi=110)
    ax = fig.add_subplot(111, projection="3d")

    # Plot surface
    surf = ax.plot_surface(
        KX, KY, E,
        rstride=1, cstride=1,
        cmap=cm.viridis,
        linewidth=0.0,
        antialiased=True,
        alpha=0.95,
    )

    # A few aesthetics
    ax.set_xlabel(r"$k_x a$")
    ax.set_ylabel(r"$k_y a$")
    ax.set_zlabel(r"$\varepsilon(\mathbf{k})$")

    # Ticks at -pi, 0, pi
    ax.set_xticks([-np.pi, 0.0, np.pi], labels=[r"$-\pi$", r"$0$", r"$\pi$"])
    ax.set_yticks([-np.pi, 0.0, np.pi], labels=[r"$-\pi$", r"$0$", r"$\pi$"])

    fig.colorbar(surf, ax=ax, shrink=0.72, pad=0.08, label=r"$\varepsilon$")
    fig.tight_layout()

    # Output path: ../figs/band_square_3d.png relative to this script
    out_path = (Path(__file__).resolve().parent.parent / "figs" / "band_square_3d.png")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out_path, bbox_inches="tight")

    print(f"Saved 3D band figure: {out_path}")


if __name__ == "__main__":
    main()
