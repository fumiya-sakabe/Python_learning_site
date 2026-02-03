# パッケージマネージャー（pip）の使い方

## このレッスンのゴール

- `pip`を使ってパッケージをインストールできる
- `requirements.txt`ファイルを作成して、依存関係を管理できる
- 仮想環境でパッケージを管理できる
- パッケージのバージョンを確認・更新できる
- パッケージをアンインストールできる

## なぜ重要なのか

`pip`は、Pythonのパッケージマネージャーで、外部ライブラリをインストールするための標準的なツールです。

実務では、`requests`、`flask`、`numpy`など、多くのサードパーティパッケージを使います。

Webアプリでも、フレームワークやライブラリをインストールするために`pip`は欠かせません。

`requirements.txt`を使って依存関係を管理することで、チーム開発やデプロイ時に環境を再現できます。

## 解説

### 1. pipの基本

`pip`はPythonに最初から含まれています。

```bash
# バージョン確認
pip --version

# パッケージ一覧の表示
pip list

# インストール済みパッケージの情報表示
pip show flask
```

### 2. パッケージのインストール

```bash
# 最新版をインストール
pip install requests

# 特定のバージョンをインストール
pip install flask==3.0.0

# バージョン範囲を指定
pip install "flask>=3.0.0,<4.0.0"
```

### 3. パッケージのアップグレード

```bash
# パッケージをアップグレード
pip install --upgrade requests

# または短縮形
pip install -U requests
```

### 4. パッケージのアンインストール

```bash
pip uninstall requests
```

### 5. requirements.txtの作成

依存関係を管理するファイルです。

```bash
# 現在インストールされているパッケージをrequirements.txtに出力
pip freeze > requirements.txt
```

`requirements.txt`の例：

```
Flask==3.0.0
requests==2.31.0
markdown==3.5.1
```

### 6. requirements.txtからのインストール

```bash
# requirements.txtに記載されたパッケージを一括インストール
pip install -r requirements.txt
```

### 7. 仮想環境での使用（推奨）

仮想環境を作成して、プロジェクトごとにパッケージを管理します。

```bash
# 仮想環境の作成
python -m venv venv

# 仮想環境の有効化（Windows）
venv\Scripts\activate

# 仮想環境の有効化（macOS/Linux）
source venv/bin/activate

# パッケージをインストール
pip install flask

# 仮想環境を無効化
deactivate
```

### 8. pipの主なオプション

```bash
# ユーザー領域にインストール（システムのPythonを使う場合）
pip install --user package_name

# キャッシュを無視して再インストール
pip install --no-cache-dir package_name

# インストール前にアップグレードチェック
pip install --upgrade-strategy eager package_name

# インストール可能なパッケージを検索
pip search package_name

# パッケージ情報の詳細表示
pip show -f package_name
```

### 9. よく使うパッケージ

Web開発関連：

```bash
# Webフレームワーク
pip install flask
pip install django

# HTTPリクエスト
pip install requests

# HTML解析
pip install beautifulsoup4

# Markdown処理
pip install markdown
```

データ処理関連：

```bash
# 数値計算
pip install numpy
pip install pandas

# 可視化
pip install matplotlib
pip install seaborn
```

その他：

```bash
# 環境変数管理
pip install python-dotenv

# 日付処理
pip install python-dateutil

# テスト
pip install pytest
```

### 10. pipのトラブルシューティング

```bash
# pip自体をアップグレード
python -m pip install --upgrade pip

# キャッシュをクリア
pip cache purge

# インストールエラー時の詳細情報
pip install --verbose package_name
```

### 11. 実践例：プロジェクトのセットアップ

1. 仮想環境を作成
2. `requirements.txt`を作成
3. パッケージをインストール

```bash
# 1. 仮想環境を作成
python -m venv venv

# 2. 仮想環境を有効化
source venv/bin/activate  # macOS/Linux
# または
venv\Scripts\activate  # Windows

# 3. 必要なパッケージをインストール
pip install flask requests markdown

# 4. requirements.txtに出力
pip freeze > requirements.txt

# 5. 別の環境で環境を再現
pip install -r requirements.txt
```

## よくある間違い

- 仮想環境を使わずにシステムのPythonに直接インストールする（推奨されない）
- `requirements.txt`を更新しない（パッケージを追加・削除した場合）
- パッケージのバージョンを固定しない（環境によって動作が変わる可能性）
- `pip`と`pip3`を混同する（Python 3を使う場合は`pip3`、通常は`pip`で良い）
- `requirements.txt`の内容を手動で編集する（`pip freeze > requirements.txt`を使う）
- 仮想環境を無効化せずにパッケージをインストールする

## 演習課題

問1. 仮想環境を作成して、`flask`パッケージをインストールしてください：

```bash
# 仮想環境を作成
# 仮想環境を有効化
# flaskをインストール
# インストールされたパッケージを確認
```

<details>
<summary>解答を表示</summary>

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
# source venv/bin/activate
pip install flask
pip list | grep Flask   # Windowsは findstr Flask
```
</details>

問2. `requirements.txt`ファイルを作成して、以下のパッケージを記載してください：

```
Flask==3.0.0
requests==2.31.0
markdown==3.5.1
```

<details>
<summary>解答を表示</summary>

```bash
pip freeze > requirements.txt
# あるいはエディタで上記3行を記載
```
</details>

問3. `requirements.txt`からパッケージを一括インストールしてください：

```bash
pip install -r requirements.txt
```

<details>
<summary>解答を表示</summary>

```bash
pip install -r requirements.txt
```
</details>

問4. インストールされているパッケージの一覧を表示して、バージョンを確認してください：

```bash
pip list
```

<details>
<summary>解答を表示</summary>

```bash
pip list
```
</details>

問5. 特定のパッケージの情報を表示してください：

```bash
pip show flask
```

<details>
<summary>解答を表示</summary>

```bash
pip show flask
# バージョン、依存関係、インストール先などが表示されます
```
</details>

## まとめ

このレッスンでは、`pip`の使い方について学びました。

- `pip`でのパッケージのインストール・アップグレード・アンインストール
- `requirements.txt`での依存関係管理
- 仮想環境でのパッケージ管理
- よく使うパッケージ
- トラブルシューティング

パッケージ管理は、Python開発の基礎なので、しっかりとマスターしておきましょう。

