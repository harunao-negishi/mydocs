import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

"""
Compute one-shot Matsubara self-energy Σ(k, iω0) using RPA effective interaction
V(q, iΩm) = (3/2) U^2 χs(q, iΩm) + (1/2) U^2 χc(q, iΩm) - U^2 χ0(q, iΩm),
where χs = χ0 / (1 - U χ0), χc = χ0 / (1 + U χ0).

We evaluate χ0(q, iΩm) via the Lindhard form after fermionic sum:
  χ0(q, iΩm) = (1/Nk) Σ_k [ f(ε_{k+q}) - f(ε_k) ] / [ iΩm - (ε_{k+q} - ε_k) ]
Handling the static uniform limit with the derivative: χ0(0, 0) = (1/Nk) Σ_k ( -∂f/∂ε_k ).

Then compute one-shot Σ(k, iω0) = (T/Nk) Σ_{q,m} V(q, iΩm) G0(k-q, iω0 - iΩm).
The sum over q is a 2D circular convolution for each m; we evaluate it with FFT2.

Outputs a figure comparing |G0(k, iω0)| vs |G_RPA(k, iω0)| at the lowest fermionic Matsubara.
"""

def dispersion_square_tb(kx, ky, t=1.0):
    return -2.0 * t * (np.cos(kx) + np.cos(ky))


def fermi(E, mu=0.0, T=0.05):
    x = (E - mu) / np.clip(T, 1e-12, None)
    # stable sigmoid
    x = np.clip(x, -60.0, 60.0)
    return 1.0 / (np.exp(x) + 1.0)


def minus_df_dE(E, mu=0.0, T=0.05):
    # -∂f/∂E = 1/(4T) sech^2((E-mu)/(2T))
    T = np.clip(T, 1e-12, None)
    x = (E - mu) / (2.0 * T)
    x = np.clip(x, -60.0, 60.0)
    sech2 = 1.0 / np.cosh(x)**2
    return sech2 / (4.0 * T)


def build_k_grid(Nk):
    # grid in [-pi, pi)
    vals = np.linspace(-np.pi, np.pi, Nk, endpoint=False)
    kx, ky = np.meshgrid(vals, vals, indexing='ij')
    return vals, kx, ky


def chi0_dynamic(qx_vals, qy_vals, kx, ky, eps_k, mu, T, boson_M):
    """
    Compute χ0(q, iΩm) for m = 0..M on the Matsubara axis using Lindhard formula.
    Returns array of shape (Nq, Nq, M+1).
    """
    Nk = kx.shape[0]
    Nq = len(qx_vals)
    f_k = fermi(eps_k, mu=mu, T=T)
    chi0 = np.zeros((Nq, Nq, boson_M + 1), dtype=np.complex128)

    for iq, qx in enumerate(qx_vals):
        for jq, qy in enumerate(qy_vals):
            eps_kq = dispersion_square_tb(kx + qx, ky + qy)
            f_kq = fermi(eps_kq, mu=mu, T=T)
            delta_eps = eps_kq - eps_k
            num = (f_kq - f_k)

            # m = 0 separately with derivative handling for q=0
            if iq == 0 and jq == 0:
                chi0[iq, jq, 0] = np.mean(minus_df_dE(eps_k, mu=mu, T=T))
            else:
                denom0 = -delta_eps  # iΩ0 = 0
                # Safe divide; where denom0 is ~0, fall back to derivative limit
                with np.errstate(divide='ignore', invalid='ignore'):
                    term0 = np.divide(num, denom0, out=np.zeros_like(num, dtype=np.complex128), where=np.abs(denom0) > 1e-12)
                # add derivative where denom ~ 0 (rare on discrete grid)
                mask = np.abs(denom0) <= 1e-12
                if np.any(mask):
                    term0[mask] = minus_df_dE(eps_k[mask], mu=mu, T=T)
                chi0[iq, jq, 0] = term0.mean()

            # m >= 1
            for m in range(1, boson_M + 1):
                Om = 2.0 * np.pi * m * T
                denom = 1j * Om - delta_eps
                chi0[iq, jq, m] = np.mean(num / denom)

    return chi0


def rpa_V_from_chi(chi0, U):
    """
    Given χ0(q, iΩm) with shape (Nq, Nq, M+1), return V(q, iΩm) with same shape.
    """
    chis = chi0 / (1.0 - U * chi0)
    chic = chi0 / (1.0 + U * chi0)
    V = 1.5 * (U**2) * chis + 0.5 * (U**2) * chic - (U**2) * chi0
    return V


def cconv2(a, b):
    """2D circular convolution via FFT2: (a * b)(k) = Σ_q a(q) b(k-q)."""
    return np.fft.ifft2(np.fft.fft2(a) * np.fft.fft2(b))


def compute_sigma_one_shot(eps_k, mu, T, U, V_qm, fermion_n=0):
    """
    Compute Σ(k, iω_n) one-shot using V(q, iΩ_m) and bare G0.
    V_qm: array (Nq, Nq, M+1), χ0-derived. n selects ω_n = (2n+1)πT; use n=0 by default.
    Returns Σ_k array shape (Nk, Nk) complex.
    """
    Nk = eps_k.shape[0]
    M = V_qm.shape[2] - 1
    wn = (2 * fermion_n + 1) * np.pi * T

    # Precompute G0(k, iω) arrays for needed frequencies per m
    def G0_of(iw):
        return 1.0 / (1j * iw - (eps_k - mu))

    Sigma = np.zeros_like(eps_k, dtype=np.complex128)

    # m = 0 term
    V0 = V_qm[:, :, 0]
    G0_w = G0_of(wn)
    conv0 = cconv2(V0, G0_w)
    Sigma += (T / (Nk * Nk)) * conv0

    # m >= 1 terms (use ±Ω_m symmetry)
    for m in range(1, M + 1):
        Om = 2.0 * np.pi * m * T
        Vm = V_qm[:, :, m]
        # ω - Ω_m
        G0_wm = G0_of(wn - Om)
        convm_minus = cconv2(Vm, G0_wm)
        # ω + Ω_m
        G0_wp = G0_of(wn + Om)
        convm_plus = cconv2(Vm, G0_wp)
        Sigma += (T / (Nk * Nk)) * (convm_minus + convm_plus)

    return Sigma


def main():
    # Parameters
    Nk = 41           # k- and q-grid size (odd preferred)
    T = 0.05
    mu = 0.0
    t = 1.0
    U = 0.8           # keep below Ucrit
    boson_M = 6       # number of positive bosonic Matsubara indices

    # Grids and energies
    q_vals, kx, ky = build_k_grid(Nk)
    eps_k = dispersion_square_tb(kx, ky, t=t)

    print(f"Building χ0(q, iΩ_m) for Nk={Nk}, M={boson_M} ...")
    chi0_qm = chi0_dynamic(q_vals, q_vals, kx, ky, eps_k, mu, T, boson_M)

    # Basic stability check near Ucrit using static χ0
    chi0_static = chi0_qm[:, :, 0].real
    max_chi0 = np.max(chi0_static)
    Ucrit_est = 1.0 / max_chi0 if max_chi0 > 0 else np.inf
    if U >= 0.95 * Ucrit_est:
        print(f"[warn] U ~ Ucrit (U={U:.3f}, Ucrit~{Ucrit_est:.3f}). Consider lowering U for stability.")

    print("Building RPA V(q, iΩ_m) ...")
    V_qm = rpa_V_from_chi(chi0_qm, U)

    print("Computing one-shot Σ(k, iω0) ...")
    Sigma_k = compute_sigma_one_shot(eps_k, mu, T, U, V_qm, fermion_n=0)

    # G0 and GRPA at lowest Matsubara
    wn0 = np.pi * T
    G0 = 1.0 / (1j * wn0 - (eps_k - mu))
    GRPA = 1.0 / (1j * wn0 - (eps_k - mu) - Sigma_k)

    abs_G0 = np.abs(G0)
    abs_GR = np.abs(GRPA)

    # Make figure directory next to this script
    script_dir = Path(__file__).resolve().parent
    figs_dir = script_dir.parent / "figs"
    figs_dir.mkdir(parents=True, exist_ok=True)

    # Plot side-by-side comparison
    vmax = np.percentile(np.concatenate([abs_G0.ravel(), abs_GR.ravel()]), 99.0)

    fig, axes = plt.subplots(1, 2, figsize=(9, 4), constrained_layout=True)
    im0 = axes[0].imshow(abs_G0.T, origin='lower', cmap='magma', vmin=0.0, vmax=vmax)
    axes[0].set_title(r"$|G_0(\mathbf{k}, i\omega_0)|$")
    im1 = axes[1].imshow(abs_GR.T, origin='lower', cmap='magma', vmin=0.0, vmax=vmax)
    axes[1].set_title(r"$|G_{\mathrm{RPA}}(\mathbf{k}, i\omega_0)|$")
    for ax in axes:
        ax.set_xticks([])
        ax.set_yticks([])
    cbar = fig.colorbar(im1, ax=axes, fraction=0.046, pad=0.04)
    cbar.set_label("magnitude")

    out_path = figs_dir / "g0_vs_grpa_matsubara_rpaSigma.png"
    fig.suptitle(f"Nk={Nk}, T={T}, mu={mu}, U={U}, M={boson_M}")
    fig.savefig(out_path, dpi=150)
    plt.close(fig)

    print(f"Saved: {out_path}")


if __name__ == "__main__":
    main()
