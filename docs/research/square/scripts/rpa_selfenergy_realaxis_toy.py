"""
Toy real-axis RPA self-energy using dominant Q=(pi,pi) channel on 2D square TB.

Steps:
 1) Build chi0^R(Q, Omega) on a small real-frequency grid using
    chi0^R(Q, Omega) = (g_s/Nk^2) sum_k [ f(Ek-mu) - f(EkQ-mu) ] / (Omega + i*eta - (EkQ - Ek))
 2) RPA: chi_s^R = chi0^R / (1 - U*chi0^R), chi_c^R = chi0^R / (1 + U*chi0^R)
 3) Effective interaction V^R(Q,Omega) = (3/2)U^2 chi_s^R + (1/2)U^2 chi_c^R - U^2 chi0^R
    (last term is double-counting correction)
 4) Convolution (q=Q only):
    Sigma^R(k, omega) ≈ ∫ dOmega / (2π) V^R(Q,Omega) * [n_B(Omega) + n_F(xi_{k-Q})] / (omega - Omega - xi_{k-Q} + i*eta)
 5) Compare A(kF, omega) vs non-interacting A0 at kF=(pi/2, pi/2).

Outputs:
  - ../figs/A_kF_rpa_vs_nonint.png
  - ../figs/imSigma_kF.png
"""
from __future__ import annotations

from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

CFG = {
    "t": 1.0,
    "Nk": 81,
    "T": 0.05,
    "mu": 0.0,
    "g_s": 2.0,
    "U": 0.8,
    "eta": 0.05,
    # frequency grid
    "Omega_max": 4.0,
    "nOmega": 161,
    "omega_max": 0.6,
    "nomega": 241,
    # figs
    "dpi": 110,
}


def eps_k(kx, ky, t):
    return -2.0 * t * (np.cos(kx) + np.cos(ky))


def fermi(x, T):
    T = max(T, 1e-12)
    y = np.clip(x / T, -60.0, 60.0)
    return 1.0 / (np.exp(y) + 1.0)


def nbose(x, T):
    T = max(T, 1e-12)
    y = np.clip(x / T, -60.0, 60.0)
    return 1.0 / (np.exp(y) - 1.0 + 1e-12)


def make_k_grid(Nk):
    k = np.linspace(-np.pi, np.pi, Nk, endpoint=False)
    KX, KY = np.meshgrid(k, k, indexing="xy")
    return k, KX, KY


def chi0_real_Q(Nk, T, mu, t, g_s, Qx, Qy, Omegas, eta):
    _, KX, KY = make_k_grid(Nk)
    Ek = eps_k(KX, KY, t)
    EkQ = eps_k(KX + Qx, KY + Qy, t)
    fk = fermi(Ek - mu, T)
    fkQ = fermi(EkQ - mu, T)
    dE = EkQ - Ek
    chi = np.zeros_like(Omegas, dtype=np.complex128)
    factor = g_s / (Nk * Nk)
    for i, Om in enumerate(Omegas):
        chi[i] = np.sum((fk - fkQ) / (Om + 1j * eta - dE)) * factor
    return chi


def main():
    Nk = CFG["Nk"]
    T = CFG["T"]
    mu = CFG["mu"]
    t = CFG["t"]
    g_s = CFG["g_s"]
    U = CFG["U"]
    eta = CFG["eta"]

    figs_dir = Path(__file__).resolve().parent.parent / "figs"
    figs_dir.mkdir(parents=True, exist_ok=True)

    # Dominant Q = (pi, pi)
    Qx, Qy = np.pi, np.pi

    # Real-frequency grids
    Omegas = np.linspace(-CFG["Omega_max"], CFG["Omega_max"], CFG["nOmega"])  # bosonic
    omeg = np.linspace(-CFG["omega_max"], CFG["omega_max"], CFG["nomega"])    # fermionic
    dOm = Omegas[1] - Omegas[0]

    # chi0^R(Q,Omega)
    chi0R = chi0_real_Q(Nk, T, mu, t, g_s, Qx, Qy, Omegas, eta)
    # RPA
    chisR = chi0R / (1.0 - U * chi0R)
    chicR = chi0R / (1.0 + U * chi0R)
    Veff = (3.0/2.0) * (U ** 2) * chisR + (1.0/2.0) * (U ** 2) * chicR - (U ** 2) * chi0R

    # Choose kF ~ (pi/2, pi/2)
    kFx, kFy = np.pi/2, np.pi/2
    xi_k = eps_k(kFx, kFy, t) - mu
    xi_kmQ = eps_k(kFx - Qx, kFy - Qy, t) - mu

    # Convolution for Sigma^R(kF, omega) using G0^R for k-Q state
    nB = nbose(Omegas, T)
    f_kmQ = fermi(xi_kmQ, T)
    weight = nB + f_kmQ

    SigmaR = np.zeros_like(omeg, dtype=np.complex128)
    for i, w in enumerate(omeg):
        denom = (w - Omegas - xi_kmQ) + 1j * eta
        integrand = Veff * (weight / denom)
        SigmaR[i] = (dOm / (2.0 * np.pi)) * np.sum(integrand)

    # Spectral functions
    G0R = 1.0 / (omeg + 1j * eta - xi_k)
    GR = 1.0 / (omeg + 1j * eta - xi_k - SigmaR)
    A0 = -(1.0/np.pi) * np.imag(G0R)
    A  = -(1.0/np.pi) * np.imag(GR)

    # Plot A0 vs A
    fig1, ax1 = plt.subplots(1, 1, figsize=(6.2, 3.2), dpi=CFG["dpi"], constrained_layout=True)
    ax1.plot(omeg, A0, label=r"$A_0(\mathbf{k}_F,\omega)$", lw=1.8)
    ax1.plot(omeg, A, label=r"$A(\mathbf{k}_F,\omega)$ (RPA toy)", lw=1.8)
    ax1.set_xlabel(r"$\omega$")
    ax1.set_ylabel(r"Spectral $A$ (arb.)")
    ax1.legend(frameon=False)
    out1 = figs_dir / "A_kF_rpa_vs_nonint.png"
    fig1.savefig(out1, bbox_inches="tight")
    print("Saved:", out1)

    # Plot Im Sigma^R
    fig2, ax2 = plt.subplots(1, 1, figsize=(6.2, 3.2), dpi=CFG["dpi"], constrained_layout=True)
    ax2.plot(omeg, np.imag(SigmaR), color='C3', lw=1.8)
    ax2.set_xlabel(r"$\omega$")
    ax2.set_ylabel(r"$\mathrm{Im}\,\Sigma^R(\mathbf{k}_F,\omega)$")
    out2 = figs_dir / "imSigma_kF.png"
    fig2.savefig(out2, bbox_inches="tight")
    print("Saved:", out2)


if __name__ == "__main__":
    main()
