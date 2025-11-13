# 仮想環境（venv）について — Windows / PowerShell 向けハンドブック

このページは、プロジェクト単位の Python 仮想環境（`venv`）を使う理由と基本操作、
「どの python / pip / mkdocs が使われているか」を確実に確認する方法をまとめた短い実用ガイドです。

目的：

- プロジェクトごとに独立した Python 環境を作成・管理する方法を理解する。
- VS Code やターミナルで仮想環境を有効化・無効化する手順を覚える。
- `python` / `pip` / `mkdocs` の実体パスを確認する方法を習得する。
- パッケージのインストール先と一覧取得方法を把握する。
- 仮想環境とグローバル環境の違いを理解する。

※ このページは Windows + PowerShell を前提としたコマンド例を載せています。

---

## 仮想環境（venv）とは & なぜ使うか

Python の仮想環境（venv）は、プロジェクトごとに独立した Python 実行環境を作成するための仕組みです。これにより、異なるプロジェクトで異なるバージョンのパッケージを安全に共存させることができます。
主な特徴と利点：

- 仮想環境は「プロジェクト専用の Python 実行環境」です。グローバルの Python とパッケージ依存を分離できます。
- 利点：
  - 依存の衝突回避：複数プロジェクトで異なるパッケージバージョンを安全に使える。
  - 再現性：requirements.txt を使えば別マシンで同じ環境を作れる。
  - 権限面の安全：システム領域にインストールしないため管理者権限が不要なことが多い。

補足: `pip freeze` による requirements には開発時に入れたツールや OS 固有のパッケージも含まれることがあります。必要に応じて `requirements_from_old_venv.txt` を手で編集し、本当に必要なパッケージだけを残してから `pip install -r` するとクリーンになります。

以下では、仮想環境の新規作成方法・既存の仮想環境の移行（更新）方法について説明します。

## 新規で `.venv` をプロジェクト直下に作る（requirements.txt が無い場合）

最初からプロジェクト用にクリーンな仮想環境を作りたい場合は、以下の手順で進めます。基本的には「作成 → アクティベート → 必要なパッケージを手動インストール → 必要なら requirements を保存」という流れです。

### 1. プロジェクトへ移動して venv を作成

```powershell
Set-Location C:\Users\harut\Documents\mydocs
python -m venv .venv
```

### 2. 仮想環境を有効化して pip を最新化

```powershell
& ".\.venv\Scripts\Activate.ps1"
# ここで、先頭に (.venv) と表示されれば仮想環境が有効化されています
# 次に、この仮想環境内の pip を最新化します
python -m pip install --upgrade pip
```

なお、仮想環境を無効化するには、以下のコマンドを実行します。

```powershell
deactivate
```

### 3. 必要なパッケージを手動でインストール

別の仮想環境で使っているrequirements.txtがある場合は、そのファイルを今いるプロジェクト直下にコピーしてから、

```powershell
pip install -r requirements.txt
```

で一括インストールできます。

requirements.txt が無い場合は、プロジェクトで実際に必要なものだけを入れるのが良いです。例えば MkDocs でドキュメントを構築・表示するなら最低限：

```powershell
pip install mkdocs mkdocs-material watchdog
```

ここで `watchdog` を入れると `mkdocs serve` の自動再ビルド（ファイル監視）がネイティブに動くようになります。開発ツール（black, flake8, isort など）は必要に応じて個別に入れてください。

### 4. 動作確認と requirements 保存（任意だが推奨）

```powershell
where.exe python
where.exe pip
where.exe mkdocs
# それぞれのパスが .venv\Scripts\python.exe などになっていればOK
mkdocs --version
pip list
pip freeze > requirements.txt
```

`requirements.txt` を保存しておけば、別マシンや将来の再構築が簡単になります。

## 既存の venv をプロジェクト直下に移したいとき

既にホーム直下など別の場所に仮想環境（例: `C:\Users\harut\.venv`）があって、それをプロジェクト（`mydocs`）の直下に置きたい場合、またはグローバルのPythonについて変更があって、仮想環境がうまく働かなくなったときなどは、単純にフォルダを移動するより「新しい venv を作ってパッケージを再インストール」する方法が安全で確実です。

以下は手順（短くコピペで実行できる順序）。ここでは既存の仮想環境からパッケージ一覧を出力済み（`requirements_from_old_venv.txt`）と仮定します。まだ出していなければ、古い venv をアクティベートして `pip freeze > requirements_from_old_venv.txt` を実行してください。

### 1. 古い仮想環境でパッケージ一覧を保存（まだのとき）

```powershell
# 古い仮想環境を有効化（Pathに注意）
& "C:\Users\harut\.venv\Scripts\Activate.ps1"
# 既存の仮想環境からパッケージ一覧を取得
pip freeze > C:\Users\harut\Documents\mydocs\requirements_from_old_venv.txt
# 古い仮想環境を無効化
deactivate
```

### 2. 古い venv を念のためバックアップ（任意）

既存の古い venv を削除・移動する前にバックアップしておくと安心です。注意: バックアップは仮想環境がアクティブでない状態（deactivate した後）で行ってください。

```powershell
# 仮想環境を無効化（アクティブなら）
deactivate

# フォルダごとコピー（同ドライブ内なら高速）
Copy-Item -Path "C:\Users\harut\.venv" -Destination "C:\Users\harut\Documents\mydocs\.venv_old" -Recurse -Force

# あるいは圧縮して保存（ファイルサイズを小さく保管したい場合）
Compress-Archive -Path "C:\Users\harut\.venv\*" -DestinationPath "C:\Users\harut\Documents\mydocs\venv_backup.zip" -Force
```

- 復元する場合はコピー先を元の場所へ戻すか、圧縮を解凍して使用します（Expand-Archive など）。
- バックアップが不要と確信できたら古いバックアップを削除してディスクを開放してください。
- バックアップは任意の手順なので、移行手順の前に必ず必要というわけではありません。

### 3. プロジェクト直下に新しい venv を作成して有効化

```powershell
Set-Location C:\Users\harut\Documents\mydocs
py -3 -m venv .venv
& ".\.venv\Scripts\Activate.ps1"
pip install --upgrade pip
```

- ターミナルのプロンプトに `(.venv)` のように表示されていれば、そのターミナルは仮想環境がアクティブです。
- `Set-Location C:\Users\harut\Documents\mydocs` : PowerShell の `cd` 相当です。作業ディレクトリをプロジェクトのルートに移します。
- `py -3 -m venv .venv` : 現在のディレクトリ内に `.venv` という新しい仮想環境フォルダを作ります。Python の `venv` モジュールを使って環境を初期化します。
- `& ".\.venv\Scripts\Activate.ps1"` : 生成した仮想環境をアクティベート（有効化）します。以降の `python` / `pip` はこの `.venv` を参照します。
- `pip install --upgrade pip` : 仮想環境内の `pip` を最新に更新します（推奨）。

### 4. 古い venv から保存した requirements を使ってパッケージを復元

```powershell
pip install -r requirements_from_old_venv.txt
```

- 再現性・依存分離の観点から、プロジェクト内に作った仮想環境で `mkdocs serve` を実行することを推奨します。
- `setx` は永続環境変数を登録しますが、既存のプロセス（例：既に開いている VS Code）には即時反映されません。

### 5. 動作確認

```powershell
mkdocs --version
pip list
```

### 6. 問題なければ古いバックアップ venv を削除（任意）

```powershell
Remove-Item -Path "C:\Users\harut\Documents\mydocs\.venv_old" -Recurse -Force
# あるいは圧縮バックアップを削除
Remove-Item -Path "C:\Users\harut\Documents\mydocs\venv_backup.zip" -Force
```

## VS Code に新しいインタプリタを認識させる

VS Code を使う場合はコマンドパレットで `Python: Select Interpreter` を実行し、`.venv\Scripts\python.exe` を選択してください。これでターミナル自動アクティベーションや拡張の参照が正しく動きます。

