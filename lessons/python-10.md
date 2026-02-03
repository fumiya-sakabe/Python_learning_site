# ファイル操作（読み書き）

## このレッスンのゴール

- ファイルを読み込んで、内容を取得できる
- ファイルに書き込んで、データを保存できる
- ファイルの存在を確認できる
- ディレクトリ（フォルダ）の操作ができる
- CSVファイルやJSONファイルを扱える

## なぜ重要なのか

ファイル操作は、データを永続化するための基本的な機能です。

アプリケーションでは、設定ファイル、ログファイル、データベースなど、ファイルを通じてデータを保存・取得することが頻繁にあります。

Webアプリでも、アップロードされたファイルの処理や、設定ファイルの読み込みなどで必要です。

ポートフォリオアプリでも、データをファイルに保存することで、アプリケーションを再起動してもデータが残ります。

## 解説

### 1. ファイルを開く

`open()`関数でファイルを開きます。

```python
# 読み込みモード（デフォルト）
file = open("example.txt", "r")

# 書き込みモード
file = open("example.txt", "w")

# 追記モード
file = open("example.txt", "a")
```

### 2. with文を使ったファイル操作

`with`文を使うと、自動的にファイルが閉じられます（推奨）。

```python
with open("example.txt", "r") as file:
    content = file.read()
    print(content)
# ファイルは自動的に閉じられる
```

### 3. ファイルを読み込む

```python
# 全て読み込む
with open("example.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print(content)

# 1行ずつ読み込む
with open("example.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line.strip())  # strip()で改行を削除

# 全ての行をリストとして取得
with open("example.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()
    for line in lines:
        print(line.strip())
```

### 4. ファイルに書き込む

```python
# 書き込みモード（既存の内容は削除される）
with open("output.txt", "w", encoding="utf-8") as file:
    file.write("Hello, World!\n")
    file.write("Python学習中")

# 追記モード（既存の内容に追加）
with open("output.txt", "a", encoding="utf-8") as file:
    file.write("\n追記された内容")
```

### 5. ファイルの存在確認

```python
import os

if os.path.exists("example.txt"):
    print("ファイルが存在します")
else:
    print("ファイルが存在しません")
```

### 6. ファイルの削除と移動

```python
import os
import shutil

# ファイルを削除
if os.path.exists("old_file.txt"):
    os.remove("old_file.txt")

# ファイルを移動（名前変更）
shutil.move("old_file.txt", "new_file.txt")

# ファイルをコピー
shutil.copy("source.txt", "destination.txt")
```

### 7. ディレクトリの操作

```python
import os

# 現在のディレクトリ
current_dir = os.getcwd()
print(current_dir)

# ディレクトリの作成
os.makedirs("new_folder", exist_ok=True)

# ディレクトリ内のファイル一覧
files = os.listdir(".")
for file in files:
    print(file)

# ディレクトリの存在確認
if os.path.isdir("folder"):
    print("ディレクトリが存在します")
```

### 8. CSVファイルの操作

```python
import csv

# CSVファイルを読み込む
with open("data.csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# CSVファイルに書き込む
data = [
    ["名前", "年齢", "都市"],
    ["太郎", "25", "東京"],
    ["花子", "30", "大阪"]
]

with open("output.csv", "w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)
```

### 9. JSONファイルの操作

```python
import json

# JSONファイルを読み込む
with open("data.json", "r", encoding="utf-8") as file:
    data = json.load(file)
    print(data)

# JSONファイルに書き込む
data = {
    "name": "太郎",
    "age": 25,
    "city": "東京"
}

with open("output.json", "w", encoding="utf-8") as file:
    json.dump(data, file, ensure_ascii=False, indent=2)
```

### 10. ファイルパスの操作

```python
import os

file_path = "folder/subfolder/file.txt"

# ディレクトリ名を取得
dir_name = os.path.dirname(file_path)  # "folder/subfolder"

# ファイル名を取得
file_name = os.path.basename(file_path)  # "file.txt"

# パスを結合
full_path = os.path.join("folder", "subfolder", "file.txt")

# 拡張子を分離
name, ext = os.path.splitext("file.txt")  # ("file", ".txt")
```

### 11. エラーハンドリング

ファイル操作では、エラーが発生する可能性があります。

```python
try:
    with open("example.txt", "r", encoding="utf-8") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("ファイルが見つかりません")
except PermissionError:
    print("ファイルへのアクセス権限がありません")
except Exception as e:
    print(f"エラーが発生しました: {e}")
```

## よくある間違い

- ファイルを閉じ忘れる（`with`文を使うと自動的に閉じられる）
- エンコーディングを指定しない（日本語が含まれる場合は`encoding="utf-8"`を指定）
- ファイルの存在確認をせずに開く（`FileNotFoundError`が発生する可能性）
- 書き込みモードで既存ファイルを開く（内容が削除される）
- CSVファイルを開く際に`newline=""`を指定しない（改行が重複する可能性）
- パスの区切り文字を直接書く（`os.path.join()`を使うとOS間で互換性がある）

## 演習課題

問1. テキストファイルに自己紹介文を書き込んで、読み込んで表示してください：

```python
# 書き込み
with open("introduction.txt", "w", encoding="utf-8") as file:
    file.write("私の名前は太郎です\n")
    file.write("Pythonを学習しています")

# 読み込み
```

<details>
<summary>解答を表示</summary>

```python
with open("introduction.txt", "w", encoding="utf-8") as f:
    f.write("私の名前は太郎です\n")
    f.write("Pythonを学習しています")

with open("introduction.txt", "r", encoding="utf-8") as f:
    print(f.read())
```
</details>

問2. CSVファイルを作成して、ユーザー情報を保存してください：

```python
users = [
    ["名前", "年齢", "都市"],
    ["太郎", "25", "東京"],
    ["花子", "30", "大阪"]
]
# CSVファイルに書き込む
```

<details>
<summary>解答を表示</summary>

```python
import csv

users = [["名前","年齢","都市"],["太郎","25","東京"],["花子","30","大阪"]]
with open("users.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(users)
```
</details>

問3. JSONファイルを作成して、設定情報を保存してください：

```python
settings = {
    "language": "ja",
    "theme": "dark",
    "notifications": True
}
# JSONファイルに書き込む
```

<details>
<summary>解答を表示</summary>

```python
import json

with open("settings.json", "w", encoding="utf-8") as f:
    json.dump(settings, f, ensure_ascii=False, indent=2)
```
</details>

問4. ファイルの存在確認をしてから読み込むプログラムを作成してください：

```python
import os

filename = "example.txt"
# 存在確認してから読み込む
```

<details>
<summary>解答を表示</summary>

```python
import os
filename = "example.txt"
if os.path.exists(filename):
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read())
else:
    print("ファイルが存在しません")
```
</details>

問5. ディレクトリ内の全てのテキストファイルを読み込んで表示してください：

```python
import os

# カレントディレクトリ内の.txtファイルを処理
```

<details>
<summary>解答を表示</summary>

```python
import os

for name in os.listdir('.'):
    if name.endswith('.txt') and os.path.isfile(name):
        with open(name, 'r', encoding='utf-8') as f:
            print(f"--- {name} ---")
            print(f.read())
```
</details>

## まとめ

このレッスンでは、ファイル操作について学びました。

- ファイルの読み書き（`open()`, `read()`, `write()`）
- `with`文を使った安全なファイル操作
- ファイルやディレクトリの操作（`os`, `shutil`モジュール）
- CSVファイルやJSONファイルの扱い方
- エラーハンドリング

次のレッスンでは、例外処理について学び、エラーを適切に処理する方法を身につけます。

