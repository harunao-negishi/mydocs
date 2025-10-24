# 第2章 ダイアグラム展開の基礎

> 本章では，相互作用表示の導入から Wick（および Bloch–de Dominicis）分解，
> さらに Feynman ダイアグラムによる計算法と 1 体既約性までを通しでまとめる。
> 記法は第1章と連続で，多軌道（内部自由度付き）を前提とする。

---

## 2.1 相互作用表示

**定義**（相互作用なしの基準）  
演算子 $A$ の相互作用表示と，相互作用なしの期待値を
$$
A_I(\tau)=e^{\tau H_0}\,A\,e^{-\tau H_0},
\qquad
\langle A\rangle_0=\frac{\mathrm{Tr}\!\left(e^{-\beta H_0}A\right)}{\mathrm{Tr}\!\left(e^{-\beta H_0}\right)}.
\tag{2.1–2.2}
$$

**$S$ 演算子の導入**  
相互作用 $H_{\mathrm{int}}$ を $H=H_0+H_{\mathrm{int}}$ と分け，
$$
S(\tau)=e^{\tau H_0}e^{-\tau H},
\qquad
S(\tau,\tau')=S(\tau)\,S^{-1}(\tau').
\tag{2.3–2.4}
$$
相互作用表示では
$$
\frac{\partial}{\partial\tau}S(\tau)=-\,H^{I}_{\mathrm{int}}(\tau)\,S(\tau),
\qquad
H^{I}_{\mathrm{int}}(\tau)=e^{\tau H_0}H_{\mathrm{int}}e^{-\tau H_0},
$$
より Dyson 展開（時間順序指数）
$$
S(\tau)=T_\tau\exp\!\left[-\int_0^{\tau}\!d\tau_1\,H^{I}_{\mathrm{int}}(\tau_1)\right].
\tag{2.5}
$$

**統計平均の変換**  
相互作用を含む期待値は
$$
\langle A\rangle=\frac{\mathrm{Tr}\!\left(e^{-\beta H}A\right)}{\mathrm{Tr}\!\left(e^{-\beta H}\right)}
=\frac{\langle S(\beta)\,A\rangle_0}{\langle S(\beta)\rangle_0}.
\tag{2.6}
$$

**1体 Green 関数の式**  
虚時間 Green 関数（第1章の定義）に $S(\tau,\tau')$ を挿入して
$$
G_{\alpha\beta}(r,r',\tau,\tau')=-
\frac{\Big\langle T_\tau\,S(\beta,\tau)\,c^{I}_{r\alpha}(\tau)\,S(\tau,\tau')\,c^{\dagger I}_{r'\beta}(\tau')\,S(\tau',0)\Big\rangle_0}
{\big\langle S(\beta,0)\big\rangle_0}.
\tag{2.11}
$$

> 💡**背景**：
> - $S$ を挟むことで「相互作用ありの平均」を**相互作用なし（Gaussian）**の平均 $\langle\cdot\rangle_0$ に帰着。
> - 以後の展開は，すべて **$H_0$ の世界での Wick 分解**に落とし込む。

---

## 2.2 Wick の定理と Bloch–de Dominicis の定理

多数の $c, c^\dagger$ の積の $\langle\cdots\rangle_0$ を，2点縮約の積に分解する。  
演算子列 $A_i\in\{c,\;c^\dagger\}$ に対して，反交換子
$$
\{A_i,A_j\}=(ij)\quad(\text{$c$-数})
\tag{2.15}
$$
が成り立つとき，偶数個の積は
$$
\big\langle A_1A_2\cdots A_{2n}\big\rangle_0
=\sum_{\text{全てのペア分割 }p}
(-1)^{\delta(p)}
\prod_{(i,j)\in p}\!\big\langle T_\tau A_iA_j\big\rangle_0.
\tag{2.16}
$$

ここで $(-1)^{\delta(p)}$ は**交換で生じる符号**（フェルミオン）。  
2点縮約 $\langle T_\tau c(\tau_i)c^\dagger(\tau_j)\rangle_0$ は**自由系の Green 関数**
$$
G^0_{\alpha\beta}(r_i,r_j;\tau_i,\tau_j)\equiv
-\,\big\langle T_\tau\,c_{r_i\alpha}(\tau_i)c^\dagger_{r_j\beta}(\tau_j)\big\rangle_0.
\tag{2.17}
$$

> 📝**実装メモ**：
> - 多軌道系では内部自由度添字を**行列**として扱う（後述の式 (2.43) 参照）。
> - 有限温度・虚時間なので $T_\tau$ を前提とする。

---

## 2.3 Green 関数の Wick 分解

### 2.3.1 時間順序
$T_\tau$ により $H_{\mathrm{int}}(\tau_i)$ の順番は積分中であらゆる並びを取りうるが，
Wick 分解では**最終的な縮約の組**のみが効く。計算の実務では，
- 生成・消滅が**交互**になる並びに並べ替え，
- そこから縮約の組を選んでいく，
という流儀で，符号は**一括管理**する（次節）。

### 2.3.2 全体の符号
Green 関数分子・分母に現れる多数の $c,c^\dagger$ を Wick 分解した際の符号は，
- 交換回数に基づく $(-1)^{\delta(p)}$，
- （後の図式規則により）**全次数 $n$ に対する $(-1)^n$** でまとめる，
の二段構えで整理できる（次節のダイアグラム規則とあわせて実務では個別の符号を追わない）。

> 💡**ポイント**：
> - **偶置換のみ**を採用する並べ替え方針にすれば，中間の符号管理を減らせる。
> - 以降は**図式規則に吸収**して，人の手計算で符号ミスを避ける。

---

## 2.4 Feynman ダイアグラム

Wick 分解の結果を**図式規則**に写像して計算する。

### 2.4.1 描き方（1体 Green 関数）
1. **相互作用頂点 $U$** を四角で $n$ 個並べる（左下: $\alpha$，左上: $\beta$，右下: $\gamma$，右上: $\lambda$）。  
2. **外線**：外部の $c(\tau)$ と $c^\dagger(\tau')$ をそれぞれ 1 個の頂点に接続する（1 組だけ選べば良い）。  
3. **内部線**：残りの $c$ と $c^\dagger$ を全て**矢印付き実線**で結ぶ（可能な結び方を網羅）。  
4. **対応付け**：実線 $\Rightarrow G_0$，四角 $\Rightarrow U$ として式に起こす。  
5. **内部和・積分**：内部変数（虚時間・位置・内部自由度）について和・積分。  
6. **全次数の符号**：その次数が $n$ なら**係数 $(-1)^n$** を掛ける。

> 🔢**組合せの整理**：  
> 外線の繋ぎ方が異なるだけで**同一の寄与**を与える図は $n!$ 個存在する。
> Dyson 展開の係数 $1/n!$ と**相殺**されるので，代表 1 個を計算すれば良い。

### 2.4.2 例：外線 2 本の一次寄与
外線を 1 つの頂点に接続し，残りを内部線で結ぶ。式にすれば
$$
G^{(1)} \sim G_0\,U\,G_0 \quad
(\text{内部変数に関する和・積分を含む}).
$$

---

## 2.5 既約性（one-particle irreducible; 1PI）

第1章の枠組みで，Green 関数は
$$
G=G_0+G_0\,s\,G_0
\tag{2.41}
$$
と書ける（$s$ は外線に直接つながる以外の内部を**全て**積分・総和し**全次数**について足し上げた核）。
並進対称性があれば
$$
G(k)=G_0(k)+G_0(k)\,s(k)\,G_0(k),\qquad k=(\boldsymbol{k},i\omega_n).
\tag{2.42}
$$

多軌道（内部自由度）では，$G_0,s,G$ は**行列**として畳み込む：
$$
\sum_{\alpha'\beta'}G^0_{\alpha\alpha'}(k)\,s_{\alpha'\beta'}(k)\,G^0_{\beta'\beta}(k).
\tag{2.43}
$$
より抽象化して，空間・時間・内部自由度をまとめた添字 $a=(r,\tau,\alpha)$ を用いれば
$$
G_{ab}=G^0_{ab}+\sum_{a'b'}G^0_{aa'}\,s_{a'b'}\,G^0_{b'b},
\tag{2.44}
$$
すなわち**行列表現**で一様に扱える。

> 🪵**骨格（skeleton） vs. 非骨格**：  
> 1PI 図は**骨格ダイアグラム**（内部線がすべて完全な $G$ で置換されたもの）と，それ以外に分解できる。
> 以降，自己無撞着な近似（例：SCBA, FLEX 等）では骨格のみを用いるのが自然。

---

### 🧭 章のまとめ（要点）
- **相互作用表示**：$S$ 演算子で相互作用ありの平均を**自由系の平均**にマップ（式 (2.6)）。  
- **Wick/Bloch–de Dominicis**：$2n$ 点平均を**2点縮約の和**に分解（式 (2.16)）。  
- **ダイアグラム規則**：$U$（四角）と $G_0$（実線）の組み合わせ／$n!$ と $1/n!$ が相殺。  
- **既約性**：$G=G_0+G_0 s G_0$（行列畳み込み）。骨格ダイアグラムの概念は近似法の基礎。

---

> ✍️ **補足：式変形の道筋（2.1→2.11）**  
> 1) $S(\tau)$ の微分方程式と Dyson 展開 → 2) $S(\tau,\tau')$ の挿入 →  
> 3) 相互作用表示 $c^I, c^{\dagger I}$ への置換 → 4) $H_0$ 世界での平均 $\langle\cdot\rangle_0$ に帰着 → (2.11)。

