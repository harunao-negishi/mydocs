# 自由系の感受率について

このページでは、前節までに求めた自由系の感受率を、実際にプロットしてみようと思う。

---

## 自由系の感受率の解析計算

非相互作用系（自由電子系）における感受率（時間順序付き）は、グリーン関数を用いて以下のように表されることを、前節で学びました：

$$
\chi_0(\mathbf{q}, i\omega_n) = -\frac{k_BT}{V} \sum_{\mathbf{k}, i\varepsilon_n} G_0(\mathbf{k}, i\varepsilon_n) \, G_0(\mathbf{k} + \mathbf{q}, i\varepsilon_n + i\omega_n)
$$

ここで、

- \( i\varepsilon_n \)：フェルミ・松原周波数（Fermionic Matsubara frequency）

- \( i\omega_n \)：ボース・松原周波数（Bosonic Matsubara frequency）

であった（感受率がボソン松原の和で書けるのは、感受率の周波数に対する周期性が、フェルミ周期性のグリーン関数二つの積で書けることから簡単に導ける）。

自由電子のグリーン関数の具体系
\( G_0(\mathbf{k}, i\varepsilon_n) = \frac{1}{i\varepsilon_n - \varepsilon_{\mathbf{k}} + \mu} \)
を代入すると、上の式は、
$$
\chi_0(\mathbf{q}, i\omega_n) = -\frac{k_BT}{V} \sum_{\mathbf{k}, i\varepsilon_n} 
\frac{1}{i\varepsilon_n - \varepsilon_{\mathbf{k}} + \mu}
\cdot
\frac{1}{i\varepsilon_n + i\omega_n - \varepsilon_{\mathbf{k+q}} + \mu}
$$
ここで、

- \( \varepsilon_{\mathbf{k}} \)：運動量 \( \mathbf{k} \) に対応する電子のエネルギー

- \( \mu \)：化学ポテンシャル

であった。

さらにこれを松原の和を無限時まで取ることが、複素積分を使うと示すことができて、  

$$
\chi_0(\mathbf{q}, i\omega_n) = \sum_{\mathbf{k}} 
\frac{f(\varepsilon_{\mathbf{k}}) - f(\varepsilon_{\mathbf{k+q}})}
{i\omega_n + \varepsilon_{\mathbf{k}} - \varepsilon_{\mathbf{k+q}}}
$$

このようにフェルミ分布関数を含んだ形になる。

実際に感受率を求めるときは、これを解析接続 (\(i\omega_n \rightarrow \hbar\omega + i\delta\))したものを用いる。

また、静的な応答に興味がある（例えば、外場が強くなくても自発的に磁化や電子密度の局在化が出るなど）ので、基本的に\(\omega \rightarrow 0\)である。

---

## 自由グリーン関数の数値解

まずは自由系のグリーン関数式のプロットを見てみよう。そのためには

``` python
chi_sum = 0
for wn in matsubara_freqs:
    for p in range(Nk):
        for q in range(Nk):
            chi_sum += 1 / ((wn - epsilon_k[p, q]) * (wn - epsilon_qk[p, q]))
chi_sum *= (-kb * T) / (Nk**2)
```





## 関連トピック

- [スピン感受率](spin_susceptibility.md)
- [RPAとは？](rpa.md)

