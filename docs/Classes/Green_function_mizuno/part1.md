# 第1章 定義やらなんやら

## 1.1 ハミルトニアン

### 1.1.1 定義

多体ハミルトニアンを以下の形で定める：

$$
H=\underbrace{\sum_{rr',\,\alpha\beta} t_{rr',\alpha\beta}\,c^{\dagger}_{r\alpha}c_{r'\beta}}_{H_0}
 +
\underbrace{\frac{1}{4}\sum_{r}\sum_{\alpha\beta\gamma\lambda}
U_{\alpha\beta\gamma\lambda}\,c^{\dagger}_{r\alpha}c^{\dagger}_{r\lambda}c_{r\gamma}c_{r\beta}}_{H_{\mathrm{int}}}
$$

(1.1)

波数空間では

$$
H=\underbrace{\sum_{k,\,\alpha\beta}\varepsilon_{k,\alpha\beta}\,c^{\dagger}_{k\alpha}c_{k\beta}}_{H_0}
 +
\underbrace{\frac{1}{4}\sum_{k' q}\sum_{\alpha\beta\gamma\lambda}
U_{\alpha\beta\gamma\lambda}\,c^{\dagger}_{k\alpha}c^{\dagger}_{k'+q,\lambda}c_{k'\gamma}c_{k+q,\beta}}_{H_{\mathrm{int}}}
$$

(1.2)

と書ける。ここで、$r$ はユニットセル位置、ギリシャ文字添え字 $\alpha,\beta,\dots$ はスピン・軌道・副格子などの**内部自由度**を表す。
$c$ と $c^\dagger$ はそれぞれ消滅・生成演算子、$U_{\alpha\beta\gamma\lambda}$ は**オンサイト・クーロン相互作用**、
$t_{rr',\alpha\beta}$ は**ホッピング積分**であり、そのフーリエ変換が $\varepsilon_{k,\alpha\beta}$ である（空間の並進対称性を仮定）。

> **用語メモ**
>
> - $H_0$：一次（1体）項（ホッピング）  
> - $H_{\mathrm{int}}$：二次（2体）項（相互作用）
>

> **補足（並進対称性がない場合）**
> 並進対称性がないときは一次項が $k-k'$ 非対角になり、
> $$
> H=\underbrace{\sum_{k k',\,\alpha\beta}\varepsilon_{k k',\alpha\beta}\,c^{\dagger}_{k\alpha}c_{k'\beta}}_{H_0}
> +
> \underbrace{\frac{1}{4}\sum_{k_1k_2k_3k_4}\sum_{\alpha\beta\gamma\lambda}
> U_{\alpha\beta\gamma\lambda}\,c^{\dagger}_{k_1\alpha}c^{\dagger}_{k_4\lambda}c_{k_3\gamma}c_{k_2\beta}}_{H_{\mathrm{int}}}
> $$
>
> (1.3)


### 1.1.2 crossing symmetry

(1.1) の相互作用項で $\beta \leftrightarrow \gamma$ を入れ替えると、生成演算子の反交換関係により

$$
H_{\mathrm{int}}=\frac{1}{4}\sum_{r}\sum_{\alpha\beta\gamma\lambda}
U_{\alpha\gamma\beta\lambda}\,c^{\dagger}_{r\alpha}c^{\dagger}_{r\lambda}c_{r\beta}c_{r\gamma}
= -\frac{1}{4}\sum_{r}\sum_{\alpha\beta\gamma\lambda}
U_{\alpha\gamma\beta\lambda}\,c^{\dagger}_{r\alpha}c^{\dagger}_{r\lambda}c_{r\gamma}c_{r\beta}
$$

(1.4)

となる。よって

$$
U_{\alpha\beta\gamma\lambda}=-\,U_{\alpha\gamma\beta\lambda}
$$

(1.5)

すなわち **生成側同士**あるいは**消滅側同士**の添え字を入れ替えると符号が反転する。これを *crossing symmetry* と呼ぶ。


## 1.2 実時間グリーン関数

### 1.2.1 定義

**遅延（Retarded）**, **先進（Advanced）**, **因果（Causal）** の 3 種を以下で定義する（$\hbar=1$）。

$$
G^{R}_{\alpha\beta}(r,r',t,t')=-\,i\,\theta(t-t')\,
\Big\langle \, [\,c_{r\alpha}(t),\,c^{\dagger}_{r'\beta}(t')\,]_+ \,\Big\rangle
$$

(1.6)

$$
G^{A}_{\alpha\beta}(r,r',t,t')=+\,i\,\theta(t'-t)\,
\Big\langle \, [\,c_{r\alpha}(t),\,c^{\dagger}_{r'\beta}(t')\,]_+ \,\Big\rangle
$$

(1.7)

$$
G^{C}_{\alpha\beta}(r,r',t,t')=-\,i\,\Big\langle T_t\,c_{r\alpha}(t)\,c^{\dagger}_{r'\beta}(t') \Big\rangle
=G^{R}_{\alpha\beta}+G^{A}_{\alpha\beta}
$$

(1.8)

ここで階段関数 $\theta(t)$ は
$$
\theta(t)=
\begin{cases}
1 &(t>0)\\
0 &(t<0)
\end{cases}
$$

(1.9)
$T_t$ は**時間順序演算子**（交換ごとにフェルミオンでマイナス、ボソンでプラス）。
ハイゼンベルグ表示は
$$
A(t)=e^{iHt}A e^{-iHt},\qquad
\langle A\rangle=\dfrac{\mathrm{Tr}(e^{-\beta H}A)}{\mathrm{Tr}(e^{-\beta H})}
$$

(1.10–1.11)

> **直観**
>
> - $G^R$ は *過去 $\to$ 未来* の応答、$G^A$ は *未来 $\leftarrow$ 過去* の相関を記述。
> - 実験的応答に最も対応が良いのは $G^R$。数学的取扱いでは $G^A$・$G^C$ も用いる。
>


### 1.2.2 運動方程式

$t-t'$ みの依存になるので $t\to t-t'$ と書き換えると

$$
G^{R}_{\alpha\beta}(r,r',t)=-\,i\,\theta(t)\,
\Big\langle \,[\,c_{r\alpha}(t),\,c^{\dagger}_{r'\beta}\,]_+ \,\Big\rangle
$$

(1.12)

消滅演算子の時間微分は

$$
i\frac{\partial}{\partial t}c_{r\alpha}(t)=[c_{r\alpha}(t),H]
= \sum_{r''\gamma}(t_{rr'',\alpha\gamma}-\mu\,\delta_{rr''}\delta_{\alpha\gamma})\,c_{r''\gamma}(t)+ e^{iHt}[c_{r\alpha},H_{\mathrm{int}}]e^{-iHt}
$$

(1.13)

これからグリーン関数の運動方程式：

$$
\begin{aligned}
i\frac{\partial}{\partial t}G^{R}_{\alpha\beta}(r,r',t)
&=\sum_{r''\gamma}(t_{rr'',\alpha\gamma}-\mu\,\delta_{rr''}\delta_{\alpha\gamma})
\,G^{R}_{\gamma\beta}(r'',r',t)\\
&\quad -\,i\Big\langle T_t\,e^{iHt}[c_{r\alpha},H_{\mathrm{int}}]e^{-iHt}\,c^{\dagger}_{r'\beta}\Big\rangle + \delta_{rr'}\delta_{\alpha\beta}\delta(t).
\end{aligned}
$$

(1.14)

ここで（天下り的に）自己エネルギー $\Sigma$ を導入：

$$
-\,i\Big\langle T_t\,e^{iHt}[c_{r\alpha},H_{\mathrm{int}}]e^{-iHt}\,c^{\dagger}_{r'\beta}\Big\rangle\\
=\sum_{r''\gamma}\int dt' \Sigma^{R}_{\alpha\gamma}(r,r'',t-t')\,G^{R}_{\gamma\beta}(r'',r',t')
$$

(1.15)

すると

$$
\sum_{r''\gamma}\int dt'\,
\Big[\big(i\partial_t+\mu\big)\delta_{rr''}\delta(t-t')\delta_{\alpha\gamma} - t_{rr'',\alpha\gamma}\delta(t-t')-\Sigma^{R}_{\alpha\gamma}(r,r'',t-t')\Big]
G^{R}_{\gamma\beta}(r'',r',t')\\
=\delta_{\alpha\beta}\delta_{rr'}\delta(t).
$$

(1.16)

フーリエ変換
$$
G^{R}_{\alpha\beta}(r,r',t)=\int d\omega\,G^{R}_{\alpha\beta}(r,r',\omega)\,e^{-i\omega t}
$$

(1.17)
より

$$
\sum_{\gamma}\Big[(\omega+\mu)\delta_{\alpha\gamma}-\varepsilon_{k,\alpha\gamma}-\Sigma^{R}_{\alpha\gamma}(k,\omega)\Big]
G^{R}_{\gamma\beta}(k,\omega)=\delta_{\alpha\beta},
$$

(1.19)

すなわち行列表記で

$$
\big[(\omega+\mu)\,I-\varepsilon_k-\Sigma^{R}(k,\omega)\big] G^{R}(k,\omega)=I\\
\quad\Rightarrow\quad
G^{R}(k,\omega)=\big[(\omega+\mu)\,I-\varepsilon_k-\Sigma^{R}(k,\omega)\big]^{-1}.
$$

(1.20)

相互作用なし ($U=0$) では

$$
G^{R}(k,\omega)=\big[(\omega+i\delta+\mu)I-\varepsilon_k\big]^{-1}.
$$

(1.21)

同様に

$$
G^{A}(k,\omega)=
\begin{cases}
\big[(\omega-i\delta+\mu)I-\varepsilon_k\big]^{-1} &(U=0)\\[4pt]
\big[(\omega+\mu)I-\varepsilon_k-\Sigma^{A}(k,\omega)\big]^{-1} &(U\neq 0)
\end{cases}
$$

(1.22)


### 1.2.3 スペクトル表示

固有方程式 $H|n\rangle=E_n|n\rangle$ を用いて

$$
\begin{aligned}
G^{R}_{\alpha\beta}(r,r',t)
&=-\,i\,\theta(t)\sum_{mn}\frac{e^{-\beta E_m}+e^{-\beta E_n}}{e^{-\beta\Omega}}
\langle m|c_{r\alpha}|n\rangle\langle n|c^{\dagger}_{r'\beta}|m\rangle\,e^{i(E_m-E_n)t},
\end{aligned}
$$

(1.23)

（並進対称性を仮定して）フーリエ変換すると

$$
G^{R}_{\alpha\beta}(k,\omega)
=\sum_{mn}\frac{e^{-\beta E_m}+e^{-\beta E_n}}{e^{-\beta\Omega}}
\frac{\langle m|c_{k\alpha}|n\rangle\langle n|c^{\dagger}_{k\beta}|m\rangle}
{\omega+i\delta-(E_n-E_m)}.
$$

(1.26)

同様に先進グリーン関数は

$$
G^{A}_{\alpha\beta}(k,\omega)
=\sum_{mn}\frac{e^{-\beta E_m}+e^{-\beta E_n}}{e^{-\beta\Omega}}
\frac{\langle m|c_{k\alpha}|n\rangle\langle n|c^{\dagger}_{k\beta}|m\rangle}
{\omega-i\delta-(E_n-E_m)}.
$$

(1.27)

ここで**スペクトル関数**

$$
A_{\alpha\beta}(k,\omega)=\sum_{mn}\frac{e^{-\beta E_m}+e^{-\beta E_n}}{e^{-\beta\Omega}}
\langle m|c_{k\alpha}|n\rangle\langle n|c^{\dagger}_{k\beta}|m\rangle\,
\delta\big(\omega-(E_n-E_m)\big)
$$

(1.28)

を導入すると

$$
G^{R}_{\alpha\beta}(k,\omega)=\int d\omega'\frac{A_{\alpha\beta}(k,\omega')}{\omega+i\delta-\omega'},
\quad
G^{A}_{\alpha\beta}(k,\omega)=\int d\omega'\frac{A_{\alpha\beta}(k,\omega')}{\omega-i\delta-\omega'}.
$$

(1.29–1.30)

さらに $1/(x\pm i\delta)=\mathcal{P}(1/x)\mp i\pi\delta(x)$ より

$$
G^{R}_{\alpha\beta}(k,\omega)=\mathcal{P}\int d\omega'\frac{A_{\alpha\beta}(k,\omega')}{\omega-\omega'} - i\pi A_{\alpha\beta}(k,\omega),
\quad
G^{A}_{\alpha\beta}(k,\omega)=\mathcal{P}\int d\omega'\frac{A_{\alpha\beta}(k,\omega')}{\omega-\omega'} + i\pi A_{\alpha\beta}(k,\omega),
$$

(1.31–1.32)

よって

$$
A_{\alpha\beta}(k,\omega)=\frac{1}{2\pi}\Big(G^{A}_{\alpha\beta}-G^{R}_{\alpha\beta}\Big),
\qquad
A_{\alpha\alpha}(k,\omega)=-\frac{1}{\pi}\,\mathrm{Im}\,G^{R}_{\alpha\alpha}(k,\omega).
$$

(1.33)

特に軌道対角成分では

$$
A_{\alpha\alpha}(k,\omega)=
\begin{cases}
\delta(\omega+\mu-\varepsilon_{\alpha\alpha}(k)) &(U=0)\\[4pt]
\dfrac{-\,\mathrm{Im}\,\Sigma^{R}(k,\omega)/\pi}
{\{\omega+\mu-\varepsilon_{\alpha\alpha}(k)-\mathrm{Re}\,\Sigma^{R}(k,\omega)\}^2+ \{\mathrm{Im}\,\Sigma^{R}(k,\omega)\}^2}
&(U\neq 0)
\end{cases}
$$

(1.34)

> **ワンポイント**
>
> - $\delta>0$ は $t\to\infty$ で相関が消える仮定を表す微小量。スペクトル表示の収束を保証。
>


## 1.3 虚時間グリーン関数

### 1.3.1 定義

虚時間（松原）グリーン関数：

$$
G_{\alpha\beta}(r,r',\tau,\tau')=-\Big\langle T_{\tau}\,c_{r\alpha}(\tau)\,c^{\dagger}_{r'\beta}(\tau')\Big\rangle,
$$

(1.35)

ここで $T_{\tau}$ は $\tau$ の大きい演算子を左へ並べ、フェルミオンで $-1$、ボソンで $+1$ の符号を与える演算子。
$\tau,\tau'\in[0,\beta]$、虚時間ハイゼンベルグ表示は

$$
A(\tau)=e^{\tau H}Ae^{-\tau H},\qquad
\langle A\rangle=\frac{\mathrm{Tr}(e^{-\beta H}A)}{\mathrm{Tr}(e^{-\beta H})}.
$$

(1.36–1.37)

trace の cyclic 則と $[H,H]=0$ から $\tau-\tau'$ のみの関数として

$$
G_{\alpha\beta}(r,r',\tau)=-\big\langle T_{\tau}\,c_{r\alpha}(\tau)\,c^{\dagger}_{r'\beta}\big\rangle.
$$

(1.38)

アンチ周期性より

$$
G_{\alpha\beta}(r,r',\tau+\beta)=-\,G_{\alpha\beta}(r,r',\tau),
\qquad
G_{\alpha\beta}(r,r',\tau+2\beta)=G_{\alpha\beta}(r,r',\tau).
$$

(1.39–1.40)

よってフーリエ級数展開は**奇数**モードのみが残り、フーリエ変換は

$$
G_{\alpha\beta}(r,r',i\omega_n)=\int_0^{\beta} d\tau\,G_{\alpha\beta}(r,r',\tau)\,e^{i\omega_n\tau},
\quad
\omega_n=\frac{(2n+1)\pi}{\beta}\ (n\in\mathbb{Z}).
$$

(1.41–1.45, 1.44)

（ボソンは $\nu_n=2n\pi/\beta$ の偶数モード）


### 1.3.2 運動方程式

消滅演算子の微分：

$$
\frac{\partial}{\partial\tau}c_{r\alpha}(\tau)=-[c_{r\alpha}(\tau),H]
=-\sum_{r''\gamma}(t_{rr'',\alpha\gamma}-\mu\,\delta_{rr''}\delta_{\alpha\gamma})\,c_{r''\gamma}(\tau) - e^{\tau H}[c_{r\alpha},H_{\mathrm{int}}]e^{-\tau H}
$$

(1.46)

より

$$
\begin{aligned}
\frac{\partial}{\partial\tau}G_{\alpha\beta}(r,r',\tau)
&=-\sum_{r''\gamma}(t_{rr'',\alpha\gamma}-\mu\,\delta_{rr''}\delta_{\alpha\gamma})\,G_{\gamma\beta}(r'',r',\tau)\\
&\quad -\Big\langle T_{\tau}\,e^{\tau H}[c_{r\alpha},H_{\mathrm{int}}]e^{-\tau H}\,c^{\dagger}_{r'\beta}\Big\rangle - \delta_{\alpha\beta}\delta_{rr'}\delta(\tau).
\end{aligned}
$$

(1.47)

自己エネルギー $\Sigma$ を導入：

$$
-\Big\langle T_{\tau}\,e^{\tau H}[c_{r\alpha},H_{\mathrm{int}}]e^{-\tau H}\,c^{\dagger}_{r'\beta}\Big\rangle
=\sum_{r''\gamma}\int d\tau'\,\Sigma_{\alpha\gamma}(r,r'',\tau-\tau')\,G_{\gamma\beta}(r'',r',\tau')
$$

(1.49)

とすると

$$
\sum_{r''\gamma}\int d\tau'\,
\Big[\big(-\partial_\tau+\mu\big)\delta_{rr''}\delta(\tau-\tau')\delta_{\alpha\gamma} - t_{rr'',\alpha\gamma}\delta(\tau-\tau')-\Sigma_{\alpha\gamma}(r,r'',\tau-\tau')\Big]
G_{\gamma\beta}(r'',r',\tau')\\
=\delta_{\alpha\beta}\delta_{rr'}\delta(\tau).
$$

(1.50)

フーリエ変換 $G(\tau)=T\sum_n G(i\omega_n)e^{-i\omega_n\tau}$ を用いれば

$$
\sum_{\gamma}\Big[(i\omega_n+\mu)\delta_{\alpha\gamma}-\varepsilon_{k,\alpha\gamma}-\Sigma_{\alpha\gamma}(k,i\omega_n)\Big]
G_{\gamma\beta}(k,i\omega_n)=\delta_{\alpha\beta},
$$

(1.53)

すなわち

$$
\big[(i\omega_n+\mu)I-\varepsilon_k-\Sigma(k,i\omega_n)\big]\\,G(k,i\omega_n)=I
\quad\Rightarrow\quad
G(k,i\omega_n)=\big[(i\omega_n+\mu)I-\varepsilon_k-\Sigma(k,i\omega_n)\big]^{-1}.
$$

(1.54)
> **補足式（段差表現）**
> $T_{\tau}$ の定義を避けて階段関数で書くと
> $$
> G_{\alpha\beta}(r,r',\tau,\tau')=-\theta(\tau-\tau')\langle c_{r\alpha}(\tau)c^{\dagger}_{r'\beta}(\tau')\rangle
> +\theta(\tau'-\tau)\langle c^{\dagger}_{r'\beta}(\tau')c_{r\alpha}(\tau)\rangle,
> $$
>
> (1.48)
>
> これを微分すれば (1.47) を再現できる。


### 1.3.3 実時間グリーン関数との関係

虚時間でもスペクトル表示が成り立つ：

$$
G_{\alpha\beta}(k,i\omega_n)=\int d\omega\,\frac{A_{\alpha\beta}(k,\omega)}{i\omega_n-\omega}.
$$

(1.55)

よって解析接続 $i\omega_n\to \omega\pm i\delta$ により
$$
G^{R}(k,\omega)=G(k,i\omega_n\to\omega+i\delta),\quad
G^{A}(k,\omega)=G(k,i\omega_n\to\omega-i\delta).
$$

> **実務メモ（数値計算）**
>
> - 松原形式（離散周波数）は計算に向くが、実周波数情報を得るには**数値的解析接続**が必要。
> - 最大エントロピー法など複数手法があるが精度・安定性に一長一短。松原上で読める情報を極力活用するのが吉。
>


