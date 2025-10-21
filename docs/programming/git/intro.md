
# Gitとは
変更履歴を記録・管理できるツール。  
複数のPC（例：研究室PCと自宅PC）間で、同じフォルダを常に同期できます。

## 主な用語
- **リポジトリ（repository）**: プロジェクトの保存庫
- **コミット（commit）**: 変更を記録する単位
- **ブランチ（branch）**: 並行開発用の枝分かれ
- **リモート（remote）**: GitHubなどの共有サーバ

---
### Windowsで必要な準備
- Gitのインストール：[公式サイト](https://git-scm.com/download/win)からダウンロード
- VS Codeのインストール：[公式サイト](https://code.visualstudio.com/)

```powershell
# Gitのバージョン確認
git --version
```
これでバージョンが出るようなら、インストール成功です！！


---
## 始め方（VS Code編）
1. VS Codeをインストール
2. Git拡張機能を追加（標準で搭載されている場合も多い）
3. プロジェクトフォルダを開き、ソース管理ビューから「リポジトリの初期化」
4. 変更を加えたら「コミット」や「プッシュ」で履歴を管理

---
### GitHub連携の始め方
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
git push
```

---
## よくあるトラブル
- GitHub認証エラー：トークン認証やSSH鍵の設定が必要な場合あり
- ファイルが反映されない：add/commit/pushの順番を確認
