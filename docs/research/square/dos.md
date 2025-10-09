# 状態密度（DOS: Density of States）

## 一般論
バンド分散 $\varepsilon(\mathbf{k})$ が与えられているとき、状態密度 $D(E)$ は次式で定義されます：

$$
D(E) = \frac{1}{N} \sum_{\mathbf{k}} \delta(E - \varepsilon(\mathbf{k}))
$$

連続系の場合は積分で表されます：

$$
D(E) = \int_{BZ} \frac{d^d k}{(2\pi)^d} \delta(E - \varepsilon(\mathbf{k}))
$$

ここで $BZ$ はブリルアンゾーン、$d$ は次元数です。

---

## 2次元正方格子のバンド分散
2次元正方格子の最近接ホッピングのみの場合、バンド分散は

$$
\varepsilon(\mathbf{k}) = -2t (\cos k_x + \cos k_y)
$$

となります。

---

## 解析的なDOSの導出
この場合、DOSは楕円積分を使って解析的に求めることができます。

$$
D(E) = \frac{1}{2\pi^2 t} K\left(\sqrt{1 - \left(\frac{E}{4t}\right)^2}\right)
$$

ここで $K$ は第1種完全楕円積分です。

---

## 数値的なDOSの計算例
$\mathbf{k}$点を格子状に取り、ヒストグラムでDOSを近似します。

```python
import numpy as np
import matplotlib.pyplot as plt

N = 400
kx = np.linspace(-np.pi, np.pi, N)
ky = np.linspace(-np.pi, np.pi, N)
KX, KY = np.meshgrid(kx, ky)
E = -2 * (np.cos(KX) + np.cos(KY))

hist, bins = np.histogram(E.flatten(), bins=200, density=True)
E_center = 0.5 * (bins[1:] + bins[:-1])

plt.plot(E_center, hist)
plt.xlabel('Energy E')
plt.ylabel('DOS D(E)')
plt.title('2D Square Lattice DOS (Numerical)')
plt.show()
```

---

## 参考
- 楕円積分による解析式は文献や教科書を参照
- 数値計算はPython, MATLAB等で容易に実装可能
