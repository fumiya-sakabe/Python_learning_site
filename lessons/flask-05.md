# Webアプリのデプロイ

## このレッスンのゴール

- アプリケーションを本番環境向けに設定できる
- 静的ファイルと環境変数の扱い方を理解できる
- PythonAnywhereやRenderなどのプラットフォームにデプロイできる
- GitHubにコードを公開できる
- デプロイ後のアプリケーションを管理できる

## なぜ重要なのか

デプロイは、作成したアプリケーションをインターネット上で公開するための重要なステップです。

ポートフォリオアプリでも、実際に動くアプリケーションを公開することで、自分のスキルをアピールできます。

実務でも、デプロイは開発の重要な部分です。

デプロイを経験することで、本番環境での注意点を学べます。

## 解説

### 1. 本番環境向けの設定

<strong class="highlight">debugモードを無効化</strong>

```python
# 開発環境
if __name__ == '__main__':
    app.run(debug=True)

# 本番環境
if __name__ == '__main__':
    app.run(debug=False)
```

<strong class="highlight">環境変数で設定を管理</strong>

```python
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-key')
app.config['DEBUG'] = os.environ.get('DEBUG', 'False') == 'True'
```

### 2. requirements.txtの確認

依存パッケージを確認します。

```bash
pip freeze > requirements.txt
```

`requirements.txt`の例：

```
Flask==3.0.0
Werkzeug==3.0.1
```

### 3. .gitignoreファイル

Gitに含めないファイルを指定します。

```
venv/
__pycache__/
*.pyc
*.db
.env
instance/
.webassets-cache
```

### 4. GitHubに公開

```bash
# Gitリポジトリを初期化
git init

# ファイルを追加
git add .

# コミット
git commit -m "Initial commit"

# GitHubリポジトリを作成してプッシュ
git remote add origin https://github.com/username/repository.git
git branch -M main
git push -u origin main
```

### 5. PythonAnywhereでのデプロイ

<strong class="highlight">手順：</strong>

1. PythonAnywhereにアカウントを作成
2. Dashboardから「Web」タブを開く
3. 「Add a new web app」をクリック
4. Python 3.xを選択
5. 「Manual configuration」を選択
6. 「Reload」をクリック

<strong class="highlight">コードのアップロード：</strong>

```bash
# Bashコンソールで実行
cd ~/myapp
git clone https://github.com/username/repository.git
```

<strong class="highlight">WSGIファイルの設定：</strong>

```python
# /var/www/username_pythonanywhere_com_wsgi.py
import sys
path = '/home/username/myapp'
if path not in sys.path:
    sys.path.insert(0, path)

from app import app as application
```

<strong class="highlight">環境変数の設定：</strong>

Dashboard → Web → Environment variables で設定

### 6. Renderでのデプロイ

<strong class="highlight">手順：</strong>

1. Renderにアカウントを作成
2. 「New」→「Web Service」を選択
3. GitHubリポジトリを接続
4. 設定を入力：
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app`
5. 「Create Web Service」をクリック

<strong class="highlight">requirements.txtに追加：</strong>

```
gunicorn==21.2.0
```

<strong class="highlight">Procfile（オプション）：</strong>

```
web: gunicorn app:app
```

### 7. Gunicornの設定

本番環境ではGunicornなどのWSGIサーバーを使います。

```bash
pip install gunicorn
```

```bash
# 起動コマンド
gunicorn -w 4 -b 0.0.0.0:8000 app:app
```

- `-w`: ワーカープロセスの数
- `-b`: バインドアドレスとポート
- `app:app`: モジュール名:アプリケーション名

### 8. 環境変数の管理

`.env`ファイルで環境変数を管理（開発環境のみ）。

```python
from dotenv import load_dotenv
load_dotenv()

SECRET_KEY = os.environ.get('SECRET_KEY')
```

<strong class="highlight">注意</strong>: `.env`ファイルはGitにコミットしない

### 9. 静的ファイルの設定

Flaskは自動的に`static`フォルダを静的ファイルとして扱います。

```
project/
    app.py
    static/
        css/
        js/
        images/
    templates/
```

### 10. データベースの管理

本番環境では、データベースファイルの場所を確認します。

```python
import os

db_path = os.path.join(os.path.dirname(__file__), 'database.db')
conn = sqlite3.connect(db_path)
```

### 11. ログの設定

本番環境ではログを記録します。

```python
import logging

if not app.debug:
    file_handler = logging.FileHandler('error.log')
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
```

### 12. セキュリティチェックリスト

- [ ] `debug=False`に設定
- [ ] `SECRET_KEY`を環境変数で設定
- [ ] SQLインジェクション対策（プレースホルダー使用）
- [ ] CSRF対策（Flask-WTFなど）
- [ ] パスワードのハッシュ化
- [ ] HTTPSを使用（本番環境）

## よくある間違い

- `debug=True`のまま本番環境にデプロイする（セキュリティリスク）
- `SECRET_KEY`をハードコードする（環境変数を使う）
- `.env`ファイルをGitにコミットする（`.gitignore`に追加）
- データベースファイルの場所を考慮しない（相対パスの問題）
- 静的ファイルのパスを間違える（`static`フォルダに配置）
- GunicornなどのWSGIサーバーを使わない（本番環境では必須）

## 演習課題

問1. 本番環境向けに`app.py`を設定してください：

   ```python
   import os
   
   app = Flask(__name__)
   app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-key')
   app.config['DEBUG'] = os.environ.get('DEBUG', 'False') == 'True'
   ```

<details>
<summary>解答を表示</summary>

```python
import os
from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', os.urandom(24))
app.config['DEBUG'] = os.environ.get('DEBUG', 'False') == 'True'

if __name__ == '__main__':
    app.run(debug=app.config['DEBUG'])
```
</details>

問2. `requirements.txt`を確認・更新してください：

   ```bash
   pip freeze > requirements.txt
   ```

<details>
<summary>解答を表示</summary>

```bash
pip freeze > requirements.txt
# 例に必要なもの
# Flask, gunicorn, python-dotenv など
```
</details>

問3. `.gitignore`ファイルを作成してください：

   ```
   venv/
   __pycache__/
   *.pyc
   *.db
   .env
   ```

<details>
<summary>解答を表示</summary>

```gitignore
venv/
__pycache__/
*.pyc
*.pyo
*.db
.env
instance/
.webassets-cache
```
</details>

問4. GitHubリポジトリを作成してコードを公開してください：

   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin <repository-url>
   git push -u origin main
   ```

<details>
<summary>解答を表示</summary>

```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/<yourname>/<repo>.git
git push -u origin main
```
</details>

問5. PythonAnywhereまたはRenderでアプリケーションをデプロイしてください：

- PythonAnywhere: Dashboard → Web → Add a new web app
- Render: New → Web Service → Connect repository

<details>
<summary>解答を表示</summary>

PythonAnywhere（例）

1) リポジトリをサーバへクローン

```bash
cd ~/myapp
git clone https://github.com/<yourname>/<repo>.git
```

2) 仮想環境を作成・有効化し、依存をインストール

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

3) WSGIに`from app import app as application`を設定しReload

Render（例）

- Build Command: `pip install -r requirements.txt`
- Start Command: `gunicorn app:app`
```
</details>

## まとめ

このレッスンでは、Webアプリのデプロイについて学びました。

- 本番環境向けの設定
- GitHubへの公開
- PythonAnywhereやRenderでのデプロイ
- Gunicornの設定
- 環境変数の管理
- セキュリティチェックリスト

デプロイを経験することで、実際に動くWebアプリケーションを作成できるようになりました。

これでPhase3のFlask学習は完了です。次のPhase4では、ポートフォリオアプリを作成していきます！

