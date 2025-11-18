# 標準ライブラリに触れてみる（datetime, randomなど）

## このレッスンのゴール

- `datetime`モジュールで日付と時刻を扱える
- `random`モジュールで乱数を生成できる
- `collections`モジュールの便利なデータ構造を使える
- `itertools`モジュールで効率的なループ処理ができる
- 標準ライブラリのドキュメントを読める

## なぜ重要なのか

標準ライブラリは、Pythonに最初から含まれている便利なモジュールの集合です。

よく使う機能が標準ライブラリに含まれているため、追加のパッケージをインストールする必要がありません。

実務でも、標準ライブラリを活用することで、開発効率が大幅に向上します。

Webアプリでも、日付処理、ランダムなID生成、データ構造の操作などで標準ライブラリは頻繁に使われます。

## 解説

### 1. datetimeモジュール

日付と時刻を扱うモジュールです。

```python
from datetime import datetime, date, timedelta

# 現在の日時
now = datetime.now()
print(now)  # 2024-01-01 12:00:00.000000

# 日付の作成
birthday = date(2000, 1, 1)
print(birthday)  # 2000-01-01

# 日時の作成
event = datetime(2024, 1, 1, 12, 30, 0)
print(event)  # 2024-01-01 12:30:00

# 日時の加算・減算
tomorrow = datetime.now() + timedelta(days=1)
next_week = datetime.now() + timedelta(weeks=1)
last_month = datetime.now() - timedelta(days=30)

# 日時のフォーマット
formatted = now.strftime("%Y年%m月%d日 %H:%M:%S")
print(formatted)  # 2024年01月01日 12:00:00

# 文字列から日時に変換
date_str = "2024-01-01 12:00:00"
parsed = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
```

### 2. randomモジュール

乱数を生成するモジュールです。

```python
import random

# 0.0以上1.0未満の乱数
print(random.random())

# 指定範囲の整数
print(random.randint(1, 10))  # 1から10まで

# 指定範囲の浮動小数点
print(random.uniform(1.0, 10.0))

# リストからランダムに選択
fruits = ["りんご", "バナナ", "オレンジ"]
print(random.choice(fruits))

# リストから複数選択（重複なし）
print(random.sample(fruits, 2))

# リストをシャッフル
numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print(numbers)

# シードを設定（再現可能な乱数）
random.seed(42)
print(random.randint(1, 10))  # 毎回同じ値
```

### 3. collectionsモジュール

便利なデータ構造が含まれています。

```python
from collections import Counter, defaultdict, deque

# Counter: 要素の数を数える
counter = Counter([1, 2, 2, 3, 3, 3])
print(counter)  # Counter({3: 3, 2: 2, 1: 1})
print(counter.most_common(2))  # [(3, 3), (2, 2)]

# defaultdict: 存在しないキーにデフォルト値を返す辞書
dd = defaultdict(int)
dd["a"] += 1  # エラーにならない
print(dd["a"])  # 1

# deque: 両端の操作が高速なリスト
d = deque([1, 2, 3])
d.appendleft(0)  # 先頭に追加
d.append(4)  # 末尾に追加
print(d)  # deque([0, 1, 2, 3, 4])
```

### 4. itertoolsモジュール

効率的なループ処理のためのツールです。

```python
from itertools import cycle, count, combinations, permutations

# count: 無限カウンター
for i in count(start=0, step=2):
    if i > 10:
        break
    print(i)  # 0, 2, 4, 6, 8, 10

# cycle: リストを繰り返す
colors = cycle(["赤", "青", "緑"])
for _ in range(5):
    print(next(colors))  # 赤, 青, 緑, 赤, 青

# combinations: 組み合わせ
items = ["A", "B", "C"]
for combo in combinations(items, 2):
    print(combo)  # ('A', 'B'), ('A', 'C'), ('B', 'C')

# permutations: 順列
for perm in permutations(items, 2):
    print(perm)  # ('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')
```

### 5. osモジュール（再掲）

ファイルシステムの操作を行います。

```python
import os

# 現在のディレクトリ
print(os.getcwd())

# 環境変数
print(os.getenv("PATH"))

# ファイルの存在確認
print(os.path.exists("example.txt"))

# パスの操作
print(os.path.join("folder", "file.txt"))
```

### 6. jsonモジュール（再掲）

JSONデータの処理を行います。

```python
import json

# PythonオブジェクトをJSON文字列に
data = {"name": "太郎", "age": 25}
json_str = json.dumps(data, ensure_ascii=False)
print(json_str)  # {"name": "太郎", "age": 25}

# JSON文字列をPythonオブジェクトに
parsed = json.loads(json_str)
print(parsed)  # {'name': '太郎', 'age': 25}
```

### 7. reモジュール

正規表現による文字列処理を行います。

```python
import re

# パターンの検索
text = "連絡先: 090-1234-5678"
pattern = r"\d{3}-\d{4}-\d{4}"
match = re.search(pattern, text)
if match:
    print(match.group())  # 090-1234-5678

# 置換
result = re.sub(r"\d+", "X", "電話番号: 090-1234-5678")
print(result)  # "電話番号: XXX-XXXX-XXXX"
```

### 8. pathlibモジュール

パス操作をオブジェクト指向で行います（Python 3.4以降）。

```python
from pathlib import Path

# パスの作成
file_path = Path("folder") / "file.txt"
print(file_path)  # folder/file.txt

# ファイルの存在確認
print(file_path.exists())

# 拡張子の取得
print(file_path.suffix)  # .txt

# 親ディレクトリ
print(file_path.parent)  # folder
```

## よくある間違い

- 標準ライブラリのモジュールをインストールしようとする（既に含まれている）
- `datetime`と`date`を混同する（`datetime`は日時、`date`は日付のみ）
- `random`のシードを設定しない（再現性が必要な場合）
- 標準ライブラリのドキュメントを読まない（公式ドキュメントが最良の参考資料）
- 自分で実装する前に標準ライブラリを確認しない（既存の機能を使うべき）

## 演習課題

1. 現在の日時を表示し、100日後の日付を計算してください：

```python
from datetime import datetime, timedelta
# ここを実装
```

<details>
<summary>解答を表示</summary>

```python
from datetime import datetime, timedelta
now = datetime.now()
print(now)
print((now + timedelta(days=100)).date())
```
</details>

2. `random`モジュールを使って、1から6までのランダムな整数を生成してください（サイコロ）：

```python
import random
# ここを実装
```

<details>
<summary>解答を表示</summary>

```python
import random
print(random.randint(1, 6))
```
</details>

3. `Counter`を使って、リスト内の要素の出現回数を数えてください：

```python
from collections import Counter
words = ["apple", "banana", "apple", "orange", "banana", "apple"]
# 出現回数を数える
```

<details>
<summary>解答を表示</summary>

```python
from collections import Counter
words = ["apple", "banana", "apple", "orange", "banana", "apple"]
print(Counter(words))  # Counter({'apple': 3, 'banana': 2, 'orange': 1})
```
</details>

4. `itertools`を使って、3つの色から2つを選ぶ組み合わせを全て表示してください：

```python
from itertools import combinations
colors = ["赤", "青", "緑"]
# 組み合わせを表示
```

<details>
<summary>解答を表示</summary>

```python
from itertools import combinations
colors = ["赤", "青", "緑"]
for c in combinations(colors, 2):
    print(c)
```
</details>

5. `json`モジュールを使って、辞書をJSON形式のファイルに保存してください：

```python
import json
data = {
    "name": "太郎",
    "age": 25,
    "city": "東京"
}
# JSONファイルに保存
```

<details>
<summary>解答を表示</summary>

```python
import json
data = {"name": "太郎", "age": 25, "city": "東京"}
with open('output.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
```
</details>

## まとめ

このレッスンでは、標準ライブラリの主要なモジュールについて学びました。

- `datetime`: 日付と時刻の処理
- `random`: 乱数の生成
- `collections`: 便利なデータ構造
- `itertools`: 効率的なループ処理
- その他の便利なモジュール

標準ライブラリを活用することで、開発効率が大幅に向上します。公式ドキュメントを参照しながら、必要な機能を見つけていきましょう。

Phase1の基礎学習はこれで完了です。次のPhase2では、実際にミニアプリを作成していきます。

