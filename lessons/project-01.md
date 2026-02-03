# ミニアプリ: コマンドラインTodoリスト

## このプロジェクトのゴール

- ファイル入出力を使ってTodoを永続化できる
- 追加・一覧・完了・削除といった基本的な操作を実装できる
- コマンドライン引数やメニュー式のUIを実装できる

## 概要

小さなCLIアプリとしてTodoリストを作成します。データは`todos.csv`や`todos.json`に保存します。

## 要件

- Todoは「ID」「タイトル」「状態(done or not)」「作成日時」を持つ
- コマンド/メニュー:
  - 追加: 新しいTodoを追加
  - 一覧: 未完了を優先して表示（完了は最後に）
  - 完了: 指定IDを完了にする
  - 削除: 指定IDを削除
  - 保存/読み込み: 起動時に読み込み、終了時に保存（自動でもOK）

## 実装ステップ

1. データ構造を決める（辞書 or dataclass）
2. 追加/一覧を先に作る
3. 完了/削除を追加
4. CSVまたはJSONで永続化

## サンプルコード（最小）

```python
# todo_app.py（例）
import json
from datetime import datetime

DATA = []
FILE = 'todos.json'


def load():
    global DATA
    try:
        with open(FILE, 'r', encoding='utf-8') as f:
            DATA = json.load(f)
    except FileNotFoundError:
        DATA = []


def save():
    with open(FILE, 'w', encoding='utf-8') as f:
        json.dump(DATA, f, ensure_ascii=False, indent=2)


def add(title: str):
    _id = (max([t['id'] for t in DATA]) + 1) if DATA else 1
    DATA.append({
        'id': _id,
        'title': title,
        'done': False,
        'created_at': datetime.now().isoformat(timespec='seconds')
    })


def list_todos():
    for t in sorted(DATA, key=lambda x: (x['done'], x['id'])):
        mark = '✅' if t['done'] else '⬜'
        print(f"{t['id']:>2} {mark} {t['title']} ({t['created_at']})")


def complete(_id: int):
    for t in DATA:
        if t['id'] == _id:
            t['done'] = True
            return True
    return False


def remove(_id: int):
    global DATA
    before = len(DATA)
    DATA = [t for t in DATA if t['id'] != _id]
    return len(DATA) != before


def main():
    load()
    while True:
        cmd = input('\n[1]追加 [2]一覧 [3]完了 [4]削除 [0]終了 > ').strip()
        if cmd == '1':
            title = input('タイトル: ').strip()
            if title:
                add(title)
                save()
        elif cmd == '2':
            list_todos()
        elif cmd == '3':
            _id = int(input('完了にするID: '))
            if complete(_id):
                save()
        elif cmd == '4':
            _id = int(input('削除するID: '))
            if remove(_id):
                save()
        elif cmd == '0':
            save()
            break

if __name__ == '__main__':
    main()
```

## 演習課題

1. 期限(due)フィールドを追加し、期限が近い順に並べ替えて表示してください。

<details>
<summary>💡 解答を見る</summary>

解答：

期限フィールドを追加するには、`add`関数で期限入力を受け取り、`list_todos`関数で期限順に並べ替えます。

実装例：

```python
def add(title: str, due: str = None):
    _id = (max([t['id'] for t in DATA]) + 1) if DATA else 1
    DATA.append({
        'id': _id,
        'title': title,
        'done': False,
        'due': due,  # 期限を追加
        'created_at': datetime.now().isoformat(timespec='seconds')
    })

def list_todos():
    # 未完了を優先し、期限内順に並べ替え
    for t in sorted(DATA, key=lambda x: (x['done'], x.get('due') or '9999')):
        mark = '✅' if t['done'] else '⬜'
        due_str = f" [期限: {t.get('due', '未設定')}]" if t.get('due') else ""
        print(f"{t['id']:>2} {mark} {t['title']}{due_str} ({t['created_at']})")

# 使用例
add("レポート作成", due="2025-12-31")
```

ポイント：
- `due`が`None`の場合は`'9999'`として扱い、最後に表示
- `sorted`の`key`で`done`（完了状態）を先に比較し、その次に`due`（期限）で比較

</details>

2. 検索コマンドを追加し、タイトルにキーワードを含むTodoだけを表示してください。

<details>
<summary>💡 解答を見る</summary>

解答：

検索関数を追加し、タイトルにキーワードを含むTodoだけをフィルタリングして表示します。

実装例：

```python
def search(keyword: str):
    """タイトルにキーワードを含むTodoを検索"""
    results = [t for t in DATA if keyword.lower() in t['title'].lower()]
    if not results:
        print(f"「{keyword}」を含むTodoが見つかりませんでした。")
        return
    
    print(f"\n「{keyword}」を含むTodo:")
    for t in sorted(results, key=lambda x: (x['done'], x['id'])):
        mark = '✅' if t['done'] else '⬜'
        print(f"{t['id']:>2} {mark} {t['title']}")

# main関数に追加
def main():
    load()
    while True:
        cmd = input('\n[1]追加 [2]一覧 [3]完了 [4]削除 [5]検索 [0]終了 > ').strip()
        # ... 既存のコード ...
        elif cmd == '5':
            keyword = input('検索キーワード: ').strip()
            if keyword:
                search(keyword)
```

ポイント：
- `keyword.lower()`で大文字小文字を区別せずに検索
- 検索結果が見つからない場合のメッセージを表示

</details>

3. JSONではなくCSV保存に対応してください（`todos.csv`）。

<details>
<summary>💡 解答を見る</summary>

解答：

`csv`モジュールを使ってCSV形式でデータを保存・読み込みます。真偽値は文字列として保存し、読み込み時に変換します。

実装例：

```python
import csv
# JSONのインポートを削除（または併用可）

FILE = 'todos.csv'

def load():
    """CSVからデータを読み込む"""
    global DATA
    DATA = []
    try:
        with open(FILE, 'r', encoding='utf-8', newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                # 文字列の'True'/'False'を真偽値に変換
                row['done'] = row['done'] == 'True'
                row['id'] = int(row['id'])
                DATA.append(row)
    except FileNotFoundError:
        DATA = []

def save():
    """CSVにデータを保存"""
    with open(FILE, 'w', encoding='utf-8', newline='') as f:
        if not DATA:
            return
        fieldnames = ['id', 'title', 'done', 'created_at']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for t in DATA:
            # 真偽値を文字列に変換
            row = t.copy()
            row['done'] = str(row['done'])  # True -> 'True', False -> 'False'
            writer.writerow(row)
```

ポイント：
- `csv.DictWriter`で辞書をCSVに書き込み
- `csv.DictReader`でCSVを辞書として読み込み
- 真偽値は`'True'`/`'False'`として保存し、読み込み時に`== 'True'`で変換
- `newline=''`を指定して改行の重複を防ぐ

</details>

4. 例外処理を追加して、ファイルアクセスや数値変換エラーで落ちないようにしてください。

<details>
<summary>💡 解答を見る</summary>

解答：

ファイルアクセスや数値変換などのエラーを`try/except`でキャッチし、適切なエラーメッセージを表示してプログラムが止まらないようにします。

実装例：

```python
def load():
    """CSVからデータを読み込む（例外処理付き）"""
    global DATA
    DATA = []
    try:
        with open(FILE, 'r', encoding='utf-8', newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                row['done'] = row['done'] == 'True'
                row['id'] = int(row['id'])
                DATA.append(row)
    except FileNotFoundError:
        DATA = []  # ファイルがなければ空リスト
    except (ValueError, OSError) as e:
        print(f"⚠️ ファイル読み込みエラー: {e}")
        DATA = []

def main():
    load()
    while True:
        cmd = input('\n[1]追加 [2]一覧 [3]完了 [4]削除 [0]終了 > ').strip()
        # ... 既存のコード ...
        elif cmd == '3':
            try:
                _id = int(input('完了にするID: '))
                if complete(_id):
                    save()
                else:
                    print(f"⚠️ ID {_id} が見つかりませんでした。")
            except ValueError:
                print("⚠️ 数値を入力してください。")
        elif cmd == '4':
            try:
                _id = int(input('削除するID: '))
                if remove(_id):
                    save()
                else:
                    print(f"⚠️ ID {_id} が見つかりませんでした。")
            except ValueError:
                print("⚠️ 数値を入力してください。")
```

ポイント：
- `FileNotFoundError`: ファイルが存在しない場合（初回実行時など）
- `ValueError`: 数値変換エラー（文字列を`int()`に変換できない場合）
- `OSError`: ファイルアクセスエラー
- エラー時は適切なメッセージを表示し、プログラムは続行

</details>







