# Flask入門（Hello Worldとルーティング）

## このレッスンのゴール

- Flaskアプリケーションの基本的な構造を理解できる
- ルーティング（URLと関数の対応付け）を設定できる
- HTMLテンプレートを表示できる
- 動的なルーティング（パラメータ）を使える
- 簡単なWebアプリケーションを作成できる

## なぜ重要なのか

Flaskは、PythonでWebアプリケーションを開発するための軽量なフレームワークです。

シンプルで学習しやすく、小規模から中規模のWebアプリケーションを効率的に開発できます。

実務でも、APIサーバーや小さなWebアプリケーションでFlaskは頻繁に使われます。

ポートフォリオアプリでも、Flaskを使ってWebアプリケーションを作成することで、実践的なスキルをアピールできます。

## 解説

### 1. Flaskのインストール

`pip`を使ってFlaskをインストールします。

```bash
pip install flask
```

### 2. 最小限のFlaskアプリ

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello, World!</h1>'

if __name__ == '__main__':
    app.run(debug=True)
```

実行すると、`http://localhost:5000`でアクセスできます。

### 3. ルーティングの基本

`@app.route()`デコレータでURLと関数を対応付けます。

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'ホームページ'

@app.route('/about')
def about():
    return 'Aboutページ'

@app.route('/contact')
def contact():
    return 'Contactページ'

if __name__ == '__main__':
    app.run(debug=True)
```

### 4. 動的なルーティング

URLにパラメータを含めることができます。

```python
@app.route('/user/<name>')
def user(name):
    return f'<h1>こんにちは、{name}さん！</h1>'

# /user/太郎 → "こんにちは、太郎さん！"
```

型を指定することもできます：

```python
@app.route('/post/<int:post_id>')
def show_post(post_id):
    return f'<h1>Post ID: {post_id}</h1>'

# 利用可能な型: int, float, path, string
```

### 5. 複数のルールを一つの関数に

複数のURLを同じ関数に対応付けできます。

```python
@app.route('/')
@app.route('/index')
@app.route('/home')
def home():
    return 'ホームページ'
```

### 6. HTTPメソッドの指定

デフォルトでは`GET`メソッドのみ受け付けます。

```python
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # POSTリクエストの処理
        return 'ログイン処理'
    # GETリクエストの処理
    return 'ログインページ'
```

### 7. リクエストデータの取得

`request`オブジェクトからデータを取得します。

```python
from flask import Flask, request

app = Flask(__name__)

@app.route('/search')
def search():
    query = request.args.get('q', '')  # URLパラメータを取得
    return f'検索キーワード: {query}'

# /search?q=python → "検索キーワード: python"
```

### 8. テンプレートの使用

HTMLテンプレートを表示できます（次回詳しく学びます）。

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', name='太郎')
```

### 9. リダイレクトとエラーハンドリング

```python
from flask import Flask, redirect, url_for, abort

app = Flask(__name__)

@app.route('/redirect')
def redirect_example():
    return redirect(url_for('index'))

@app.route('/error')
def error_example():
    abort(404)  # 404エラーを返す

@app.errorhandler(404)
def not_found(error):
    return 'ページが見つかりません', 404
```

### 10. アプリケーションの実行

```python
if __name__ == '__main__':
    app.run(
        debug=True,  # デバッグモード
        host='0.0.0.0',  # 全てのネットワークインターフェースでリッスン
        port=5000  # ポート番号
    )
```

**注意**: 本番環境では`debug=False`にします。

## よくある間違い

- `debug=True`のまま本番環境にデプロイする（セキュリティリスク）
- ルーティングのデコレータを忘れる（`@app.route()`が必要）
- 関数名とルートの対応を間違える（URLと関数が対応しない）
- 動的ルーティングで型を指定しない（文字列として扱われる）
- `if __name__ == '__main__'`を忘れる（インポート時に実行される）

## 演習課題

1. 最小限のFlaskアプリを作成して、Hello Worldを表示してください：

```python
from flask import Flask

app = Flask(__name__)

# ここを実装
```

<details>
<summary>解答を表示</summary>

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)
```
</details>

2. 以下のルートを追加してください：
- `/`: ホームページ
- `/about`: Aboutページ
- `/contact`: Contactページ

```python
# 各ルートを実装
```

<details>
<summary>解答を表示</summary>

```python
@app.route('/')
def home():
    return 'ホームページ'

@app.route('/about')
def about():
    return 'Aboutページ'

@app.route('/contact')
def contact():
    return 'Contactページ'
```
</details>

3. 動的ルーティングを使って、ユーザー名を表示するページを作成してください：

```python
@app.route('/user/<name>')
def user(name):
    # ここを実装
    pass
```

<details>
<summary>解答を表示</summary>

```python
@app.route('/user/<name>')
def user(name):
    return f'こんにちは、{name}さん！'
```
</details>

4. URLパラメータから検索キーワードを取得して表示してください：

```python
from flask import request

@app.route('/search')
def search():
    # ここを実装（request.args.get()を使う）
    pass
```

<details>
<summary>解答を表示</summary>

```python
from flask import request

@app.route('/search')
def search():
    q = request.args.get('q', '')
    return f'検索キーワード: {q}'
```
</details>

5. エラーハンドラーを追加して、404エラーのカスタムページを表示してください：

```python
@app.errorhandler(404)
def not_found(error):
    # ここを実装
    pass
```

<details>
<summary>解答を表示</summary>

```python
@app.errorhandler(404)
def not_found(error):
    return 'ページが見つかりません', 404
```
</details>

## まとめ

このレッスンでは、Flaskの基本について学びました。

- Flaskアプリケーションの作成
- ルーティングの設定
- 動的なルーティング（パラメータ）
- リクエストデータの取得
- エラーハンドリング

次のレッスンでは、テンプレートとフォームについて詳しく学びます。

