# テンプレートとフォーム

## このレッスンのゴール

- Jinja2テンプレートを使ってHTMLを生成できる
- テンプレートに変数を渡して動的なコンテンツを表示できる
- テンプレートの継承を使って、共通部分を再利用できる
- HTMLフォームを作成して、ユーザー入力を受け取れる
- フォームデータを処理して検証できる

## なぜ重要なのか

テンプレートは、HTMLとPythonコードを分離して、コードを整理するための重要な機能です。

実務でも、テンプレートを使うことで、デザインとロジックを分離し、保守性が向上します。

フォームは、ユーザーからデータを受け取るための標準的な方法です。

Webアプリでは、ログインフォーム、検索フォーム、コメントフォームなど、多くの場面でフォームが使われます。

## 解説

### 1. テンプレートの基本構造

テンプレートファイルは`templates`フォルダに配置します。

```
project/
    app.py
    templates/
        index.html
        base.html
```

### 2. テンプレートのレンダリング

`render_template()`関数でテンプレートを表示します。

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    name = '太郎'
    return render_template('index.html', name=name)
```

### 3. テンプレート内で変数を使用

```html
<!-- templates/index.html -->
<!DOCTYPE html>
<html>
<head>
    <title>ホーム</title>
</head>
<body>
    <h1>こんにちは、{{ name }}さん！</h1>
</body>
</html>
```

### 4. テンプレートの制御構文

<strong class="term">条件分岐</strong>

```html
{% if user %}
    <p>こんにちは、{{ user }}さん</p>
{% else %}
    <p>ログインしてください</p>
{% endif %}
```

<strong class="term">ループ</strong>

```html
<ul>
{% for item in items %}
    <li>{{ item }}</li>
{% endfor %}
</ul>
```

<strong class="term">辞書のループ</strong>

```html
{% for key, value in data.items() %}
    <p>{{ key }}: {{ value }}</p>
{% endfor %}
```

### 5. テンプレートの継承

共通部分をベーステンプレートに定義します。

```html
<!-- templates/base.html -->
<!DOCTYPE html>
<html>
<head>
    <title>{% block title %}{% endblock %}</title>
</head>
<body>
    <nav>
        <a href="/">ホーム</a>
        <a href="/about">About</a>
    </nav>
    {% block content %}{% endblock %}
    <footer>
        <p>&copy; 2024 My App</p>
    </footer>
</body>
</html>
```

子テンプレートで継承：

```html
<!-- templates/index.html -->
{% extends "base.html" %}

{% block title %}ホーム{% endblock %}

{% block content %}
<h1>ホームページ</h1>
<p>ようこそ！</p>
{% endblock %}
```

### 6. テンプレートのインクルード

共通部分を別ファイルに分離できます。

```html
<!-- templates/header.html -->
<header>
    <h1>My Website</h1>
</header>
```

```html
<!-- templates/index.html -->
{% include "header.html" %}
<main>
    <p>コンテンツ</p>
</main>
```

### 7. フォームの基本

HTMLフォームを作成します。

```html
<!-- templates/form.html -->
<form method="POST" action="/submit">
    <label for="name">名前:</label>
    <input type="text" id="name" name="name" required>
    
    <label for="email">メール:</label>
    <input type="email" id="email" name="email" required>
    
    <button type="submit">送信</button>
</form>
```

### 8. フォームデータの処理

```python
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        # データを処理
        return redirect(url_for('success', name=name))
    return render_template('form.html')

@app.route('/success/<name>')
def success(name):
    return f'<h1>送信完了: {name}さん</h1>'
```

### 9. フォームの検証

```python
@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip()
        
        errors = []
        
        if not name:
            errors.append('名前を入力してください')
        
        if not email:
            errors.append('メールアドレスを入力してください')
        elif '@' not in email:
            errors.append('有効なメールアドレスを入力してください')
        
        if errors:
            return render_template('form.html', errors=errors)
        
        # 検証成功
        return redirect(url_for('success', name=name))
    
    return render_template('form.html')
```

テンプレートでエラーを表示：

```html
{% if errors %}
    <ul>
    {% for error in errors %}
        <li>{{ error }}</li>
    {% endfor %}
    </ul>
{% endif %}
```

### 10. WTFormsを使ったフォーム（オプション）

より高度なフォーム処理にはWTFormsが便利です。

```bash
pip install flask-wtf
```

```python
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email

class ContactForm(FlaskForm):
    name = StringField('名前', validators=[DataRequired()])
    email = StringField('メール', validators=[DataRequired(), Email()])
    submit = SubmitField('送信')
```

## よくある間違い

- テンプレートフォルダの名前を間違える（`templates`が正しい）
- 変数を渡さずにテンプレートで使おうとする（エラーになる）
- フォームの`method`属性を忘れる（デフォルトは`GET`）
- CSRF対策をしない（本番環境では必要）
- フォームの検証をしない（セキュリティリスク）
- テンプレートの継承を理解しない（コードの重複が増える）

## 演習課題

問1. テンプレートを作成して、変数を表示してください：

```python
@app.route('/')
def index():
    items = ["りんご", "バナナ", "オレンジ"]
    return render_template('index.html', items=items)
```

<details>
<summary>解答を表示</summary>

```html
<!-- templates/index.html -->
<!DOCTYPE html>
<html>
<body>
    <ul>
        {% for item in items %}
            <li>{{ item }}</li>
        {% endfor %}
    </ul>
</body>
</html>
```
</details>

問2. ベーステンプレートを作成して、他のテンプレートで継承してください：

```html
<!-- base.html を作成 -->
<!-- index.html と about.html で継承 -->
```

<details>
<summary>解答を表示</summary>

```html
<!-- templates/base.html -->
<!DOCTYPE html>
<html>
<head>
  <title>{% block title %}{% endblock %}</title>
</head>
<body>
  <header>ヘッダー</header>
  {% block content %}{% endblock %}
  <footer>フッター</footer>
</body>
</html>

<!-- templates/index.html -->
{% extends "base.html" %}
{% block title %}ホーム{% endblock %}
{% block content %}<h1>ホーム</h1>{% endblock %}
```
</details>

問3. ログインフォームを作成して、ユーザー名とパスワードを受け取ってください：

```python
@app.route('/login', methods=['GET', 'POST'])
def login():
    # フォーム処理を実装
    pass
```

<details>
<summary>解答を表示</summary>

```python
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        return f"{username} さんでログイン"
    return render_template('login.html')
```

```html
<!-- templates/login.html -->
<form method="POST">
  <input name="username" placeholder="ユーザー名" required>
  <input name="password" type="password" placeholder="パスワード" required>
  <button type="submit">ログイン</button>
</form>
```
</details>

問4. フォームの検証を追加して、エラーメッセージを表示してください：

```python
# フォームの検証ロジックを実装
```

<details>
<summary>解答を表示</summary>

```python
@app.route('/form', methods=['GET', 'POST'])
def form():
    errors = []
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip()
        if not name:
            errors.append('名前を入力してください')
        if not email or '@' not in email:
            errors.append('有効なメールアドレスを入力してください')
        if not errors:
            return redirect(url_for('success', name=name))
    return render_template('form.html', errors=errors)
```
</details>

問5. 条件分岐とループを使って、動的なリストを表示してください：

```html
{% for item in items %}
    {% if item.status == "active" %}
        <li>{{ item.name }}</li>
    {% endif %}
{% endfor %}
```

<details>
<summary>解答を表示</summary>

```html
<ul>
{% for item in items %}
  {% if item.status == 'active' %}
    <li>{{ item.name }}</li>
  {% endif %}
{% endfor %}
</ul>
```
</details>

## まとめ

このレッスンでは、テンプレートとフォームについて学びました。

- Jinja2テンプレートの基本
- テンプレートの継承とインクルード
- HTMLフォームの作成
- フォームデータの処理と検証
- WTFormsの基本（オプション）

次のレッスンでは、データベース（SQLite）を使って、データを永続化する方法を学びます。

