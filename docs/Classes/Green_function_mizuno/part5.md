# 5 SU(2) symmetric case

## 5.1 相関関数

スピン空間の回転対称性 (SU(2) symmetry) がある場合、スピン自由度の組み合わせによって、2 体のグリーン関数やバーテックス関数は電荷・スピン・一重項ペア・三重項ペアに対応するチャネルに分解できます。本節ではまず「電荷チャネル（charge channel）」、すなわち電荷密度の相関関数を詳しく見ていきます。式番号や小節分けは Part 4 のスタイルに合わせてあります。

### 5.1.1 電荷密度演算子の定義

実空間での電荷密度演算子は

$$
\rho(\mathbf{r})=\sum_{\sigma} c^{\dagger}_{\sigma}(\mathbf{r})\,c_{\sigma}(\mathbf{r})
$$

これを波数空間にフーリエ変換すると、波数 $\mathbf{q}$ の電荷密度演算子は

$$
\rho(\mathbf{q})=\int d^{d}r\;e^{-i\mathbf{q}\cdot\mathbf{r}}\,\rho(\mathbf{r}).
$$

電子演算子のフーリエ展開

$$
c_{\sigma}(\mathbf{r})=\frac{1}{\sqrt{V}}\sum_{\mathbf{k}}e^{i\mathbf{k}\cdot\mathbf{r}}c_{\mathbf{k}\sigma}
$$

を代入して整理すると、よく使われる形として

$$
\rho(\mathbf{q})=\sum_{\mathbf{k},\sigma}c^{\dagger}_{\mathbf{k}+\mathbf{q},\sigma}\,c_{\mathbf{k},\sigma}\tag{5.1}
$$

物理的には $c^{\dagger}_{\mathbf{k}+\mathbf{q},\sigma}c_{\mathbf{k},\sigma}$ が「運動量 $\mathbf{k}$ の電子を $\mathbf{k}+\mathbf{q}$ に移す」操作で、波数 $\mathbf{q}$ の密度ゆらぎ（charge fluctuation）を生成します。従って $\rho(\mathbf{q})$ は波数 $\mathbf{q}$ の電荷密度モードを表します。

### 5.1.2 電荷相関関数の定義

電荷密度の相関関数は

$$
\langle\rho(\mathbf{q})\;\rho(-\mathbf{q})\rangle
$$

と定義されます。式 (5.1) を代入して展開すると

$$
\rho(\mathbf{q})\,\rho(-\mathbf{q})=\sum_{\mathbf{k}_1,\sigma_1}\sum_{\mathbf{k}_2,\sigma_2} c^{\dagger}_{\mathbf{k}_1+\mathbf{q},\sigma_1}c_{\mathbf{k}_1,\sigma_1}\;c^{\dagger}_{\mathbf{k}_2-\mathbf{q},\sigma_2}c_{\mathbf{k}_2,\sigma_2}
$$

順序を入れ替え、記法を簡潔にすると

$$
\rho(\mathbf{q})\,\rho(-\mathbf{q})=\sum_{\mathbf{k},\sigma_1}\sum_{\mathbf{k}^\prime,\sigma_2} c^{\dagger}_{\mathbf{k}+\mathbf{q},\sigma_1}c_{\mathbf{k},\sigma_1}\;c^{\dagger}_{\mathbf{k}^\prime,\sigma_2}c_{\mathbf{k}^\prime+\mathbf{q},\sigma_2}\tag{5.2}
$$

この期待値を取ることで電荷相関関数（または電荷感受率）を得ます。

### 5.1.3 スピン添字を明示した 2 体量

スピン成分の組み合わせを明示するため、次の 4 つのスピン添字を持つ量を導入します：

$$
C_{\sigma_1\sigma_2\sigma_3\sigma_4}(\mathbf{k},\mathbf{k}^\prime;\mathbf{q})\equiv\langle c^{\dagger}_{\mathbf{k}+\mathbf{q},\sigma_2}\,c_{\mathbf{k},\sigma_1}\; c^{\dagger}_{\mathbf{k}^\prime,\sigma_3}\,c_{\mathbf{k}^\prime+\mathbf{q},\sigma_4}\rangle\tag{5.3}
$$

この $C_{\sigma_1\sigma_2\sigma_3\sigma_4}$ は time-ordered な 2 体グリーン関数を等時刻極限で評価したものに対応します。

### 5.1.4 電荷相関関数のスピン構造展開

電荷密度演算子は同スピンの粒子数を数えるので、各対でスピンは保存されます（$\sigma_1=\sigma_2$, $\sigma_3=\sigma_4$）。したがって電荷相関へ寄与する組み合わせは次の 4 通りです：

$$
\langle\rho\rho\rangle=C_{\uparrow\uparrow\uparrow\uparrow}+C_{\uparrow\uparrow\downarrow\downarrow}+C_{\downarrow\downarrow\uparrow\uparrow}+C_{\downarrow\downarrow\downarrow\downarrow}\tag{5.4}
$$

ここから SU(2) 対称性を使うと更に簡約できます。

### 5.1.5 SU(2) 対称性による簡約と電荷チャネル定義

SU(2)（スピン回転）対称性があるとアップ・ダウンの寄与は等しく、

$$
C_{\uparrow\uparrow\uparrow\uparrow}=C_{\downarrow\downarrow\downarrow\downarrow},\qquad C_{\uparrow\uparrow\downarrow\downarrow}=C_{\downarrow\downarrow\uparrow\uparrow}.
$$

従って式 (5.4) は

$$
\langle\rho\rho\rangle=2\bigl(C_{\uparrow\uparrow\uparrow\uparrow}+C_{\uparrow\uparrow\downarrow\downarrow}\bigr)
$$

ここで電荷チャネルのスカラー量 $C_{c}$ を

$$
C_{c}\equiv\frac{1}{2}\langle\rho\rho\rangle = C_{\uparrow\uparrow\uparrow\uparrow}+C_{\uparrow\uparrow\downarrow\downarrow}\tag{5.5}
$$

と定義します。$C_{c}$ は電荷揺らぎ（charge channel）の強度を表す量です。

### 5.1.6 物理的解釈（ポイント）

- $C_{\uparrow\uparrow\uparrow\uparrow}$: 同スピン間の相関。スピン保存のもとでの粒子–穴励起（電荷密度ゆらぎ）。
- $C_{\uparrow\uparrow\downarrow\downarrow}$: 異スピン間の相関。スピンが異なる電子間の電荷ゆらぎの寄与。
- $C_{c}$: これらをまとめたスカラーで、電荷チャネル（charge channel）の強度を与える。

### 5.1.7 波数依存性について（補足）

実際には $C_{\sigma_1\sigma_2\sigma_3\sigma_4}$ は内部運動量 $\mathbf{k},\mathbf{k}^\prime$ に依存し、より正確には式 (5.3) のように書きます。
しかし電荷相関関数 $\langle\rho(\mathbf{q})\rho(-\mathbf{q})\rangle$ を得る際にはそれらを全て和（積分）してしまうため、観測されるのは外部波数 $\mathbf{q}$ のみです。

線形応答的には、この量は電荷感受率（charge susceptibility）として

$$
\chi_{c}(\mathbf{q})\propto \langle\rho(\mathbf{q})\rho(-\mathbf{q})\rangle
$$

と解釈されます。

---

## 5.2 次にやるべきこと（案）

- 同様の方法で「スピンチャネル」「ペアチャネル（singlet/triplet）」の節を追加する。
- 具体例として非相互作用系での $C_{\sigma\cdots}$ の計算例や、RPA での近似式（$\chi_c,\chi_s$ の導出）を添える。


以上。読みやすさや節の分割など、さらに調整したい点があれば指示ください。

### 5.1.8 スピン相関関数（詳細まとめ）

0) 準備：実空間と運動量空間の対応

電子演算子のフーリエ変換（体積 $V$, 格子定数 1 の想定）を再掲すると

$$
c_{r\sigma}=\frac{1}{\sqrt{V}}\sum_{k} e^{i k\cdot r}\, c_{k\sigma},\qquad
c^{\dagger}_{r\sigma}=\frac{1}{\sqrt{V}}\sum_{k} e^{-i k\cdot r}\, c^{\dagger}_{k\sigma}.
$$

実空間のスピン密度（パウリ行列 $\boldsymbol{\sigma}=(\sigma_x,\sigma_y,\sigma_z)$ を用いる）

$$
S_{\mu}(r)=\sum_{\sigma,\sigma'} c^{\dagger}_{r\sigma}\, (\sigma_{\mu})_{\sigma\sigma'}\, c_{r\sigma'},
$$

そのフーリエ成分（運動量 $q$ 成分）は

$$
S_{\mu}(q)=\sum_{r} e^{-i q\cdot r}\, S_{\mu}(r)=\sum_{k,\sigma,\sigma'} c^{\dagger}_{k+q,\sigma}\, (\sigma_{\mu})_{\sigma\sigma'}\, c_{k\sigma'}.
	ag{5.6}
$$

意味：$c^{\dagger}_{k+q} c_k$ は“運動量 $q$ の粒子–穴励起”を作り、$\sigma_{\mu}$ によってその励起のスピン成分（$x,y,z$）を抽出する。

1) スピン相関関数の定義と 2 体グリーン関数への書き換え

等時刻（Matsubara 時間順序の等時極限）でのスピン相関関数は

$$
\langle S(q)\cdot S(-q)\rangle
=\sum_{\mu}\,\langle S_{\mu}(q)\,S_{\mu}(-q)\rangle.
$$

式 (5.6) を 2 回代入して展開すると、スピン指標を明示した 4 本脚量

$$
C_{\sigma_1\sigma_2\sigma_3\sigma_4}(k,k';q)\equiv
\langle c^{\dagger}_{k+q,\sigma_2}\, c_{k,\sigma_1}\; c^{\dagger}_{k',\sigma_4}\, c_{k'+q,\sigma_3}\rangle
$$

を用いて

$$
\langle S(q)S(-q)\rangle=\sum_{k,k'}\sum_{\substack{\sigma_1,\sigma'_1 \\ \sigma_2,\sigma'_2}} (\boldsymbol{\sigma})_{\sigma_1\sigma'_1}\cdot(\boldsymbol{\sigma})_{\sigma_2\sigma'_2}\; C_{\sigma_1\sigma'_1\sigma_2\sigma'_2}(k,k';q).\tag{5.7}
$$

ここで $C_{\cdots}$ は等時極限での 4 点関数（Matsubara の 4 点関数を適切に極限化したもの）を意味する。

2) 成分ごとの展開（$S_x,S_y,S_z$）

パウリ行列の成分を代入すると、成分ごとの縮約により (5.8)–(5.16) のような形が得られる。代表例を示す：

$$
\langle S_x S_x\rangle = C_{\uparrow\downarrow\uparrow\downarrow}+C_{\uparrow\downarrow\downarrow\uparrow}+C_{\downarrow\uparrow\uparrow\downarrow}+C_{\downarrow\uparrow\downarrow\uparrow},\tag{5.8}
$$

$$
\langle S_y S_y\rangle = C_{\uparrow\downarrow\uparrow\downarrow}-C_{\uparrow\downarrow\downarrow\uparrow}-C_{\downarrow\uparrow\uparrow\downarrow}+C_{\downarrow\uparrow\downarrow\uparrow},\tag{5.9}
$$

$$
\langle S_z S_z\rangle = C_{\uparrow\uparrow\uparrow\uparrow}-C_{\uparrow\uparrow\downarrow\downarrow}-C_{\downarrow\downarrow\uparrow\uparrow}+C_{\downarrow\downarrow\downarrow\downarrow}.\tag{5.10}
$$

これらの係数はパウリ行列の要素（符号・虚数単位 $i$ の有無）に由来する。$S_x,S_y$ はスピン反転（flip）成分を含む一方、$S_z$ は上・下の重み差を測る。

3) スピン数保存（$S^z$ 保存）を仮定した簡約

もしハミルトニアンが総 $S^z$ を保存する（$[H,S^z_{\mathrm{tot}}]=0$）ならば、スピンを同時に 2 本以上反転させるような項は寄与しない。すると残る寄与は簡約され、例えば

$$
\langle S_x S_x\rangle = C_{\uparrow\downarrow\uparrow\downarrow}+C_{\downarrow\uparrow\downarrow\uparrow},\tag{5.17}
$$

$$
\langle S_y S_y\rangle = C_{\uparrow\downarrow\uparrow\downarrow}+C_{\downarrow\uparrow\downarrow\uparrow},\tag{5.18}
$$

$$
\langle S_z S_z\rangle = C_{\uparrow\uparrow\uparrow\uparrow}-C_{\uparrow\uparrow\downarrow\downarrow}-C_{\downarrow\downarrow\uparrow\uparrow}+C_{\downarrow\downarrow\downarrow\downarrow}.\tag{5.19}
$$

また交差成分は

$$
\langle S_x S_y\rangle = i\,(C_{\uparrow\downarrow\uparrow\downarrow}-C_{\downarrow\uparrow\downarrow\uparrow}),\qquad
\langle S_y S_x\rangle = -i\,(C_{\uparrow\downarrow\uparrow\downarrow}-C_{\downarrow\uparrow\downarrow\uparrow}).\tag{5.20-5.21}
$$

さらに

$$
\langle S_x S_z\rangle=\langle S_z S_x\rangle=\langle S_y S_z\rangle=\langle S_z S_y\rangle=0.\tag{5.22-5.25}
$$

4) SU(2) 等方性の帰結

系が SU(2) 回転対称（等方）であれば $x,y,z$ 成分は等価になり、従ってスピン応答は単一のスカラー関数 $C_s$ に縮約される：

$$
	frac{1}{2}\langle S_x S_x\rangle = \tfrac{1}{2}\langle S_y S_y\rangle = \tfrac{1}{2}\langle S_z S_z\rangle \equiv C_s.\tag{5.26}
$$

スピン指標の 4 本脚表記に戻すと、$C_s$ は (5.26) に示すような特定の組合せで表される。

5) 運動量依存性と観測量との対応

実験（中性子散乱など）が測るのは外部波数 $q$ に依存するスピン感受率 $\chi_s(q)\propto\langle S(q)S(-q)\rangle$ である。理論的には内部運動量 $k,k'$ をループ和として処理し、RPA/FLEX のような近似で

$$
\chi_c(q),\,\chi_s(q)\simeq \frac{\chi_0(q)}{1\pm U\chi_0(q)}
$$

のようなチャネル別の表現を得る（符号はチャネルに依存）。

6) まとめ（チャネル分解の位置づけ）

- 密度（電荷）チャネル：$\rho(q)=\sum_{k,\sigma} c^{\dagger}_{k+q,\sigma} c_{k\sigma}$（スピンを反転しない ph 和）。
- スピンチャネル：$S_{\mu}(q)=\sum_{k,\sigma,\sigma'} c^{\dagger}_{k+q,\sigma}(\sigma_{\mu})_{\sigma\sigma'} c_{k\sigma'}$（スピン構造を持つ ph 和）。

SU(2) 等方性のもとではスピン応答は単一のスカラー関数 $C_s$ に縮約され、計算実務では内部運動量の和を取り、RPA/FLEX 等でチャネルごとの有効相互作用を導入して評価する。

---

（注）本文中の式番号はこの節内での容易な参照のためにつけてあります。さらに具体的な公式や非相互作用系での例（ループ計算による $C_{\sigma\cdots}$ の評価）を追加したい場合は指示してください。

以上。読みやすさや節の分割など、さらに調整したい点があれば指示ください。



