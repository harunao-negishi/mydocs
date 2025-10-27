"""
Convergence of finite-N fermionic Matsubara sum to Lindhard form for chi0(Q,iOmega1).

Model: 2D square-lattice tight-binding, eps(k) = -2 t (cos kx + cos ky), a=1, t=1
Parameters: mu=0 (half filling), T=0.05, Nk=81
External bosonic frequency: iOmega1 with Omega1 = 2*pi*T (m=1)
Wave vector: Q = (pi, pi)

We compute chi0 via two routes:
  (A) Finite fermionic Matsubara sum (truncate |n|<=Nn):
      chi0^(Nn)(Q, iOmega1) = (g_s/Nk^2) * T * sum_k sum_{n=-Nn..Nn} G0(k,iwn) G0(k+Q,i(wn+Omega1))
  (B) Lindhard closed form:
      chi0^L(Q, iOmega1) = (g_s/Nk^2) * sum_k [ f(Ek-mu) - f(EkQ-mu) ] / ( iOmega1 - (EkQ - Ek) )
And show chi0^(Nn) -> chi0^L as Nn increases.

Output:
  - ../figs/chi0_Qpi_convergence.png
"""
from __future__ import annotations

from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

CFG = {
    "t": 1.0,
    "a": 1.0,
    "Nk": 81,
    "T": 0.05,
    "mu": 0.0,
    "g_s": 2.0,
    "Nn_list": [1, 2, 4, 8, 16, 32, 64, 128],
    "figsize": (6.2, 3.2),
    "dpi": 110,
}


def eps_k(kx: np.ndarray, ky: np.ndarray, t: float) -> np.ndarray:
    return -2.0 * t * (np.cos(kx) + np.cos(ky))


def fermi(x: np.ndarray, T: float) -> np.ndarray:
    xT = x / max(T, 1e-12)
    xT = np.clip(xT, -60.0, 60.0)
    return 1.0 / (np.exp(xT) + 1.0)


def make_k_grid(Nk: int):
    k = np.linspace(-np.pi, np.pi, Nk, endpoint=False)
    KX, KY = np.meshgrid(k, k, indexing="xy")
    return k, KX, KY


def chi0_lindhard_Q(Nk: int, T: float, mu: float, t: float, g_s: float) -> float:
    _, KX, KY = make_k_grid(Nk)
    Ek = eps_k(KX, KY, t)
    # Q=(pi,pi) corresponds to index shift Nk//2 on both axes for endpoint=False grid
    EkQ = np.roll(np.roll(Ek, shift=Nk//2, axis=0), shift=Nk//2, axis=1)
    fk = fermi(Ek - mu, T)
    fkQ = fermi(EkQ - mu, T)
    Omega1 = 2.0 * np.pi * T
    denom = 1j * Omega1 - (EkQ - Ek)
    chi = ((fk - fkQ) / denom).sum() * (g_s / (Nk * Nk))
    return float(np.real(chi))


def chi0_matsubara_sum_Q(Nk: int, T: float, mu: float, t: float, g_s: float, Nn: int) -> float:
    _, KX, KY = make_k_grid(Nk)
    Ek = eps_k(KX, KY, t)
    EkQ = np.roll(np.roll(Ek, shift=Nk//2, axis=0), shift=Nk//2, axis=1)
    Omega1 = 2.0 * np.pi * T

    # Accumulate over n = -Nn..Nn
    acc = 0.0 + 0.0j
    for n in range(-Nn, Nn + 1):
        wn = (2 * n + 1) * np.pi * T  # fermionic Matsubara
        Gk = 1.0 / (1j * wn - (Ek - mu))
        GkQ = 1.0 / (1j * (wn + Omega1) - (EkQ - mu))
        acc += (Gk * GkQ).sum()

    chi = (g_s / (Nk * Nk)) * T * acc
    return float(np.real(chi))


def main():
    Nk = int(CFG["Nk"])
    T = float(CFG["T"])
    mu = float(CFG["mu"])
    t = float(CFG["t"])
    g_s = float(CFG["g_s"])

    figs_dir = Path(__file__).resolve().parent.parent / "figs"
    figs_dir.mkdir(parents=True, exist_ok=True)

    chi_L = chi0_lindhard_Q(Nk, T, mu, t, g_s)

    Nn_list = CFG["Nn_list"]
    chi_sum = []
    for Nn in Nn_list:
        val = chi0_matsubara_sum_Q(Nk, T, mu, t, g_s, Nn)
        chi_sum.append(val)
        print(f"Nn={Nn:3d}: chi_sum={val:.8f} | chi_L={chi_L:.8f} | diff={abs(val-chi_L):.3e}")

    fig, ax = plt.subplots(1, 1, figsize=CFG["figsize"], dpi=CFG["dpi"], constrained_layout=True)
    ax.plot(Nn_list, chi_sum, 'o-', label=r"$\chi_0^{(N_n)}$ (sum)")
    ax.hlines(chi_L, xmin=min(Nn_list), xmax=max(Nn_list), colors='k', linestyles='--', label=r"$\chi_0^{\rm Lindhard}$")
    ax.set_xscale('log', base=2)
    ax.set_xlabel(r"$N_n$ (fermionic Matsubara terms)")
    ax.set_ylabel(r"$\chi_0(\mathbf{Q}, i\Omega_1)$")
    ax.legend(frameon=False)
    out = figs_dir / "chi0_Qpi_convergence.png"
    fig.savefig(out, bbox_inches="tight")
    print("Saved:", out)


if __name__ == "__main__":
    main()
