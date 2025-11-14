# Gitとは

**Git** は、ファイルの変更履歴を記録・管理できるツールです。  
特に便利なのは、**複数のPC（例：研究室PCと自宅PC）間で、同じプロジェクトを同期できる**ことです。

GitHub などのサービスと組み合わせると、

- 研究室PCで編集 → GitHubにアップ
- 自宅PCで GitHub から取得 → 続きから編集

ということが簡単にできます。

---

## 主な用語

- **リポジトリ（repository）**  
  プロジェクトの「保存庫」。  
  1つのリポジトリの中にソースコードや設定ファイル、履歴などがすべて入る。

- **コミット（commit）**  
  変更を記録するスナップショット。  
  「ここまでの状態を保存！」というマイルストーン。

- **ブランチ（branch）**  
  並行して開発するための枝。  
  `main` ブランチが「本線」で、そこから派生して試したりする。

- **リモート（remote）**  
  GitHub などのサーバ上にあるリポジトリのこと。  
  ローカルPCのリポジトリと同期することで、複数PCで共有できる。

---

### Windowsで必要な準備

- Gitのインストール：[公式サイト](https://git-scm.com/download/win)からダウンロード

インストール後、PowerShellで確認：

```powershell
# Gitのバージョン確認
git --version
```

これでバージョンが出るようなら、インストール成功です！

Git がどこに入っているか確認したいときは：

```powershell
where.exe git
```

出力結果が、

```
C:\Program Files\Git\cmd\git.exe
```

のようになっていればOKです。

その後はPCごとに一度だけ、ユーザー情報を設定します。

```powershell
# ユーザー名の設定
git config --global user.name "あなたの名前"
# メールアドレスの設定
git config --global user.email "あなたのメールアドレス"
```

config の `--global` オプションは「このPC全体で共通の設定にする」という意味です。

config の内容を確認したいときは：

```powershell
git config --global --list
```

---

## 基本のワークフローの2パターン

Git + GitHub の使い方として、よく出てくるのは次の2パターンです。

- パターンA：GitHub に既にあるリポジトリを、別PCに持ってきて使う（＝clone）
→ 今回やりたい「Documents/mydocs に GitHub から取ってくる」パターン
- パターンB：ローカルで作ったプロジェクトを、新しく GitHub に公開する
→ 研究室PCで新しいプロジェクトを作るときなど

どちらにも共通する「日々の更新」の流れは同じです：

```text
編集 → git add → git commit → git push
（別PCでは）git pull で最新状態を取得
```

### 共通で使う基本コマンド

```powershell
# 現在の状況を確認（変更されたファイルの一覧など）
git status

# 変更をステージング（コミット対象として追加）
git add ファイル名
# 全部まとめて追加したい場合
git add .

# 変更をコミット（履歴として保存）
git commit -m "メッセージ"

# リモート（GitHub）の main ブランチに反映
git push origin main

# GitHub 上の最新の変更を取得
git pull origin main
```

---
## パターンA：既存のGitHubリポジトリを別PC／別フォルダに持ってくる（clone）

使う場面としては、

- 研究室PC で作業している `mydocs`（GitHub 上のリポジトリ）がある
- 自宅PCでも同じ `mydocs` を使いたい
- あるいは、フォルダ構成を変えて、`Documents/mydocs` に置き直したい

こういうときは、新しい場所で `git clone` するのが正解です。
`git init` や `git remote add origin` は不要（clone が全部やってくれる）。

以下、進め方です：

```powershell
# 今回は `Documents/mydocs` にクローンすることにします。
cd ~/Documents
# GitHub のリポジトリURLを使って clone
git clone https://github.com/ユーザー名/リポジトリ名.git mydocs
# 最後の mydocs は、ローカルフォルダ名です
# → これで Documents/mydocs が作られ、その中にリポジトリ一式が入る

cd mydocs
code .
```

この後は通常通りの運用の仕方をして問題ありません。

### パターンB：ローカルから新しいプロジェクトをGitHubに公開する

GitHub 側にまだリポジトリがない状態から始める場合の流れです。

1. GitHubで新しいリポジトリを作成
2. VS Codeのターミナルで以下のコマンドを実行

```powershell
# ローカルリポジトリをGitHubに接続
git remote add origin https://github.com/ユーザー名/リポジトリ名.git
# 最初のプッシュ
git push -u origin main
```

---

### よく使うコマンド

```powershell
# 変更を記録
git add .
git commit -m "初回コミット"
# リモートに反映
git push origin main
# 最新の変更を取得
git pull origin main
```

---

## よくあるトラブル

- GitHub認証エラー：トークン認証やSSH鍵の設定が必要な場合あり
- ファイルが反映されない：add/commit/pushの順番を確認
