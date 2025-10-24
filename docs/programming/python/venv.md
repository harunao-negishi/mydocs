# 仮想環境（venv）について — Windows / PowerShell 向けハンドブック

このページは、プロジェクト単位の Python 仮想環境（`venv`）を使う理由と基本操作、
「どの python / pip / mkdocs が使われているか」を確実に確認する方法をまとめた短い実用ガイドです。

目的：
- 仮想環境とグローバル環境の違いを理解する。

---

## 安全・推奨手順（既存の venv をプロジェクト直下に移したいとき）

既にホーム直下など別の場所に仮想環境（例: `C:\Users\harut\.venv`）があって、それをプロジェクト（`mydocs`）の直下に置きたい場合、単純にフォルダを移動するより「新しい venv を作ってパッケージを再インストール」する方法が安全で確実です。

以下は手順（短くコピペで実行できる順序）。ここでは既存の仮想環境からパッケージ一覧を出力済み（`requirements_from_old_venv.txt`）と仮定します。まだ出していなければ、古い venv をアクティベートして `pip freeze > requirements_from_old_venv.txt` を実行してください。

1. 古い仮想環境でパッケージ一覧を保存（まだのとき）

```powershell
# 古い venv を有効化してから
& "C:\Users\harut\.venv\Scripts\Activate.ps1"
pip freeze > C:\Users\harut\Documents\mydocs\requirements_from_old_venv.txt
deactivate
```

2. 古い venv を念のためバックアップ（任意）

```powershell
- 仮想環境に入る／抜ける方法（PowerShell）を覚える。
- `python` / `pip` / `mkdocs` の実体（どのパスを参照しているか）を確認する方法。
- パッケージのインストール先、一覧取得、トラブル対処（watchdog／MkDocs の自動再ビルド等）。

3. プロジェクト直下に新しい venv を作成して有効化

```powershell

※ このページは Windows + PowerShell を前提としたコマンド例を載せています。

## 1. 要点まとめ（結論）
- ターミナルのプロンプトに `(.venv)` のように表示されていれば、そのターミナルは仮想環境がアクティブです。

各行の簡単な解説：
- `Set-Location C:\Users\harut\Documents\mydocs` : PowerShell の `cd` 相当です。作業ディレクトリをプロジェクトのルートに移します。
- `py -3 -m venv .venv` : 現在のディレクトリ内に `.venv` という新しい仮想環境フォルダを作ります。Python の `venv` モジュールを使って環境を初期化します。
- `& ".\.venv\Scripts\Activate.ps1"` : 生成した仮想環境をアクティベート（有効化）します。以降の `python` / `pip` はこの `.venv` を参照します。
- `pip install --upgrade pip` : 仮想環境内の `pip` を最新に更新します（推奨）。

4. 旧環境で保存した requirements を使ってパッケージを復元

```powershell
- 再現性・依存分離の観点から、プロジェクト内に作った仮想環境で `mkdocs serve` を実行することを推奨します。
- `setx` は永続環境変数を登録しますが、既存のプロセス（例：既に開いている VS Code）には即時反映されません。

5. 動作確認

```powershell

---

## 2. 仮想環境（venv）とは & なぜ使うか


6. 問題なければ古いバックアップ venv を削除（任意）

```powershell
- 仮想環境は「プロジェクト専用の Python 実行環境」です。グローバルの Python とパッケージ依存を分離できます。
- 利点：

補足: `pip freeze` による requirements には開発時に入れたツールや OS 固有のパッケージも含まれることがあります。必要に応じて `requirements_from_old_venv.txt` を手で編集し、本当に必要なパッケージだけを残してから `pip install -r` するとクリーンになります。

以上の手順なら移行は面倒ではなく、環境の破損リスクも低いです。

---

## 新規で `.venv` をプロジェクト直下に作る（requirements.txt が無い場合）

もし古い仮想環境から requirements を取ってこられない、あるいは最初からプロジェクト用にクリーンな仮想環境を作りたい場合は、以下の手順で進めます。基本的には「作成 → アクティベート → 必要なパッケージを手動インストール → 必要なら requirements を保存」という流れです。

1. プロジェクトへ移動して venv を作成

```powershell
Set-Location C:\Users\harut\Documents\mydocs
py -3 -m venv .venv
```

2. 仮想環境を有効化して pip を最新化

```powershell
& ".\.venv\Scripts\Activate.ps1"
pip install --upgrade pip
```

3. 必要なパッケージを手動でインストール

requirements.txt が無い場合は、プロジェクトで実際に必要なものだけを入れるのが良いです。例えば MkDocs でドキュメントを構築・表示するなら最低限：

```powershell
pip install mkdocs mkdocs-material watchdog
```

補足:
- ここで `watchdog` を入れると `mkdocs serve` の自動再ビルド（ファイル監視）がネイティブに動くようになります。
- 開発ツール（black, flake8, isort など）は必要に応じて個別に入れてください。

4. 動作確認と requirements 保存（任意だが推奨）

```powershell
mkdocs --version
pip list
pip freeze > requirements.txt
```

`requirements.txt` を保存しておけば、別マシンや将来の再構築が簡単になります。

5. VS Code に新しいインタプリタを認識させる

VS Code を使う場合はコマンドパレットで `Python: Select Interpreter` を実行し、`
.venv\Scripts\python.exe` を選択してください。これでターミナル自動アクティベーションや拡張の参照が正しく動きます。

---

まとめ: requirements.txt が無ければ、必要なパッケージを手動で入れるだけで問題ありません。入れたら `pip freeze > requirements.txt` を作っておくと後で楽になります。
  - 依存の衝突回避（複数プロジェクトで異なるパッケージバージョンを安全に使える）。
  - 再現性（requirements.txt を使えば別マシンで同じ環境を作れる）。
  - 権限面の安全（システム領域にインストールしないため管理者権限が不要なことが多い）。

短所はほとんどなく、プロジェクトごとに一つの venv を作っておくのが現代的な運用です。

---

## 3. よく使う操作（PowerShell）

以下はコピペで実行できる一連の操作（プロジェクトが `C:\Users\harut\Documents\mydocs` にある想定）。パスは実際の環境に合わせて読み替えてください。

- プロジェクトへ移動：

```powershell
Set-Location C:\Users\harut\Documents\mydocs
```

- 仮想環境を作る（プロジェクト直下に作る推奨）：

```powershell
py -3 -m venv .venv
```

- 仮想環境に入る（Activate）：

```powershell
& "C:\Users\harut\Documents\mydocs\.venv\Scripts\Activate.ps1"
# あるいは、もし .venv がホーム直下にある場合はパスを合わせる
```

プロンプトが `(.venv) PS C:\Users\harut\Documents\mydocs>` のようになれば有効です。

- 仮想環境から抜ける（Deactivate）：

```powershell
deactivate
# プロンプトから (.venv) が消えます。
```

- パッケージのインストール（仮想環境が有効なターミナルで）：

```powershell
pip install mkdocs mkdocs-material watchdog
```

---

## 4. どの `python` / `pip` / `mkdocs` を参照しているか確認する

以下のコマンドで「実体のパス」を確認できます。仮想環境をアクティブにしてから実行すると、仮想環境内の実行ファイルを指すはずです。

- PowerShell での確認例：

```powershell
Get-Command python | Format-List Path
Get-Command pip    | Format-List Path
Get-Command mkdocs | Format-List Path
```

出力例（仮想環境内なら）: `C:\...\mydocs\.venv\Scripts\python.exe` のようなパスが返る。

- Windows の `where` コマンド（複数候補を列挙）

```powershell
where python
where pip
where mkdocs
```

- Python 自体がどの実行ファイルを使っているか（Python 内から）

```powershell
python -c "import sys; print(sys.executable)"
python -c "import site; print(site.getsitepackages() if hasattr(site,'getsitepackages') else 'no getsitepackages')"
python -c "import sysconfig; print(sysconfig.get_paths())"
```

これで `site-packages` や `Scripts` の実体パスがわかります。

---

## 5. パッケージのインストール先と確認方法

- `pip install ...` を実行すると、インストール先はその `pip` が指す Python の `site-packages` 配下に入ります。仮想環境が有効なら `.venv\Lib\site-packages`（Windows）です。
- `pip show <package>` で各パッケージのインストール場所を確認できます。

```powershell
pip show mkdocs
# 出力の Location: 行がインストール先ディレクトリ（site-packages）を示す
```

- インストール済みパッケージ一覧: 

```powershell
pip list
# または要件ファイルを作るときは
pip freeze > requirements.txt
```

---

## 6. MkDocs / watchdog の観測（watch）に関する注意点

- MkDocs は編集検知のために OS のファイル監視機構（watchdog）を使います。watchdog が正しくインストールされていない、または異なる Python 環境に入っていると自動リビルドや自動リロードが動かないことがあります。
- そのため `mkdocs serve` は「仮想環境をアクティブにしてから」起動するのが安全です。

- ポーリング監視に切り替える（watchdog の問題回避、CPU 負荷は増す）:

```powershell
#$Env:MKDOCS_WATCH_FORCE_POLLING はそのセッションのみ有効
$Env:MKDOCS_WATCH_FORCE_POLLING = "true"
mkdocs serve -v

# 永続的に windows ユーザ環境変数に登録するなら（1回だけ）:
setx MKDOCS_WATCH_FORCE_POLLING true
# ただし、setx は新しいプロセスで有効になるため VS Code を再起動する必要があります。
```

---

## 7. トラブルシュート（ファイル変更が反映されないときのチェックリスト）

1. ターミナルに `(.venv)` が出ているか確認。出ていなければ仮想環境をアクティブにする。
2. `Get-Command mkdocs | Format-List Path` で mkdocs の実体が仮想環境を指しているか確認。
3. `pip show watchdog` で watchdog が仮想環境に入っているか確認。入っていなければ `pip install watchdog`。
4. それでも検知しない場合は `$Env:MKDOCS_WATCH_FORCE_POLLING = "true"` を設定して `mkdocs serve -v` を起動し、Markdown 保存時にターミナルに `Detected change` が出るか確認。
5. `setx` を使って永続化した場合は VS Code を再起動する。

コマンド参考：

```powershell
Get-Command mkdocs | Format-List Path
pip show watchdog
$Env:MKDOCS_WATCH_FORCE_POLLING = "true"
mkdocs serve -v
```

---

## 8. 具体的に「今どの Python が使われているか」を確かめるワンセット（実行順）

PowerShell を開き、次を順に実行してください（プロジェクトで作業する想定）：

```powershell
# 1) プロジェクトへ移動
Set-Location C:\Users\harut\Documents\mydocs
# 2) 仮想環境を有効化（パスは環境に合わせる）
& "C:\Users\harut\Documents\mydocs\.venv\Scripts\Activate.ps1"
# 3) 実体の確認
Get-Command python | Format-List Path
Get-Command pip    | Format-List Path
Get-Command mkdocs | Format-List Path
# 4) python 側から詳細を確認
python -c "import sys, sysconfig; print('exe=', sys.executable); print('site-packages=', sysconfig.get_paths()['purelib'])"
# 5) pip のパッケージ一覧
pip list
# 6) mkdocs の詳細
mkdocs --version
pip show mkdocs
```

期待値：`Get-Command` の結果が `.venv\Scripts\...` を指しており、`pip show mkdocs` の Location が `.venv\Lib\site-packages` を示せば OK。

---

## 9. VS Code の自動アクティベーションについて

- VS Code の Python 拡張は新しいターミナルを開くと仮想環境をアクティブにする設定になっていることがあります（便利）。不要なら Settings で `python.terminal.activateEnvironment` を `false` にできます。

---

## 10. 参考コマンド（まとめ）

```powershell
# 作成
py -3 -m venv .venv
# 有効化
& "C:\path\to\.venv\Scripts\Activate.ps1"
# 無効化
deactivate
# 仮想環境内の mkdocs 起動
mkdocs serve -v
# watchdog が怪しいときは一時的に
$Env:MKDOCS_WATCH_FORCE_POLLING = "true"
mkdocs serve -v
# 実体確認
Get-Command mkdocs | Format-List Path
python -c "import sys; print(sys.executable)"
pip show mkdocs
pip list
# 永続的なポーリングを登録（注意: VS Code 再起動が必要）
setx MKDOCS_WATCH_FORCE_POLLING true
```

---

必要なら、このファイルに「プロジェクト固有の推奨手順」を追記できます（例：`.venv` をプロジェクト直下に置く、`requirements.txt` を用意する、`README` に起動手順を書く等）。どれを追加しましょうか？
