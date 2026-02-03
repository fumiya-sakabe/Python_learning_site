# 変数と基本のデータ型（int, float, str, bool）

## このレッスンのゴール

- 変数を作成して値を保存できる
- 4つの基本データ型（int, float, str, bool）を理解し、使い分けられる
- 変数に値を代入して、計算や操作に使える
- データ型を確認する方法を覚える

## なぜ重要なのか

変数は、プログラミングの最も基本的な概念の一つです。

データを一時的に保存したり、コードを読みやすくしたり、再利用可能なプログラムを書くために必要不可欠です。

また、データ型を正しく理解することで、エラーを防ぎ、効率的なコードを書けるようになります。

実務でも、データの型を意識してプログラミングすることは重要です。

## 解説

### 1. 変数とは

変数は、データを保存するための「箱」のようなものです。

```python
name = "田中"
age = 25
height = 170.5
```

変数を使うことで、値を後から変更したり、繰り返し使ったりできます。

### 2. 整数型（int）

整数を扱うデータ型です。

```python
age = 25
count = 100
temperature = -10

print(type(age))  # <class 'int'>
```

### 3. 浮動小数点型（float）

小数を含む数値を扱うデータ型です。

```python
height = 170.5
price = 99.99
pi = 3.14159

print(type(height))  # <class 'float'>
```

整数と浮動小数点の計算結果は浮動小数点になります：

```python
result = 5 / 2
print(result)  # 2.5
print(type(result))  # <class 'float'>
```

### 4. 文字列型（str）

文字列を扱うデータ型です。シングルクォートまたはダブルクォートで囲みます。

```python
name = "Python"
message = 'Hello, World!'
multiline = """複数行の
文字列も
書けます"""

print(type(name))  # <class 'str'>
```

文字列の連結：

```python
first_name = "太郎"
last_name = "山田"
full_name = first_name + last_name
print(full_name)  # 太郎山田
```

### 5. ブール型（bool）

真偽値（TrueまたはFalse）を扱うデータ型です。

```python
is_student = True
is_adult = False

print(type(is_student))  # <class 'bool'>
```

比較演算子の結果はブール型になります：

```python
age = 20
is_adult = age >= 20
print(is_adult)  # True
```

### 6. 型の確認と変換

`type()`関数で型を確認できます：

```python
value = 42
print(type(value))  # <class 'int'>
```

型を変換する関数：

```python
# 文字列→整数
number_str = "42"
number = int(number_str)

# 整数→文字列
age = 25
age_str = str(age)

# 文字列→浮動小数点
pi_str = "3.14"
pi = float(pi_str)

# 数値→ブール型（0以外はTrue、0はFalse）
print(bool(1))  # True
print(bool(0))  # False
```

### 7. 変数の命名規則

変数名には以下のルールがあります：

```python
# 良い例
user_name = "太郎"
user_age = 25
is_active = True

# 悪い例（エラーになる）
# 2name = "太郎"  # 数字で始められない
# user-name = "太郎"  # ハイフンは使えない
# class = "A"  # 予約語は使えない
```

## よくある間違い

- 文字列と数値を直接計算しようとする（型を揃える必要がある）
- 変数を宣言せずに使おうとする（変数は必ず値を代入してから使う）
- 変数名に日本語を使う（英語の方が一般的）
- `=`と`==`を混同する（`=`は代入、`==`は比較）
- 文字列のクォートを閉じ忘れる（シンタックスエラーになる）
- `True`と`False`の最初の文字を小文字で書く（大文字で始める必要がある）

## 演習課題

問1. 以下の変数を作成して、それぞれの型を確認してください：
   - 年齢（整数）
   - 身長（浮動小数点）
   - 名前（文字列）
   - 学生かどうか（ブール型）

   ```python
   age = 25
   height = 170.5
   name = "あなたの名前"
   is_student = True
   
   # それぞれの型を表示
   ```

<details>
<summary>解答を表示</summary>

```python
age = 25
height = 170.5
name = "山田太郎"
is_student = True

print(type(age))       # <class 'int'>
print(type(height))    # <class 'float'>
print(type(name))      # <class 'str'>
print(type(is_student))# <class 'bool'>
```
</details>

問2. 変数を使って簡単な計算をしてください：

```python
price = 1000
tax_rate = 0.1
# 税込み価格を計算して表示
```

<details>
<summary>解答を表示</summary>

```python
price = 1000
tax_rate = 0.1
total = int(price * (1 + tax_rate))
print(total)  # 1100
```
</details>

問3. 文字列を連結して自己紹介文を作成してください：

```python
first_name = "太郎"
last_name = "山田"
# フルネームを作成して表示
```

<details>
<summary>解答を表示</summary>

```python
first_name = "太郎"
last_name = "山田"
full_name = first_name + last_name
print(full_name)
print(f"私の名前は{full_name}です")
```
</details>

問4. 型変換を使って、文字列の数字を整数に変換して計算してください：

```python
num1_str = "10"
num2_str = "20"
# 型変換して足し算の結果を表示
```

<details>
<summary>解答を表示</summary>

```python
num1_str = "10"
num2_str = "20"
result = int(num1_str) + int(num2_str)
print(result)  # 30
```
</details>

## まとめ

このレッスンでは、変数と基本データ型について学びました。

- 変数を使って値を保存する方法
- 4つの基本データ型（int, float, str, bool）
- 型の確認方法（`type()`関数）
- 型の変換方法

次のレッスンでは、条件分岐（if文）を使って、プログラムの流れを制御する方法を学びます。

