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
<summary>解答を表示</summary>

- `add`で`due`入力を受け取り、ISO文字列で保存
- `list_todos`で`sorted(DATA, key=lambda x: (x['done'], x.get('due') or '9999'))`
</details>

2. 検索コマンドを追加し、タイトルにキーワードを含むTodoだけを表示してください。

<details>
<summary>解答を表示</summary>

- `search(keyword)`関数を追加して`[t for t in DATA if keyword.lower() in t['title'].lower()]`を表示
</details>

3. JSONではなくCSV保存に対応してください（`todos.csv`）。

<details>
<summary>解答を表示</summary>

- `csv.DictWriter`/`csv.DictReader`で入出力、ヘッダー: `id,title,done,created_at`
- 真偽値は`'1'/'0'`や`'true'/'false'`で保存して読み戻す際に変換
</details>

4. 例外処理を追加して、ファイルアクセスや数値変換エラーで落ちないようにしてください。

<details>
<summary>解答を表示</summary>

- `try/except (FileNotFoundError, ValueError, OSError)`でハンドリングし、ユーザーに再入力を促す
</details>
