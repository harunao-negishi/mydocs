# Green関数講義ノート Part 3

- 元資料: `GreenFunction_diagram.pdf`
- 範囲: 第3章（2体Green関数の定義から自己エネルギーまで）

## 3.1 2体グリーン関数の定義

2体グリーン関数は 1 体グリーン関数を拡張し、粒子間相互作用を直接扱うための基本量である。虚時間表示での定義は

$$
G^{(2)}_{\alpha\beta\gamma\lambda}(r_1,r_2,r_3,r_4;\tau_1,\tau_2,\tau_3,\tau_4)
= \Big\langle T_{\tau}\,
 c_{r_1\alpha}(\tau_1)\, c_{r_2\beta}(\tau_2)\,
 c^{\dagger}_{r_3\gamma}(\tau_3)\, c^{\dagger}_{r_4\lambda}(\tau_4)
\Big\rangle,\tag{3.1}
$$

が式(3.1)に相当する。トレースの巡回性を利用すると時間変数を 1 つ減らせるため、$\tau_3$ を原点に取った 3 変数表示を用いる：

$$
G^{(2)}_{\alpha\beta\gamma\lambda}(r_1,r_2,r_3,r_4;\tau_1,\tau_2,\tau_4)
= \big\langle T_{\tau}\, c_{r_1\alpha}(\tau_1)\, c_{r_2\beta}(\tau_2)\, c^{\dagger}_{r_4\lambda}(\tau_4)\, c^{\dagger}_{r_3\gamma}(0) \big\rangle.\tag{3.2}
$$

空間並進対称性を仮定すると、$r_3$ を基準サイトとして相対座標の関数へ書き換えられる：

$$
G^{(2)}_{\alpha\beta\gamma\lambda}(r_1,r_2,r_4;\tau_1,\tau_2,\tau_4)
= \big\langle T_{\tau}\, c_{(r_1-r_3)\alpha}(\tau_1)\, c_{(r_2-r_3)\beta}(\tau_2)\, c^{\dagger}_{(r_4-r_3)\lambda}(\tau_4)\, c^{\dagger}_{0\gamma}(0) \big\rangle.
$$

空間・時間座標をまとめた $x_i = (r_i,\tau_i)$、対応する一般化運動量 $k_i = (k_i, i\omega_{n_i})$ を導入すると、Fourier 変換は

$$
G^{(2)}_{\alpha\beta\gamma\lambda}(k_1,k_2,k_4)
= \int dx_1\, dx_2\, dx_4\; G^{(2)}_{\alpha\beta\gamma\lambda}(x_1,x_2,x_4)
\, e^{ik_1 x_1}\, e^{ik_2 x_2}\, e^{ik_4 x_4}.\tag{3.3}
$$

粒子–正孔対が運ぶボソン量 $q=(q,\nu_m)$ を明示するために、

$$
k_1 \to k,\qquad k_2 \to -k-q,\qquad k_4 \to k'+q,\tag{3.6}
$$

のような変数変換を行うと最終的に

$$
G^{(2)}_{\alpha\beta\gamma\lambda}(k,k',q)
= \int dx_1\, dx_2\, dx_4\; G^{(2)}_{\alpha\beta\gamma\lambda}(x_1,x_2,x_4)
\, e^{ikx_1}\, e^{-i(k+q)x_2}\, e^{i(k'+q)x_4}.\tag{3.7}
$$

脚注※25では添字の並べ方が内部自由度と結び付いていること、※26では時間変数の定義域が変化することが注意されている。

## 3.2 2体グリーン関数のダイアグラム構造

位置空間での 2 体グリーン関数は、切断可能な項（disconnected part）と切断不可能な項（connected part）へ分解できる。

\[
\begin{aligned}
G^{(2)}_{\alpha\beta\gamma\lambda}(x_1,x_2,x_3,x_4)
&= G_{\alpha\beta}(x_1,x_2) G_{\lambda\gamma}(x_4,x_3)
	- G_{\alpha\gamma}(x_1,x_3) G_{\lambda\beta}(x_4,x_2) \\
&\quad + \sum_{\alpha'\beta'\gamma'\lambda'}
	\int dx'_1 dx'_2 dx'_3 dx'_4\;
	G_{\alpha\alpha'}(x_1,x'_1) G_{\beta'\beta}(x'_2,x_2) \\
&\qquad \times F_{\alpha'\beta'\gamma'\lambda'}(x'_1,x'_2,x'_3,x'_4)
	G_{\gamma'\gamma}(x'_3,x_3) G_{\lambda\lambda'}(x_4,x'_4).
\end{aligned}
\]

ここで $F$ がフルバーテックスであり、図7ではその接続構造が示される。Fourier 空間では同様に

\[
\begin{aligned}
G^{(2)}_{\alpha\beta\gamma\lambda}(k,k',q)
&= G_{\alpha\beta}(k) G_{\lambda\gamma}(k') \, \delta_{q,0}
	- G_{\alpha\gamma}(k) G_{\lambda\beta}(k+q) \, \delta_{k,k'} \\
&\quad + \sum_{\alpha'\beta'\gamma'\lambda'}
		G_{\alpha\alpha'}(k) G_{\beta'\beta}(k+q)
		F_{\alpha'\beta'\gamma'\lambda'}(k,k',q)
		G_{\gamma'\gamma}(k') G_{\lambda\lambda'}(k'+q)
\end{aligned}
\]

と表される（式(3.9)）。第1項と第2項が切断可能部、第3項が connected part に対応する。

### 3.2.1 時空変数を含む crossing symmetry

生成・消滅演算子の入れ替えに伴う 2 体 Green 関数の対称性は

\[
G^{(2)}_{\alpha\beta\gamma\lambda}(x_1,x_2,x_3,x_4)
 = - G^{(2)}_{\alpha\gamma\beta\lambda}(x_1,x_3,x_2,x_4),
\]

\[
G^{(2)}_{\alpha\beta\gamma\lambda}(x_1,x_2,x_3,x_4)
 = - G^{(2)}_{\lambda\beta\gamma\alpha}(x_4,x_2,x_3,x_1)
\]

（式(3.10),(3.11)）として表される。これらが成り立つためには、フルバーテックス自身も

\[
F_{\alpha\beta\gamma\lambda}(x_1,x_2,x_3,x_4)
 = - F_{\alpha\gamma\beta\lambda}(x_1,x_3,x_2,x_4)
\]

（式(3.13)）を満たす必要がある。時空変数を含む crossing symmetry は後述の pp 表現とも整合するよう定義される。

### 3.2.2 2 つの 2 体バーテックスの繋ぎ方

U を 2 つ配置した 2 次摂動項を解析すると、3 種類の接続様式（ph、\bar{ph}、pp）のみを考慮すれば十分であることが分かる。ph チャネルでは 16 通りの同等な寄与があり、係数 $(1/4)^2$ と相殺される。pp チャネルでは crossing 操作で同一図が得られるため 8 つの独立な寄与に減り、残余の係数として 1/2 が現れる（脚注※28）。以降は各チャネルを ph, $\bar{\text{ph}}$, pp と呼び、図8(a)–(c) に対応する代表的な図のみを保持すればよい。

### 3.2.3 pp 表現

ph 表現では $\alpha\lambda$ が消滅演算子、$\beta\gamma$ が生成演算子に対応していた。pp 表現では左右を入れ替え、以下のように定義する。

$$
G^{(2)}_{\alpha\beta\gamma\lambda,\mathrm{pp}}(r_1,r_2,r_3,r_4;\tau_1,\tau_2,\tau_3,\tau_4)
= \left\langle T_{\tau}
  c_{r_1\alpha}(\tau_1) c_{r_2\beta}(\tau_2)
  c^{\dagger}_{r_4\lambda}(\tau_4) c^{\dagger}_{r_3\gamma}(\tau_3)
\right\rangle,
$$

となり（式(3.19)）、位置空間では

$$
\begin{aligned}
G^{(2)}_{\alpha\beta\gamma\lambda,\mathrm{pp}}(x_1,x_2,x_3,x_4)
&= - G_{\alpha\lambda}(x_1,x_4) G_{\beta\gamma}(x_2,x_3)
	+ G_{\alpha\gamma}(x_1,x_3) G_{\beta\lambda}(x_2,x_4) \\
&\quad + \sum_{\alpha'\beta'\gamma'\lambda'}
	\int dx'_1 dx'_2 dx'_3 dx'_4\;
	G_{\alpha\alpha'}(x_1,x'_1) G_{\beta\beta'}(x_2,x'_2) \\
&\qquad \times F^{\mathrm{pp}}_{\alpha'\beta'\gamma'\lambda'}(x'_1,x'_2,x'_3,x'_4)
	G_{\gamma'\gamma}(x'_3,x_3) G_{\lambda'\lambda}(x'_4,x_4),
\end{aligned}
$$

（式(3.20)）を得る。ph 表現と pp 表現は crossing 操作により結び付けられ、例えば

$$
F^{\mathrm{pp}}_{\alpha\beta\gamma\lambda}(x_1,x_2,x_3,x_4)
 = - F^{\mathrm{pp}}_{\alpha\beta\lambda\gamma}(x_1,x_2,x_4,x_3)
 = - F_{\alpha\lambda\gamma\beta}(x_1,x_4,x_3,x_2)
 = F_{\alpha\lambda\beta\gamma}(x_1,x_3,x_4,x_2)
$$

（式(3.21)–(3.23)）が成り立つ。

内部自由度・時空変数・運動量の組を

\[
\begin{aligned}
D &= (\alpha,\beta,\gamma,\lambda;\, x_1,x_2,x_3,x_4;\, k,k',q), \\
T &= (\alpha,\beta,\lambda,\gamma;\, x_1,x_2,x_4,x_3;\, k,-q-k',q), \\
C &= (\alpha,\gamma,\beta,\lambda;\, x_1,x_3,x_2,x_4;\, k,k+q,k'-k), \\
P &= (\alpha,\lambda,\gamma,\beta;\, x_1,x_4,x_3,x_2;\, k,k',-q-k-k'), \\
X &= (\alpha,\gamma,\lambda,\beta;\, x_1,x_3,x_4,x_2;\, k,-k'-q,k'-k)
\end{aligned}
\]

（式(3.24)–(3.26)）と定義すれば、crossing symmetry は compact に

\[
F(D) = -F(C),\quad F^{\mathrm{pp}}(D) = -F^{\mathrm{pp}}(T),\quad F^{\mathrm{pp}}(D) = -F(P) = F(X)
\]

（式(3.27)–(3.31)）と書ける。pp チャネルでは 1/2 の係数を付ける流儀もあり、後の式で一貫するよう取り扱う。

### 3.2.4 高次バーテックスの作り方

ph, $\bar{\text{ph}}$, pp それぞれの pair で切れるダイアグラムだけを機械的に生成するため、次の手順を用いる（式(3.32)）。

1. $V_1 = U$。
2. $V_2 = V_1 + V_1 \chi^{ph}_0 V_1 + V_1 \chi^{\bar{ph}}_0 V_1 + V_1 \chi^{pp}_0 V_1$。
3. 同様に $V_3 = V_2 + V_2 \chi^{ph}_0 V_2 + V_2 \chi^{\bar{ph}}_0 V_2 + V_2 \chi^{pp}_0 V_2$。
4. 以降同じ構造で反復し、重複図が生じた場合は double counting を取り除く。

ここで $\chi^{ph}_0$ などはチャネル毎の非相互作用ペア伝搬（既約感受率）を示す行列である。

### 3.2.5 parquet 方程式

上記の議論から、完全既約バーテックス $\Lambda$ と各チャネル可約バーテックス $\Phi_l$（$l = \text{ph},\bar{\text{ph}},\text{pp}$）を用いて

\[
F(D) = \Lambda(D) + \Phi_{\text{ph}}(D) + \Phi_{\bar{\text{ph}}}(D) + \Phi_{\text{pp}}(D)
\]

（式(3.33)）が成り立つ。2 つ以上のチャネルに同時に可約なバーテックスは存在しないため（図12）、チャネル $l$ に関する既約バーテックス

\[
\Gamma_l = \Lambda + \sum_{l' \neq l} \Phi_{l'}
\]

（式(3.36)）を定義できる。可約バーテックスは Bethe–Salpeter 方程式

\[
F = \Gamma_l + \Phi_l,\qquad \Phi_l = \Gamma_l \chi^{l}_0 \Gamma_l + \Gamma_l \chi^{l}_0 \Gamma_l \chi^{l}_0 \Gamma_l + \cdots
\]

に従い、形式的には

\[
F = \Gamma_l + \Gamma_l \chi^{l}_0 F
\]

（式(3.37)）とまとめられる。数値的には以下の反復で解く。

1. 初期値 $\Gamma_l^{(0)} = \Lambda$ を与える。
2. Bethe–Salpeter 方程式から $\Phi_l$ を計算する。
3. 式(3.36) で $\Gamma_l$ を更新する。
4. 収束まで 2–3 を繰り返す。
5. 収束後に式(3.33) もしくは式(3.37) から $F$ を再構築する。

完全既約バーテックス $\Lambda$ を厳密に得ることは難しいが、parquet 方程式を枠組みとして様々な近似（例えば $\Lambda\approx U$）を体系的に比較できる。

## 3.3 感受率

感受率（susceptibility）は、系が外場や摂動に対してどのように応答するかを表す物理量であり、2体グリーン関数から独立粒子成分を除いたものとして定義されます。

その一般化された形は次式で与えられます：

\[
\begin{aligned}
\chi^{\text{ph}}_{\alpha\beta\gamma\lambda}(x_1,x_2,x_3,x_4) = - G_{\alpha\gamma}(x_1,x_3)\, G_{\lambda\beta}(x_4,x_2)\\
 - \sum_{\alpha'\beta'\gamma'\lambda'} \int dx'_1 dx'_2 dx'_3 dx'_4\;
 G_{\alpha\alpha'}(x_1,x'_1)\, G_{\beta'\beta}(x'_2,x_2)\times F_{\alpha'\beta'\gamma'\lambda'}(x'_1,x'_2,x'_3,x'_4)\,
 G_{\gamma'\gamma}(x'_3,x_3)\, G_{\lambda\lambda'}(x_4,x'_4)
\end{aligned}
\]

で与えられます。

--- 

### 補足

定義に従えば、位置空間の ph 感受率は

$$
\chi^{\text{ph}}_{\alpha\beta\gamma\lambda}(x_1,x_2,x_3,x_4)
= G_{\alpha\beta}(x_1,x_2)\, G_{\gamma\lambda}(x_3,x_4)
 - G_{\alpha\gamma}(x_1,x_3)\, G_{\beta\lambda}(x_2,x_4).
$$

最も簡単な例として単一軌道系を考え、\(\alpha,\beta\) を上向きスピン、\(\gamma,\lambda\) を下向きスピンとし、時間順序 \(\tau_1<\tau_2\), \(\tau_3>\tau_4\) を保ったまま \(x_1,x_2,x_3,x_4\to 0\) とすると、

$$
\chi^{\text{ph}} \;\longrightarrow\; \langle n_\uparrow n_\downarrow \rangle
 - \langle n_\uparrow \rangle\, \langle n_\downarrow \rangle \tag{3.40}
$$

のように密度揺らぎが現れる。この静的な揺らぎを動的に一般化したものが感受率である。また、\(\alpha,\beta,\gamma,\lambda\) の選び方によって、スピン揺らぎ・超伝導揺らぎ・軌道揺らぎなど様々な感受率を定義できる。最も一般的な形は式 (3.38) に相当するため、これを一般化感受率と呼ぶ。

Fourier 空間では

\[
\chi^{\text{ph}}_{\alpha\beta\gamma\lambda}(k,k',q)
 = - G_{\alpha\gamma}(k) G_{\lambda\beta}(k+q) \delta_{k,k'}
 - \sum_{\alpha'\beta'\gamma'\lambda'} G_{\alpha\alpha'}(k) G_{\beta'\beta}(k+q)
	 F_{\alpha'\beta'\gamma'\lambda'}(k,k',q)
	 G_{\gamma'\gamma}(k') G_{\lambda\lambda'}(k'+q)
\]

ほかのチャネルでの感受率がどう描けるかを見ていこう。ph チャネルは D→C の変換を用いると次の表式でも書ける：

\[
\chi^{\text{ph}}_{\alpha\beta\gamma\lambda}(k,k',q)
= G_{\alpha\beta}(k)\, G_{\lambda\gamma}(k')\, \delta_{q,0}
- \sum_{\alpha'\beta'\gamma'\lambda'} G_{\alpha\alpha'}(k)\, G_{\gamma'\gamma}(k')\,
  F_{\alpha'\gamma'\beta'\lambda'}\bigl(k,\, k+q,\, k'-k\bigr)
	\, G_{\beta'\beta}(k+q)\, G_{\lambda\lambda'}(k'+q)
	ag{3.42}
\]

pp チャネルの一般化感受率は、pp 表現の 2 体グリーン関数 (3.21) の最初の項を除くと

\[
\chi^{\text{pp}}_{\alpha\beta\gamma\lambda}(k,k',q)
 = G_{\alpha\gamma}(k) G_{\beta\lambda}(-k-q) \delta_{k,k'}
 - \sum_{\alpha'\beta'\gamma'\lambda'} G_{\alpha\alpha'}(k) G_{\beta\beta'}(-k-q)
	 F^{\mathrm{pp}}_{\alpha'\beta'\gamma'\lambda'}(k,k',q)
	 G_{\gamma'\gamma}(k') G_{\lambda'\lambda}(-k'-q)
\]

（式(3.43)）。

フルバーテックスを無視した場合の既約感受率は

\[
\chi^{l}_0(k,k',q) =
\begin{cases}
 -G_{\alpha\gamma}(k) G_{\lambda\beta}(k+q) \delta_{k,k'} & (l=\text{ph}),\\
	G_{\alpha\beta}(k) G_{\lambda\gamma}(k') \delta_{q,0} & (l=\bar{\text{ph}}),\\
	G_{\alpha\gamma}(k) G_{\beta\lambda}(-k-q) \delta_{k,k'} & (l=\text{pp})
\end{cases}
\]

（式(3.44)）であり、Bethe–Salpeter 方程式から

\[
\chi^{l} = \chi^{l}_0 + \chi^{l}_0 F^{(l)} \chi^{l}_0
 = \chi^{l}_0 + \chi^{l}_0 \Gamma_l \chi^{l}
\]

（式(3.45)–(3.48)）を得る。脚注※44では単一軌道モデルで $\chi$ が密度揺らぎへ還元される例が示されている。

## 3.4 自己エネルギー

自己エネルギーはハミルトニアン $H = H_0 + H_{\text{int}}$ に対するシュウィンガー–ダイソン方程式

\[
-\left\langle T_{\tau} e^{\tau H} [ c_{r\alpha}, H_{\text{int}} ] e^{-\tau H} c^{\dagger}_{r'\beta} \right\rangle
 = \int d\tau'' \sum_{r''\gamma} \Sigma_{\alpha\gamma}(r,r''; \tau-\tau'')
	 G_{\gamma\beta}(r'',r'; \tau''-\tau')
\]

（式(3.49)）から定義される。相互作用の交換関係を展開すると、Hartree–Fock 項と相関項に分かれ、式(3.54) の形に整理できる。

\[
\Sigma_{\alpha\beta}(x,x') = -\sum_{\gamma\lambda} U_{\alpha\gamma\beta\lambda}
	G_{\gamma\lambda}(\tau=-0, r=0)
	- \frac{1}{2} \sum_{\substack{\beta'\gamma'\lambda' \\ \alpha''\beta''\lambda''}}
	U_{\alpha\beta'\gamma'\lambda'}
	G_{\gamma'\alpha''}(x,x'_1) G_{\beta''\lambda'}(x'_2,x)
	F_{\alpha''\beta''\beta\lambda''}(x'_1,x',x'_2,x'_4)
	G_{\beta'\lambda''}(x,x'_4).
\]

第一項が $\Sigma_{\text{HF}}$、第二項が相関部分 $\Sigma_{\text{cr}}$ に対応する。運動量表示では

\[
\begin{aligned}
\Sigma_{\alpha\beta}(k)
&= - \sum_{\gamma\lambda} U_{\alpha\gamma\beta\lambda}
		G_{\gamma\lambda}(k) e^{-i\omega_n 0^+} \\
&\quad - \frac{1}{2} \sum_{\substack{\beta'\gamma'\lambda' \\ \alpha''\beta''\lambda''}}
		\sum_{k' q} F_{\alpha\beta'\gamma'\lambda'}(k,k',q)
		G_{\gamma'\alpha''}(k') G_{\beta''\lambda'}(k'+q)
		U_{\alpha''\beta''\beta\lambda''} G_{\beta'\lambda''}(k+q)
\end{aligned}
\]

（式(3.55)）となり、図13に対応する skeleton ダイアグラムが得られる。

## 3.5 備考

提供された PDF では、第3章は上記の 3.4 節までで区切られ、そのまま第4章「超伝導」へ移行する構成になっている。独立した 3.5 節の本文は確認できなかったため、本ノートではここを補足事項とした。必要に応じて原典の最新版を再確認してほしい。
