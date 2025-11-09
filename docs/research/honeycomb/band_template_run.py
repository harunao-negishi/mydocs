import numpy as np
import matplotlib.pyplot as plt

# ===========================
# パラメータ定義
# ===========================
a = 1.0
t = 1.0
tperp = 0.2
density = 100
Nk = 300
N_DOS = 500
rfill = 2

# --- 六角形BZ範囲 ---
kx_max = 4 * np.pi / (3 * a)
ky_max = 2 * np.pi / (a * np.sqrt(3))

# ===========================
# 1. 高対称点経路の生成
# ===========================
Gamma = np.array([0.0, 0.0])
K = np.array([kx_max, 0.0])
K2 = np.array([kx_max * np.cos(np.pi/3), kx_max * np.sin(np.pi/3)])
M = (K + K2) / 2
points = [Gamma, K, M, Gamma]
labels = ["$\\Gamma$", "K", "M", "$\\Gamma$"]

k_path = [points[0]]
tick_positions = [0]
x_axis = [0.0]
for i in range(len(points) - 1):
    start = points[i]
    end = points[i+1]
    for j in range(density):
        frac = (j+1) / density
        k_now = start + frac * (end - start)
        k_path.append(k_now)
        if len(k_path) > 1:
            dist = np.linalg.norm(k_path[-1] - k_path[-2])
            x_axis.append(x_axis[-1] + dist)
    tick_positions.append(x_axis[-1])
k_path = np.array(k_path)
x_axis = np.array(x_axis)

# ===========================
# 2. バンド構造 (経路上)
# ===========================
def f_k(kx, ky):
    delta = np.array([
        [0, a/np.sqrt(3)],
        [-a/2, -a/(2*np.sqrt(3))],
        [a/2, -a/(2*np.sqrt(3))]
    ])
    return sum(np.exp(1j * (kx*d[0] + ky*d[1])) for d in delta)

E_plus1, E_plus2, E_minus1, E_minus2 = [], [], [], []
for k in k_path:
    fk = f_k(k[0], k[1])
    e = t * np.abs(fk)
    E_plus2.append(e + tperp)
    E_plus1.append(e - tperp)
    E_minus2.append(-e + tperp)
    E_minus1.append(-e - tperp)
E_plus2 = np.array(E_plus2)
E_plus1 = np.array(E_plus1)
E_minus2 = np.array(E_minus2)
E_minus1 = np.array(E_minus1)

# ===========================
# 3. 全k空間グリッドとエネルギー
# ===========================
kx = np.linspace(-kx_max, kx_max, Nk)
ky = np.linspace(-ky_max, ky_max, Nk)
KX, KY = np.meshgrid(kx, ky, indexing='ij')

E1, E2, E3, E4 = [], [], [], []
mask_list = []
for i in range(Nk):
    for j in range(Nk):
        # 六角形BZ内のみ
        if (np.abs(KX[i,j]) / np.sqrt(3) + np.abs(KY[i,j]) < kx_max):
            fk = f_k(KX[i,j], KY[i,j])
            e = t * np.abs(fk)
            E2.append(e + tperp)
            E1.append(e - tperp)
            E4.append(-e + tperp)
            E3.append(-e - tperp)
            mask_list.append((i, j))  # BZ内のインデックス保存

E1 = np.array(E1)
E2 = np.array(E2)
E3 = np.array(E3)
E4 = np.array(E4)

# ===========================
# 4. DOS・フェルミエネルギー
# ===========================
all_E = np.concatenate([E1, E2, E3, E4])
e_min, e_max = all_E.min(), all_E.max()
de = (e_max - e_min) / N_DOS
dos = np.zeros(N_DOS + 1, dtype=int)
for e in all_E:
    k = int(np.round((e - e_min) / de))
    if 0 <= k <= N_DOS:
        dos[k] += 1

# フェルミエネルギー
Nk_total = len(E1)
band_num = 4    # AAバイレイヤー
N_state = Nk_total * band_num
n_filled = int((rfill / band_num) * N_state)
energy_sorted = np.sort(all_E)
ef = energy_sorted[n_filled]

# ===========================
# 5. フェルミ面マスク作成
# ===========================
FS1 = np.abs(E1 - ef) < de
FS2 = np.abs(E2 - ef) < de
FS3 = np.abs(E3 - ef) < de
FS4 = np.abs(E4 - ef) < de

kx_FS = np.array([KX[i,j] for (i,j) in mask_list])
ky_FS = np.array([KY[i,j] for (i,j) in mask_list])

# ===========================
# 6. プロット
# ===========================
fig, axs = plt.subplots(1, 3, figsize=(17, 5))

# --- 1. バンド図 ---
axs[0].plot(x_axis, E_plus1, color="b", label="E1")
axs[0].plot(x_axis, E_minus1, color="b")
axs[0].plot(x_axis, E_plus2, color="r", label="E2")
axs[0].plot(x_axis, E_minus2, color="r")
axs[0].axhline(ef, color='black', linestyle='--', label="$E_F$")
for pos in tick_positions:
    axs[0].axvline(pos, color='gray', linestyle='--', linewidth=1)
axs[0].set_xticks(tick_positions, labels, fontsize=14)
axs[0].set_ylabel("Energy")
axs[0].set_xlabel("k-path")
axs[0].set_title("AA-bilayer Band Structure\n$t_\\perp$={tperp}, rfill={rfill}".format(tperp=tperp, rfill=rfill))
axs[0].legend()

# --- 2. DOS ---
energies_dos = np.linspace(e_min, e_max, N_DOS+1)
axs[1].plot(energies_dos, dos, drawstyle='steps-mid', color='blue')
axs[1].axvline(ef, color="black", linestyle="--", label="$E_F$")
axs[1].set_xlabel("Energy")
axs[1].set_ylabel("DOS")
axs[1].set_title("DOS\n$t_\\perp$={tperp}, rfill={rfill}".format(tperp=tperp, rfill=rfill))
axs[1].legend()

# --- 3. フェルミ面 ---
axs[2].scatter(kx_FS[FS1], ky_FS[FS1], color='b', s=2, label='FS1')
axs[2].scatter(kx_FS[FS2], ky_FS[FS2], color='r', s=2, label='FS2')
axs[2].scatter(kx_FS[FS3], ky_FS[FS3], color='b', s=2)
axs[2].scatter(kx_FS[FS4], ky_FS[FS4], color='r', s=2)
axs[2].set_xlabel("$k_x$")
axs[2].set_ylabel("$k_y$")
axs[2].set_title("Fermi Surface\n$t_\\perp$={tperp}, rfill={rfill}".format(tperp=tperp, rfill=rfill))
axs[2].set_aspect('equal')
fs_labels = [
    {"label": "$\\Gamma$", "pos": (0, 0)},
    {"label": "K", "pos": (kx_max, 0)},
    {"label": "M", "pos": ((kx_max + K2[0]) / 2, (0 + K2[1]) / 2)}
]
for item in fs_labels:
    axs[2].text(item["pos"][0], item["pos"][1], item["label"],
                fontsize=15, color='k', ha='center', va='center', fontweight='bold', zorder=12)
bz_radius = kx_max
angles = np.linspace(0, 2 * np.pi, 7)
hx = bz_radius * np.cos(angles)
hy = bz_radius * np.sin(angles)
axs[2].plot(hx, hy, color='k', lw=2, linestyle='--', label='BZ boundary')
axs[2].legend(markerscale=5, fontsize=12)

plt.tight_layout()
plt.savefig("tp{tperp}_fill{rfill}_AA_honeycomb_band_dos_fs.png".format(tperp=tperp, rfill=rfill), dpi=300)
