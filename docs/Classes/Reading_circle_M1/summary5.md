# 第5章 一般ボーズ系（General Bose Systems）
## 5.1 ボーズ凝縮（Bose Condensation）

自然界には多くの種類のボソンが存在し、その中にはフォノンや光子のように粒子数が保存されないものもある。このような場合は化学ポテンシャルが常に

$$
\mu = 0
$$

となる。一方、ヘリウム 4 原子のように粒子数が保存されるボソンもあり、その場合の化学ポテンシャル \(\mu\) は粒子密度 \(n\) を一定に保つ条件で決まる。このような系で起こる現象がボーズ凝縮である。

相互作用のない理想ボーズ気体を考える。1 粒子エネルギーは

$$
\varepsilon_{\mathbf{p}} = \frac{p^{2}}{2m}
$$

で与えられ、粒子数密度は

$$
n = \frac{1}{(2 \pi \hbar)^{3}} \int \frac{d^{3}p}{\exp[(\varepsilon_{\mathbf{p}} - \mu)/T] - 1} \tag{5.1}
$$

となる。高温では \(\mu < 0\) で、温度を下げると \(\mu\) が上昇し、ある臨界温度 \(T_{0}\) で \(\mu = 0\) に達する。\(\mu\) はバンド底よりも小さくなければ分配関数が発散するため、\(\mu \le 0\) が必要条件である。

臨界温度では

$$
n = \frac{1}{(2 \pi \hbar)^{3}} \int \frac{d^{3}p}{\exp(p^{2}/2m T_{0}) - 1} \tag{5.2}
$$

となり、変数変換 \(\varepsilon = p^{2}/2m\) により

$$
n = \frac{(2 m T_{0})^{3/2}}{2 \pi^{2} \hbar^{3}} \int_{0}^{\infty} \frac{\sqrt{\varepsilon}\, d\varepsilon}{\exp(\varepsilon/T_{0}) - 1} \tag{5.3}
$$

が得られる。さらに \(z = \varepsilon/T\) とすると

$$
n = \frac{(2 m T)^{3/2}}{2 \pi^{2} \hbar^{3}} \int_{0}^{\infty} \frac{\sqrt{z}\, dz}{\exp(z - \mu/T) - 1} \tag{5.4}
$$

となる。この種の積分は一般に

$$
\int_{0}^{\infty} \frac{z^{x-1}}{e^{z} - 1}\,dz = \Gamma(x)\,\zeta(x)
$$

と表せるので、\(x = 3/2\) を代入すると

$$
n = \frac{(m T_{0})^{3/2}}{2 \pi^{2} \hbar^{3}} \zeta(3/2) \tag{5.5}
$$

を得る。臨界温度は

$$
T_{0} = \frac{2 \pi \hbar^{2}}{m} \left( \frac{n}{\zeta(3/2)} \right)^{2/3} \tag{5.6}
$$

であり、これが理想ボーズ気体のボーズ＝アインシュタイン凝縮温度である。

温度を \(T_{0}\) より下げると、化学ポテンシャルは \(\mu = 0\) のまま固定される。その結果、励起状態（\(\varepsilon > 0\)）にある粒子数は

$$
n_{\varepsilon>0} = \frac{1}{(2 \pi \hbar)^{3}} \int \frac{d^{3}p}{\exp(p^{2}/2mT) - 1} = n \left(\frac{T}{T_{0}}\right)^{3/2} \tag{5.7}
$$

となる。残り

$$
n_{0} = n \left[1 - \left(\frac{T}{T_{0}}\right)^{3/2}\right] \tag{5.8}
$$

が基底状態 \(\mathbf{p}=0\) に凝縮する粒子数である。つまり、\(T < T_{0}\) では巨視的な占有が基底状態に現れる。

一般の \(d\) 次元系における状態密度は

$$
g_{d}(\varepsilon) \propto \varepsilon^{d/2 - 1} \tag{5.9}
$$

であり、\(d = 3\) の場合は積分が有限で凝縮が起こるが、\(d = 1, 2\) では発散するため有限温度でのボーズ凝縮は生じない。

理想ボーズ気体のエネルギー \(E\)、自由エネルギー \(F\)、エントロピー \(S\)、比熱 \(C_{V}\) は臨界点で連続である。そのためこの転移は二次ではなく三次の相転移（\(dC_{V}/dT\) が不連続）と分類される。例外として、一定圧力下では二次相転移となること、また相互作用を導入すると転移の性質が大きく変化することが挙げられる。

### 補足: 自由ボーズ気体でなぜ \(\mu<0\) か

自由ボーズ気体の分布関数は

$$
n(\varepsilon)=\frac{1}{e^{(\varepsilon-\mu)/k_B T}-1}
$$

で与えられる。分母がゼロに近づくと占有数が発散するため、任意の \(\varepsilon\) について分母の正値性、すなわち

$$
e^{(\varepsilon-\mu)/k_B T}-1>0\qquad\forall\,\varepsilon
$$

が必要である。これには \(\varepsilon-\mu>0\)（すなわち \(\mu<\varepsilon\)）が十分で、自由粒子では最低エネルギーが \(\varepsilon_{\min}=0\) なので必須条件として

$$
\mu<0
$$

が求められる。物理的には、ボース粒子系で \(\mu\) がバンド底（ここでは 0）に近づくと基底状態に粒子が急増し、基底状態の占有が巨視的になる（ボース＝アインシュタイン凝縮）ため、\(\mu\) はそれ以上大きくなれない、という制約が働くことを意味する。

### 補足: なぜ1次元・2次元で BEC が起きないのか（簡潔な導出）

全粒子数は状態密度 \(D(\varepsilon)\) と分布関数で

$$
N=\int_{0}^{\infty} D(\varepsilon)\, n(\varepsilon)\, d\varepsilon
$$

と表される。\(d\) 次元における単純な自由粒子の状態密度は低エネルギーで

$$
D(\varepsilon) \propto \varepsilon^{d/2-1}
$$

と振る舞う。\(\mu\to 0^{-}\) の極限で分布関数は

$$
n(\varepsilon)\approx \frac{k_B T}{\varepsilon}
$$

となるため、\(\varepsilon\to0\) の寄与を調べると

$$
N'\equiv\int_{0}^{\infty} D(\varepsilon)\, n(\varepsilon)\, d\varepsilon \sim \int_{0} \varepsilon^{d/2-1} \frac{k_B T}{\varepsilon} \, d\varepsilon \sim k_B T \int_{0} \varepsilon^{d/2-2} \, d\varepsilon .
$$

この積分が \(\varepsilon\to0\) で収束するための条件は

$$
d/2-2>-1 \quad\Longrightarrow\quad d>2.
$$

したがって、三次元（\(d=3\)）では積分が収束し有限個の粒子を励起状態に収められるため残りが基底に凝縮し得るが、\(d=2\) や \(d=1\) では低エネルギー寄与が発散し、任意に多くの粒子を低エネルギー励起に格納できてしまうため有限温度で巨視的な基底占有（BEC）は生じない。

物理的直感としては、低次元では長波長（低エネルギー）の励起モードの寄与が大きく、熱揺らぎが秩序（単一状態への巨視的占有）を破壊してしまうためである。さらに 2 次元では Mermin–Wagner の議論により長距離の連続対称性の自発的破れが禁止されるため、厳密な意味での BEC は起こらない（ただし有限系・準長距離秩序・BKT などの別の現象は現得る）。
## 5.2 弱く相互作用するボーズ気体

ボソン間に相互作用を導入するとき、密度演算子 \(n(\mathbf{r}) = \psi^{\dagger}(\mathbf{r})\psi(\mathbf{r})\) を用いると

$$
V(\mathbf{r}-\mathbf{r}') n(\mathbf{r}) n(\mathbf{r}') = V(\mathbf{r}-\mathbf{r}') \, \psi^{\dagger}(\mathbf{r})\psi(\mathbf{r})\psi^{\dagger}(\mathbf{r}')\psi(\mathbf{r}') \tag{5.13}
$$

のように書ける。この章ではこの相互作用を弱いものとして扱う。二次量子化の枠組みでは運動量表示を用いるのが便利であり、ハミルトニアンは

$$
H = \sum_{\mathbf{p}} \varepsilon_{\mathbf{p}}\, a_{\mathbf{p}}^{\dagger} a_{\mathbf{p}} + \frac{1}{2} \sum_{\mathbf{p}_1,\mathbf{p}_2,\mathbf{p}_3,\mathbf{p}_4} V_{\mathbf{p}_1-\mathbf{p}_3}\, a_{\mathbf{p}_1}^{\dagger} a_{\mathbf{p}_2}^{\dagger} a_{\mathbf{p}_3} a_{\mathbf{p}_4} \, \delta_{\mathbf{p}_1+\mathbf{p}_2,\mathbf{p}_3+\mathbf{p}_4} \tag{5.14}
$$

（別表記では \(\sum V_{\mathbf{p}\mathbf{q}\mathbf{s}\mathbf{t}} a_{\mathbf{p}}^{\dagger} a_{\mathbf{q}}^{\dagger} a_{\mathbf{s}} a_{\mathbf{t}}\) とも書かれる）となる。ここでは単純化のために相互作用を定数 \(V_{\mathbf{p}} = U / V_{\mathrm{sys}}\) とみなし、散乱は角度依存性のない s 波散乱に支配されるとする。この仮定は接触相互作用に対応する。

ボーズ凝縮状態では運動量 \(\mathbf{p}=0\) の状態に巨視的な占有数 \(N_0\) が存在する。そのため

$$
a_{0} \sim \sqrt{N_0} \gg 1 \tag{5.15}
$$

と見なせ、交換子

$$
[a_{0}, a_{0}^{\dagger}] = a_{0} a_{0}^{\dagger} - a_{0}^{\dagger} a_{0} = 1 \tag{5.16}
$$

は \(a_0\) 自身の大きさに比べて無視できる。したがって凝縮状態では \(a_{0}, a_{0}^{\dagger}\) を大きな \(c\) 数として扱うことができ、一般に

$$
a_{0} = \sqrt{N_0}\, e^{-i\phi}, \qquad a_{0}^{\dagger} = \sqrt{N_0}\, e^{i\phi} \tag{5.17}
$$

と表せる。位相 \(\phi\) は本質的には重要であるが、本節では二乗形式のみを扱うため明示的には追跡しない。

凝縮成分を \(c\) 数として置き換え、励起演算子 \(a_{\mathbf{p}\neq 0}\) に関する 2 次の項まで残すとハミルトニアンは

$$
H \approx \frac{U N_0^2}{2 V_{\mathrm{sys}}} + \sum_{\mathbf{p}\neq 0} \left[(\varepsilon_{\mathbf{p}} + n U) a_{\mathbf{p}}^{\dagger} a_{\mathbf{p}} + \frac{nU}{2} \left(a_{\mathbf{p}}^{\dagger} a_{-\mathbf{p}}^{\dagger} + a_{\mathbf{p}} a_{-\mathbf{p}}\right) \right] \tag{5.18}
$$

となる（ここで \(n = N / V_{\mathrm{sys}}\)）。弱い相互作用では \(N_0 \approx N\) が成り立ち、\(a_{\mathbf{p}}\) に比例する項を小さな摂動として扱う。数演算子 \(\hat{N} = \sum_{\mathbf{p}} a_{\mathbf{p}}^{\dagger} a_{\mathbf{p}}\) の期待値は

$$
\langle \hat{N} \rangle = N_0 + \sum_{\mathbf{p} \neq 0} \langle a_{\mathbf{p}}^{\dagger} a_{\mathbf{p}} \rangle \tag{5.19}
$$

であり、この和の第 2 項は \(N_0\) に比べて小さい（式 (5.20)）。そのため、式 (5.18) の 2 次項を保持しつつ、\(N_0\) には \(N\) を代入できる。

上式を整理すると

$$
H = \frac{U N^{2}}{2 V_{\mathrm{sys}}} + \sum_{\mathbf{p} \neq 0} (\varepsilon_{\mathbf{p}} + n U) a_{\mathbf{p}}^{\dagger} a_{\mathbf{p}} + \frac{nU}{2} \sum_{\mathbf{p} \neq 0} \left(a_{\mathbf{p}}^{\dagger} a_{-\mathbf{p}}^{\dagger} + a_{\mathbf{p}} a_{-\mathbf{p}}\right) \tag{5.22}
$$

が得られる。このハミルトニアンは対生成項を含む非対角形なので、ボゴリューボフの正準変換（\(u\!-
ボソン間の弱相互作用を導入すると、凝縮の上に「集合モード」としての励起が現れ、系の物性（音速、超流動性、基底エネルギーの修正など）が変わる。ここでは元の式や導出は残しつつ、話の流れを平易に整理する。

まず、二体相互作用は位置空間で密度演算子を用いて

$$
V(\mathbf{r}-\mathbf{r}')\, n(\mathbf{r}) n(\mathbf{r}') = V(\mathbf{r}-\mathbf{r}')\, \psi^{\dagger}(\mathbf{r})\psi(\mathbf{r})\psi^{\dagger}(\mathbf{r}')\psi(\mathbf{r}') \tag{5.13}
$$

と書ける。運動量表示に移すとハミルトニアンは

$$
H = \sum_{\mathbf{p}} \varepsilon_{\mathbf{p}}\, a_{\mathbf{p}}^{\dagger} a_{\mathbf{p}} + \frac{1}{2} \sum_{\mathbf{p}_1,\mathbf{p}_2,\mathbf{p}_3,\mathbf{p}_4} V_{\mathbf{p}_1-\mathbf{p}_3}\, a_{\mathbf{p}_1}^{\dagger} a_{\mathbf{p}_2}^{\dagger} a_{\mathbf{p}_3} a_{\mathbf{p}_4}\, \delta_{\mathbf{p}_1+\mathbf{p}_2,\mathbf{p}_3+\mathbf{p}_4} \tag{5.14}
$$

で表される。ここで簡単化のために接触相互作用（s波散乱）を仮定し、ポテンシャルの運動量表現を定数とおくと

$$
V_{\mathbf{p}} = \frac{U}{V_{\mathrm{sys}}}, \qquad U = \frac{4\pi\hbar^{2} a}{m} \tag{5.32}
$$

（\(a\) は散乱長）という近似が使える。

次にボーズ凝縮の特徴を利用する。凝縮成分は \(\mathbf{p}=0\) に巨視的に占有され、生成消滅演算子は大きな c 数と見なせる：

$$
a_{0} \approx \sqrt{N_0}\, e^{-i\phi}, \qquad N_0 \sim O(N). \tag{5.17}
$$

この置き換えの下でハミルトニアンを励起演算子 \(a_{\mathbf{p}\neq0}\) について 2 次まで展開すると、非対角（対生成・対消滅）項を含む二次形式が得られる：

$$
H \approx \frac{U N^{2}}{2 V_{\mathrm{sys}}} + \sum_{\mathbf{p}\neq 0} \left[(\varepsilon_{\mathbf{p}} + n U) a_{\mathbf{p}}^{\dagger} a_{\mathbf{p}} + \frac{nU}{2} \left(a_{\mathbf{p}}^{\dagger} a_{-\mathbf{p}}^{\dagger} + a_{\mathbf{p}} a_{-\mathbf{p}}\right)\right]. \tag{5.22}
$$

非対角項を含むと直接のエネルギー固有状態が見えにくいので、ボゴリューボフの正準変換を導入して準粒子の自然な記述に移る。変換は

$$
a_{\mathbf{p}} = u_{\mathbf{p}} b_{\mathbf{p}} + v_{\mathbf{p}} b_{-\mathbf{p}}^{\dagger}, \qquad a_{\mathbf{p}}^{\dagger} = u_{\mathbf{p}} b_{\mathbf{p}}^{\dagger} + v_{\mathbf{p}} b_{-\mathbf{p}} \tag{5.23}
$$

という形で、ボース交換関係を保つために

$$
u_{\mathbf{p}}^{2} - v_{\mathbf{p}}^{2} = 1 \tag{5.25}
$$

が必要である。

非対角成分を消す条件から係数を決めると、ハミルトニアンは対角化されて準粒子（ボゴリューボフ粒子）で表される：

$$
H = E_{0} + \sum_{\mathbf{p} \neq 0} E_{\mathbf{p}}\, b_{\mathbf{p}}^{\dagger} b_{\mathbf{p}}, \qquad E_{\mathbf{p}} = \sqrt{\varepsilon_{\mathbf{p}}(\varepsilon_{\mathbf{p}} + 2 n U)}. \tag{5.30,5.31}
$$

この式が物理的に重要なのは、\(E_{\mathbf{p}}\)（励起のエネルギー分散）が運動量に応じて 2 つの極限に分かれる点である：

- 小さな運動量（長波長）で

	$$E_{\mathbf{p}} \approx c\, p, \qquad c = \sqrt{\frac{n U}{m}},$$

	すなわち線形分散（音波的励起）。

- 大きな運動量で

	$$E_{\mathbf{p}} \approx \varepsilon_{\mathbf{p}} + nU \sim \frac{p^{2}}{2m},$$

	すなわち自由粒子に近い放物線的分散。

この「音波から粒子的励起への連続的な移行」が Bogolyubov スペクトルの本質で、超流動性や臨界速度（Landauの基準）と直結する。

さらに基底エネルギー密度や量子補正（Lee–Huang–Yang 補正）は

$$
\frac{E_{0}}{V_{\mathrm{sys}}} = \frac{2\pi\hbar^{2} a n^{2}}{m} \left[1 + \frac{128}{15\sqrt{\pi}}(n a^{3})^{1/2} + \cdots\right] \tag{5.33}
$$

のように与えられ、弱結合条件は \(n a^{3} \ll 1\) である。

Q&A（補足的な問いと答え）

Q: ここでいう「エネルギー分散」とは具体的に何を意味しますか？

A: 分散 \(E(\mathbf{p})\) は「運動量 \(\mathbf{p}\) をもつ単一の励起（準粒子）を系の基底の上に一つ作るのに要るエネルギー」を表します。言い換えれば、凝縮を基準にしてその上に小さなゆらぎ（位相や密度の揺らぎ）を1個作るときのエネルギーコストです。低運動量ではそのゆらぎは集合的（音波）で、エネルギーは線形に増える（\(E\propto p\)）。高運動量では個々の粒子に近い振る舞いとなり、放物線的（\(E\propto p^{2}\)）になります。

Q: 「巨視的に \(p=0\) に入っていた粒子が直接動いてエネルギーを取り出す」という意味ですか？

A: いいえ。凝縮に入っている粒子全体を直接“動かす”話（系全体に位相勾配を与えて超流動流れを作る）とは別です。分散 \(E(p)\) はあくまで「凝縮上の小さな励起一つ」を作るコストであり、その励起が長波長なら音波、短波長なら粒子的励起として観測されます。凝縮全体を動かすマクロな運動は位相勾配（\(\mathbf{v}_s \propto \nabla\phi\)）で表されます。

Q: どうやって実験で確認するのですか？

A: 冷却原子 BEC ではブラッグ分光や励起の時間発展、動的構造因子の測定で \(E(p)\) を直接測定できます。低 \(p\) での線形分散と高 \(p\) での放物線的挙動への移行が確認されています。

このように、5.2 節の計算は「凝縮があるときの励起の性質」を明確にし、超流動や音速といった現象の基礎を与える。

補足ミニまとめ（小 p / 大 p での準粒子の姿）

- 小 p（長波長）:
	- 分散は E_p ≈ c p（線形）。
	- 準粒子の正体は密度・位相の集合モード＝音波（フォノン）。
	- 係数は u_p ≈ v_p（5.29 の極限）。b_p^† は「粒子を足す／引く」が混ざった波的励起。
	- 物理的帰結: ランドウの臨界速度 v_c = min_p E_p/p = c。

- 大 p（短波長）:
	- 分散は E_p ≈ ε_p + nU ≈ p^2/2m（自由粒子的）。
	- 係数は v_p ≪ u_p。b_p^† ≈ a_p^† で、ほぼ 1 粒子励起。

要するに: 「p が小さいと準粒子＝音の量子（集団励起）、p が大きいと準粒子＝ほぼ単一粒子の励起」。この間は図 5.2 のように滑らかに遷移する。

---
**Problem:** この状況を通常の結晶のフォノンと比較せよ。
