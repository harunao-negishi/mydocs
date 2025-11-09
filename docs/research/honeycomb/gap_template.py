import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import TwoSlopeNorm

# --- Parameters ---
nk={nk} # type: ignore
nw={nw} # type: ignore
T={T} # type: ignore
U={U} # type: ignore
psym={psym} # type: ignore
tperp={tperp} # type: ignore
rfill={rfill} # type: ignore

files = [
    ("phisb-la-nk10-11-kz00.dat", "Band 1"),
    ("phisb-la-nk10-22-kz00.dat", "Band 2"),
    ("phisb-la-nk10-33-kz00.dat", "Band 3"),
    ("phisb-la-nk10-44-kz00.dat", "Band 4"),
]
output_file = f"plot_gap(tperp{tperp}, psym{psym}, U{U}, rfill{rfill}).png"

# --- Load all values to determine global color range ---
all_values = []
for filename, _ in files:
    data = np.loadtxt(filename)
    all_values.extend(data[:, 2])  # Re(gap)

vmin = np.min(all_values)
vmax = np.max(all_values)

# --- Use colormap centered at zero ---
cmap = plt.get_cmap("coolwarm")
norm = TwoSlopeNorm(vcenter=0.0, vmin=vmin, vmax=vmax)

b1 = np.array([np.sqrt(3)*np.pi, -np.pi])
b2 = np.array([np.sqrt(3)*np.pi,  np.pi])

fig, axes = plt.subplots(2, 2, figsize=(12, 6), constrained_layout=True)
axes_flat = axes.ravel()

for ax, (filename, title) in zip(axes_flat, files):
    data = np.loadtxt(filename)
    k1 = data[:, 0] / nk
    k2 = data[:, 1] / nk
    # --- (b1, b2)基底でk座標を計算 ---
    kx = k1 * b1[0] + k2 * b2[0]
    ky = k1 * b1[1] + k2 * b2[1]
    val = data[:, 2] 
    # ---六角形にブリルアンゾーンを切り取る---
    mask1 = (ky <= np.sqrt(3) * kx - 2 * np.pi) & (ky <= 0)
    kx[mask1] = kx[mask1] - b1[0]
    ky[mask1] = ky[mask1] - b1[1]

    mask2 = (ky >= -np.sqrt(3) * kx + 2 * np.pi) & (ky >= 0)
    kx[mask2] = kx[mask2] - b2[0]
    ky[mask2] = ky[mask2] - b2[1]

    mask3 = (ky >= np.sqrt(3) * kx + 2 * np.pi) & (ky >= 0)
    kx[mask3] = kx[mask3] + b1[0]
    ky[mask3] = ky[mask3] + b1[1]

    mask4 = (ky <= -np.sqrt(3) * kx - 2 * np.pi) & (ky <= 0)
    kx[mask4] = kx[mask4] + b2[0]
    ky[mask4] = ky[mask4] + b2[1]

    im = ax.scatter(kx, ky, c=val, cmap=cmap, norm=norm, s=35, edgecolors='none')
    ax.set_title(title)
    ax.set_xlabel("kx")
    ax.set_ylabel("ky")
    ax.set_aspect('equal')

fig.suptitle(f"gap_func(tperp{tperp}, psym{psym}, U{U}, rfill{rfill})")
# --- Add shared colorbar ---
cbar = fig.colorbar(im, ax=axes.ravel().tolist(), shrink=0.8, label="Re(gap)")
plt.savefig(output_file, dpi=150)
plt.close()
