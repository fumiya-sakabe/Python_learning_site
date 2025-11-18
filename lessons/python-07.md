# 辞書と集合

## このレッスンのゴール

- 辞書を作成して、キーと値のペアでデータを管理できる
- 辞書の要素にアクセスして、追加・削除・変更ができる
- 集合を作成して、重複のないデータを管理できる
- 辞書と集合の操作メソッドを理解できる
- データ構造の使い分けができる

## なぜ重要なのか

辞書は、キーと値を対応付けてデータを管理する重要なデータ構造です。

ユーザーの設定、JSONデータ、データベースのレコードなど、多くの場面で辞書形式でデータが扱われます。

Webアプリでも、フォームデータやAPIのレスポンスなどが辞書形式で扱われることが多いです。

集合は、重複を除去したり、集合演算を行ったりする際に便利です。

## 解説

### 1. 辞書の作成

辞書は波括弧`{}`で作成し、キーと値をコロン（`:`）で区切ります。

```python
person = {
    "name": "太郎",
    "age": 25,
    "city": "東京"
}

# 空の辞書
empty = {}

# dict()関数でも作成可能
person2 = dict(name="花子", age=30)
```

### 2. 辞書の要素にアクセス

キーを使って値を取得します。

```python
person = {"name": "太郎", "age": 25}

print(person["name"])  # "太郎"
print(person.get("age"))  # 25
print(person.get("city", "不明"))  # "不明"（キーが存在しない場合のデフォルト値）

# キーの存在確認
if "name" in person:
    print(person["name"])
```

### 3. 辞書の要素を変更・追加

```python
person = {"name": "太郎", "age": 25}

person["age"] = 26  # 変更
person["city"] = "東京"  # 追加
```

### 4. 辞書の要素を削除

```python
person = {"name": "太郎", "age": 25, "city": "東京"}

del person["city"]  # キーを指定して削除
value = person.pop("age")  # 削除して値を返す
person.clear()  # 全て削除
```

### 5. 辞書のメソッド

```python
person = {"name": "太郎", "age": 25}

# キーの一覧
keys = person.keys()

# 値の一覧
values = person.values()

# キーと値のペア
items = person.items()

# 辞書をループ処理
for key, value in person.items():
    print(f"{key}: {value}")

# 辞書のコピー
person_copy = person.copy()
```

### 6. 辞書の更新

```python
person = {"name": "太郎", "age": 25}
person.update({"age": 26, "city": "東京"})
```

### 7. 集合の作成

集合は波括弧`{}`で作成します（辞書と同じ記号ですが、値のみ）。

```python
fruits = {"りんご", "バナナ", "オレンジ"}
numbers = {1, 2, 3, 4, 5}

# 空の集合（波括弧だけだと辞書になるため、set()を使う）
empty = set()

# リストから集合を作成（重複が自動的に除去される）
numbers_list = [1, 2, 2, 3, 3, 4]
unique_numbers = set(numbers_list)  # {1, 2, 3, 4}
```

### 8. 集合の操作

```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# 和集合（どちらかに含まれる要素）
union = set1 | set2  # {1, 2, 3, 4, 5}
union = set1.union(set2)

# 積集合（両方に含まれる要素）
intersection = set1 & set2  # {3}
intersection = set1.intersection(set2)

# 差集合（set1にあってset2にない要素）
difference = set1 - set2  # {1, 2}
difference = set1.difference(set2)

# 対称差集合（どちらか一方にだけ含まれる要素）
symmetric = set1 ^ set2  # {1, 2, 4, 5}
symmetric = set1.symmetric_difference(set2)
```

### 9. 集合のメソッド

```python
fruits = {"りんご", "バナナ"}

# 要素を追加
fruits.add("オレンジ")

# 要素を削除
fruits.remove("バナナ")  # キーが存在しないとエラー
fruits.discard("バナナ")  # キーが存在しなくてもエラーにならない

# 要素の存在確認
if "りんご" in fruits:
    print("りんごがあります")

# 要素数を取得
print(len(fruits))
```

### 10. データ構造の使い分け

- **リスト**: 順序が重要、重複可能、変更可能
- **タプル**: 順序が重要、重複可能、変更不可
- **辞書**: キーでアクセス、変更可能、キーは重複不可
- **集合**: 順序なし、重複不可、変更可能

## よくある間違い

- 辞書のキーにリストを使おうとする（リストは変更可能なので辞書のキーに使えない）
- 存在しないキーにアクセスしてエラーになる（`get()`メソッドや`in`演算子を使う）
- 集合を作る際に空の波括弧`{}`を使う（辞書になってしまう、`set()`を使う）
- 辞書と集合を混同する（辞書はキーと値のペア、集合は値のみ）
- 集合にリストを追加しようとする（集合には変更不可能な要素しか追加できない）
- 辞書の順序を前提にした処理を書く（Python 3.7以降は順序が保証されるが、古いバージョンでは注意）

## 演習課題

1. 辞書を作成して、ユーザー情報を保存してください：

```python
user = {
    "name": "太郎",
    "age": 25,
    "email": "taro@example.com"
}
# 年齢を変更
# 新しいキー"city"を追加
# 全てのキーと値を表示
```

<details>
<summary>解答を表示</summary>

```python
user = {"name": "太郎", "age": 25, "email": "taro@example.com"}
user["age"] = 26
user["city"] = "東京"
for k, v in user.items():
    print(k, v)
```
</details>

2. 辞書のループ処理を使って、全てのキーと値を表示してください：

```python
scores = {"数学": 85, "英語": 90, "国語": 78}
# for文で全て表示
```

<details>
<summary>解答を表示</summary>

```python
scores = {"数学": 85, "英語": 90, "国語": 78}
for subject, score in scores.items():
    print(f"{subject}: {score}")
```
</details>

3. 集合を使って、重複を除去してください：

```python
numbers = [1, 2, 2, 3, 3, 4, 5, 5]
# 集合に変換して重複を除去
```

<details>
<summary>解答を表示</summary>

```python
numbers = [1, 2, 2, 3, 3, 4, 5, 5]
unique = set(numbers)
print(unique)  # {1,2,3,4,5}
```
</details>

4. 2つの集合の和集合、積集合、差集合を計算してください：

```python
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
# 各演算の結果を表示
```

<details>
<summary>解答を表示</summary>

```python
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print(set1 | set2)  # 和集合
print(set1 & set2)  # 積集合
print(set1 - set2)  # 差集合
```
</details>

5. 辞書を使って、単語と意味の対応を作成してください（辞書型の辞書）：

```python
dictionary = {
    "python": "プログラミング言語の名前",
    "list": "複数の要素を順番に並べたデータ構造"
}
# 単語を検索する機能を実装
```

<details>
<summary>解答を表示</summary>

```python
dictionary = {
    "python": "プログラミング言語の名前",
    "list": "複数の要素を順番に並べたデータ構造"
}
word = "python"
meaning = dictionary.get(word, "未登録の単語です")
print(meaning)
```
</details>

## まとめ

このレッスンでは、辞書と集合について学びました。

- 辞書の作成、要素へのアクセス、変更
- 辞書のメソッド（`keys()`, `values()`, `items()`など）
- 集合の作成と操作（和集合、積集合、差集合）
- データ構造の使い分け

次のレッスンでは、関数の基本について学び、コードを再利用可能にする方法を身につけます。

