"""
Plot band structure for a 2D square lattice tight-binding model along Γ–X–M–Γ.
Outputs: ../figs/band_square.png (relative to this script's folder)

Model: ε(k) = ε0 + 2t(cos kx a + cos ky a) + 4t'(cos kx a cos ky a) + 2t''(cos 2kx a + cos 2ky a)

Usage (from repo root or anywhere):
  python docs/research/square/scripts/plot_band.py
"""
from __future__ import annotations
import os
import numpy as np
import matplotlib.pyplot as plt

# ---------- CONFIG ----------
CONFIG = {
    "a": 1.0,
    "t": -1.0,     # sign convention: common in condensed matter to take t<0
    "tp": 0.0,
    "tpp": 0.0,
    "eps0": 0.0,
    "nk_per_segment": 200,
    "fig_dpi": 110,
    "figsize": (5.0, 3.2),
}
# ----------------------------


def eps_k(kx: np.ndarray, ky: np.ndarray, *, a: float, t: float, tp: float, tpp: float, eps0: float) -> np.ndarray:
    return (
        eps0
        + 2 * t * (np.cos(kx * a) + np.cos(ky * a))
        + 4 * tp * np.cos(kx * a) * np.cos(ky * a)
        + 2 * tpp * (np.cos(2 * kx * a) + np.cos(2 * ky * a))
    )


def kpath_G_X_M_G(*, a: float, nk: int):
    """Return concatenated k-path Γ(0,0)→X(π/a,0)→M(π/a,π/a)→Γ(0,0).
    Returns (kx, ky, x_coords, xtick_positions, xtick_labels)
    """
    G = np.array([0.0, 0.0])
    X = np.array([np.pi / a, 0.0])
    M = np.array([np.pi / a, np.pi / a])

    def segment(p0, p1, n):
        t = np.linspace(0.0, 1.0, n, endpoint=False)
        return (1 - t)[:, None] * p0[None, :] + t[:, None] * p1[None, :]

    s1 = segment(G, X, nk)
    s2 = segment(X, M, nk)
    s3 = segment(M, G, nk + 1)  # include last point

    k = np.vstack([s1, s2, s3])
    kx, ky = k[:, 0], k[:, 1]

    # Build x-axis as cumulative distance
    dk = np.sqrt(np.diff(kx) ** 2 + np.diff(ky) ** 2)
    x = np.concatenate([[0.0], np.cumsum(dk)])
    xticks = [0.0, x[len(s1) - 1], x[len(s1) + len(s2) - 1], x[-1]]
    xticklabels = ["Γ", "X", "M", "Γ"]
    return kx, ky, x, xticks, xticklabels


def main():
    a = CONFIG["a"]
    t = CONFIG["t"]
    tp = CONFIG["tp"]
    tpp = CONFIG["tpp"]
    eps0 = CONFIG["eps0"]
    nk = CONFIG["nk_per_segment"]

    kx, ky, x, xticks, xticklabels = kpath_G_X_M_G(a=a, nk=nk)
    ek = eps_k(kx, ky, a=a, t=t, tp=tp, tpp=tpp, eps0=eps0)

    fig, ax = plt.subplots(figsize=CONFIG["figsize"], dpi=CONFIG["fig_dpi"]) 
    ax.plot(x, ek, color="#1f77b4", lw=1.5)
    for xv in xticks:
        ax.axvline(x=xv, color="#cccccc", lw=0.8)
    ax.set_xticks(xticks)
    ax.set_xticklabels(xticklabels)
    ax.set_xlim(x[0], x[-1])
    ax.set_ylabel(r"$\varepsilon(\mathbf{k})$")
    ax.set_title("Square lattice band: Γ–X–M–Γ")
    ax.grid(True, ls=":", alpha=0.4)
    fig.tight_layout()

    script_dir = os.path.dirname(os.path.abspath(__file__))
    out = os.path.normpath(os.path.join(script_dir, "..", "figs", "band_square.png"))
    os.makedirs(os.path.dirname(out), exist_ok=True)
    fig.savefig(out)
    print(f"Saved figure: {out}")


if __name__ == "__main__":
    main()
