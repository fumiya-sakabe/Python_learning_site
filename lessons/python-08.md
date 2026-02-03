# 関数の基本（引数・戻り値）

## このレッスンのゴール

- 関数を定義して、再利用可能なコードを書ける
- 引数を渡して、関数にデータを伝えられる
- 戻り値を使って、関数から結果を受け取れる
- デフォルト引数や可変長引数を使える
- 関数のスコープ（変数の有効範囲）を理解できる

## なぜ重要なのか

関数は、コードを再利用可能にするための重要な機能です。

同じ処理を何度も書くのではなく、関数として定義することで、コードを整理し、保守しやすくできます。

実務でも、複雑な処理を小さな関数に分割することで、コードの可読性と保守性が向上します。

Webアプリでも、処理を関数として定義することで、コードの構造化が可能になります。

## 解説

### 1. 関数の定義

`def`キーワードを使って関数を定義します。

```python
def greet():
    print("Hello, World!")

# 関数の呼び出し
greet()
```

### 2. 引数を持つ関数

関数にデータを渡すために引数を使います。

```python
def greet(name):
    print(f"Hello, {name}!")

greet("太郎")  # "Hello, 太郎!"
```

### 3. 複数の引数

複数の引数を渡すことができます。

```python
def add(a, b):
    result = a + b
    print(f"{a} + {b} = {result}")

add(3, 5)  # "3 + 5 = 8"
```

### 4. 戻り値

`return`文で値を返すことができます。

```python
def add(a, b):
    return a + b

result = add(3, 5)
print(result)  # 8
```

### 5. 複数の戻り値

タプルを使って複数の値を返すことができます。

```python
def divide(a, b):
    quotient = a // b
    remainder = a % b
    return quotient, remainder

q, r = divide(10, 3)
print(f"商: {q}, 余り: {r}")  # "商: 3, 余り: 1"
```

### 6. デフォルト引数

引数にデフォルト値を設定できます。

```python
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("太郎")  # "Hello, 太郎!"
greet("花子", "こんにちは")  # "こんにちは, 花子!"
```

### 7. キーワード引数

引数を名前で指定できます。

```python
def introduce(name, age, city):
    print(f"私は{name}、{age}歳、{city}在住です")

introduce(name="太郎", city="東京", age=25)  # 順序を変えられる
```

### 8. 可変長引数

`*args`で任意の数の引数を受け取れます。

```python
def sum_all(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total

result = sum_all(1, 2, 3, 4, 5)
print(result)  # 15
```

### 9. キーワード可変長引数

`**kwargs`でキーワード引数を辞書として受け取れます。

```python
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="太郎", age=25, city="東京")
```

### 10. 変数のスコープ

関数内で定義した変数は、関数内でのみ有効です（ローカルスコープ）。

```python
def my_function():
    local_var = "ローカル変数"
    print(local_var)

# print(local_var)  # エラー！関数外では使えない

global_var = "グローバル変数"

def another_function():
    print(global_var)  # グローバル変数は使える

# グローバル変数を変更する場合
def modify_global():
    global global_var
    global_var = "変更されました"
```

### 11. ラムダ関数（無名関数）

簡単な関数を一行で定義できます。

```python
# 通常の関数
def add(a, b):
    return a + b

# ラムダ関数
add_lambda = lambda a, b: a + b

# 同じ結果
print(add(3, 5))  # 8
print(add_lambda(3, 5))  # 8
```

## よくある間違い

- `return`を書き忘れる（関数は値を返さずに終了する）
- 引数の順序を間違える（キーワード引数を使えば回避できる）
- グローバル変数を変更しようとしてエラーになる（`global`キーワードが必要）
- デフォルト引数に変更可能なオブジェクト（リストなど）を指定する（バグの原因になりやすい）
- 引数と戻り値の型を意識しない（型ヒントを使うと良い）
- 関数名を日本語にする（英語の方が一般的）

## 演習課題

問1. 2つの数値を引数として受け取り、その和を返す関数を作成してください：

```python
def add(a, b):
    # ここを実装
    pass
```

<details>
<summary>解答を表示</summary>

```python
def add(a, b):
    return a + b
```
</details>

問2. 文字列を受け取り、それを逆順にして返す関数を作成してください：

```python
def reverse_string(text):
    # ここを実装
    pass
```

<details>
<summary>解答を表示</summary>

```python
def reverse_string(text):
    return text[::-1]
```
</details>

問3. デフォルト引数を使って、挨拶文を表示する関数を作成してください：

```python
def greet(name, greeting="こんにちは"):
    # ここを実装
    pass
```

<details>
<summary>解答を表示</summary>

```python
def greet(name, greeting="こんにちは"):
    print(f"{greeting}, {name}!")
```
</details>

問4. 可変長引数を使って、任意の数の数値を受け取り、その平均を返す関数を作成してください：

```python
def average(*numbers):
    # ここを実装
    pass
```

<details>
<summary>解答を表示</summary>

```python
def average(*numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)
```
</details>

問5. 複数の戻り値を使って、円の面積と円周を計算する関数を作成してください：

```python
import math

def circle_info(radius):
    # ここを実装
    # 面積 = π * r^2
    # 円周 = 2 * π * r
    pass
```

<details>
<summary>解答を表示</summary>

```python
import math

def circle_info(radius):
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    return area, circumference
```
</details>

## まとめ

このレッスンでは、関数の基本について学びました。

- 関数の定義と呼び出し
- 引数と戻り値
- デフォルト引数とキーワード引数
- 可変長引数（`*args`, `**kwargs`）
- 変数のスコープ
- ラムダ関数

次のレッスンでは、モジュールとパッケージについて学び、コードをファイルに分割して管理する方法を身につけます。

