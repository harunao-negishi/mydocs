# Python 日常運用の基本

## 1. Pythonコマンドの確認
```powershell
python --version
```
- バージョンが表示されればPython本体が利用可能。
- 複数バージョンがある場合は `py -0` で一覧を確認。

## 2. PATH設定（Scripts フォルダを通す）
1. 以下のパスをコピーしておく。
   - `C:\Users\harut\AppData\Local\Python\PythonCore-3.14-64\`
   - `C:\Users\harut\AppData\Local\Python\PythonCore-3.14-64\Scripts\`
2. Windowsの「環境変数の編集」→「ユーザー環境変数」から `Path` に上記を追加。
3. 新しく開いた PowerShell で `pip --version` を実行し、認識されるか確認。

> 一時的にPATHを通したいだけなら、PowerShellで
> ```powershell
> $env:Path += ";C:\Users\harut\AppData\Local\Python\PythonCore-3.14-64;C:\Users\harut\AppData\Local\Python\PythonCore-3.14-64\Scripts"
> ```
> と入力してもよい（端末を閉じると元に戻る）。

## 3. 仮想環境（venv）の作成
```powershell
python -m venv .venv
```
- プロジェクト直下に `.venv` フォルダが生成される。
- PowerShellでの有効化は
  ```powershell
  .\.venv\Scripts\Activate.ps1
  ```

## 4. パッケージ管理
- インストール: `python -m pip install <package>`
- アップデート: `python -m pip install --upgrade <package>`
- インストール済み一覧: `python -m pip list`

依存関係を書き出す場合は `requirements.txt` を用意し、
```powershell
python -m pip install -r requirements.txt
```
が便利。

## 5. スクリプトの実行
```powershell
python scripts/mytool.py --option value
```
- `python -m モジュール名` でモジュールとして実行することも可能。

## 6. Jupyter Notebookの簡易利用
```powershell
python -m pip install jupyter
jupyter notebook
```
- MkDocsプロジェクト内にノートブックを置く場合は、`docs/` 配下に `notebooks/` フォルダを作成し、Markdownにリンクする形式が扱いやすい。

## 7. よく使うトラブルシューティング
- `pip` が見つからない: PATHが通っているか、または `python -m pip` を使う。
- `ModuleNotFoundError`: 仮想環境が有効になっているか確認し、必要なら再インストール。
- スクリプト実行時に文字化け: PowerShellを `chcp 65001` でUTF-8に設定すると解決することが多い。

---
日常的には「Pythonの場所」と「pipの場所」を確実にPATHに通しておき、プロジェクトごとに仮想環境を作る習慣をつけると環境が安定します。
