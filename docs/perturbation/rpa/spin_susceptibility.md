# スピン感受率の計算メモ

## 定義
外部磁場 $h$ に対する磁化 $M$ の応答：
$$
\chi_s(q,\omega) = \left.\frac{\partial M(q,\omega)}{\partial h(q,\omega)}\right|_{h\to 0}
$$

## 非相互作用系での $\chi_0$
フェルミ気体の場合（有限温度版 Lindhard 関数）：
$$
\chi_0(q,\omega) = \sum_k \frac{f(\epsilon_{k+q}) - f(\epsilon_k)}{
\hbar\omega + \epsilon_k - \epsilon_{k+q} + i0^+}
$$

## RPAによる補正
静的極限で $\chi_{\text{RPA}} = \chi_0 / (1 - U\chi_0)$。$U>0$ の場合、分母が 0 になる条件が強磁性不安定性（Stoner 条件）となる。

## メモ
- 実際の計算では数値積分で $\chi_0$ を評価する。
- 低温かつ 3D の場合、臨界条件は概ね $U N(0) = 1$ （$N(0)$ は状態密度）。
