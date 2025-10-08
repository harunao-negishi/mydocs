# グリーン関数と諸性質

この章では、後の有限温度形式やファインマン図法で基礎となる**1粒子グリーン関数**を導入する。  
電子の運動や励起状態に関する情報を含む量であり、状態密度や応答関数など多くの物理量の出発点となる。
とはいえ、実際の計算で使うのは温度グリーン関数だし、そこまで重要ではないから、飛ばしても構わない。

歴史的には、実グリーン関数が有限温度でのwickの定理が使えないということで虚時間のグリーン関数が生まれたため、その道具としての有効性はFDを申し分なく使える虚時間グリーン関数に軍配が上がる。

---

## 1. **定義**

**1粒子グリーン関数**は、時刻 \(t'\) に電子を生成し、時刻 \(t\) に電子を消滅させたときの**伝播の確率振幅**として定義される。

$$
G_{\alpha\beta}(t-t';\mathbf r,\mathbf r') =
-\,i\,\langle\,T\,\psi_{\alpha}(\mathbf r,t)\,
\psi_{\beta}^\dagger(\mathbf r',t')\,\rangle,
$$

ここで  


- \(T\)：時間順序演算子（後の時刻の演算子を左に置く、その時の置換が奇置換なら-1を掛ける）  


- \(\psi_{\alpha}(\mathbf r,t)\)：Heisenberg表示の消滅演算子　[\(
  \psi_{\alpha}(\mathbf r,t) = e^{iHt}\psi_{\alpha}(\mathbf r)e^{-iHt}.
  \)]  


- 平均 \(\langle \mathcal{O} \rangle\)：**基底状態**または平衡状態での期待値　
  $$
   \langle \mathcal{O} \rangle
  = \frac{\mathrm{Tr}\left[e^{-\beta\,(H-\mu N)}\,\mathcal{O}\right]}
         {\mathrm{Tr}\left[e^{-\beta\,(H-\mu N)}\right]}
  \equiv \frac{1}{\mathcal{Z}}\,\mathrm{Tr}\left[e^{-\beta\,(H-\mu N)}\,\mathcal{O}\right],
  \qquad \mathcal{Z}=\mathrm{Tr}\left[e^{-\beta\,(H-\mu N)}\right].
  $$

  トレースは完全系 \(\{\lvert n\rangle\}\) (主には$H_0$の状態を使うことが多い) で、
  $$
  \mathrm{Tr}[\,\cdots\,]
  = \sum_n \langle n \lvert \,\cdots\, \rvert n \rangle.
  $$


---
## 2. **基本性質**

### (1) 等時刻での不連続性（フェルミオン固有の性質）

時間順序積によって、グリーン関数は時間の前後で符号が変わる：

$$
G(t-t')=
\begin{cases}
-i\,\langle \psi(t)\psi^\dagger(t')\rangle, & (t>t')\\[4pt]
+i\,\langle \psi^\dagger(t')\psi(t)\rangle, & (t<t')
\end{cases}
$$

\(t\to t'\) の極限で両者を比較する：

$$
\begin{aligned}
G(0^+) - G(0^-)
&= \lim_{t\to t'^+}(-i)\langle\psi(t)\psi^\dagger(t')\rangle
 - \lim_{t\to t'^-}(+i)\langle\psi^\dagger(t')\psi(t)\rangle \\[4pt]
&= -i\,\langle\{\psi,\psi^\dagger\}\rangle = -\,i\,\delta_{\alpha\beta}\,\delta(\mathbf r-\mathbf r').
\end{aligned}
$$

この時、フェルミ粒子の生成・消滅演算子の反交換関係$\left(\{\psi_{\alpha}(\mathbf r,t),\,\psi_{\beta}^\dagger(\mathbf r',t)\}
= \delta_{\alpha\beta}\,\delta(\mathbf r-\mathbf r')\right)$を用いた。

- グリーン関数は **\(t=t'\)** でジャンプ（不連続）を持つ。  
- このジャンプはフェルミ粒子の**反交換関係**に起因する。  
- つまり「1粒子分の占有」を反映した**粒子統計的構造**を示す。

> 🔸 ボソンの場合（交換関係）は、同様の導出で**不連続性は現れない**。

---

### (2) 複素共役（エルミート共役）関係

フェルミオンのグリーン関数の複素共役は、

$$ G_{\alpha\beta}^*(t-t')= i\,\langle T^\dagger\,\psi_{\alpha}^\dagger(t)\psi_{\beta}(t')\rangle $$

で与えられる。ここで、時間順序演算子のエルミート共役は「**逆時間順序演算子**」\( \tilde{T} \)に対応し、
$$ T^\dagger \psi(t)\psi^\dagger(t') = \tilde{T}\,\psi^\dagger(t)\psi(t') $$

が成り立つ。これを用いると、
$$ G_{\alpha\beta}^*(t-t') = i\,\langle \tilde{T}\,\psi_{\beta}(t')\psi_{\alpha}^\dagger(t)\rangle $$

フェルミ粒子の反交換関係により演算子の順序を入れ替えると符号が反転するため、最終的に
$$ \boxed{G_{\alpha\beta}^*(t-t') = -\,G_{\beta\alpha}(t'-t)}$$

が得られる。

この関係は、グリーン関数が**エルミート共役で時間反転した形を保つ**ことを意味している。  
フェルミ統計により符号が \(-1\) になる点が特徴的であり、この性質は後に導入する**遅延・先進グリーン関数**の対称性$(G^A = [G^R]^*)$ にも直接つながる。

---

### (3) 時間並進対称性（平衡系） 　

時間に依存しないハミルトニアン\(H\)を考える。
グリーン関数の時間発展はハイゼンベルグ表示で与えられていた。
計算の簡単のために$t>t'$を仮定したとき、グリーン関数は 

$$ G_{\alpha\beta}(t, t';\mathbf r,\mathbf r') = -\frac{i}{\mathcal{Z}}\mathrm{Tr} \left[e^{-\beta(H-\mu N)}\psi_{\alpha}(\mathbf r, t)\,\psi_{\beta}^\dagger(\mathbf r', t')\right] $$ 

で与えられる。ハイゼンベルグ表示を代入して、トレースの循環則 
$$ \mathrm{Tr}[AB]=\mathrm{Tr}[BA] $$ 
を用いると、 
$$ G_{\alpha\beta}(t, t';\mathbf r,\mathbf r') = -\frac{i}{\mathcal{Z}} \mathrm{Tr}\left[e^{-\beta(H-\mu N)}e^{iH(t-t')}\psi_{\alpha}(\mathbf r)e^{-iH(t-t')}\psi_{\beta}^\dagger(\mathbf r')\right] $$ 
となり、$t-t'$の形でしか依存しなくなる。 すなわち、**平衡系のグリーン関数は時間差のみに依存する**：
$$ \boxed{G(t,t') = G(t-t')} $$ 
この性質は、後にフーリエ変換で 
$$ G(\omega) = \int_{-\infty}^{\infty} dt\,e^{i\omega t}G(t) $$ 
を定義できる根拠となる。


## 3. 運動方程式（Equation of Motion）

Heisenberg方程式
$$ i\frac{\partial \psi(\mathbf r,t)}{\partial t} = [\psi(\mathbf r,t),H] $$
を用いて、グリーン関数を時間で偏微分してみると、グリーン関数がなぜグリーン関数と呼ばれているのかがわかる：
$$ \left[i\frac{\partial}{\partial t} - h_0(\mathbf r)\right]G(t-t';\mathbf r,\mathbf r')= \delta(t-t')\,\delta(\mathbf r-\mathbf r'), \qquad h_0(\mathbf r) = -\frac{\nabla^2}{2m} + V(\mathbf r) - \mu $$

ここで \(h_0(\mathbf r)\) は単粒子作用素である（今回は相互作用のない系を考えた）。

数学用語でグリーン関数とは変微分方程式の作用素を作用させたときにデルタ関数を返す関数のことだったが、今回は見事にシュレディンガー方程式の作用素を作用させたときにデルタ関数を返す形になっている。

この導出及び相互作用のある系での方程式の導出は演習とする。

---

## 4. フーリエ変換とエネルギー表現

平衡系では時間差のみの関数 \(G(t-t')\) を
フーリエ変換してエネルギー表現を得る。

$$
G(\omega) = \int_{-\infty}^{\infty}
dt\,e^{i\omega t}\,G(t).
$$

このとき
$$
G(t) = \int\frac{d\omega}{2\pi}\,e^{-i\omega t}\,G(\omega).
$$

また、当然のことだが並進対称性がある系では位置の部分も運動量空間にフーリエ変換することができる。
詳しい計算は温度グリーン関数に譲ることとする。

---

## 5. まとめ

- グリーン関数は、電子の生成・消滅過程の時間発展を表す量。  
- 等時刻の不連続、共役関係、時間並進対称性をもつ。  
- 運動方程式を満たし、相互作用なしではシュレディンガー方程式に対応。  
- フーリエ変換により、エネルギー領域での解析が可能になる。

次章では、このエネルギー表現を有限温度（虚時間）形式に拡張する。