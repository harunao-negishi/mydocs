# Windows の環境変数(environment variable)・PATH の仕組みと編集方法まとめ

このドキュメントでは、Windows における「環境変数」「PATH」の仕組みと、
Python のセットアップ時にどのように編集すべきかをまとめる。

特に、

Microsoft Store の Python（WindowsApps の python.exe）

古い Python のシム（bin\python.exe）

正規の Python.org 版 Python

が混在して PATH が壊れる問題について、実際に行った解決手順も含めて整理する。

## 1. 環境変数とは？

Windows では、OS やアプリが参照する値を「環境変数」として保存している。

代表的な項目：

PATH

TEMP, USERPROFILE

PYTHONPATH など

環境変数は 2種類 存在する。

● ① ユーザー環境変数（上段）

そのユーザーだけに適用

優先されやすい
（PATH の先頭に来ることが多い）

● ② システム環境変数（下段）

PC 全体に適用

管理者権限が必要なことも多い

Windows は両方を結合して PATH として扱う。

## 2. PATH（パス）とは？

PATH は「コマンドの検索場所」を定義するリスト。

例：

C:\Users\<user>\AppData\Local\Programs\Python\Python313\
C:\Windows\system32\
C:\Users\<user>\AppData\Local\Python\bin\


PowerShell / コマンドプロンプトで python と打つと、
PATH に記載された順にフォルダを調べて、最初に見つかった python.exe を使う。

➡ PATH に複数の Python があると 競合してカオスになる。

## 3. PATH を確認するコマンド

PowerShell：

where python


→ すべての python.exe の場所を一覧表示。

$env:PATH -split ';'


→ PATH の中身を 1 行ずつ見る。

## 4. PATH を編集する手順
① Windowsキー →「環境変数」で検索

→ 「システム環境変数の編集」 を開く
→ 下部にある 「環境変数(N)…」 をクリック

ここで2種類の PATH が見られる：

上段：ユーザー環境変数 Path

下段：システム環境変数 Path

② 編集したい PATH を選んで「編集」
③ 不要な行を削除 / 必要な行を追加

例：
削除するべき例

C:\Users\<user>\AppData\Local\Python\bin\
C:\Users\<user>\AppData\Local\Microsoft\WindowsApps\


追加するべき例

C:\Users\<user>\AppData\Local\Programs\Python\Python313\

④ OK を押して閉じる
⑤ PowerShell を「閉じて開き直す」

環境変数は新しいシェルでしか反映されない。

## 5. 今回実際に行った作業（Python クリーンアップ）
### ✔ 1. Microsoft Store の python.exe を PATH から排除

WindowsApps 配下にある python.exe はダミーのランチャー。
PATH から削除して正常化した。

例：

C:\Users\harut\AppData\Local\Microsoft\WindowsApps\python.exe


これは消して正解。

### ✔ 2. 古い Python のラッパー (shims) を PATH から削除

例：

C:\Users\harut\AppData\Local\Python\bin\python.exe


これは昔のインストールが作る “仮の python” で、
実体は失われていたため PATH から削除した。

### ✔ 3. 正規の Python 3.13 を公式サイトからインストール

インストール先：

C:\Users\harut\AppData\Local\Programs\Python\Python313\


ここが現在の 正しい Python 本体。

### ✔ 4. venv を作り直して mkdocs を再セットアップ
Remove-Item -Recurse -Force .venv
python -m venv .venv
.\.venv\Scripts\Activate
pip install mkdocs mkdocs-material


これで mkdocs が正常に起動するようになった。

## 6. トラブルシューティング：where python で複数出る場合

ユーザー Path にある

システム Path にある

WindowsApps のエイリアス

古い bin フォルダ

Anaconda などの Python

などが混ざると複数表示される。

対策のポイント

ユーザー Path の Python を優先（Python.org のやつ）

古い bin フォルダは削除

WindowsApps の python.exe は無効化

必要なら py.exe の admin privilege は “入れない”

venv は親 Python が変わったら作り直す

## 7. 最終的に目指す正常状態

以下のようになったら成功：

where python
→ C:\Users\harut\AppData\Local\Programs\Python\Python313\python.exe
（これ1行だけ）


さらに：

python -c "import sys; print(sys.executable)"
→ C:\Users\harut\AppData\Local\Programs\Python\Python313\python.exe


仮想環境では：

C:\Users\harut\Documents\mydocs\.venv\Scripts\python.exe


が出れば正常。

## 8. おすすめ運用ルール

Python を再インストールしたら venv は作り直す

PATH に Python のフォルダは 1つだけ にする

WindowsApps の python は 永久に OFF

設定 → アプリ → アプリ実行エイリアス → Python OFF

VS Code は Python: Select Interpreter で正しい python を選ぶ

## 9. まとめ（今回の作業の全体像）

PATH の仕組みと編集方法を理解した

Microsoft Store の python を完全排除

古い bin シムを削除

Python 3.13 を正規にインストール

PATH を整えて where python を 1 行に統一

mkdocs の .venv を再構築して復旧

Windows の Python 環境が完全に正常化された