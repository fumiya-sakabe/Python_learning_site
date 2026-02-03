# SQLiteでメモアプリ

## このレッスンのゴール

- SQLiteデータベースを使って、データを永続化できる
- SQLの基本（SELECT, INSERT, UPDATE, DELETE）を理解できる
- Flaskアプリケーションからデータベースに接続できる
- CRUD操作（作成・読み取り・更新・削除）を実装できる
- 簡単なメモアプリを作成できる

## なぜ重要なのか

データベースは、データを永続化するための標準的な方法です。

SQLiteは、ファイルベースの軽量なデータベースで、小規模なアプリケーションに最適です。

実務でも、データの永続化にはデータベースが欠かせません。

ポートフォリオアプリでも、データベースを使うことで、本格的なアプリケーションを作成できます。

## 解説

### 1. SQLiteの基本

SQLiteは、Pythonに標準で含まれているデータベースです。

```python
import sqlite3

# データベースに接続（ファイルが存在しない場合は作成される）
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# テーブルの作成
cursor.execute('''
    CREATE TABLE IF NOT EXISTS memos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        content TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
''')

conn.commit()
conn.close()
```

### 2. データの挿入（INSERT）

```python
import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

cursor.execute('''
    INSERT INTO memos (title, content)
    VALUES (?, ?)
''', ('タイトル', 'メモの内容'))

conn.commit()
conn.close()
```

### 3. データの取得（SELECT）

```python
import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# 全てのメモを取得
cursor.execute('SELECT * FROM memos')
memos = cursor.fetchall()

for memo in memos:
    print(memo)

# 特定のメモを取得
cursor.execute('SELECT * FROM memos WHERE id = ?', (1,))
memo = cursor.fetchone()

conn.close()
```

### 4. データの更新（UPDATE）

```python
import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

cursor.execute('''
    UPDATE memos
    SET title = ?, content = ?
    WHERE id = ?
''', ('新しいタイトル', '新しい内容', 1))

conn.commit()
conn.close()
```

### 5. データの削除（DELETE）

```python
import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

cursor.execute('DELETE FROM memos WHERE id = ?', (1,))

conn.commit()
conn.close()
```

### 6. Flaskアプリケーションとの統合

データベース操作を関数にまとめます。

```python
import sqlite3
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row  # 辞書形式で取得
    return conn

def init_db():
    conn = get_db_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS memos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    conn = get_db_connection()
    memos = conn.execute('SELECT * FROM memos ORDER BY created_at DESC').fetchall()
    conn.close()
    return render_template('index.html', memos=memos)

@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        
        conn = get_db_connection()
        conn.execute('INSERT INTO memos (title, content) VALUES (?, ?)',
                    (title, content))
        conn.commit()
        conn.close()
        
        return redirect(url_for('index'))
    
    return render_template('create.html')

@app.route('/<int:id>/edit', methods=['GET', 'POST'])
def edit(id):
    conn = get_db_connection()
    memo = conn.execute('SELECT * FROM memos WHERE id = ?', (id,)).fetchone()
    
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        
        conn.execute('UPDATE memos SET title = ?, content = ? WHERE id = ?',
                    (title, content, id))
        conn.commit()
        conn.close()
        
        return redirect(url_for('index'))
    
    conn.close()
    return render_template('edit.html', memo=memo)

@app.route('/<int:id>/delete', methods=['POST'])
def delete(id):
    conn = get_db_connection()
    conn.execute('DELETE FROM memos WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
```

### 7. テンプレートの例

<strong class="term">index.html</strong>

```html
{% extends "base.html" %}

{% block content %}
<h1>メモ一覧</h1>
<a href="{{ url_for('create') }}">新規作成</a>

<ul>
{% for memo in memos %}
    <li>
        <h3>{{ memo.title }}</h3>
        <p>{{ memo.content }}</p>
        <small>{{ memo.created_at }}</small>
        <a href="{{ url_for('edit', id=memo.id) }}">編集</a>
        <form method="POST" action="{{ url_for('delete', id=memo.id) }}">
            <button type="submit">削除</button>
        </form>
    </li>
{% endfor %}
</ul>
{% endblock %}
```

<strong class="term">create.html</strong>

```html
{% extends "base.html" %}

{% block content %}
<h1>新規メモ</h1>
<form method="POST">
    <label for="title">タイトル:</label>
    <input type="text" id="title" name="title" required>
    
    <label for="content">内容:</label>
    <textarea id="content" name="content"></textarea>
    
    <button type="submit">作成</button>
</form>
{% endblock %}
```

### 8. SQLインジェクション対策

プレースホルダー（`?`）を使うことで、SQLインジェクションを防ぎます。

```python
# 危険（SQLインジェクションの脆弱性）
query = f"SELECT * FROM memos WHERE title = '{title}'"

# 安全（プレースホルダーを使用）
cursor.execute('SELECT * FROM memos WHERE title = ?', (title,))
```

### 9. エラーハンドリング

```python
import sqlite3

def get_db_connection():
    try:
        conn = sqlite3.connect('database.db')
        conn.row_factory = sqlite3.Row
        return conn
    except sqlite3.Error as e:
        print(f"データベースエラー: {e}")
        return None
```

### 10. データベースの初期化

アプリケーション起動時にデータベースを初期化します。

```python
if __name__ == '__main__':
    init_db()
    app.run(debug=True)
```

## よくある間違い

- SQLインジェクション対策をしない（プレースホルダーを使う）
- データベース接続を閉じない（メモリリークの原因）
- トランザクションを理解しない（`commit()`が必要）
- エラーハンドリングをしない（データベースエラーが発生する可能性）
- `row_factory`を設定しない（辞書形式で取得できない）
- データベースファイルの場所を意識しない（相対パスに注意）

## 演習課題

問1. データベースを初期化して、メモテーブルを作成してください：

```python
def init_db():
    # ここを実装
    pass
```

<details>
<summary>解答を表示</summary>

```python
import sqlite3

def init_db():
    conn = sqlite3.connect('database.db')
    conn.execute('''
        CREATE TABLE IF NOT EXISTS memos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()
```
</details>

問2. メモを作成する機能を実装してください：

```python
@app.route('/create', methods=['GET', 'POST'])
def create():
    # ここを実装
    pass
```

<details>
<summary>解答を表示</summary>

```python
@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        conn = get_db_connection()
        conn.execute('INSERT INTO memos (title, content) VALUES (?, ?)', (title, content))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    return render_template('create.html')
```
</details>

問3. メモ一覧を表示する機能を実装してください：

```python
@app.route('/')
def index():
    # ここを実装
    pass
```

<details>
<summary>解答を表示</summary>

```python
@app.route('/')
def index():
    conn = get_db_connection()
    memos = conn.execute('SELECT * FROM memos ORDER BY created_at DESC').fetchall()
    conn.close()
    return render_template('index.html', memos=memos)
```
</details>

問4. メモを編集する機能を実装してください：

```python
@app.route('/<int:id>/edit', methods=['GET', 'POST'])
def edit(id):
    # ここを実装
    pass
```

<details>
<summary>解答を表示</summary>

```python
@app.route('/<int:id>/edit', methods=['GET', 'POST'])
def edit(id):
    conn = get_db_connection()
    memo = conn.execute('SELECT * FROM memos WHERE id = ?', (id,)).fetchone()
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        conn.execute('UPDATE memos SET title = ?, content = ? WHERE id = ?', (title, content, id))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    conn.close()
    return render_template('edit.html', memo=memo)
```
</details>

問5. メモを削除する機能を実装してください：

```python
@app.route('/<int:id>/delete', methods=['POST'])
def delete(id):
    # ここを実装
    pass
```

<details>
<summary>解答を表示</summary>

```python
@app.route('/<int:id>/delete', methods=['POST'])
def delete(id):
    conn = get_db_connection()
    conn.execute('DELETE FROM memos WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))
```
</details>

## まとめ

このレッスンでは、SQLiteデータベースを使ったメモアプリの作成について学びました。

- SQLiteの基本操作（SELECT, INSERT, UPDATE, DELETE）
- Flaskアプリケーションとの統合
- CRUD操作の実装
- SQLインジェクション対策
- エラーハンドリング

次のレッスンでは、より実践的な学習記録アプリを作成していきます。

