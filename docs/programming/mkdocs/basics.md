# MkDocs 日常運用の基本

## 1. プロジェクトの構造
- 設定ファイル: `mkdocs.yml`
- ドキュメント: `docs/` フォルダ以下に Markdown を配置
- 追加リソース: `docs/` 内に画像・PDF・CSS 等を置けばリンク可能

## 2. ローカルでプレビューする
```powershell
mkdocs serve
```
- 端末を同じディレクトリ（`mydocs/`）で開いた状態で実行。
- ブラウザで `http://127.0.0.1:8000/` にアクセスするとリアルタイム更新される。
- PDFや画像を追加した場合も、保存すれば自動で反映される。

### 自動リロードが効かないとき
- `python -m pip install watchdog` を実行してファイル監視ライブラリを入れる。
- PowerShellを開き直し、再度 `mkdocs serve` を実行。

## 3. ビルドして成果物を確認する
```powershell
mkdocs build
```
- `site/` フォルダに静的ファイルが生成される。
- 本番デプロイ前にリンク切れやレンダリング崩れをチェックしたいときに便利。

## 4. GitHub Pages に公開する
```powershell
mkdocs gh-deploy
```
- `gh-pages` ブランチに成果物がプッシュされ、GitHub Pages が更新される。
- 通常は `git push` で本文を反映した後に実行するとよい。

## 5. よくある操作の組み合わせ
| 作業内容 | コマンド例 |
| --- | --- |
| ローカルでプレビュー | `mkdocs serve`
| リンク切れチェック | `mkdocs build`
| 公開サイト更新 | `mkdocs gh-deploy`

## 6. ナビゲーションの更新
- `mkdocs.yml` の `nav:` セクションに Markdown ファイルへのパスを追記する。
- 階層は `- 見出し: path/to/file.md` 形式で表現。

## 7. カスタムCSS・JSの追加
- `docs/extra.css` や `docs/javascripts/*.js` を用意して `mkdocs.yml` の `extra_css`, `extra_javascript` に追記する。

## 8. トラブルシューティング
- 警告: 「navに含まれていないファイル」は `mkdocs.yml` に追加するか、不要なら削除。
- 画像が表示されない: 相対パスの確認（Markdownから見た位置で指定）。
- デプロイ後に更新されない: ブラウザのキャッシュをクリア、または `Ctrl + F5` で再読み込み。

---
日常的には「serveで確認 → git commit/push → gh-deployで公開」のループで運用するとシンプルでミスが少なくなります。
