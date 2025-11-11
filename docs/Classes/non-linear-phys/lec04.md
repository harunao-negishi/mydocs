# 第4回 非線形物理講義ノート
- 授業日: 2025-11-11 （想定）
- 科目: Statistical mechanics of disordered systems
- 担当: 吉野元

# Part II: p-spin models on a dense graph  (p-spin模型の平均場理論的解析)
## IV. Warming up: Ferromagnetism  (ウォーミングアップ：強磁性)
### A. Basic phenomenology of ferromagnetism（強磁性の基本的現象論）

---

### 図の説明（FIG. 10）
図10は**ランダウ自由エネルギー（Landau free-energy）**の典型的な形状を示している。  
左図では係数 \( a > 0 \)（臨界温度 \( T_c \) より高温側）、右図では \( a < 0 \)（低温側）で、\( b > 0 \) は通常の**強磁性イジング模型（Ising model, p=2）**に対応している。  
高温では磁化は0付近に一つの極小を持つが、低温になると対称な二つの極小が現れ、これが**自発的対称性の破れ（spontaneous symmetry breaking）**を示している。

---

## 強磁性転移（Ferromagnetic phase transition）

ここでは、**強磁性相転移**について議論する。  
この節の目的は、のちに**ガラス系（glassy systems）**を解析する際にも用いる、**相転移の解析戦略**を導入することにある。

---

### 1. 順序変数と共役場

強磁性の現象論は広く知られている。  
**順序変数（order parameter）**は磁化 \( m \) であり、  
**共役場（conjugated field）**は外部磁場 \( h_{\text{ext}} \) である。

系が外場を持たない場合（\( h_{\text{ext}} = 0 \)）には、磁化の反転対称性 \( m \to -m \) が成り立つ。  
一方、外部磁場 \( h_{\text{ext}} \) はこの対称性を破る。

---

### 2. 自発磁化（spontaneous magnetization）の定義

我々が興味を持つのは**自発磁化（spontaneous magnetization）**と呼ばれる物理量であり、次のように定義される：

\[
m_s = \lim_{h_{\text{ext}}\to 0^+} \lim_{N\to\infty} m(h_{\text{ext}}),
\tag{IV.1}
\]

つまりこれは、外部磁場を先にゼロにしてから熱力学極限を取るのではなく、熱力学極限を先に取ってから外部磁場をゼロにする操作である。

ここで \( N \) は系のサイズ（スピンの数）を表す。  
この極限操作は「**自発的対称性の破れ（spontaneous symmetry breaking）**」を反映している。

---

### 3. 極限操作の非可換性

**常磁性相（paramagnetic phase）**では、極限の順序を入れ替えても結果は同じで、磁化はゼロとなる：

\[
\lim_{h\to 0} \lim_{N\to\infty} m(h)
= \lim_{N\to\infty} \lim_{h\to 0} m(h)
= 0.
\]

しかし、**強磁性相（ferromagnetic phase）**では極限が可換ではない：

\[
\lim_{N\to\infty} \lim_{h\to 0} m(h) = 0,
\]

一方で

\[
\lim_{h\to 0^+} \lim_{N\to\infty} m(h) > 0, \quad
\lim_{h\to 0^-} \lim_{N\to\infty} m(h) < 0.
\]

この非可換性が、系が**外部場がゼロであっても一方向に磁化を選ぶ**（＝対称性が自発的に破れる）ことを示している。

---

## ランダウ理論（Landau theory）

ランダウ理論は、強磁性相の出現を**定性的に（mean-field的に）**理解する枠組みである。  
その本質は、自由エネルギー \( F(m) \) を磁化 \( m \) の関数として展開することである。

---

### 1. 自由エネルギー展開

系の磁化が固定された状態における自由エネルギー \( F(m) \) は、次のように展開できると仮定する：

\[
-\frac{\beta F(m)}{N} = a m^2 + b m^4 + \cdots,
\tag{IV.2}
\]

ここで：
- \( a \) は温度に依存する係数（\( a \propto (T_c - T) \)）  
- \( b > 0 \) は安定性を保証するための正の定数  
- \(\beta = 1 / (k_B T)\) は逆温度  

したがって、\( a > 0 \) のときは**単一極小**（常磁性）、  
\( a < 0 \) のときは**二重極小構造**（強磁性）が現れる。

---

### 2. 外部磁場を加えたときの自由エネルギー

外部磁場 \( h_{\text{ext}} \) が存在する場合、全自由エネルギー \( G(h_{\text{ext}}) \) は次のように書ける：

\[
e^{-\beta G(h_{\text{ext}})} = 
\int dm\, e^{N h_{\text{ext}} m - \beta F(m)}
\simeq e^{N [h_{\text{ext}} m^*(h_{\text{ext}}) - \beta F(m^*(h_{\text{ext}}))]},
\tag{IV.3}
\]

ここで \( m^*(h_{\text{ext}}) \) は積分の**鞍点（saddle point）**であり、次の条件で決定される：

\[
h_{\text{ext}} = \frac{1}{N} \frac{\partial(-\beta F(m))}{\partial m}
\Big|_{m = m^*(h_{\text{ext}})}.
\tag{IV.4}
\]

これは、**自由エネルギーの極値条件**に相当する。

---

### ① 外部磁場を導入したときの統計力学的枠組み

統計力学では、巨視的自由エネルギー \( G(h_{\text{ext}}) \) は、**分配関数（partition function）**を通して定義される。

磁化 \( m \) を固定した系の自由エネルギーを \( F(m) \) とすると、外部磁場をかけたときの「全体の分配関数」は：

\[
Z(h_{\text{ext}}) = \int dm \, e^{N h_{\text{ext}} m - \beta F(m)}.
\]

ここで：
- \( N \) はスピンの数（系のサイズ）  
- \( \beta = 1 / (k_B T) \) は逆温度  
- \( h_{\text{ext}} m \) の項は「外場との相互作用エネルギー」  

物理的な意味としては、  
「各磁化状態 \( m \) に重み \( e^{-\beta F(m)} \) を与え、さらに外場によってエネルギーがシフトする」  
という状況を表している。

---

### ② 巨視的自由エネルギー \( G(h_{\text{ext}}) \) の定義

次に、この分配関数から**巨視的自由エネルギー（Gibbs自由エネルギー）**を定義する：

\[
G(h_{\text{ext}}) = - \frac{1}{\beta} \log Z(h_{\text{ext}}).
\]

この式は「統計的な平均エネルギー」と「エントロピー寄与」をまとめたもので、外場 \( h_{\text{ext}} \) を制御変数とするエネルギー表現である。

これを式の形に直すと：

\[
e^{-\beta G(h_{\text{ext}})} = \int dm\, e^{N h_{\text{ext}} m - \beta F(m)}.
\tag{IV.3}
\]

---

### ③ 鞍点近似（Saddle-point approximation）

ここで、スピン数 \( N \) は非常に大きい（熱力学極限）と考える。  
その場合、上の積分は指数の中に \( N \) が掛かっているため、  
**ラプラスの方法（Laplace’s method）**または**鞍点近似（saddle-point approximation）**を使うことができる。

---

#### 🔹鞍点近似とは？

積分
\[
I = \int dx\, e^{N f(x)}
\]
において、\( N \gg 1 \) のときは、\( f(x) \) が最大となる点 \( x^* \) の近傍が支配的になる。

したがって、
\[
I \approx e^{N f(x^*)}.
\]

この近似を使うと、式 (IV.3) の右辺は次のようになる：

\[
e^{-\beta G(h_{\text{ext}})} \simeq 
e^{N [h_{\text{ext}} m^*(h_{\text{ext}}) - \beta F(m^*(h_{\text{ext}}))]}.
\]

ここで \( m^*(h_{\text{ext}}) \) は、指数部が最大になる点、すなわち**鞍点（saddle point）**である。

---

### ④ 鞍点条件の導出

鞍点条件は「指数の中の関数が極値をとる点」で決まる。  
したがって、次の条件を課す：

\[
\frac{d}{dm}\left[ h_{\text{ext}} m - \frac{\beta}{N} F(m) \right]_{m = m^*} = 0.
\]

これを整理すると、

\[
h_{\text{ext}} = \frac{1}{N} \frac{\partial(-\beta F(m))}{\partial m}
\Big|_{m = m^*(h_{\text{ext}})}.
\tag{IV.4}
\]

これが式 (IV.4) の由来であり、**自由エネルギーの極値条件**と呼ばれる。

---

### ⑤ 物理的意味：外場と自由エネルギーの関係

この関係式を物理的に読み解くと：

- 左辺 \( h_{\text{ext}} \) は「外部磁場」  
- 右辺は「内部的な応答（自由エネルギーの勾配）」  

つまり、「外場が与える力」と「系がもつ内部エネルギー勾配」が釣り合う点が、平衡状態の磁化 \( m^*(h_{\text{ext}}) \) である、という意味になる。

---

### ⑥ 熱力学的関係式との対応

実はこの式は、マクロ熱力学の次の関係と同じ構造をもつ：

\[
h_{\text{ext}} = \frac{\partial F}{\partial M}
\]

ここで \( F \) はヘルムホルツ自由エネルギー、\( M \) は磁化（＝順序変数）。  
したがって、式 (IV.4) は「自由エネルギー \( F(m) \) の最小化条件」を意味する。

---

### ⑦ 結果：外場ゼロでの自発磁化

このようにして求めた \( m^*(h_{\text{ext}}) \) のうち、外場をゼロにしたときの値：

\[
m_s = m^*(0),
\]

が、系の**自発磁化（spontaneous magnetization）**となる。

この値がゼロなら常磁性、非ゼロなら強磁性であり、  
これがランダウ理論における**相転移の判定基準**となる。

---

### 🔍 補足：Legendre変換との関係

式 (IV.3) と (IV.4) の関係は、より一般的には**自由エネルギーのLegendre変換**と見なせる：

\[
G(h) = F(m^*) - N h m^*,
\]
\[
\frac{\partial F}{\partial m} = N h.
\]

つまり、\( F(m) \) と \( G(h) \) は互いに共役な変数（\( m \leftrightarrow h \)）をもつ**双対関数**である。

この「\( m \) と \( h \) のLegendre変換関係」は、後に**スピングラス**や**p-spin模型**の解析でも頻繁に用いられる。

---

### 💡まとめ

| 概念 | 数式 | 意味 |
|------|------|------|
| 分配関数 | \( Z(h) = \int dm\, e^{N h m - \beta F(m)} \) | 外場付き自由エネルギーの基礎 |
| 巨視的自由エネルギー | \( G(h) = -\frac{1}{\beta} \log Z(h) \) | 外場を制御変数とする自由エネルギー |
| 鞍点近似 | \( e^{-\beta G(h)} \simeq e^{N[h m^* - \beta F(m^*)]} \) | 熱力学極限で支配的な磁化を抽出 |
| 鞍点条件 | \( h = \frac{1}{N}\frac{\partial(-\beta F)}{\partial m} \) | 自由エネルギー極小化条件 |
| 自発磁化 | \( m_s = m^*(0) \) | 外場ゼロでの平衡磁化 |

---

以上が、式 (IV.3) および (IV.4) の詳細な物理的・数学的意味である。

### 3. 自発磁化の導出

系のサイズ \( N \to \infty \) の熱力学極限を取ると、  
順序変数 \( m_s \) は次のように得られる：

\[
m_s = m^*(0).
\]

つまり、外部場を取り去った状態での鞍点磁化が、系の**自発磁化**を与える。

---

## まとめと次節への導入

ここまでで、ランダウ理論に基づいて**強磁性転移**を定性的に理解した。  
次節では、この自由エネルギー \( F(m) \)（および \( G(h) \)）を、  
**より具体的な可解模型（solvable mean-field microscopic model）**の枠組みの中で導出していく。

---

# B. Generic Strategy（一般的な戦略）

ここでは、強磁性系に限らず一般のスピン系に対して、**順序変数（order parameter）**と**共役場（conjugated field）**をどのように導入し、自由エネルギーとの関係をどのように整理するかを議論する。  
この枠組みは、後にスピングラスやp-spin模型などにもそのまま応用される。

## 1. The Order Parameter and Conjugated Field（順序変数と共役場）

### 1️⃣ スピン系と外部磁場の導入

スピン変数 $S_i$（$i = 1, 2, \dots, N$）を持つ系のハミルトニアンを $H[\{S_i\}]$ とする。  
ここに外部磁場 $h$ による結合項を追加して、次のように書き換える：

$$
- \beta H[\{S_i\}] \;\longrightarrow\; - \beta H[\{S_i\}] + h \sum_{i=1}^N S_i.
\tag{IV.5}
$$

ここで：
- $\beta = 1 / (k_B T)$ は逆温度  
- 第2項 $h \sum_i S_i$ は、スピンが磁場と相互作用する項である  

これにより、外部磁場 $h$ が**共役場（conjugated field）**として導入される。  
すなわち、磁場がスピンの並びを制御する変数となる。

---

### 2️⃣ 自由エネルギーの定義

上のように外部磁場を導入したとき、  
系の自由エネルギー $G(h)$（Gibbs型自由エネルギー）は次のように定義される：

$$
- \beta G(h) = \ln 
\left[
\prod_{i=1}^N \mathrm{Tr}_{S_i}
\right]
e^{-\beta H[\{S_i\}] + h \sum_{i=1}^N S_i}.
\tag{IV.6}
$$

ここで：
- $\mathrm{Tr}_{S_i}$ はスピン $S_i$ の全ての状態（例：$S_i = \pm 1$）に対する和  
- $e^{-\beta H[\{S_i\}]}$ はボルツマン因子  
- 対数を取ることで「分配関数の対数 = 自由エネルギー」を得ている  

この式は、**外部磁場を制御変数とする統計系の基本的定義**である。

---

### 3️⃣ 磁化（Magnetization）の定義

上の自由エネルギーを用いると、  
磁化 $m(h)$（スピン1個あたりの平均磁化）は次のように計算できる：

$$
m(h) = \frac{1}{N} \sum_{i=1}^N \langle S_i \rangle_h
= \frac{1}{N} \frac{\partial (-\beta G(h))}{\partial h}.
\tag{IV.7}
$$

ここで：
- $\langle \cdots \rangle_h$ は「外部磁場 $h$ のもとでの熱平均」  
- $\frac{\partial G}{\partial h}$ が磁化に対応することは、  
  熱力学における一般的な関係式 $\partial G / \partial h = -M$ の統計力学版である。

---

### 4️⃣ 対称性の破れと外場の役割

次に、スピン系が「反転対称性」を持つ場合を考える。

$$
S_i \rightarrow -S_i \quad \forall i.
$$

このとき、外場 $h$ はこの対称性を**明示的に破る**。  
つまり、$h > 0$ ならスピンは上向きに揃いやすく、$h < 0$ なら下向きに揃いやすくなる。

しかし、$h = 0$ の場合でも、系が**自発的に**一方向を選ぶことがある。  
これが「**自発的対称性の破れ（spontaneous symmetry breaking）**」である。

---

### 5️⃣ 自発磁化（Spontaneous Magnetization）の定義

強磁性をもつ系では、外場を取り去ったときにも有限の磁化が残る。  
この「外場がないのに磁化が存在する状態」を**自発磁化**と呼び、次のように定義する：

$$
m_s = \lim_{h \to 0} \lim_{N \to \infty} m(h).
\tag{IV.8}
$$

ここで重要なのは**極限の順序**である。

---

### 6️⃣ 極限操作の非可換性（Non-commutativity of Limits）

常磁性相（paramagnetic phase）では、磁化は常にゼロであり、極限の順序を入れ替えても同じ結果になる：

$$
\lim_{h \to 0} \lim_{N \to \infty} m(h)
= \lim_{N \to \infty} \lim_{h \to 0} m(h)
= 0.
$$

一方で、強磁性相（ferromagnetic phase）では、極限が可換でない。すなわち：

$$
\lim_{N \to \infty} \lim_{h \to 0} m(h) = 0,
$$

だが、

$$
\lim_{h \to 0^+} \lim_{N \to \infty} m(h) > 0,
\quad
\lim_{h \to 0^-} \lim_{N \to \infty} m(h) < 0.
$$

---

### 🔹 物理的意味

- **$h \to 0$ の前に $N \to \infty$ を取る**：  
  系が十分大きいと、わずかな外場で対称性が破れる → 自発磁化が現れる。  

- **$N \to \infty$ の前に $h \to 0$ を取る**：  
  有限サイズでは外場がない限り平均磁化はゼロ → 対称性が保持される。

この非可換性こそが、**「自発的対称性の破れ」**を定量的に記述する本質である。

---

### ✅ まとめ

| 概念 | 数式 | 意味 |
|------|------|------|
| 外場つきハミルトニアン | $-\beta H + h \sum_i S_i$ | 外部磁場の導入 |
| 自由エネルギー | $- \beta G(h) = \ln \sum_{\{S_i\}} e^{-\beta H + h \sum_i S_i}$ | 統計的重みの対数 |
| 磁化 | $m(h) = \frac{1}{N} \frac{\partial(-\beta G)}{\partial h}$ | 外場に対する応答 |
| 自発磁化 | $m_s = \lim_{h\to 0} \lim_{N\to\infty} m(h)$ | 対称性破れの指標 |
| 非可換性 | $\lim_{N\to\infty}\lim_{h\to0} \neq \lim_{h\to0}\lim_{N\to\infty}$ | 強磁性の特徴 |

---

### 💬 補足：順序変数と共役場の関係

- **順序変数（Order parameter）**：系の「秩序」の度合いを測る指標。  
  強磁性では磁化 $m$ がその役割を果たす。

- **共役場（Conjugated field）**：順序変数に直接結合する外場。  
  磁化 $m$ に対しては磁場 $h$ が共役場となる。

この $m$–$h$ の関係は、以降の**Legendre変換**（$F(m)$ と $G(h)$ の対応）や、  
**鞍点近似による自由エネルギー評価**の基本構造に直結していく。


## 2. Legendre Transform（ルジャンドル変換）

この節では、自由エネルギーの2つの表現  
すなわち「外部磁場 $h$ を制御変数とする $G(h)$」と  
「磁化 $m$ を制御変数とする $F(m)$」の間の関係を、  
**Legendre変換**によって厳密に対応づける。

この構造は、統計力学における**双対性（duality）**の最も基本的な例であり、  
以降のガラス系やp-spin模型でも中心的な役割を果たす。

### 1️⃣ Legendre変換の定義

Legendre変換とは、ある関数をその傾き（＝共役変数）で書き換える操作である。  
ここでは、磁化 $m$ と外部磁場 $h$ が互いに**共役変数（conjugate variables）**として働く。

#### 定義式：

$$
- \beta F(m) = - \beta G(h^*) - N h^* m
\tag{IV.9}
$$

ここで：

- $G(h)$：外場を固定したときの自由エネルギー（Gibbs型）  
- $F(m)$：磁化を固定したときの自由エネルギー（Helmholtz型）  
- $h^* = h^*(m)$：磁化 $m$ に対応する外場の値  

---

### 2️⃣ $h^*(m)$ の決定条件（順方向）

$h^*(m)$ は、$G(h)$ の傾きに関する次の条件から求められる：

$$
m = \frac{1}{N} \frac{\partial (-\beta G(h))}{\partial h}
\Big|_{h = h^*(m)}
= \frac{1}{N} \sum_{i=1}^N \langle S_i \rangle_{h = h^*(m)}.
\tag{IV.10}
$$

つまり、  
「外場 $h^*$ をかけたときの磁化の平均値が $m$ になるように $h^*$ を選ぶ」  
という意味である。

---

#### 🔹物理的な意味

- $G(h)$ は「外場をかけたときの自由エネルギー」なので、  
  その勾配 $\frac{\partial G}{\partial h}$ が磁化に対応する。
- 逆に言えば、磁化を固定したいときは「その磁化を実現する $h^*$」を求める。

この関係式が、$m$ と $h$ を結ぶ**状態方程式（equation of state）**を定義する。

---

### 3️⃣ 磁化率（Linear Susceptibility）

磁化率 $\chi$ は「外場の変化に対する磁化の応答」を表す。  
つまり、$m(h)$ の1次微分として次のように定義される：

$$
\chi = \frac{\partial m}{\partial h}
= \frac{1}{N} \frac{\partial^2 (-\beta G(h))}{\partial h^2}
\Big|_{h = h^*(m)}.
\tag{IV.11a}
$$

統計力学的に書くと：

$$
\chi = \frac{1}{N} \sum_{i,j=1}^N
\Big( \langle S_i S_j \rangle - \langle S_i \rangle \langle S_j \rangle \Big),
\tag{IV.11b}
$$

すなわち「スピンの相関の総和」として表される。

---

#### 🔹物理的解釈

- $\chi > 0$：外場を強めると磁化も増える → 安定な平衡状態  
- $\chi < 0$：応答が反転する（不安定） → 鞍点近似が破綻する  

つまり、安定な熱平衡状態では常に $\chi > 0$ でなければならない。

---

### 4️⃣ 逆Legendre変換（逆方向）

次に、$F(m)$ から $G(h)$ を復元する逆操作を定義する。

### 定義式：

$$
- \beta G(h) = - \beta F(m^*) + N h m^*,
\tag{IV.12}
$$

ここで $m^* = m^*(h)$ は、与えられた外場 $h$ に対して平衡に達する磁化であり、  
次の条件式を満たす：

$$
- h = \frac{1}{N} \frac{\partial (-\beta F(m))}{\partial m}
\Big|_{m = m^*(h)}.
\tag{IV.12′}
$$

---

### 5️⃣ $m(h)$ と $h(m)$ の対称性

上の式を見比べると、次のような**完全な対称性**が見えてくる：

| 方向 | 定義関係 | 意味 |
|------|-----------|------|
| $h \to m$ 方向 | $m = \frac{1}{N} \frac{\partial(-\beta G(h))}{\partial h}$ | 外場を与えて磁化を測る（実験的状況） |
| $m \to h$ 方向 | $-h = \frac{1}{N} \frac{\partial(-\beta F(m))}{\partial m}$ | 磁化を固定して必要な外場を求める（理論的構築） |

この対称性こそが **Legendre変換の核心** であり、  
$F(m)$ と $G(h)$ が互いに「双対関数」であることを意味する。

---

### 6️⃣ 逆磁化率（Inverse Susceptibility）

Legendre変換の対称性から、  
磁化率の逆数（外場応答の勾配）も自然に得られる：

$$
\chi^{-1} = \frac{\partial h}{\partial m}
= \frac{1}{N} \frac{\partial^2 (\beta F(m))}{\partial m^2}
\Big|_{m = m^*(h)}.
\tag{IV.13}
$$

---

#### 🔹対応関係まとめ

| 量 | $G(h)$側の表現 | $F(m)$側の表現 | 意味 |
|----|----------------|----------------|------|
| 平衡条件 | $\displaystyle m = \frac{1}{N}\frac{\partial(-\beta G)}{\partial h}$ | $\displaystyle -h = \frac{1}{N}\frac{\partial(-\beta F)}{\partial m}$ | 双対条件 |
| 磁化率 | $\displaystyle \chi = \frac{\partial m}{\partial h}$ | $\displaystyle \chi^{-1} = \frac{\partial h}{\partial m}$ | 応答と安定性 |
| 自由エネルギー | $G(h)$ | $F(m)$ | 制御変数の違い |
| 安定性条件 | $\chi > 0$ | $\chi^{-1} > 0$ | 極小点の安定性 |

---

#### 💬 直感的なイメージ

- $G(h)$：外場を操作して「磁化がどう応答するか」を見る（実験家の視点）  
- $F(m)$：磁化を固定して「その状態を保つために必要な外場」を計算する（理論家の視点）  

どちらも同じ物理系を記述しているが、**制御変数（input）と応答変数（output）を入れ替えた**だけである。

---

#### ✅ まとめ

$$
\boxed{
\begin{aligned}
m(h) &= \frac{1}{N}\frac{\partial(-\beta G)}{\partial h}, \\[4pt]
h(m) &= -\frac{1}{N}\frac{\partial(-\beta F)}{\partial m}, \\[6pt]
\chi &= \frac{\partial m}{\partial h}, \quad
\chi^{-1} = \frac{\partial h}{\partial m}.
\end{aligned}
}
$$

このように、$m(h)$ と $h(m)$ は完全に双対的な関係にあり、  
それぞれの自由エネルギー $G(h)$ と $F(m)$ は互いに**Legendre変換**で結ばれている。

---

## 3. 1st Step of the Recipe（計算手順の第1ステップ）

ここでは、前節で導入した **Legendre変換（ルジャンドル変換）** とその逆変換を、実際にどのように統計力学的に実装できるかを示す。  
その基本的な考え方は、「磁化 $m$ を固定した積分表現」を導入することで、  
自由エネルギー $F(m)$ と $G(h)$ をつなぐものである。

---

### 1️⃣ δ関数による制約の導入

まず、磁化 $m = \frac{1}{N} \sum_i S_i$ を導入するために、次の恒等式を用いる：

$$
1 = N \int dm\, \delta\left( N m - \sum_{i=1}^N S_i \right).
$$

これは、磁化 $m$ がスピンの平均であるという定義を「δ関数」で強制するものである。  
これを **複素積分表示** に書き換えると次のようになる：

$$
1 = N \int dm \int_{-i\infty}^{i\infty} \frac{dh}{2\pi i}\,
e^{-N m h} \prod_{i=1}^N e^{h S_i}.
\tag{IV.15}
$$

ここで用いたのが、**δ関数の積分表示**：

$$
\delta(x) = \int_{-i\infty}^{i\infty} \frac{dk}{2\pi i}\, e^{-k x}.
\tag{IV.16}
$$

---

### 2️⃣ 外部磁場つき分配関数の再定式化

外部磁場 $h_{\text{ext}}$ のもとでの分配関数は次のように書ける：

$$
Z(h_{\text{ext}}) =
\prod_{i=1}^N \mathrm{Tr}_{S_i}\,
e^{-\beta H + h_{\text{ext}} \sum_{i=1}^N S_i}.
$$

ここで前述の恒等式（IV.15）を代入することで、$m$ と $h$ に関する積分表現を得る：

$$
Z(h_{\text{ext}})
= N \int dm \int_{-i\infty}^{i\infty} \frac{dh}{2\pi i}\,
e^{-N m h}
\prod_{i=1}^N
\left(
\mathrm{Tr}_{S_i} e^{(h + h_{\text{ext}}) S_i}
\right)
e^{-\beta H}.
\tag{IV.17-first}
$$

---

### 3️⃣ 非相互作用系の導入

次に、「相互作用を持たない」基準系を定義する：

$$
- \beta G_0(h) = N \ln \mathrm{Tr}_S e^{h S}.
\tag{IV.18}
$$

このとき、**非相互作用平均**（相互作用を無視した場合の平均値）を次のように定義する：

$$
\langle \cdots \rangle_{h,0}
=
\frac{\prod_i \mathrm{Tr}_{S_i} \, e^{h S_i} (\cdots)}
{\prod_i \mathrm{Tr}_{S_i} \, e^{h S_i}}.
\tag{IV.19}
$$

この平均では、各スピンが互いに独立であるため、

$$
\langle S_i S_j \rangle_{h,0} = 
\langle S_i \rangle_{h,0}\langle S_j \rangle_{h,0} \quad (i \neq j)
\tag{IV.20}
$$

が成立する。

---

### 4️⃣ 相互作用を含めた自由エネルギー

実際の系では相互作用 $H[\{S_i\}]$ が存在するため、  
全自由エネルギー $G(h)$ を次のように定義する：

$$
- \beta G(h) = - \beta G_0(h) + \ln \langle e^{-\beta H} \rangle_h.
\tag{IV.21}
$$

ここで $\langle \cdots \rangle_h$ は、相互作用を含めた系の平均を意味する。  
すなわち（IV.19）の平均とは異なる。

---

### 5️⃣ 鞍点近似による $h$ 積分

スピン数 $N$ が非常に大きい（熱力学極限）場合、  
積分は指数部が最大となる点（**鞍点**）で支配される。

したがって、$h$ に関する積分は鞍点近似により評価できる。

- 鞍点条件：  
  $$
  \frac{\partial}{\partial h}
  \left[
  -N m h - \beta G(h)
  \right] = 0.
  $$
- これが成立する点を $h = h^*(m)$ とする。

この近似が有効であるためには、**磁化率**
$$
\chi = \frac{\partial m}{\partial h}
\tag{IV.11}
$$
が **正定値（positive semi-definite）** であることが必要。  
（そうでない場合、鞍点が不安定となる。）

---

### 6️⃣ 再び $m$ に関する鞍点近似

次に、$m$ に関しても鞍点法を適用する。  
結果として次の形を得る：

$$
Z(h_{\text{ext}}) =
N \int dm\, e^{N h_{\text{ext}} m - \beta F(m)}
\simeq
e^{N h_{\text{ext}} m^*(h_{\text{ext}}) - \beta F(m^*(h_{\text{ext}}))}.
\tag{IV.17-final}
$$

これは、前節の Legendre変換（Eq. (IV.9)）
$$
- \beta F(m) = - \beta G(h^*(m)) - N h^*(m) m
$$
を用いて導かれる。

---

### 7️⃣ 鞍点条件（磁化の自己無撞着条件）

$h^*(m)$ は、以下の条件によって決まる：

$$
m =
\frac{1}{N} \frac{\partial(-\beta G(h))}{\partial h}
\Big|_{h = h^*(m)}
= \frac{1}{N} \sum_{i=1}^N \langle S_i \rangle_{h = h^*(m)}.
\tag{IV.23}
$$

全スピンが等価であるため、任意の $i$ について：

$$
m = \langle S_i \rangle_{h = h^*(m)} \quad \forall i.
\tag{IV.24}
$$

---

### 8️⃣ 鞍点近似の安定性条件

最後に、$m$-積分における鞍点近似が有効であるためには、  
**逆磁化率 $\chi^{-1}$**（Eq. (IV.14)）が正定値である必要がある。  
これにより、鞍点が局所的に安定な極値であることが保証される。

---

### 🔹まとめ

| ステップ | 内容 | 式 |
|-----------|------|----|
| (1) δ関数導入 | 磁化を固定する | (IV.15) |
| (2) 外場付き分配関数 | $Z(h_{\text{ext}})$ の積分表示 | (IV.17) |
| (3) 非相互作用系 | $G_0(h)$ と平均の定義 | (IV.18)–(IV.20) |
| (4) 相互作用系 | $G(h) = G_0(h) - \frac{1}{\beta}\ln \langle e^{-\beta H} \rangle_h$ | (IV.21) |
| (5) 鞍点法（h積分） | $\chi > 0$ なら有効 | — |
| (6) 鞍点法（m積分） | Legendre変換に対応 | (IV.9), (IV.17-final) |
| (7) 鞍点条件 | $m = \langle S_i \rangle_{h=h^*(m)}$ | (IV.23)–(IV.24) |
| (8) 安定性 | $\chi^{-1} > 0$ が必要 | — |

---

これにより、  
統計力学的に **自由エネルギー $F(m)$** と **巨視的自由エネルギー $G(h)$** を  
厳密に対応づける操作（Legendre変換）が、  
「磁化固定条件をδ関数で実装 → 鞍点近似で評価」という具体的手順として再現された。

---
