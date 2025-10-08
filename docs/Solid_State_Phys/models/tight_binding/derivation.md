# 原子軌道展開とホッピングの導出

## 1. 原子軌道を基底とする波動関数展開

電子の波動関数を原子軌道 $\phi_i(\mathbf r - \mathbf R_i)$ の線形結合で表す：

$$
\psi_k(\mathbf r) = \frac{1}{\sqrt{N}} \sum_i e^{i\mathbf k\cdot\mathbf R_i} \phi(\mathbf r - \mathbf R_i)
$$

これをハミルトニアン
$$
H = \frac{p^2}{2m} + V(\mathbf r)
$$
に代入し、$H$ の行列要素をとる：

$$
H_{ij} = \langle \phi_i | H | \phi_j \rangle
       = \begin{cases}
         \epsilon_0 & (i=j) \\
         -t & (i,j:\text{隣接}) \\
         0 & (\text{その他})
         \end{cases}
$$

---

## 2. エネルギー固有値の導出（1D鎖）

波数空間で対角化すると：

$$
E(k) = \epsilon_0 - 2t\cos(ka)
$$

→ バンド幅：$W = 4t$

 ここでの $t$ は波動関数の重なり積分から決まる：
> $t = -\int \phi_i^*(r) H \phi_{i+1}(r)\,dr$  
> 原子間距離が大きいほど $t$ は急減し、バンドが狭くなる。
