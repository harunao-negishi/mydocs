# Green関数講義ノート Part 4

- 元資料: `GreenFunction_diagram.pdf`
- 範囲: 第4章 (超伝導)

## 4.1 南部表示と超伝導状態のグリーン関数

### 南部ベクトルの導入

超伝導状態では通常の電子の生成・消滅に加えて、電子対（ペア）の生成・消滅が重要となる。そこで、生成・消滅演算子を 1 つのベクトルにまとめた南部表示（Nambu representation）を導入する：

$$
\Psi(x) = \begin{pmatrix}
 c_{r\alpha_1}(\tau) \\
 c_{r\alpha_2}(\tau) \\
 \vdots \\
 c_{r\alpha_N}(\tau) \\
 c^{\dagger}_{r\alpha_1}(\tau) \\
 c^{\dagger}_{r\alpha_2}(\tau) \\
 \vdots \\
 c^{\dagger}_{r\alpha_N}(\tau)
\end{pmatrix},\tag{4.1}
$$

ここで $N$ は内部自由度（スピンや軌道など）の数である。南部表示により、電子とホールを統一的に扱うことができる。

### 南部グリーン関数の定義

南部ベクトルを用いると、グリーン関数は

$$
\mathcal{G}(x,x') = -\langle T_{\tau}\, \Psi(x)\, \Psi^{\dagger}(x') \rangle
= \begin{pmatrix}
 G(x,x') & F(x,x') \\
 \overline{F}(x,x') & \overline{G}(x,x')
\end{pmatrix} \tag{4.2}
$$

と書ける。ブロック行列の成分は次で定義される：

$$
G_{\alpha\beta}(x,x') = -\langle T_{\tau}\, c_{r\alpha}(\tau)\, c^{\dagger}_{r'\beta}(\tau') \rangle \tag{4.3}
$$

$$
\overline{G}_{\alpha\beta}(x,x') = -\langle T_{\tau}\, c^{\dagger}_{r\alpha}(\tau)\, c_{r'\beta}(\tau') \rangle \tag{4.4}
$$

$$
F_{\alpha\beta}(x,x') = -\langle T_{\tau}\, c_{r\alpha}(\tau)\, c_{r'\beta}(\tau') \rangle \tag{4.5}
$$

$$
\overline{F}_{\alpha\beta}(x,x') = -\langle T_{\tau}\, c^{\dagger}_{r\alpha}(\tau)\, c^{\dagger}_{r'\beta}(\tau') \rangle \tag{4.6}
$$

ここで $G,\overline{G}$ は正常グリーン関数（normal）、$F,\overline{F}$ は異常グリーン関数（anomalous）である。

### 対称性関係

粒子とホールの交換対称性から、

$$
\overline{G}_{\alpha\beta}(x,x') = -\, G_{\beta\alpha}(x',x) \tag{4.7}
$$

が成り立つ。また、虚時間ハイゼンベルグ表示のエルミート共役 $\{A(\tau)\}^{\dagger} = A^{\dagger}(-\tau)$ を用いると、

$$
\overline{F}_{\alpha\beta}(x,x') = F^{*}_{\beta\alpha}(\tau,\tau';\, r',r) \tag{4.8}
$$

が得られる。

さらに並進対称性と反転対称性を仮定して Fourier 変換すると、

$$
\overline{G}_{\alpha\beta}(k) = -\, G_{\beta\alpha}(-k), \qquad
\overline{F}_{\alpha\beta}(k) = F^{*}_{\beta\alpha}(-k) \tag{4.9, 4.10}
$$

が成立する。これにより粒子–ホール対称性が明示的になる。

### 自己エネルギーの拡張（南部表示）

南部表示では、自己エネルギーもブロック行列として拡張される：

$$
\Sigma(k) = \begin{pmatrix}
 \Sigma(k) & \Delta(k) \\
 \overline{\Delta}(k) & \overline{\Sigma}(k)
\end{pmatrix}.\tag{4.11}
$$

$\Sigma,\overline{\Sigma}$ は正常自己エネルギー、$\Delta,\overline{\Delta}$ は異常自己エネルギーであり、$G\leftrightarrow\overline{G}$、$F\leftrightarrow\overline{F}$ と同様の関係性をもつ。

### Dyson 方程式（南部形式）

通常の Dyson 方程式 $G=G_0+G_0\Sigma G$ を南部表示へ拡張すると、

$$
\mathcal{G}(k) = \mathcal{G}_0(k) + \mathcal{G}_0(k)\, \Sigma(k)\, \mathcal{G}_0(k)
 + \mathcal{G}_0(k)\, \Sigma(k)\, \mathcal{G}_0(k)\, \Sigma(k)\, \mathcal{G}_0(k) + \cdots
 = \mathcal{G}_0(k) + \mathcal{G}_0(k)\, \Sigma(k)\, \mathcal{G}(k).\tag{4.12}
$$

相互作用がない場合には $F=\overline{F}=0$ で、自由グリーン関数はブロック対角：

$$
\mathcal{G}_0(k) = \begin{pmatrix}
 G_0(k) & 0 \\
 0 & \overline{G}_0(k)
\end{pmatrix}.\tag{4.13}
$$

これが常伝導状態の南部形式に対応する。

## 4.2 エリアシュベルグ方程式（Eliashberg equation）

超伝導状態では、異常グリーン関数 $F,\,\overline{F}$（生成・消滅演算子のペア相関）がダイアグラム展開に現れ、常伝導に比べて構造が複雑になる。しかし、正常自己エネルギー $\Sigma$ と異常自己エネルギー $\Delta$ は、形式的に次のように書ける：

$$
\Sigma_{\alpha\gamma}(k)
= \sum_{\beta\lambda} \sum_{k',q}\, V^{\Sigma}_{\alpha\beta\gamma\lambda}(k,k',q)\, G_{\beta\lambda}(k'+q),\tag{4.14}
$$

$$
\Delta_{\alpha\lambda}(k)
= \sum_{\beta\gamma} \sum_{k',q}\, V^{\Delta}_{\alpha\beta\gamma\lambda}(k,k',q)\, F_{\beta\gamma}(k'+q).\tag{4.15}
$$

ここで $V^{\Sigma},\,V^{\Delta}$ は、それぞれ正常・異常自己エネルギーを与える（有効）頂点である。式 (4.12) の Dyson 方程式と (4.14)–(4.15) を連立したものをエリアシュベルグ方程式と呼ぶ。一般には $V^{\Sigma},\,V^{\Delta}$ の中に $F$ も現れるため、常伝導の議論をそのまま流用はできない。ただし、$F$ や $\Delta$ が十分小さい（転移温度 $T_c$ 付近）では常伝導近似が有効になる。

### 4.2.1 Dyson 方程式（南部表示）と成分形式

南部表示での Dyson $\,\mathcal{G}=\mathcal{G}_0+\mathcal{G}_0\Sigma\,\mathcal{G}\,$から、成分を明示すると

$$
\begin{pmatrix}
G & F\\
\overline{F} & \overline{G}
\end{pmatrix}
=
\begin{pmatrix}
G_0 + G_0\Sigma\, G + G_0\Delta\, \overline{F} & \quad G_0\Sigma\, F + G_0\Delta\, \overline{G} \\
\overline{G}_0\overline{\Delta}\, G + \overline{G}_0\overline{\Sigma}\, \overline{F} & \quad \overline{G}_0 + \overline{G}_0\overline{\Delta}\, F + \overline{G}_0\overline{\Sigma}\, \overline{G}
\end{pmatrix}.\tag{4.16}
$$

$T_c$ 付近で $F,\,\Delta$ を 1 次まで残す線形化では

$$
\begin{pmatrix}
G & F\\
\overline{F} & \overline{G}
\end{pmatrix}
=
\begin{pmatrix}
G_0 + G_0\Sigma\, G & \quad G_0\Sigma\, F + G_0\Delta\, \overline{G} \\
\overline{G}_0\overline{\Delta}\, G + \overline{G}_0\overline{\Sigma}\, \overline{F} & \quad \overline{G}_0 + \overline{G}_0\overline{\Sigma}\, \overline{G}
\end{pmatrix}.\tag{4.17}
$$

右上ブロックから

$$
F(k) = G_0(k)\,\Sigma(k)\,F(k) + G_0(k)\,\Delta(k)\, \overline{G}(k)
\ \Rightarrow\ [G_0^{-1}(k)-\Sigma(k)]\,F(k) = \Delta(k)\, \overline{G}(k)
\ \Rightarrow\ F(k) = G(k)\,\Delta(k)\, \overline{G}(k).\tag{4.18}
$$

ここで、$ [G_0^{-1}(k)-\Sigma(k)] = G^{-1}(k) $ は、ダイソン方程式からの結果を用いた。
同様に $\overline{F}$ についても成り立つ。したがって最終的に

$$
\begin{pmatrix}
G & F\\
\overline{F} & \overline{G}
\end{pmatrix}
=
\begin{pmatrix}
G_0 + G_0\Sigma\, G & \quad G\,\Delta\, \overline{G} \\
\overline{G}\,\overline{\Delta}\, G & \quad \overline{G}_0 + \overline{G}_0\overline{\Sigma}\, \overline{G}
\end{pmatrix},\qquad
G=[G_0^{-1}-\Sigma]^{-1},\; \overline{G}=[\overline{G}_0^{-1}-\overline{\Sigma}]^{-1}.\tag{4.19}
$$

### 4.2.2 運動方程式から見た $\Delta$ の構造

まずハイゼンベルグ表示の運動方程式

$$
\frac{\partial}{\partial\tau} c_{r\alpha}(\tau)
= -\sum_{r''\gamma} (t_{rr''\alpha\gamma}-\mu\,\delta_{rr''}\delta_{\alpha\gamma})\, c_{r''\gamma}(\tau)
- e^{\tau H}\,[c_{r\alpha}, H_{\mathrm{int}}] \, e^{-\tau H} \tag{4.20}
$$

から、異常グリーン関数 $F_{\alpha\beta}(r,r',\tau)(=\langle T_{\tau}\, c_{r\alpha}(\tau)\, c_{r'\beta}(\tau') \rangle )$ の運動方程式は

$$
\frac{\partial}{\partial\tau} F_{\alpha\beta}(r,r',\tau)
= -\sum_{r''\gamma} (t_{rr''\alpha\gamma}-\mu\,\delta_{rr''}\delta_{\alpha\gamma})\, F_{\gamma\beta}(r'',r',\tau)
- \langle -T_{\tau}\, e^{\tau H}[c_{r\alpha}, H_{\mathrm{int}}]e^{-\tau H} \, c_{r'\beta}\rangle.\tag{4.21}
$$

一方、(4.16) 右上成分 $ F(k) = G_0(k)\,\Sigma(k)\,F(k) + G_0(k)\,\Delta(k)\, \overline{G}(k) $と比較すると

$$
\langle -T_{\tau}\, e^{\tau H}[c_{r\alpha}, H_{\mathrm{int}}]e^{-\tau H} \, c_{r'\beta} \rangle
= \sum_{r''\gamma}\! \int d\tau''\, \Sigma_{\alpha\gamma}(r,r'',\tau-\tau'')\, F_{\gamma\beta}(r'',r',\tau'')
 + \sum_{r''\gamma}\! \int d\tau''\, \Delta_{\alpha\gamma}(r,r'',\tau-\tau'')\, \overline{G}_{\gamma\beta}(r'',r',\tau'').\tag{4.22}
$$

他方、相互作用 $H_{\mathrm{int}}$ に対して交換関係を用いると

$$
\langle -T_{\tau}\, e^{\tau H}[c_{r\alpha}, H_{\mathrm{int}}]e^{-\tau H} \, c_{r'\beta} \rangle
= \tfrac{1}{2}\! \sum_{\beta'\gamma'\lambda'} U_{\alpha\beta'\gamma'\lambda'}\, \langle T_{\tau}\, c_{r\gamma'}(\tau) c^{\dagger}_{r\lambda'}(\tau) c_{r\beta'}(\tau) c_{r'\beta} \rangle
 + \tfrac{1}{2}\! \sum_{\beta'\lambda'} U_{\alpha\lambda'\beta'\lambda'}\, \langle T_{\tau}\, c_{r\beta'}(\tau) c_{r'\beta} \rangle.\tag{4.23}
$$

!!! note "式 (4.22) の導出の見取り図"
	式 (4.21) は左辺を自由部分の作用素 $\mathcal{L}\equiv \partial_\tau - (t-\mu)$ として
	$\mathcal{L}\,F = \text{(右辺第2項)}$ と見なせる（右辺第1項は $\mathcal{L}$ を $F$ に作用させたもの）。
	自由グリーン関数 $G_0$ は $\mathcal{L}$ の逆作用素で、畳み込みの意味で $\mathcal{L}\otimes G_0 = \delta$ を満たす。
	両辺に $G_0$ を作用させると $F = G_0 \otimes \{\text{(右辺第2項)}\}$ が得られ、
	その“源”$\{\text{(右辺第2項)}\}$ を自己エネルギーの成分に分解して $\Sigma\otimes F + \Delta\otimes \overline{G}$ と書けば、
	ちょうど式 (4.22) の畳み込み表示（$\sum_{r''\gamma}\int d\tau''$）になる、という見取り図で理解できる。

ここで、異常 2 体グリーン関数を

$$
	ilde{G}^{(2)}_{\alpha\beta\gamma\lambda}(r_1,r_2,r_3,r_4;\tau_1,\tau_2,\tau_3,\tau_4)
	ilde{G}^{(2)}_{\alpha\beta\gamma\lambda}(r_1,r_2,r_3,r_4;\tau_1,\tau_2,\tau_3,\tau_4)
$$

と定める（記号と順序は便宜に合わせた）。$F$ を 1 次で残す近似では（crossing を含めて）

$$
\begin{aligned}
	ilde{G}^{(2)}_{\alpha\beta\gamma\lambda}(x_1,x_2,x_3,x_4)
&= G_{\alpha\beta}(x_1,x_2)F_{\lambda\gamma}(x_4,x_3)
 - F_{\alpha\gamma}(x_1,x_3)G_{\lambda\beta}(x_4,x_2)
 + F_{\alpha\lambda}(x_1,x_4)G_{\gamma\beta}(x_3,x_2) \\
&\quad - G_{\alpha\alpha'}G_{\beta'\beta}\, F_{\alpha'\beta'\gamma'\lambda'}\, F_{\gamma'\gamma}\, G_{\lambda\lambda'}
 + G_{\alpha\alpha'}G_{\beta'\beta}\, F_{\alpha'\beta'\gamma'\lambda'}\, F_{\lambda\gamma'}\, G_{\gamma\lambda'} \\
&\quad + F_{\alpha\gamma'}G_{\beta'\beta}\, F_{\alpha'\beta'\gamma'\lambda'}\, G_{\gamma\alpha'} G_{\lambda\lambda'}
 - 2\, G_{\alpha\alpha'}G_{\beta'\beta}\, \tilde{F}_{\alpha'\beta'\gamma'\lambda'}\, G_{\gamma\gamma'} G_{\lambda\lambda'}.
\end{aligned}\tag{4.25}
$$

最後の $\tilde{F}$ は内部に $F$ を 1 つだけ含む異常フル頂点（crossing 対称性より 2 通りの寄与をまとめて係数 2）。(4.25) を (4.23) に代入し、crossing に基づく合体も含めて整理すると、正常自己エネルギー（常伝導 3.4 節と同様の形）

$$
\Sigma_{\alpha\beta}(k)
= - \sum_{\gamma\lambda} U_{\alpha\gamma\beta\lambda}\, \sum_{k} G_{\gamma\lambda}(k)\, e^{-i\omega(-0)}
 - \tfrac{1}{2} \sum_{k' q} F_{\alpha\beta'\gamma'\lambda'}(k,k',q)\, G_{\gamma'\alpha''}(k') G_{\beta''\lambda'}(k'+q)\, U_{\alpha''\beta''\beta\lambda''}\, G_{\beta'\lambda''}(k+q),\tag{4.27}
$$

および異常自己エネルギー

$$
\begin{aligned}
\Delta_{\alpha\beta}(k)
&= -\tfrac{1}{2} \sum_{\beta'\gamma'} U_{\alpha\beta'\gamma'\beta}\, \sum_k F_{\gamma'\beta'}(k) \\
&\quad - \sum_{k' q} U_{\alpha\beta'\gamma'\lambda'}\, G_{\gamma'\alpha''}(k') G_{\beta''\lambda'}(k'+q)\, F_{\alpha''\beta''\gamma''\beta}(k',k,q)\, F_{\beta'\gamma''}(k+q) \\
&\quad + \sum_{k' q} U_{\alpha\beta'\gamma'\lambda'}\, G_{\gamma'\alpha''}(k') G_{\beta''\lambda'}(k'+q)\, \tilde{F}_{\alpha''\beta''\gamma''\lambda''}(k,k',q)\, G_{\beta\gamma''}(k+q),
\end{aligned}\tag{4.28}
$$

が得られる。ここで (4.28) 右辺第 3 項は、$\tilde{F}$ 内部の $F$ を変数変換で外に“出す”と形式的に (4.15) の形へ吸収できる。このとき $V^{\Delta}$ の核に $F$ は含まれず、$\Delta(k)$ についての線形方程式になる。これが線形化エリアシュベルグ方程式（linearized Eliashberg equation）。

直感として、$T_c$ 付近では $F,\Delta$ が小さいため、$\Delta$ に関する固有値問題 $\,\lambda(T)\,\Delta = K[\Delta]$ に落ち、$\lambda(T_c)=1$ を満たす温度が $T_c$ である。

### 4.2.3 近似とチャネルの役割（概念メモ）

$\tilde{F}$ には ph や $\overline{ph}$ が途中で pp チャネルに切り替わるような構造が混ざる。多くの場合、ph 系（スピン・電荷）が運ぶ一般化波数と pp 系（ペア）が運ぶ一般化波数は異なる。よって $T_c$ 付近の線形化では、$\tilde{F}$ 由来の複雑な混成は影響が小さいとみなせることが多い。実務上は、常伝導で構築した有効相互作用（$\chi_{s/c}$ など）から $V^{\Delta}$ を作り、$\Delta$ の固有方程式を解くのが定番である。

### 4.2.4 実務的な計算形（よく使う最終形）

スカラー記法（内部自由度を絞った想定）で、Matsubara 和・Brillouin ゾーン和をまとめると、線形化 Eliashberg 方程式は

$$
\Delta(k) = -\, \frac{T}{N_k} \sum_{k'} V^{\Delta}(k,k')\, G(k')\, \overline{G}(k')\, \Delta(k').\tag{4.29}
$$

ここで $G\,\overline{G} \sim |G|^2$ はペア伝播の重み。離散化すると固有値問題 $\lambda\, \Delta = \widehat{K}^{\Delta}[\Delta]$ で、$\lambda(T_c)=1$ が転移温度となる。

注：上式の核 $V^{\Delta}$ は、しばしばスピン揺らぎ（$\propto U^2\chi_s$）や電荷揺らぎ（$\propto -U^2\chi_c$）など、常伝導で評価した感受率から組む（RPA/FLEX の流儀）。