# 学習記録アプリ

## このレッスンのゴール

- 複数のテーブルを持つデータベースを設計できる
- リレーションシップ（関連性）を理解できる
- より複雑なクエリを書ける
- 実践的なアプリケーションを作成できる
- データの集計や統計を表示できる

## なぜ重要なのか

実践的なアプリケーションでは、複数のテーブルを扱うことが一般的です。

リレーションシップを理解することで、効率的なデータベース設計ができます。

学習記録アプリを作成することで、実際のポートフォリオアプリに必要な技術を身につけられます。

ポートフォリオアプリでも、複数のテーブルを扱うスキルは重要です。

## 解説

### 1. データベースの設計

学習記録アプリのデータベース設計例：

```python
def init_db():
    conn = sqlite3.connect('learning.db')
    cursor = conn.cursor()
    
    # カテゴリテーブル
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS categories (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE
        )
    ''')
    
    # 学習記録テーブル
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS learning_records (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            category_id INTEGER,
            title TEXT NOT NULL,
            content TEXT,
            study_time INTEGER DEFAULT 0,
            date DATE NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (category_id) REFERENCES categories(id)
        )
    ''')
    
    conn.commit()
    conn.close()
```

### 2. リレーションシップの利用

JOINを使って関連データを取得します。

```python
def get_all_records():
    conn = get_db_connection()
    records = conn.execute('''
        SELECT 
            lr.id,
            lr.title,
            lr.study_time,
            lr.date,
            c.name as category_name
        FROM learning_records lr
        LEFT JOIN categories c ON lr.category_id = c.id
        ORDER BY lr.date DESC
    ''').fetchall()
    conn.close()
    return records
```

### 3. 統計情報の取得

集計関数を使って統計を計算します。

```python
def get_statistics():
    conn = get_db_connection()
    
    # 総学習時間
    total_time = conn.execute('SELECT SUM(study_time) FROM learning_records').fetchone()[0] or 0
    
    # 総記録数
    total_records = conn.execute('SELECT COUNT(*) FROM learning_records').fetchone()[0]
    
    # カテゴリ別の学習時間
    category_stats = conn.execute('''
        SELECT 
            c.name,
            SUM(lr.study_time) as total_time
        FROM categories c
        LEFT JOIN learning_records lr ON c.id = lr.category_id
        GROUP BY c.id, c.name
    ''').fetchall()
    
    conn.close()
    
    return {
        'total_time': total_time,
        'total_records': total_records,
        'category_stats': category_stats
    }
```

### 4. 日付範囲での検索

```python
def get_records_by_date_range(start_date, end_date):
    conn = get_db_connection()
    records = conn.execute('''
        SELECT * FROM learning_records
        WHERE date BETWEEN ? AND ?
        ORDER BY date DESC
    ''', (start_date, end_date)).fetchall()
    conn.close()
    return records
```

### 5. 完全なアプリケーション例

```python
from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from datetime import datetime

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('learning.db')
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS categories (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS learning_records (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            category_id INTEGER,
            title TEXT NOT NULL,
            content TEXT,
            study_time INTEGER DEFAULT 0,
            date DATE NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (category_id) REFERENCES categories(id)
        )
    ''')
    
    # サンプルカテゴリを追加
    cursor.execute('''
        INSERT OR IGNORE INTO categories (name) VALUES
        ('Python'),
        ('Flask'),
        ('データベース')
    ''')
    
    conn.commit()
    conn.close()

@app.route('/')
def index():
    conn = get_db_connection()
    records = conn.execute('''
        SELECT 
            lr.id,
            lr.title,
            lr.study_time,
            lr.date,
            c.name as category_name
        FROM learning_records lr
        LEFT JOIN categories c ON lr.category_id = c.id
        ORDER BY lr.date DESC
        LIMIT 10
    ''').fetchall()
    
    stats = get_statistics()
    
    conn.close()
    return render_template('index.html', records=records, stats=stats)

def get_statistics():
    conn = get_db_connection()
    total_time = conn.execute('SELECT SUM(study_time) FROM learning_records').fetchone()[0] or 0
    total_records = conn.execute('SELECT COUNT(*) FROM learning_records').fetchone()[0]
    conn.close()
    return {
        'total_time': total_time,
        'total_records': total_records
    }

@app.route('/create', methods=['GET', 'POST'])
def create():
    conn = get_db_connection()
    categories = conn.execute('SELECT * FROM categories').fetchall()
    
    if request.method == 'POST':
        category_id = request.form.get('category_id')
        title = request.form.get('title')
        content = request.form.get('content')
        study_time = int(request.form.get('study_time', 0))
        date = request.form.get('date')
        
        conn.execute('''
            INSERT INTO learning_records (category_id, title, content, study_time, date)
            VALUES (?, ?, ?, ?, ?)
        ''', (category_id, title, content, study_time, date))
        conn.commit()
        conn.close()
        
        return redirect(url_for('index'))
    
    conn.close()
    return render_template('create.html', categories=categories)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
```

### 6. テンプレートの例

**index.html**

```html
{% extends "base.html" %}

{% block content %}
<h1>学習記録</h1>

<div class="stats">
    <h2>統計</h2>
    <p>総学習時間: {{ stats.total_time }}分</p>
    <p>総記録数: {{ stats.total_records }}件</p>
</div>

<a href="{{ url_for('create') }}">新規記録</a>

<ul>
{% for record in records %}
    <li>
        <h3>{{ record.title }}</h3>
        <p>カテゴリ: {{ record.category_name }}</p>
        <p>学習時間: {{ record.study_time }}分</p>
        <p>日付: {{ record.date }}</p>
    </li>
{% endfor %}
</ul>
{% endblock %}
```

## よくある間違い

- リレーションシップを理解しない（JOINの使い方を間違える）
- 外部キー制約を設定しない（データの整合性が保たれない）
- 集計関数のNULL値を考慮しない（`or 0`などでデフォルト値を設定）
- 日付の形式を統一しない（データベースで日付形式を統一する）
- カテゴリの存在確認をしない（存在しないカテゴリIDを参照する）

## 演習課題

1. データベースを設計して、カテゴリと学習記録のテーブルを作成してください：

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
    conn = sqlite3.connect('learning.db')
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS categories (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE
        )
    ''')
    cur.execute('''
        CREATE TABLE IF NOT EXISTS learning_records (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            category_id INTEGER,
            title TEXT NOT NULL,
            content TEXT,
            study_time INTEGER DEFAULT 0,
            date DATE NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (category_id) REFERENCES categories(id)
        )
    ''')
    conn.commit()
    conn.close()
```
</details>

2. 学習記録を作成する機能を実装してください（カテゴリも選択できるように）：

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
    conn = get_db_connection()
    categories = conn.execute('SELECT * FROM categories').fetchall()
    if request.method == 'POST':
        category_id = request.form.get('category_id')
        title = request.form.get('title')
        content = request.form.get('content')
        study_time = int(request.form.get('study_time', 0))
        date = request.form.get('date')
        conn.execute(
            'INSERT INTO learning_records (category_id, title, content, study_time, date) VALUES (?, ?, ?, ?, ?)',
            (category_id, title, content, study_time, date)
        )
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    conn.close()
    return render_template('create.html', categories=categories)
```
</details>

3. 統計情報を表示する機能を実装してください：

   ```python
   def get_statistics():
       # 総学習時間、総記録数、カテゴリ別の統計を返す
       pass
   ```

<details>
<summary>解答を表示</summary>

```python
def get_statistics():
    conn = get_db_connection()
    total_time = conn.execute('SELECT COALESCE(SUM(study_time),0) FROM learning_records').fetchone()[0]
    total_records = conn.execute('SELECT COUNT(*) FROM learning_records').fetchone()[0]
    category_stats = conn.execute('''
        SELECT c.name, COALESCE(SUM(lr.study_time),0) AS total_time
        FROM categories c
        LEFT JOIN learning_records lr ON lr.category_id = c.id
        GROUP BY c.id, c.name
    ''').fetchall()
    conn.close()
    return {
        'total_time': total_time,
        'total_records': total_records,
        'category_stats': category_stats
    }
```
</details>

4. 日付範囲で検索する機能を実装してください：

   ```python
   @app.route('/search', methods=['GET', 'POST'])
   def search():
       # ここを実装
       pass
   ```

<details>
<summary>解答を表示</summary>

```python
from datetime import datetime

@app.route('/search', methods=['GET', 'POST'])
def search():
    records = []
    start_date = end_date = ''
    if request.method == 'POST':
        start_date = request.form.get('start')
        end_date = request.form.get('end')
        conn = get_db_connection()
        records = conn.execute(
            'SELECT * FROM learning_records WHERE date BETWEEN ? AND ? ORDER BY date DESC',
            (start_date, end_date)
        ).fetchall()
        conn.close()
    return render_template('search.html', records=records, start=start_date, end=end_date)
```
</details>

5. カテゴリ別の学習記録を表示するページを作成してください：

   ```python
   @app.route('/category/<int:category_id>')
   def category_records(category_id):
       # ここを実装
       pass
   ```

<details>
<summary>解答を表示</summary>

```python
@app.route('/category/<int:category_id>')
def category_records(category_id):
    conn = get_db_connection()
    category = conn.execute('SELECT * FROM categories WHERE id = ?', (category_id,)).fetchone()
    records = conn.execute('''
        SELECT lr.* FROM learning_records lr
        WHERE lr.category_id = ?
        ORDER BY lr.date DESC
    ''', (category_id,)).fetchall()
    conn.close()
    return render_template('category.html', category=category, records=records)
```
</details>

## まとめ

このレッスンでは、より実践的な学習記録アプリの作成について学びました。

- 複数テーブルのデータベース設計
- リレーションシップ（JOIN）の利用
- 統計情報の取得（集計関数）
- 日付範囲での検索
- 実践的なアプリケーションの作成

次のレッスンでは、Webアプリをデプロイして、インターネット上で公開する方法を学びます。

