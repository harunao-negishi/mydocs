"""
Compute filling n(mu, T) for a 2D square-lattice tight-binding model
with nearest-neighbor hopping using a uniform k-grid, and plot n vs mu
for T=0 and a small finite temperature.

Model: epsilon(k) = -2 t (cos kx + cos ky), t>0, a=1
We report spinful filling n in [0, 2] with gs=2 by default.
"""
from __future__ import annotations

from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

CFG = {
    "a": 1.0,
    "t": 1.0,          # use t>0 consistent with DOS page convention
    "Nk": 601,         # k-grid per axis (Nk x Nk)
    "gs": 2,          # spin degeneracy (2 for spinful)
    "mu_min": -4.0,   # in units of t
    "mu_max": 4.0,
    "n_mu": 401,
    "kBT_list": [0.0, 0.1],  # temperatures in units of |t|
    "figsize": (5.0, 3.2),
    "dpi": 110,
}


def epsilon_k(kx: np.ndarray, ky: np.ndarray, t: float) -> np.ndarray:
    return -2.0 * t * (np.cos(kx) + np.cos(ky))


def fermi(E: np.ndarray, mu: float, kBT: float) -> np.ndarray:
    if kBT == 0.0:
        # Heaviside step: 1 for E < mu, 0.5 at equality is irrelevant for measure zero
        return (E < mu).astype(float)
    x = (E - mu) / (kBT + 1e-15)
    # Clip to avoid overflow in exp
    x = np.clip(x, -50.0, 50.0)
    return 1.0 / (np.exp(x) + 1.0)


def compute_n_mu(Ek: np.ndarray, mu_grid: np.ndarray, kBT: float, gs: int) -> np.ndarray:
    # Average f(Ek) over k for each mu
    n_vals = []
    for mu in mu_grid:
        occ = fermi(Ek, mu, kBT).mean()
        n_vals.append(gs * occ)
    return np.asarray(n_vals)


def n_of_mu(Ek: np.ndarray, mu: float, kBT: float, gs: int) -> float:
    return float(gs * fermi(Ek, mu, kBT).mean())


def invert_mu_for_n(
    Ek: np.ndarray,
    n_target: float,
    kBT: float,
    gs: int,
    mu_lo: float,
    mu_hi: float,
    tol: float = 1e-8,
    max_iter: int = 100,
) -> float:
    """Find μ such that n(μ,kBT)=n_target using bisection (n is monotonic in μ)."""
    n_lo = n_of_mu(Ek, mu_lo, kBT, gs)
    n_hi = n_of_mu(Ek, mu_hi, kBT, gs)
    # Ensure bracket
    if not (min(n_lo, n_hi) <= n_target <= max(n_lo, n_hi)):
        # Clip target to bracket range to avoid failure due to numerical edges
        n_target = min(max(n_target, min(n_lo, n_hi)), max(n_lo, n_hi))
    a, b = (mu_lo, mu_hi)
    fa = n_of_mu(Ek, a, kBT, gs) - n_target
    fb = n_of_mu(Ek, b, kBT, gs) - n_target
    for _ in range(max_iter):
        m = 0.5 * (a + b)
        fm = n_of_mu(Ek, m, kBT, gs) - n_target
        if abs(fm) < tol or (b - a) < tol:
            return m
        # Monotonic with μ: choose sub-interval with sign change
        if fa * fm <= 0:
            b, fb = m, fm
        else:
            a, fa = m, fm
    return 0.5 * (a + b)


def main() -> None:
    a = CFG["a"]
    t = CFG["t"]
    Nk = int(CFG["Nk"])
    gs = int(CFG["gs"])

    # k grid in [-pi, pi]
    kx = np.linspace(-np.pi, np.pi, Nk)
    ky = np.linspace(-np.pi, np.pi, Nk)
    KX, KY = np.meshgrid(kx, ky, indexing="xy")

    Ek = epsilon_k(KX, KY, t=t).ravel()

    mu_grid = np.linspace(CFG["mu_min"] * abs(t), CFG["mu_max"] * abs(t), CFG["n_mu"])  # absolute energy units

    # Figure 1: n(μ) curves (supplement)
    fig1, ax1 = plt.subplots(figsize=CFG["figsize"], dpi=CFG["dpi"])
    for kBT in CFG["kBT_list"]:
        n_vals = compute_n_mu(Ek, mu_grid, kBT * abs(t), gs=gs)
        label = ("T=0" if kBT == 0.0 else fr"k_B T={kBT}|t|")
        ax1.plot(mu_grid / abs(t), n_vals, label=label, lw=1.8)
    ax1.set_xlabel(r"$\mu/|t|$")
    ax1.set_ylabel(r"filling $n$ (per site, spinful)")
    ax1.set_title("2D square TB: n vs μ")
    ax1.set_xlim(CFG["mu_min"], CFG["mu_max"])
    ax1.set_ylim(-0.05, 2.05)
    ax1.grid(True, ls=":", alpha=0.4)
    ax1.legend()
    fig1.tight_layout()
    out1 = Path(__file__).resolve().parent.parent / "figs" / "filling_mu_tb.png"
    out1.parent.mkdir(parents=True, exist_ok=True)
    fig1.savefig(out1, bbox_inches="tight")
    print("Saved:", out1)

    # Figure 2: μ(n) curves (main)
    n_min, n_max = 0.0, float(gs)  # one band per site assumed
    n_grid = np.linspace(n_min, n_max, 201)
    fig2, ax2 = plt.subplots(figsize=CFG["figsize"], dpi=CFG["dpi"])

    # Pre-sort energies for fast T=0 inversion; also prepare a coarse μ grid for T>0 interpolation
    Ek_sorted = np.sort(Ek)
    mu_grid_dense = np.linspace(CFG["mu_min"] * abs(t), CFG["mu_max"] * abs(t), 1201)

    for kBT in CFG["kBT_list"]:
        mu_vals = []
        if kBT == 0.0:
            # Direct quantile: n = gs * fraction(E<=mu) ⇒ mu is the quantile at p = n/gs
            for n_target in n_grid:
                p = np.clip(n_target / float(gs), 0.0, 1.0)
                mu_star = np.quantile(Ek_sorted, p)
                mu_vals.append(mu_star / abs(t))
        else:
            # Precompute n(mu) on a dense grid and invert by monotone interpolation
            n_mu_dense = compute_n_mu(Ek, mu_grid_dense, kBT * abs(t), gs=gs)
            # Ensure monotonicity (numerical noise): enforce non-decreasing by cumulative maximum
            n_mu_dense = np.maximum.accumulate(n_mu_dense)
            for n_target in n_grid:
                n_clamped = np.clip(n_target, n_mu_dense[0], n_mu_dense[-1])
                mu_star = np.interp(n_clamped, n_mu_dense, mu_grid_dense)
                mu_vals.append(mu_star / abs(t))
        label = ("T=0" if kBT == 0.0 else fr"k_B T={kBT}|t|")
        ax2.plot(n_grid, mu_vals, label=label, lw=1.8)
    ax2.axhline(0.0, color="#888", lw=0.8, ls="--")
    ax2.axvline(float(gs) / 2.0, color="#888", lw=0.8, ls="--")
    ax2.set_xlabel(r"filling $n$ (per site, spinful)")
    ax2.set_ylabel(r"$\mu/|t|")
    ax2.set_title("2D square TB: μ vs n")
    ax2.set_xlim(n_min, n_max)
    ax2.grid(True, ls=":", alpha=0.4)
    ax2.legend()
    fig2.tight_layout()
    out2 = Path(__file__).resolve().parent.parent / "figs" / "mu_vs_filling_tb.png"
    fig2.savefig(out2, bbox_inches="tight")
    print("Saved:", out2)


if __name__ == "__main__":
    main()
