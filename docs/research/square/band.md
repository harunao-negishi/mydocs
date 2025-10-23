# 2次元正方格子のバンド分散

まず初めに、二次元正方格子のバンド分散についてまとめてみましょう。

強束縛模型のハミルトニアンを構築して、そこから**波数に対するエネルギー分散、\(\epsilon(k)\)**を求めてそれをプロットすることが目標になります。

## 0. ねらい
- 強束縛模型の**一般形**からスタートし、
- フーリエ変換で **\(k\)-空間ハミルトニアン**を導出、
- **2次元正方格子**に適用して**分散関係 \(\varepsilon(\mathbf{k})\)** を得る。

> 記法：格子定数 \(a\)、格子点位置 \(\mathbf{R}\)、運動量 \(\mathbf{k}\)、最近接ホッピング \(t\)、次近接 \(t'\)、第3近接 \(t''\)。

---

## 1. 一般化した強束縛模型（単一軌道・スピンなし）

実空間の二次量子化ハミルトニアン：

$$ 
\hat{H}= \sum_{\mathbf{R}} \epsilon_0\, \hat{c}^\dagger_{\mathbf{R}} \hat{c}_{\mathbf{R}}+ \sum_{\mathbf{R}}\sum_{\boldsymbol{\delta}} t(\boldsymbol{\delta})\,\hat{c}^\dagger_{\mathbf{R}} \hat{c}_{\mathbf{R}+\boldsymbol{\delta}}. 
$$

ここでは、１サイトに１軌道しかないものとして扱う。多軌道・多サイトは別のタブで考える。
Rについての和は、全サイトで取るようにする。

- \(\hat{c}^\dagger_{\mathbf{R}}\)：サイト \(\mathbf{R}\) での生成演算子  
- \(\epsilon_0\)：オンサイトエネルギー  (そのサイトに電子が一つ存在するときのエネルギー)
- \(t(\boldsymbol{\delta})\)：相対ベクトル \(\boldsymbol{\delta}\) へのホッピング（距離に応じて \(t, t', t''\dots\)）

ハミルトニアンはエルミート演算子であることから、**エルミート性**より

\[
t(\boldsymbol{\delta}) = t^*(-\boldsymbol{\delta}).
\]

実パラメータを仮定すれば \(t(\boldsymbol{\delta}) = t(-\boldsymbol{\delta})\)。

---

## 2. フーリエ変換と \(\mathbf{k}\)-空間ハミルトニアン

ここでは実空間の二次量子化ハミルトニアンをフーリエ変換する。

\[
\hat{c}_{\mathbf{R}} = \frac{1}{\sqrt{N}}\sum_{\mathbf{k}} e^{i\mathbf{k}\cdot\mathbf{R}} \hat{c}_{\mathbf{k}},
\quad
\hat{c}^\dagger_{\mathbf{R}} = \frac{1}{\sqrt{N}}\sum_{\mathbf{k}} e^{-i\mathbf{k}\cdot\mathbf{R}} \hat{c}^\dagger_{\mathbf{k}}.
\]

これを実空間の二次量子化ハミルトニアンに代入する：

### (1) オンサイト項

\[
\sum_{\mathbf{R}} \epsilon_0\, \hat{c}^\dagger_{\mathbf{R}} \hat{c}_{\mathbf{R}}
= \frac{\epsilon_0}{N}\sum_{\mathbf{R}}\sum_{\mathbf{k},\mathbf{k}'}
e^{-i\mathbf{k}\cdot\mathbf{R}} e^{i\mathbf{k}'\cdot\mathbf{R}}
\hat{c}^\dagger_{\mathbf{k}}\hat{c}_{\mathbf{k}'}
= \epsilon_0\sum_{\mathbf{k}}\hat{c}^\dagger_{\mathbf{k}}\hat{c}_{\mathbf{k}}.
\]

（\(\sum_{\mathbf{R}} e^{i(\mathbf{k}'-\mathbf{k})\cdot\mathbf{R}} = N \delta_{\mathbf{k},\mathbf{k}'}\) を使用）

### (2) ホッピング項

\[
\sum_{\mathbf{R},\boldsymbol{\delta}} t(\boldsymbol{\delta})
\hat{c}^\dagger_{\mathbf{R}} \hat{c}_{\mathbf{R}+\boldsymbol{\delta}}
= \frac{1}{N}\sum_{\mathbf{R},\boldsymbol{\delta}} t(\boldsymbol{\delta})
\sum_{\mathbf{k},\mathbf{k}'}
e^{-i\mathbf{k}\cdot\mathbf{R}}
e^{i\mathbf{k}'\cdot(\mathbf{R}+\boldsymbol{\delta})}
\hat{c}^\dagger_{\mathbf{k}}\hat{c}_{\mathbf{k}'}.
\]

\[
= \frac{1}{N}\sum_{\boldsymbol{\delta}} t(\boldsymbol{\delta})
\sum_{\mathbf{k},\mathbf{k}'} e^{i\mathbf{k}'\cdot\boldsymbol{\delta}}
\left[\sum_{\mathbf{R}} e^{i(\mathbf{k}'-\mathbf{k})\cdot\mathbf{R}}\right]
\hat{c}^\dagger_{\mathbf{k}}\hat{c}_{\mathbf{k}'}
= \sum_{\mathbf{k}}\left[\sum_{\boldsymbol{\delta}} t(\boldsymbol{\delta}) e^{i\mathbf{k}\cdot\boldsymbol{\delta}}\right]
\hat{c}^\dagger_{\mathbf{k}}\hat{c}_{\mathbf{k}}.
\]

よって

\[
\hat{H}=\sum_{\mathbf{k}} \varepsilon(\mathbf{k})\,\hat{c}^\dagger_{\mathbf{k}}\hat{c}_{\mathbf{k}},
\quad
\boxed{\ \varepsilon(\mathbf{k})
= \epsilon_0 + \sum_{\boldsymbol{\delta}} t(\boldsymbol{\delta}) e^{i\mathbf{k}\cdot\boldsymbol{\delta}}.\ }
\]


> 直感：\(\varepsilon(\mathbf{k})\) は「全ホッピングの**位相和**」。  
> 対称性 \(t(\boldsymbol{\delta})=t(-\boldsymbol{\delta})\) を使うと
> 
> \[
> \varepsilon(\mathbf{k}) = \epsilon_0 + 2\sum_{\boldsymbol{\delta}>0} t(\boldsymbol{\delta}) \cos(\mathbf{k}\cdot\boldsymbol{\delta}).
> \]

---

## 3. 2次元正方格子（square lattice）への適用

### 3.1 格子とブリルアンゾーン
- 実空間基底：\(\mathbf{a}_1=(a,0),\ \mathbf{a}_2=(0,a)\)  
- 逆格子基底：\(\mathbf{b}_1=\tfrac{2\pi}{a}(1,0),\ \mathbf{b}_2=\tfrac{2\pi}{a}(0,1)\)  （具体的な形がわからなくても、\(\mathbf{a}_i\cdot\mathbf{b}_j=2\pi i\delta_{ij}\)をわかっていればよい）
- 1次BZ：\(k_x, k_y \in [-\pi/a,\,\pi/a]\)

**最近接（NN）**の相対ベクトル：

\[
\boldsymbol{\delta}\in\{(\pm a,0),(0,\pm a)\}.
\]

これについても、実空間の基底に対して…と考えた方が応用が効いてよいと思われる。

### 3.2 近接の順に加える

#### (i) 最近接のみ（\(t\)）

\[
\varepsilon_{\text{NN}}(\mathbf{k})
= \epsilon_0 + t\big(e^{ik_x a}+e^{-ik_x a}+e^{ik_y a}+e^{-ik_y a}\big)
= \epsilon_0 + 2t\big(\cos k_x a + \cos k_y a\big).
\]

> 物性ではしばしば \(t>0\) と置き、バンドを \(-2t(\cos k_xa + \cos k_ya)\) と書く流儀もある。  
> **符号は定義（基底の位相やエネルギー原点）で変わり得る**ので、後の比較では一貫性を持たせること。

#### (ii) 次近接（\(t'\)）：斜め（対角）ホッピング

\[
\boldsymbol{\delta}\in\{(\pm a,\pm a)\}.
\]

\[
\sum_{\text{NNN}} e^{i\mathbf{k}\cdot\boldsymbol{\delta}}
= 2\cos(k_x a + k_y a)+2\cos(k_x a - k_y a)
= 4\cos k_x a \cos k_y a.
\]

\[
\Rightarrow\ \varepsilon_{\text{NNN}}(\mathbf{k})
= \varepsilon_{\text{NN}}(\mathbf{k}) + 4t' \cos k_x a \cos k_y a.
\]

#### (iii) 第3近接（\(t''\)）：直交2a

\[
\boldsymbol{\delta}\in\{(\pm 2a,0),(0,\pm 2a)\}.
\]

\[
\Rightarrow\ \varepsilon_{\text{3rd}}(\mathbf{k})
= \varepsilon_{\text{NNN}}(\mathbf{k}) + 2t''\big(\cos 2k_x a + \cos 2k_y a\big).
\]

### 3.3 まとめ（代表的な形）

$$ \boxed{\;\varepsilon(\mathbf{k})= \epsilon_0+ 2t\big(\cos k_x a + \cos k_y a\big)+ 4t'\cos k_x a \cos k_y a+ 2t''\big(\cos 2k_x a + \cos 2k_y a\big)+\cdots\;} $$

> しばしば \(\epsilon_0\) を吸収して **化学ポテンシャル** \(\mu\) を用い、\(\xi(\mathbf{k})=\varepsilon(\mathbf{k})-\mu\) と書く。

---

## 4. バンドの特徴（メモ）
- 最近接のみ：帯域幅 \(W=8|t|\)、頂点・谷は \(\Gamma=(0,0)\) と \((\pi/a,\pi/a)\)。  
- \(t'\) を入れると**電子–正孔非対称**が生じ、\((\pi/a,0)\)・\((0,\pi/a)\) 付近（\(\mathrm{M}\)点）で**鞍点（van Hove）**の位置やエネルギーがずれる。  
- \(t''\) はさらなる非対称性や曲率調整に効く。

---

## 5. よくある拡張・注意
- **多軌道**：\(\hat{H}(\mathbf{k})\) は行列になり、固有値問題 \(\det|H(\mathbf{k})-E|=0\)。  
- **スピン**：スピン縮退やスピン–軌道相互作用（SOC）を入れるとブロックが増える。  
- **規格化**：フーリエ変換の \(1/\sqrt{N}\) などは全体で整合すればOK。  
- **符号規約**：文献間で \(t\) の符号や \(\epsilon_0\) の取り方が違うことがあるので比較時は注意。

---

## 6. 多軌道（多サイト）強束縛模型の基本

単一セルに \(M\) 軌道（あるいは \(M\) サブ格子）ある場合、実空間は

\[
\hat{H}
= \sum_{\mathbf{R}}\sum_{\alpha=1}^{M}\epsilon_\alpha\,
\hat{c}^\dagger_{\mathbf{R}\alpha}\hat{c}_{\mathbf{R}\alpha}
+ \sum_{\mathbf{R}}\sum_{\boldsymbol{\delta}}\sum_{\alpha,\beta}
t_{\alpha\beta}(\boldsymbol{\delta})\,
\hat{c}^\dagger_{\mathbf{R}\alpha}\hat{c}_{\mathbf{R}+\boldsymbol{\delta},\beta}.
\]

\[
\hat{c}_{\mathbf{R}\alpha} = \frac{1}{\sqrt{N}}\sum_{\mathbf{k}} e^{i\mathbf{k}\cdot\mathbf{R}} \hat{c}_{\mathbf{k}\alpha}
\quad\Rightarrow\quad
\hat{H} = \sum_{\mathbf{k}} \hat{\boldsymbol{c}}^\dagger_{\mathbf{k}}\, H(\mathbf{k})\, \hat{\boldsymbol{c}}_{\mathbf{k}},
\]

\[
\boxed{\ H_{\alpha\beta}(\mathbf{k})
= \epsilon_\alpha \delta_{\alpha\beta} + \sum_{\boldsymbol{\delta}} t_{\alpha\beta}(\boldsymbol{\delta}) e^{i\mathbf{k}\cdot\boldsymbol{\delta}}.\ }
\]

ここで \(\hat{\boldsymbol{c}}_{\mathbf{k}} = (\hat{c}_{\mathbf{k}1},\dots,\hat{c}_{\mathbf{k}M})^\mathsf{T}\)。  
固有値問題：

\[
H(\mathbf{k}) \, \boldsymbol{u}_n(\mathbf{k}) = E_n(\mathbf{k}) \boldsymbol{u}_n(\mathbf{k}),
\quad n=1,\dots,M.
\]

### 例：2サイト（A/B）モデル

\[
H(\mathbf{k})=
\begin{pmatrix}
\epsilon_A + \sum_{\delta} t_{AA}(\delta)e^{i\mathbf{k}\cdot\delta} & \sum_{\delta} t_{AB}(\delta)e^{i\mathbf{k}\cdot\delta} \\
\sum_{\delta} t_{BA}(\delta)e^{i\mathbf{k}\cdot\delta} & \epsilon_B + \sum_{\delta} t_{BB}(\delta)e^{i\mathbf{k}\cdot\delta}
\end{pmatrix}.
\]

- サブ格子（ハニカム等）や多軌道（\(d_{x^2-y^2}\), \(d_{3z^2-r^2}\) …）はこの枠組みで扱える。  
- スピンを含めるなら、各ブロックを \(\uparrow/\downarrow\) で直積化、SOCならスピン-軌道のオフ対角を追加。

## 7. 多軌道（多サイト）強束縛模型をもう一歩

### 7.1 一般式の復習と行列表現
単位胞に \(M\) 軌道（or サブ格子）があるとき、実空間ハミルトニアンは

\[
\hat{H}
= \sum_{\mathbf{R}}\sum_{\alpha=1}^M \epsilon_\alpha
  \hat{c}^\dagger_{\mathbf{R}\alpha}\hat{c}_{\mathbf{R}\alpha}
+ \sum_{\mathbf{R}}\sum_{\boldsymbol{\delta}}\sum_{\alpha,\beta}
  t_{\alpha\beta}(\boldsymbol{\delta})
  \hat{c}^\dagger_{\mathbf{R}\alpha}\hat{c}_{\mathbf{R}+\boldsymbol{\delta},\beta}.
\]

フーリエ変換で

\[
\hat{H}=\sum_{\mathbf{k}} \hat{\boldsymbol{c}}^\dagger_{\mathbf{k}}\,H(\mathbf{k})\,\hat{\boldsymbol{c}}_{\mathbf{k}},
\quad
H_{\alpha\beta}(\mathbf{k})
=\epsilon_\alpha \delta_{\alpha\beta}
 + \sum_{\boldsymbol{\delta}} t_{\alpha\beta}(\boldsymbol{\delta}) e^{i\mathbf{k}\cdot\boldsymbol{\delta}}.
\]

固有値問題 \(H(\mathbf{k})\boldsymbol{u}_n(\mathbf{k})=E_n(\mathbf{k})\boldsymbol{u}_n(\mathbf{k})\) を解けば \(M\) 本のバンド \(E_n(\mathbf{k})\)。

---

### 7.2 2サイト（A/B）・最近接のみの基本形
A/B サブ格子（1サイト/サブ格子、単位胞に2サイト）。A↔B のみ最近接 \(t\) とする：

\[
H(\mathbf{k})=
\begin{pmatrix}
\epsilon_A & \gamma(\mathbf{k}) \\
\gamma^*(\mathbf{k}) & \epsilon_B
\end{pmatrix},\quad
\gamma(\mathbf{k})=\sum_{\delta\in \text{A→B}} t\, e^{i\mathbf{k}\cdot\boldsymbol{\delta}}.
\]

固有値：

\[
E_\pm(\mathbf{k})=\frac{\epsilon_A+\epsilon_B}{2}
\pm \sqrt{\left(\frac{\epsilon_A-\epsilon_B}{2}\right)^2 + |\gamma(\mathbf{k})|^2 }.
\]

- \(\Delta\equiv \epsilon_A-\epsilon_B\) が **質量項**となり、\(\mathbf{k}\) に依らない**ギャップ**を開く。
- \(|\gamma(\mathbf{k})|\) は**分散**を決める“構造因子”。格子で形が変わる。

**例：正方格子（A/Bにチェッカーボード状）**  
A→Bの最近接 \(\boldsymbol{\delta}\in\{\pm(a,0),\pm(0,a)\}\) とすれば

\[
\gamma(\mathbf{k}) = t\left(e^{ik_x a}+e^{-ik_x a}+e^{ik_y a}+e^{-ik_y a}\right)
= 2t\left(\cos k_x a + \cos k_y a\right).
\]

\(\epsilon_A=\epsilon_B\) なら

\[
E_\pm(\mathbf{k}) = \pm\,|\gamma(\mathbf{k})| = \pm\,2|t|\,|\cos k_x a + \cos k_y a|.
\]

（サブ格子対称性があると**バンドが±対称**になり、\(\Delta\neq0\) で開口）

**例：ハニカム（A/B）**  
最近接3本で

\[
\gamma(\mathbf{k})=t\left(1+e^{i\mathbf{k}\cdot\mathbf{a}_1}+e^{i\mathbf{k}\cdot\mathbf{a}_2}\right),
\]

\(K\) 点で \(\gamma=0\) → **ディラック点**。\(\Delta\neq 0\) でギャップ。

---

### 7.3 2軌道（同一サイト内）の場合（軌道混成）
同じサイトに \(\{1,2\}\) 軌道（例：\(d_{x^2-y^2}, d_{3z^2-r^2}\)）。  
オンサイト混成 \(V\) と、各軌道の自己ホッピング \(\varepsilon_{1,2}(\mathbf{k})\) を入れる：

\[
H(\mathbf{k})=
\begin{pmatrix}
\varepsilon_1(\mathbf{k}) & V(\mathbf{k}) \\
V^*(\mathbf{k}) & \varepsilon_2(\mathbf{k})
\end{pmatrix}.
\]

固有値：

\[
E_\pm(\mathbf{k})=\frac{\varepsilon_1+\varepsilon_2}{2}
\pm \sqrt{\left(\frac{\varepsilon_1-\varepsilon_2}{2}\right)^2 + |V(\mathbf{k})|^2 }.
\]

- \(\varepsilon_{1,2}(\mathbf{k})\) はそれぞれ単軌道の式（例：\(2t(\cos k_x a+\cos k_y a)+\dots\)）。  
- \(V(\mathbf{k})\) は対称性で決まる（Slater–Koster表：\(pd\sigma\), \(dd\pi\) など）。

---

### 7.4 次近接やSOCの入れ方メモ
- **同一サブ格子内**の NNN は対角要素に入る：  
  \(H_{AA}\sim 4t'_{AA}\cos k_xa\,\cos k_ya\) など。
- **SOC**（スピンまで含む）ではブロックが \(2M\times2M\) に拡張：  
  \(H\to H\otimes \mathbb{1}_\text{spin} + \lambda\,\mathbf{L}\cdot\mathbf{S}\) の形でオフ対角が増える。



## 7. 参考：最小コード片（\(\varepsilon(\mathbf{k})\)）

```python
import numpy as np

def eps_k(kx, ky, a=1.0, t=-1.0, tp=0.0, tpp=0.0, eps0=0.0):
    return (eps0
            + 2*t*(np.cos(kx*a) + np.cos(ky*a))
            + 4*tp*np.cos(kx*a)*np.cos(ky*a)
            + 2*tpp*(np.cos(2*kx*a) + np.cos(2*ky*a))) 
```
