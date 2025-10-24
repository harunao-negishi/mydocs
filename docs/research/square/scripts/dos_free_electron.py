"""
Generate free-electron DOS plots in 1D/2D/3D (spinless) and save figures under ../figs/.
Analytic curves are compared with numerical histograms from k-space sampling.
"""
from __future__ import annotations

from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

HBAR = 1.0  # choose units with ħ=1
M = 1.0     # effective mass (spinless)

# Figure sizing (smaller, for compact display)
FIGSIZE_ONE = (5.0, 3.2)
DPI_ONE = 110
FIGSIZE_OVERLAY = (5.2, 3.4)
DPI_OVERLAY = 110


def dos_analytic(E: np.ndarray, dim: int, m: float = M, hbar: float = HBAR) -> np.ndarray:
    # Note: For 1D, avoid plotting a misleading value at E=0 by returning NaN for E<=0
    if dim == 1:
        D = np.full_like(E, np.nan, dtype=float)
        mask = E > 0.0
        D[mask] = (1/np.pi) * np.sqrt(m/(2*hbar*hbar)) / np.sqrt(E[mask])
        return D
    E = np.maximum(E, 0.0)
    if dim == 2:
        return (m/(2*np.pi*hbar*hbar)) * (E >= 0)
    if dim == 3:
        return (1/(2*np.pi**2)) * (2*m/(hbar*hbar))**1.5 * np.sqrt(E)
    raise ValueError("dim must be 1, 2, or 3")


def dos_numeric(dim: int, n_samples: int = 300_000, kmax: float = 4.0, m: float = M, hbar: float = HBAR,
                bins: int = 200) -> tuple[np.ndarray, np.ndarray]:
    rng = np.random.default_rng(1234)
    if dim == 1:
        k = rng.uniform(-kmax, kmax, size=(n_samples, 1))
    elif dim == 2:
        k = rng.uniform(-kmax, kmax, size=(n_samples, 2))
    elif dim == 3:
        k = rng.uniform(-kmax, kmax, size=(n_samples, 3))
    else:
        raise ValueError("dim must be 1, 2, or 3")

    k2 = np.sum(k*k, axis=1)
    E = (hbar*hbar * k2) / (2*m)

    hist, edges = np.histogram(E, bins=bins, density=True)
    centers = 0.5*(edges[1:] + edges[:-1])
    return centers, hist


def plot_one(dim: int, outpath: Path) -> None:
    E_max = 8.0
    E = np.linspace(0.0, E_max, 1000)
    Ea, Da = E, dos_analytic(E, dim)
    # Increase samples/bins for smoother numerics
    n_samp = 400_000 if dim == 1 else (600_000 if dim == 2 else 900_000)
    En, Dn = dos_numeric(dim, n_samples=n_samp, kmax=np.sqrt(2*E_max), bins=300)

    fig, ax = plt.subplots(figsize=FIGSIZE_ONE, dpi=DPI_ONE)
    ax.plot(Ea, Da, label=f"analytic {dim}D", lw=2)
    ax.plot(En, Dn, label=f"numeric {dim}D", ls=":", lw=1.8)
    ax.set_xlabel("Energy E")
    ax.set_ylabel("DOS D(E)")
    ax.set_title(f"Free-electron DOS ({dim}D)")
    ax.legend()
    fig.tight_layout()
    outpath.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(outpath, bbox_inches="tight")


def plot_overlay(outpath: Path) -> None:
    E_max = 8.0
    E = np.linspace(0.0, E_max, 2000)
    fig, ax = plt.subplots(figsize=FIGSIZE_OVERLAY, dpi=DPI_OVERLAY)
    for dim, color in [(1, "tab:blue"), (2, "tab:orange"), (3, "tab:green")]:
        ax.plot(E, dos_analytic(E, dim), label=f"analytic {dim}D", lw=2, color=color)
    ax.set_xlabel("Energy E")
    ax.set_ylabel("DOS D(E)")
    ax.set_title("Free-electron DOS: analytic (1D/2D/3D)")
    ax.legend()
    fig.tight_layout()
    outpath.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(outpath, bbox_inches="tight")


def main() -> None:
    here = Path(__file__).resolve().parent
    figs = here.parent / "figs"
    plot_one(1, figs / "dos_free_1d.png")
    plot_one(2, figs / "dos_free_2d.png")
    plot_one(3, figs / "dos_free_3d.png")
    plot_overlay(figs / "dos_free_overlay.png")
    print("Saved DOS figures to:", figs)


if __name__ == "__main__":
    main()
