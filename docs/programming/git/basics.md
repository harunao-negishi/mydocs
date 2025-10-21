# Gitの基本運用フロー

## 日々の作業手順（ローカル → GitHub）
1. **最新状態を取得**
	```powershell
	git pull origin main
	```
	- 別端末での変更があるかもしれないので、作業前に必ず最新化。

2. **作業する**
	- ドキュメントの編集や新規追加などを実施。

3. **変更内容の確認**
	```powershell
	git status
	git diff
	```
	- 何が変わったかを把握してからコミットする。

4. **ステージング**
	```powershell
	git add .
	```
	- 「.」で全変更をステージ。ファイルを絞りたい場合は個別に指定。

5. **コミット作成**
	```powershell
	git commit -m "Add lecture 01 notes"
	```
	- メッセージは何をしたか分かるように具体的に。

6. **リモートへ反映**
	```powershell
	git push origin main
	```
	- プッシュ後はGitHub上の履歴にも反映される。

## 別ブランチで作業したいとき
```powershell
git checkout -b feature/note-update   # 新しいブランチを作成して移動
# 作業後
git push -u origin feature/note-update
```
- Pull Requestを作りたい場合はブランチで作業してGitHub上でPRを作成。

## よく使うメンテナンスコマンド
- コミット履歴の確認: `git log --oneline --graph`
- 直前のコミットを修正: `git commit --amend`
- ステージ解除: `git reset HEAD <file>`
- 作業前後で差分を比較: `git diff HEAD~1`

## MkDocsとの連携
- ローカルでの確認: `mkdocs serve`
  - ブラウザで `http://127.0.0.1:8000` を開くと変更がライブ反映。
- 公開サイト更新: `mkdocs gh-deploy`
  - `git push` で本文が反映された後に実行するとGitHub Pagesが更新される。
- 変更を戻したいとき: `git checkout -- <file>` でワーキングコピーをリセット。

## 作業のワークフローまとめ
1. pull → 作業 → add → commit → push → （必要に応じて）gh-deploy
2. 途中で迷ったら `git status` を確認し、現在の状態を把握する。
3. 大きな変更の前には必ず最新の `main` を取得し、競合を避ける。
