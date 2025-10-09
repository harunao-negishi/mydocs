```powershell
# SSHクライアントのバージョン確認
ssh -V
```

---
### SSH接続例
```powershell
ssh ユーザー名@ホスト名
```
（例：`ssh harut@example.com`）

---
### よくあるトラブル
- ファイアウォールやネットワーク設定で接続できない場合がある
- SSH鍵の作成・登録が必要な場合は、以下のコマンドで鍵を作成

```powershell
ssh-keygen -t rsa -b 4096
```
作成した公開鍵（.pub）をサーバーの`~/.ssh/authorized_keys`に登録
# Remote SSHとは
リモートのサーバーやPCにSSH接続し、ローカルと同じようにファイル操作や開発作業ができる仕組みです。

## 主な用途
- サーバー上での開発・デバッグ
- リモート環境への安全なアクセス
- 複数環境の統合管理

## 対象ユーザー
- サーバー管理者
- クラウドやリモート開発を行うエンジニア

## 始め方（VS Code編）
1. VS Codeで「Remote - SSH」拡張機能をインストール
2. コマンドパレットから「Remote-SSH: Connect to Host...」を選択
3. SSH接続情報を入力し、リモート環境に接続
4. 接続後はローカルと同じようにファイル編集・ターミナル操作が可能

---
### Windowsで必要な準備
- SSHクライアントはWindows 10以降標準搭載ですが、古い場合は[OpenSSH](https://docs.microsoft.com/ja-jp/windows-server/administration/openssh/openssh_install_firstuse)をインストールしてください。
- VS Codeのインストール：[公式サイト](https://code.visualstudio.com/)
- Remote - SSH拡張機能のインストール：VS Codeの拡張機能検索で「Remote - SSH」を選択

```powershell
# SSHクライアントのバージョン確認
ssh -V
```
