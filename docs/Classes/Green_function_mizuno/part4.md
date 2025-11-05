# Green関数講義ノート Part 4

- 元資料: `GreenFunction_diagram.pdf`
- 範囲: 第4章 (超伝導)

## 4.1 南部表示（Nambu representation）

本節では、南部表示の導入とその主要な帰結（各成分の定義・対称性・自己エネルギーの分類）を整理する。超伝導では通常の粒子のみの扱いに加えてペア（粒子–粒子、粒子–正孔）の相関が重要になるため、粒子と正孔をまとめた 2N 成分のスピノルを用いると議論が統一的かつ簡潔になる。

### 4.1.1 南部スピノルの定義

生成・消滅演算子を縦に並べた 2N 成分ベクトル（南部スピノル）を導入する：

$$
\Psi(x)=\begin{pmatrix}
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

ここで $N$ は内部自由度（スピンや軌道など）の数。上半分が粒子（electron）成分、下半分が正孔（hole, creation operator）成分である。

> 意味合い：この表現により「電子伝搬」と「ペア（異常）伝搬」を同じ行列形式で扱えるようになる。

### 4.1.2 南部グリーン関数 — 成分定義

南部スピノルを用いると、時間順序付きグリーン関数は 2×2 ブロック行列で表せる：

$$
\mathcal{G}(x,x') = -\langle T_{\tau}\,\Psi(x)\,\Psi^{\dagger}(x')\rangle
=\begin{pmatrix}
 G(x,x') & F(x,x') \\
 \overline{F}(x,x') & \overline{G}(x,x')
\end{pmatrix}.\tag{4.2}
$$

各成分は通常次のように定義される（時間順序付き期待値、等時刻極限の記法を含む）：

$$
G_{\alpha\beta}(x,x') = -\langle T_{\tau}\, c_{r\alpha}(\tau)\, c^{\dagger}_{r'\beta}(\tau') \rangle,\tag{4.3}
$$

$$
\overline{G}_{\alpha\beta}(x,x') = -\langle T_{\tau}\, c^{\dagger}_{r\alpha}(\tau)\, c_{r'\beta}(\tau') \rangle,\tag{4.4}
$$

$$
F_{\alpha\beta}(x,x') = -\langle T_{\tau}\, c_{r\alpha}(\tau)\, c_{r'\beta}(\tau') \rangle,\tag{4.5}
$$

$$
\overline{F}_{\alpha\beta}(x,x') = -\langle T_{\tau}\, c^{\dagger}_{r\alpha}(\tau)\, c^{\dagger}_{r'\beta}(\tau') \rangle.\tag{4.6}
$$

名称（要点）:
- $G,\overline{G}$: 正常グリーン関数（電子／正孔の伝搬）
- $F,\overline{F}$: 異常グリーン関数（ペアの生成・消滅、クーパー対に対応）

### 4.1.3 成分間の対称性

基本的な演算子性質と時間順序性から、成分間には次の関係が成り立つ：

粒子–正孔変換（演算子の反交換と時間順序を利用）により

$$
\overline{G}_{\alpha\beta}(x,x') = -\, G_{\beta\alpha}(x',x).\tag{4.7}
$$

異常成分は虚時間ハイゼンベルグ表示の共役性から

$$
\overline{F}_{\alpha\beta}(x,x') = F^{*}_{\beta\alpha}(-x',-x).\tag{4.8}
$$

さらに並進対称性・時間平行移動・反転対称性を仮定してフーリエ変換すると、波数・マツバラ周波数表現では

$$
\overline{G}_{\alpha\beta}(k) = -\, G_{\beta\alpha}(-k),\qquad
\overline{F}_{\alpha\beta}(k) = F^{*}_{\beta\alpha}(-k).\tag{4.9--4.10}
$$

これらは南部表示における粒子–正孔対称性と異常成分の共役関係を明示する。

### 4.1.4 常伝導と超伝導の識別

状態別に非ゼロとなる相関は次のように区別できる：

- 常伝導（normal）：$\langle c c \rangle = \langle c^{\dagger} c^{\dagger} \rangle = 0$（異常成分は消える）
- 超伝導（superconducting）：$\langle c c \rangle,\;\langle c^{\dagger} c^{\dagger} \rangle \neq 0$（$F,\overline{F}$ が有限）

したがって常伝導では南部グリーン関数はブロック対角（$F=\overline{F}=0$）、超伝導では異常ブロックが現れ行列構造が本質的になる。

### 4.1.5 ダイアグラム展開と自己エネルギーの分類

場の理論的なダイアグラム展開において「1 本の自由伝搬線を切ると 2 つに分かれない図」の集合を自己エネルギーと定義したが、南部表示では伝搬線が 4 種類存在する：

- $G_0$（粒子線）
- $\overline{G}_0$（正孔線）
- $F_0,\;\overline{F}_0$（ペア線、異常伝搬）

これに対応して自己エネルギーも拡張され、南部空間の 2×2 行列として

$$
\Sigma(k)=\begin{pmatrix}
 \Sigma(k) & \Delta(k) \\
 \overline{\Delta}(k) & \overline{\Sigma}(k)
\end{pmatrix} \tag{4.11 revisited}
$$

を導入する。ここで
- $\Sigma,\overline{\Sigma}$ は正常自己エネルギー（電子／正孔の単粒子補正）
- $\Delta,\overline{\Delta}$ は異常自己エネルギー（ペアポテンシャル、しばしばギャップ関数と同値）

図式的にはそれぞれ異なる種類の伝搬線を切ったときに分離しない部分集合を集めることで対応する自己エネルギー成分が得られる。

### 4.1.6 Dyson 方程式（南部形式）

南部形式の Dyson 方程式は行列形式で通常と同じ形を保つ：

$$
\mathcal{G}(k)=\mathcal{G}_0(k)+\mathcal{G}_0(k)\,\Sigma(k)\,\mathcal{G}(k),\tag{4.12}
$$

展開すると全ての自己エネルギー挿入を含む無限級数になる。相互作用がない極限では $\Delta=0$ であり、自由グリーン関数はブロック対角：

$$
\mathcal{G}_0(k)=\begin{pmatrix}G_0(k)&0\\0&\overline{G}_0(k)\end{pmatrix}.\tag{4.13}
$$

### 4.1.7 要点のまとめ

1. 南部スピノルは粒子と正孔をまとめることで、正常・異常成分を 2×2 行列で統一的に扱える。 
2. 異常グリーン関数 $F,\overline{F}$ は超伝導の本質であり、$\Delta$ はその自己エネルギー（ギャップ）に対応する。 
3. 成分間の共役・粒子–正孔対称性（(4.7)–(4.10)）は解析や近似（RPA, Eliashberg など）で重要な制約を与える。

以上を踏まえて、次節ではエリアシュベルグ方程式へつなげるための要素（自己エネルギー項の一般形）へ進む。

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

## 4.3 U(1) 対称性（ゲージ対称性と粒子数）

🧭 概要

超伝導状態では異常グリーン関数 $F,\overline{F}$ が有限になります。これは $F\sim\langle c c\rangle$ が「2つの電子を同時に作る（あるいは消す）」相関を表し、粒子数を変化させる操作に対応するため、粒子数が定まっていないことを意味します。本節では U(1) ゲージ対称性（粒子数保存）がどのように表現され、それが破れるとは何を意味するかを整理します。

### 4.3.1 U(1) ゲージ変換

電子生成・消滅演算子に対する位相変換（ゲージ変換）を次のように定義します：

$$
U^{\dagger}(\theta)\, c_{r\alpha}\, U(\theta) = e^{-i\theta}\, c_{r\alpha}.\tag{4.30}
$$

ここで $U(\theta)$ は一粒子状態の位相を $\theta$ だけ回転させるユニタリ演算子です。

### 4.3.2 ハミルトニアンの対称性と粒子数生成子

ハミルトニアン $H$ がこの変換に不変であれば

$$
U^{\dagger}(\theta)\, H\, U(\theta) = H,\tag{4.31}
$$

系は U(1) ゲージ対称性を持ちます。この対称性の生成子が粒子数演算子 $N$ であり、

$$
N = \sum_{r\alpha} c^{\dagger}_{r\alpha} c_{r\alpha},\qquad U(\theta)=e^{i\theta N}.\tag{4.32}
$$

U(1) 対称性があるということは物理的には粒子数保存を意味し、$[H,N]=0$ が成り立ちます。

### 4.3.3 粒子数固有状態の位相変換

粒子数 $N$ が定まった状態を

$$
|\Psi_N\rangle = \prod_{j=1}^N c^{\dagger}_{r_j\alpha_j}\,|0\rangle \tag{4.33}
$$

と表すと、この状態にゲージ変換を作用させると

$$
U(\theta)|\Psi_N\rangle = e^{iN\theta} |\Psi_N\rangle.\tag{4.34}
$$

つまり粒子数 $N$ の状態は全体位相 $e^{iN\theta}$ を受け取るだけで物理状態は不変です。これは粒子数が確定している限り U(1) は保存されていることを示します。

### 4.3.4 超伝導と U(1) の自発的破れ

超伝導状態では

$$
F\equiv\langle c c \rangle \neq 0.
$$

この量はゲージ変換で次のように変化します：

$$
U^{\dagger}(\theta)\, F\, U(\theta) = e^{-2i\theta}\, F.\tag{4.35}
$$

したがって $F\neq0$ の状態はもはや $U(\theta)$ に不変ではありません。すなわち U(1) ゲージ対称性が自発的に破れている（spontaneous symmetry breaking）ことになります。

直感的には、常伝導状態は粒子数 $N$ の固有状態であるのに対し、超伝導状態は $N,N\pm2,N\pm4,\dots$ の重ね合わせであり、粒子数の揺らぎを伴う代わりにマクロな位相（秩序パラメータの位相）が確定します。

### 4.3.5 まとめ（要点）

- ゲージ変換 $c\to e^{-i\theta}c$ をハミルトニアンが保持する場合、系は U(1)（粒子数保存）対称性を持つ。 
- 粒子数固有状態は全体位相 $e^{iN\theta}$ を受け取るが物理的に不変である。 
- 超伝導では $F=\langle cc\rangle\neq0$ となり、$F$ は位相を持つため U(1) が自発的に破れる。 

一言で言うと：超伝導とは「U(1) ゲージ対称性を自発的に破った状態」であり、粒子数が確定していない代わりに秩序パラメータの位相がマクロに確定する現象である。

### 4.3.6 異常相関と粒子数不確定性の詳細（F\neq 0 の議論）

前半では $F=0$ の場合（粒子数が良い量である場合）について触れたが、ここからは $F\neq0$ を実際に実現するための条件を導出・整理する。まず異常グリーン関数を改めて定義する：

$$
F_{\alpha\beta}(r,r',\tau-\tau') = \langle T_{\tau}\, c_{r\alpha}(\tau)\, c_{r'\beta}(\tau') \rangle.
$$

時刻順序で $\tau>\tau'$ とすると分解展開を用いて熱平均を明示的に書ける：

$$
F_{\alpha\beta}(\tau,\tau') = \sum_m \langle m\vert e^{-\beta H}\, c_{r\alpha}(\tau)\, c_{r'\beta}(\tau') \vert m\rangle. \tag{4.36}
$$

ここで系は U(1) に対する単位変換 $U(\theta)$ を持つと仮定する。単位分解 $U(\theta)U^{\dagger}(\theta)=1$ を (4.36) の中に挿入し、遷移した基底 $\vert m'\rangle=U(\theta)\vert m\rangle$ を用いると、演算子の変換 $U^{\dagger}(\theta)\, c\, U(\theta)=e^{-i\theta} c$ より次が得られる：

$$
\begin{aligned}
F_{\alpha\beta}(\tau,\tau') &= \sum_m \langle m\vert e^{-\beta H}\, U(\theta)U^{\dagger}(\theta)\, c_{r\alpha}(\tau)\, U(\theta)U^{\dagger}(\theta)\, c_{r'\beta}(\tau')\, U(\theta)U^{\dagger}(\theta) \vert m\rangle \\
&= \sum_m e^{-\beta E_m} \langle m' \vert U^{\dagger}(\theta) c_{r\alpha}(\tau) U(\theta)\; U^{\dagger}(\theta) c_{r'\beta}(\tau') U(\theta) \vert m' \rangle \\
&= e^{-2i\theta} \sum_m e^{-\beta E_m} \langle m' \vert c_{r\alpha}(\tau) c_{r'\beta}(\tau') \vert m' \rangle = e^{-2i\theta} F_{\alpha\beta}(\tau,\tau').
\end{aligned}\tag{4.37}
$$

式 (4.37) は任意の角度 $\theta$ に対して成り立つため、もし場の状態群がすべて粒子数固有状態（すなわち $U(\theta)\vert m\rangle = e^{iN_m\theta}\vert m\rangle$）であれば右辺は $e^{-2i\theta}F$ と位相だけ変化し、角度が連続的に変わる全ての $\theta$ に対して不変であるためには $F=0$ でなければならない。言い換えると、粒子数が良い量（確定している）なら異常相関は自明となる。

一方で $F\neq0$ を実現するためには、系の状態が粒子数固有状態の重ね合わせである必要がある。一般の状態を粒子数 $N$ の固有状態 $\vert\Psi_N\rangle$ の重ね合わせで書くと

$$
\vert m\rangle = \sum_N C_N\, \vert \Psi_N\rangle.
$$

このとき $U(\theta)$ を作用させると各成分は相位 $e^{iN\theta}$ を得て、重ね合わせ係数間に相対位相が生じる。生成演算子側から出てくる $e^{-2i\theta}$ と状態側の相対位相が互いに打ち消し合えば、(4.37) のような単純な位相因子は消え、結果として $F\neq0$ が可能となる。

代表例が BCS 波動関数である：

$$
\vert \Psi_{\mathrm{BCS}} \rangle = \prod_k (u_k + v_k\, c^{\dagger}_k c^{\dagger}_{-k})\, \vert 0\rangle,
\qquad |u_k|^2 + |v_k|^2 = 1. \tag{4.38}
$$

BCS 状態は粒子数の不確定性を持ち、異なる位相 $\theta$ を持つ BCS 状態は互いに縮退して存在する（位相を変えた状態は別のエルゴード的元で同じエネルギーを持つ）。異なる位相の BCS 状態間の重なりは

$$
\langle \Psi_{\mathrm{BCS}} \vert \Psi_{\mathrm{BCS}} \rangle_{\theta}
= \prod_k (|u_k|^2 + e^{2i\theta} |v_k|^2), \tag{4.39}
$$

と書ける。小さな $\theta$ 展開と和を取り扱うと、対数の挙動から

$$
\langle \Psi_{\mathrm{BCS}} \vert \Psi_{\mathrm{BCS}} \rangle_{\theta}
\propto \exp(-2\alpha N \theta^2) \quad(\text{適当な定数 }\alpha),\tag{4.40}
$$

となる（大まかなスケール関係）。したがって熱力学極限 $N\to\infty$ では異なる位相を持つ状態は直交し、系は一つの位相を実際に選ぶ（位相が実効的に固定される）。これが U(1) の自発的対称性破れ（SSB）であり、位相の固定に伴って $F\neq0$ が成立する物理的理由である。

要点：

- 任意の粒子数固有状態のみからなる混合では $F$ は零となる。 
- 粒子数不確定な重ね合わせ（BCS のような波動関数）をとることで $F\neq0$ が可能となり、これは U(1) の自発的破れとして解釈される。

次に、これらの位相揺らぎがどのようにゴールドストーン場やゲージ結合（ジョセフソン効果等）につながるかを簡単に述べる（図示・具体例は次節以降）。

### 4.3.7 trace 形式の限界と準平均法（Bogoliubov の quasi-average）

以下では、統計平均を「トレース形式」

$$
\langle A\rangle = \frac{\mathrm{Tr}\, e^{-\beta H} A}{\mathrm{Tr}\, e^{-\beta H}}
$$

で定義したときに生じる問題点と、現実的に自発的対称性破れ（SSB）を扱うための実用的な手法について整理する。

1) trace 形式ではなぜ $F=0$ になるのか（簡単な導出）

異常相関 $F=\langle c c\rangle$ をトレースで書くと、ユニタリ変換 $U(\theta)$ を挿入して演算子側の位相変換を適用すると

$$
\langle c c \rangle = \frac{\mathrm{Tr}\, e^{-\beta H} c c}{\mathrm{Tr}\, e^{-\beta H} }
= \frac{\mathrm{Tr}\, U^{\dagger}(\theta) e^{-\beta H} U\; U^{\dagger}(\theta) c U\; U^{\dagger}(\theta) c U}{\mathrm{Tr}\, e^{-\beta H} }
= e^{-2i\theta} \langle c c \rangle.
$$

ここでトレースの循環律 $\mathrm{Tr}(AB)=\mathrm{Tr}(BA)$ を利用して簡潔に示した。任意の角度 $\theta$ に対して上式が成り立つため、$\langle c c\rangle$ は $e^{-2i\theta}\langle c c\rangle$ と等しくなければならず、これは一般には $\langle c c\rangle=0$ を意味する。

⚠️ つまり、統計平均がトレース形式で与えられる限り（系が U(1) 対称であるなら）異常相関は消えてしまう。

2) なぜ trace 形式は SSB を表現できないのか（直感）

トレース形式は系の全ての位相を平均する操作であり、異なる位相をもつ純粋状態（例えば位相 $\theta$ を持つ BCS 状態群）を同等に扱って混合してしまう。したがって混合状態として見る限り平均すると秩序パラメータは消え、対称性は復元される。有限系ではこの混合は物理的に正しいが、熱力学極限では異なる位相の状態群がセクター分離し得るため、実際の系は単一セクターに閉じ込められ、$F\neq0$ が観測されうる。

3) C*-代数と KMS 状態による厳密な定式化（概観）

厳密には作用素環（C*-代数）の枠組みで KMS 条件を用いて熱平衡状態を定義すると、熱力学極限で状態空間は複数の超選択セクターに分かれ得る。各セクターは異なる秩序パラメータ（ここでは位相）を持つ純粋表現に対応し、セクター間で遷移が起こらない（互いに直交する）ため、1 セクター内では $F\neq0$ が成立し得る。有限系ではこのセクター分離は厳密には起きないが、遷移時間が天文学的に長い場合などは有効に「閉じ込められる」。

4) Bogoliubov の準平均（quasi-average） — 実用的トリック

理論や数値でトレース平均しか扱えない場合、Bogoliubov の準平均法がしばしば使われる。手順は簡単である：

- 元のハミルトニアン $H$ に、小さな対称性破れ項 $H'\propto \epsilon$ を加える（例：対称性を破るフィールドとしてペア生成項）

$$
H' = \epsilon (c c + c^{\dagger} c^{\dagger}),\qquad \epsilon\to 0.
$$

- まず有限の系（もしくは熱平衡の trace 平均）で $H+H'$ を使って平均 $\langle\cdots\rangle_{\epsilon}$ を取り、最後に順序付けて極限を取る：熱力学極限 $N\to\infty$ を先に、次に $\epsilon\to0$ を取る。すなわち

$$
\langle A\rangle_{\mathrm{q.a.}} = \lim_{\epsilon\to0^+} \lim_{N\to\infty} \langle A \rangle_{H+H'}.
$$

この順序付けられた極限により、トレース平均では消えてしまう秩序パラメータが有限に残る（準平均を得る）。実務的には数式的トリックだが、無限自由度系の性質を反映する妥当な操作として広く用いられている。

5) ダイアグラム展開との関係（補足）

ダイアグラム展開自体はグリーン関数を基本要素として構築される形式的展開であり、どのように $F$ が有限になったか（仮定か準平均かセクター選択か）には依存しない。つまり、展開の局所的なトポロジーや再正規化の手続きは同じで、$F\neq0$ を入力した場合の計算結果はそのまま得られる。ただし、境界条件・極限の取り方（有限系 vs 熱力学極限）や「小さな外場の導入と除去」の順序が物理結果に影響を与える点には注意が必要である。

---

この節は、4.3 の前半（$F=0$ 場合の議論）と 4.3.6（$F\neq0$ の実現条件）の間の橋渡しとなる形式的・実用的な補足である。必要ならば次に「Bogoliubov 準平均を用いた具体的な例（簡易模型での導出）」や「C*-代数的な厳密定理の参考文献（Haag, Bratteli–Robinson など）」への参照を付け加えます。
