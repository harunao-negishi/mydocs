# 多軌道（多サイト）強束縛模型のフーリエ変換と対角化
単位胞に複数サイト（サブ格子）/軌道を持つ TB モデルを、実空間から **\(k\)-空間** へ写像し、一般式と具体例（A/B 二サイトの正方格子・ハニカム）で **固有値・固有ベクトル** まで追う。

---

## 1. 一般多軌道 TB のフーリエ変換（単位胞内位置を明示）
**前提**：  

- 単位胞位置ベクトル：\(\mathbf R\)  
- 単位胞内のサブ格子/軌道インデックス：\(\alpha,\beta=1,\dots,M\)(これは単位胞内の別の原子位置でもいいし、同じ原子の異なる軌道でもよい。両者の違いはそのホッピングにのみ現れる)　
- 単位胞内の相対位置（**重要**）：\(\boldsymbol\tau_\alpha\)  
- 生成消滅演算子：\(\hat c^\dagger_{\mathbf R\alpha},\ \hat c_{\mathbf R\alpha}\) は単位胞 \(\mathbf R\) の **\(\alpha\) **に対応。  
- \(\boldsymbol\delta\)：**単位胞間**の相対ベクトル（格子ベクトルの整数和）

### 1.1 実空間ハミルトニアン（最一般形）

\[
\hat H=\sum_{\mathbf R}\sum_{\alpha}\epsilon_\alpha\,\hat c^\dagger_{\mathbf R\alpha}\hat c_{\mathbf R\alpha}
+\sum_{\mathbf R}\sum_{\boldsymbol\delta}\sum_{\alpha,\beta}
t_{\alpha\beta}(\boldsymbol\delta)\,
\hat c^\dagger_{\mathbf R\alpha}\hat c_{\mathbf R+\boldsymbol\delta,\beta}.
\]

- \(t_{\alpha\beta}(\boldsymbol\delta)\)：単位胞 \(\mathbf R\) の \(\alpha\) から、\(\mathbf R+\boldsymbol\delta\) の \(\beta\) へのホッピング。  
  **幾何的距離**は \((\mathbf R+\boldsymbol\tau_\alpha)\to(\mathbf R+\boldsymbol\delta+\boldsymbol\tau_\beta)\)。
- 同じ単位胞内の異なるサイト間のホッピング… \(\boldsymbol\delta=0\) として、\(\alpha, \beta\) の区別で表現する。

### 1.2 フーリエ変換（単位胞内位置を位相に反映）
\[
\hat c_{\mathbf R\alpha}=\frac{1}{\sqrt N}\sum_{\mathbf k}e^{i\mathbf k\cdot(\mathbf R+\boldsymbol\tau_\alpha)}\hat c_{\mathbf k\alpha},
\quad
\hat c^\dagger_{\mathbf R\alpha}=\frac{1}{\sqrt N}\sum_{\mathbf k}e^{-i\mathbf k\cdot(\mathbf R+\boldsymbol\tau_\alpha)}\hat c^\dagger_{\mathbf k\alpha}.
\]
> **ポイント**：単位胞内位置 \(\boldsymbol\tau_\alpha\) の位相を **演算子側** に含めると、最終的な \(H_{\alpha\beta}(\mathbf k)\) は **物理的に不変**（ゲージに依存しない見た目）になりやすい。

この定義を代入・整理する:

### 1) オンサイト項

\[
\sum_{\mathbf R,\alpha}\epsilon_\alpha\,\hat c^\dagger_{\mathbf R\alpha}\hat c_{\mathbf R\alpha}
=\sum_{\mathbf R,\alpha}\epsilon_\alpha
\left(\frac{1}{\sqrt N}\sum_{\mathbf k}e^{-i\mathbf k\cdot(\mathbf R+\boldsymbol\tau_\alpha)}\hat c^\dagger_{\mathbf k\alpha}\right)
\left(\frac{1}{\sqrt N}\sum_{\mathbf k'}e^{i\mathbf k'\cdot(\mathbf R+\boldsymbol\tau_\alpha)}\hat c_{\mathbf k'\alpha}\right).
\]

\[
=\frac{1}{N}\sum_{\alpha}\sum_{\mathbf k,\mathbf k'}
\left[\sum_{\mathbf R}e^{i(\mathbf k'-\mathbf k)\cdot\mathbf R}\right]
e^{i(\mathbf k'-\mathbf k)\cdot\boldsymbol\tau_\alpha}\,
\epsilon_\alpha\,\hat c^\dagger_{\mathbf k\alpha}\hat c_{\mathbf k'\alpha}.
\]

\[
\sum_{\mathbf R}e^{i(\mathbf k'-\mathbf k)\cdot\mathbf R}=N\,\delta_{\mathbf k,\mathbf k'}
\quad\Rightarrow\quad
\sum_{\mathbf R,\alpha}\epsilon_\alpha\,\hat c^\dagger_{\mathbf R\alpha}\hat c_{\mathbf R\alpha}
=\sum_{\mathbf k,\alpha}\epsilon_\alpha\,\hat c^\dagger_{\mathbf k\alpha}\hat c_{\mathbf k\alpha}.
\]

（\(\mathbf k=\mathbf k'\) となるため \(\boldsymbol\tau_\alpha\) に依存する位相因子は消える。）

---

### 2) ホッピング項

\[
\sum_{\mathbf R,\boldsymbol\delta,\alpha,\beta}
t_{\alpha\beta}(\boldsymbol\delta)\,
\hat c^\dagger_{\mathbf R\alpha}\hat c_{\mathbf R+\boldsymbol\delta,\beta}
\]

\[
=\sum_{\mathbf R,\boldsymbol\delta,\alpha,\beta}
t_{\alpha\beta}(\boldsymbol\delta)\,
\left(\frac{1}{\sqrt N}\sum_{\mathbf k}e^{-i\mathbf k\cdot(\mathbf R+\boldsymbol\tau_\alpha)}\hat c^\dagger_{\mathbf k\alpha}\right)
\left(\frac{1}{\sqrt N}\sum_{\mathbf k'}e^{i\mathbf k'\cdot(\mathbf R+\boldsymbol\delta+\boldsymbol\tau_\beta)}\hat c_{\mathbf k'\beta}\right).
\]

\[
=\frac{1}{N}\sum_{\boldsymbol\delta,\alpha,\beta}\sum_{\mathbf k,\mathbf k'}
\left[\sum_{\mathbf R}e^{i(\mathbf k'-\mathbf k)\cdot\mathbf R}\right]
t_{\alpha\beta}(\boldsymbol\delta)\,
e^{i\mathbf k'\cdot(\boldsymbol\delta+\boldsymbol\tau_\beta)}
e^{-i\mathbf k\cdot\boldsymbol\tau_\alpha}\,
\hat c^\dagger_{\mathbf k\alpha}\hat c_{\mathbf k'\beta}.
\]

\[
\sum_{\mathbf R}e^{i(\mathbf k'-\mathbf k)\cdot\mathbf R}=N\,\delta_{\mathbf k,\mathbf k'}
\quad\Rightarrow\quad
\sum_{\mathbf R,\boldsymbol\delta,\alpha,\beta}\cdots
=\sum_{\mathbf k}\sum_{\boldsymbol\delta,\alpha,\beta}
t_{\alpha\beta}(\boldsymbol\delta)\,
e^{i\mathbf k\cdot(\boldsymbol\delta+\boldsymbol\tau_\beta-\boldsymbol\tau_\alpha)}
\hat c^\dagger_{\mathbf k\alpha}\hat c_{\mathbf k\beta}.
\]

---

### 3) まとめ（\(k\)-空間ハミルトニアン）

\[
\hat H=\sum_{\mathbf k}\hat{\boldsymbol c}^\dagger_{\mathbf k}\,H(\mathbf k)\,\hat{\boldsymbol c}_{\mathbf k},
\qquad
\hat{\boldsymbol c}_{\mathbf k}=(\hat c_{\mathbf k1},\dots,\hat c_{\mathbf kM})^\mathsf T.
\]

\[
\boxed{
\ H_{\alpha\beta}(\mathbf k)
=\epsilon_\alpha\,\delta_{\alpha\beta}
+\sum_{\boldsymbol\delta}t_{\alpha\beta}(\boldsymbol\delta)\,
e^{i\mathbf k\cdot(\boldsymbol\delta+\boldsymbol\tau_\beta-\boldsymbol\tau_\alpha)}\ .
}
\]

- **対角成分**：オンサイト＋（同一サブ格子内の）同胞間ホッピングの和  
- **非対角成分**：サブ格子間ホッピングの位相和  
- エルミート性：\(H_{\alpha\beta}(\mathbf k)=H_{\beta\alpha}(\mathbf k)^*\)

> \(\boldsymbol\tau_\alpha\) を 0 と置く（“原点を各サブ格子に置く”流儀）も可能。その場合、上式の \(\boldsymbol\tau\) 差は 0 になり、
> \(H_{\alpha\beta}(\mathbf k)=\epsilon_\alpha\delta_{\alpha\beta}+\sum_{\boldsymbol\delta}t_{\alpha\beta}(\boldsymbol\delta)e^{i\mathbf k\cdot\boldsymbol\delta}\) となる（**ゲージ選択**）。

---

## 2. 二サイト（A/B）モデルの一般対角化（位相込み）
以下では \(M=2\)（A/B）で、代表的に

\[
H(\mathbf k)=
\begin{pmatrix}
\epsilon_A + f_{AA}(\mathbf k) & \gamma(\mathbf k)\\
\gamma^*(\mathbf k) & \epsilon_B + f_{BB}(\mathbf k)
\end{pmatrix},
\quad
\gamma(\mathbf k)=\sum_{\text{A}\to\text{B}} t_{AB}(\boldsymbol\delta)\,
e^{\,i\mathbf k\cdot(\boldsymbol\delta+\boldsymbol\tau_B-\boldsymbol\tau_A)}.
\]

- \(f_{AA}, f_{BB}\)：同一サブ格子内の NNN など（対角補正）。最近接 A↔B のみなら \(f_{AA}=f_{BB}=0\)。

固有値は

\[
\boxed{
E_\pm(\mathbf k)=\frac{\xi_A(\mathbf k)+\xi_B(\mathbf k)}{2}
\pm \sqrt{\left(\frac{\xi_A(\mathbf k)-\xi_B(\mathbf k)}{2}\right)^2+|\gamma(\mathbf k)|^2}\ ,
}
\]

\[
\xi_{A/B}(\mathbf k)\equiv \epsilon_{A/B}+f_{A/B\,A/B}(\mathbf k),\qquad
\Delta(\mathbf k)\equiv \xi_A(\mathbf k)-\xi_B(\mathbf k).
\]

**固有ベクトル**（規格化済、\(\phi_{\mathbf k}\equiv \arg\gamma(\mathbf k)\)）：

\[
\begin{aligned}
|u_+(\mathbf k)\rangle
&=\begin{pmatrix}
\cos\frac{\theta_{\mathbf k}}{2}\\[2pt]
e^{\,i\phi_{\mathbf k}}\sin\frac{\theta_{\mathbf k}}{2}
\end{pmatrix},
\quad
|u_-(\mathbf k)\rangle
=\begin{pmatrix}
-\sin\frac{\theta_{\mathbf k}}{2}\\[2pt]
e^{\,i\phi_{\mathbf k}}\cos\frac{\theta_{\mathbf k}}{2}
\end{pmatrix},\\[6pt]
&\text{with}\quad
\tan\theta_{\mathbf k}=\frac{2|\gamma(\mathbf k)|}{\Delta(\mathbf k)}\ ,\qquad
\theta_{\mathbf k}\in[0,\pi].
\end{aligned}
\]

- 直感：\(\Delta\) が“質量（ギャップ）”、\(|\gamma|\) が“運動量依存の結合”。\(\gamma=0\) でバンド接触、\(\Delta\neq0\) で開口。

---

## 3. 具体例1：正方格子（A/Bチェッカーボード）
**幾何**：  
- ブラベー格子は正方格子（格子定数 \(a\)）、**二サブ格子 A/B** をチェッカーボード状に配置。  
- 近接は **A–B 最近接のみ** とする（\(\boldsymbol\tau_B-\boldsymbol\tau_A\) は格子の中心対称で 0 に取っても OK）。

**最近接 A→B の相対ベクトル**：\(\boldsymbol\delta\in\{(\pm a,0),(0,\pm a)\}\)  
\[
\gamma(\mathbf k)=t\sum_{\boldsymbol\delta}e^{i\mathbf k\cdot\boldsymbol\delta}
=t\left(e^{ik_xa}+e^{-ik_xa}+e^{ik_ya}+e^{-ik_ya}\right)
=2t\left(\cos k_xa+\cos k_ya\right).
\]

**サブ格子ポテンシャル** \(\epsilon_A=+\Delta/2,\ \epsilon_B=-\Delta/2\) とすれば
\[
H(\mathbf k)=
\begin{pmatrix}
\Delta/2 & \gamma(\mathbf k)\\
\gamma(\mathbf k) & -\Delta/2
\end{pmatrix},\qquad
E_\pm(\mathbf k)=\pm\sqrt{(\Delta/2)^2+\gamma(\mathbf k)^2}.
\]
- \(\Delta=0\)：\(\Gamma(\mathbf k=0)\) で分離最大、\((\pi/a,\pi/a)\) で接近。  
- \(\Delta\neq0\)：全域で**ギャップ \(=|\Delta|\)**。  
- NNN（同一サブ格子内）を入れるなら
  \(f_{AA}=f_{BB}=4t'\cos k_xa\cos k_ya+2t''(\cos 2k_xa+\cos 2k_ya)\) を足す。

**固有ベクトル**は上の一般式で \(\phi_{\mathbf k}=\arg\gamma(\mathbf k)\)（ここでは \(\gamma\) 実数なので 0 か \(\pi\)）。

---

## 4. 具体例2：ハニカム格子（グラフェン型 A/B）
**幾何**（代表的取り方）：  
- 最近接距離を \(a\) とする（注意：文献により“格子定数”の定義が異なる）。  
- 単位胞内位置は \(\boldsymbol\tau_A=\mathbf 0\)、\(\boldsymbol\tau_B=\boldsymbol\delta_1\) に取る流儀もあるが、ここでは簡単のため **\(\boldsymbol\tau_B-\boldsymbol\tau_A=0\)** と置くゲージを使う。  
- 最近接ベクトル
\[
\boldsymbol\delta_1=a(0,1),\quad
\boldsymbol\delta_2=a\left(\frac{\sqrt3}{2},-\frac{1}{2}\right),\quad
\boldsymbol\delta_3=a\left(-\frac{\sqrt3}{2},-\frac{1}{2}\right).
\]

**構造因子**：
\[
\gamma(\mathbf k)=t\sum_{j=1}^3 e^{i\mathbf k\cdot\boldsymbol\delta_j}
=t\Big(
e^{ik_y a}
+e^{\,i(\frac{\sqrt3}{2}k_x-\frac{1}{2}k_y)a}
+e^{\,-i(\frac{\sqrt3}{2}k_x+\frac{1}{2}k_y)a}
\Big).
\]

**2×2 ハミルトニアン**（サブ格子ポテンシャル \(\pm \Delta/2\) を任意に許す）：
\[
H(\mathbf k)=\begin{pmatrix}
\Delta/2 & \gamma(\mathbf k)\\
\gamma^*(\mathbf k) & -\Delta/2
\end{pmatrix},
\qquad
E_\pm(\mathbf k)=\pm\sqrt{(\Delta/2)^2+|\gamma(\mathbf k)|^2}.
\]

**ディラック点**：\(\gamma(\mathbf k)=0\) を満たす \(\mathbf k\)（\(\Delta=0\) なら接触）  
代表的に
\[
\mathbf K=\left(\frac{4\pi}{3\sqrt3 a},\,0\right),\qquad
\mathbf K'=-\mathbf K,
\]
で \(\gamma(\mathbf K)=0\)。\(\Delta\neq0\) なら **ギャップ \(|\Delta|\)**。

**低エネルギー展開**（\(\mathbf k=\mathbf K+\mathbf q\)、小 \(|\mathbf q|\)）：
\[
H(\mathbf q)\approx v_F\,(q_x\sigma_x+q_y\sigma_y)+\frac{\Delta}{2}\sigma_z,\qquad
v_F=\frac{\sqrt3}{2}|t|a\ .
\]
- \(\Delta=0\)：質量なしの**ディラック分散**。  
- \(\Delta\neq0\)：質量付き（ギャップ開口）。

**固有ベクトル**は一般式で \(\phi_{\mathbf k}=\arg\gamma(\mathbf k)\)。位相の\(\mathbf k\) 依存が **ベリー位相・擬スピンの巻き付き**に対応。

---

## 5. 実装ミニコード（数値対角化）
### 5.1 正方格子 A/B（二サイト、最近接のみ）
```python
import numpy as np

def H_square_AB(kx, ky, a=1.0, t=1.0, Delta=0.0):
    # gamma = 2 t (cos kx a + cos ky a) ・・・実数
    g = 2.0*t*(np.cos(kx*a) + np.cos(ky*a))
    H = np.array([[+Delta/2.0, g],
                  [g,         -Delta/2.0]], dtype=complex)
    return H

def bands_square(kx, ky, **kw):
    w, _ = np.linalg.eigh(H_square_AB(kx, ky, **kw))
    return np.sort(w)  # [-, +]
