# リスト内包表記とジェネレータ

## このレッスンのゴール

- リスト内包表記を使って、簡潔にリストを作成できる
- 条件付きリスト内包表記を書ける
- ジェネレータを作成して、メモリ効率的にデータを処理できる
- ジェネレータ式を使って、簡潔にジェネレータを作成できる
- `yield`キーワードの使い方を理解できる

## なぜ重要なのか

リスト内包表記は、Python特有の簡潔で読みやすいコードを書くための機能です。

実務でも、リスト内包表記は頻繁に使われ、コードの可読性と簡潔性を向上させます。

ジェネレータは、大量のデータを効率的に処理する際に重要です。メモリを節約しながら、データを順次処理できます。

Webアプリでも、データベースから取得した大量のレコードを処理する際にジェネレータが役立ちます。

## 解説

### 1. リスト内包表記の基本

通常のループを簡潔に書けます。

```python
# 通常の書き方
squares = []
for i in range(10):
    squares.append(i ** 2)

# リスト内包表記
squares = [i ** 2 for i in range(10)]
print(squares)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

### 2. 条件付きリスト内包表記

`if`文を使って条件を追加できます。

```python
# 偶数だけを2乗
evens_squared = [i ** 2 for i in range(10) if i % 2 == 0]
print(evens_squared)  # [0, 4, 16, 36, 64]

# 文字列のリストから特定の条件でフィルタ
words = ["apple", "banana", "cherry", "date"]
long_words = [word for word in words if len(word) > 5]
print(long_words)  # ["banana", "cherry"]
```

### 3. ネストしたリスト内包表記

複数のループを組み合わせられます。

```python
# 九九の表
table = [[i * j for j in range(1, 10)] for i in range(1, 10)]
print(table[0])  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# フラットなリストにする
flat = [i * j for i in range(1, 4) for j in range(1, 4)]
print(flat)  # [1, 2, 3, 2, 4, 6, 3, 6, 9]
```

### 4. 三項演算子との組み合わせ

条件に応じて異なる値を生成できます。

```python
numbers = [1, 2, 3, 4, 5]
result = ["偶数" if n % 2 == 0 else "奇数" for n in numbers]
print(result)  # ["奇数", "偶数", "奇数", "偶数", "奇数"]
```

### 5. 辞書内包表記

辞書も内包表記で作成できます。

```python
# キーと値のペアから辞書を作成
squares = {i: i ** 2 for i in range(5)}
print(squares)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# 条件付き
even_squares = {i: i ** 2 for i in range(5) if i % 2 == 0}
print(even_squares)  # {0: 0, 2: 4, 4: 16}
```

### 6. 集合内包表記

集合も内包表記で作成できます。

```python
# 文字列の長さの集合
words = ["apple", "banana", "cherry"]
lengths = {len(word) for word in words}
print(lengths)  # {5, 6}
```

### 7. ジェネレータ関数

`yield`キーワードでジェネレータ関数を定義します。

```python
def count_up_to(n):
    """1からnまでの数を生成"""
    count = 1
    while count <= n:
        yield count
        count += 1

# 使用例
for num in count_up_to(5):
    print(num)  # 1, 2, 3, 4, 5
```

### 8. ジェネレータ式

リスト内包表記の角括弧を丸括弧に変えるとジェネレータになります。

```python
# リスト内包表記（メモリに全てを保持）
squares_list = [i ** 2 for i in range(10)]

# ジェネレータ式（必要な時に生成）
squares_gen = (i ** 2 for i in range(10))

# 使用例
for square in squares_gen:
    print(square)  # 0, 1, 4, 9, 16, 25, 36, 49, 64, 81
```

### 9. ジェネレータのメリット

メモリ効率が良い：

```python
# リスト（全てメモリに保存）
big_list = [i ** 2 for i in range(1000000)]

# ジェネレータ（必要な時に生成）
big_gen = (i ** 2 for i in range(1000000))

# ジェネレータの方がメモリ使用量が少ない
```

### 10. `next()`関数

ジェネレータから次の値を取得できます。

```python
def count():
    n = 1
    while True:
        yield n
        n += 1

counter = count()
print(next(counter))  # 1
print(next(counter))  # 2
print(next(counter))  # 3
```

### 11. 実践例：フィボナッチ数列

```python
def fibonacci():
    """フィボナッチ数列を生成"""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# 最初の10個を取得
fib = fibonacci()
for _ in range(10):
    print(next(fib))
```

## よくある間違い

- リスト内包表記を複雑にしすぎる（可読性を損なう場合は通常のループを使う）
- ジェネレータをリストのように扱おうとする（一度しかイテレートできない）
- `yield`と`return`を混同する（`yield`は値を生成し、`return`は関数を終了）
- ジェネレータ式を変数に保存した後、再度使おうとする（一度しか使えない）
- メモリに全て保持できる場合はジェネレータを使わない（シンプルな方が良い場合もある）

## 演習課題

1. リスト内包表記を使って、1から20までの偶数を2乗したリストを作成してください：

```python
# リスト内包表記で
```

<details>
<summary>解答を表示</summary>

```python
result = [n**2 for n in range(1, 21) if n % 2 == 0]
print(result)
```
</details>

2. 文字列のリストから、5文字以上の文字列だけを大文字に変換したリストを作成してください：

```python
words = ["apple", "banana", "cat", "dog", "elephant"]
# リスト内包表記で
```

<details>
<summary>解答を表示</summary>

```python
words = ["apple", "banana", "cat", "dog", "elephant"]
result = [w.upper() for w in words if len(w) >= 5]
print(result)
```
</details>

3. 辞書内包表記を使って、1から10までの数字をキー、その2乗を値とする辞書を作成してください：

```python
# 辞書内包表記で
```

<details>
<summary>解答を表示</summary>

```python
squares = {n: n**2 for n in range(1, 11)}
print(squares)
```
</details>

4. ジェネレータ関数を作成して、1からnまでの素数を生成してください：

```python
def primes(n):
    # ここを実装
    pass
```

<details>
<summary>解答を表示</summary>

```python
def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

def primes(n):
    for x in range(2, n + 1):
        if is_prime(x):
            yield x

print(list(primes(20)))
```
</details>

5. ジェネレータ式を使って、1から100までの3の倍数を生成してください：

```python
# ジェネレータ式で
```

<details>
<summary>解答を表示</summary>

```python
gen = (n for n in range(1, 101) if n % 3 == 0)
print(list(gen))
```
</details>

## まとめ

このレッスンでは、リスト内包表記とジェネレータについて学びました。

- リスト内包表記の基本と条件付き
- 辞書内包表記と集合内包表記
- ジェネレータ関数（`yield`）
- ジェネレータ式
- メモリ効率と使い分け

これらの機能を使うことで、より簡潔で効率的なコードを書けるようになります。

