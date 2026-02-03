# 繰り返し処理（for, while）

## このレッスンのゴール

- `for`文を使ってリストなどの要素を繰り返し処理できる
- `while`文を使って条件が真の間処理を繰り返せる
- `range()`関数を使って数値の範囲を生成できる
- `break`と`continue`でループを制御できる
- ネストしたループを理解できる

## なぜ重要なのか

繰り返し処理は、プログラミングの基本的な制御構造の一つです。

同じ処理を何度も書くのではなく、ループを使うことでコードを簡潔に、そして保守しやすくできます。

Webアプリでは、リストのデータを表示したり、データベースから取得した複数のレコードを処理したりする際に必須です。

ポートフォリオアプリでも、繰り返し処理は頻繁に使われます。

## 解説

### 1. for文の基本

リストなどの要素を順番に処理します。

```python
fruits = ["りんご", "バナナ", "オレンジ"]

for fruit in fruits:
    print(fruit)
```

### 2. range()関数

数値の範囲を生成して繰り返し処理します。

```python
# 0から9まで（10回繰り返し）
for i in range(10):
    print(i)

# 1から10まで
for i in range(1, 11):
    print(i)

# 2ずつ増やす（2, 4, 6, 8, 10）
for i in range(2, 11, 2):
    print(i)
```

### 3. enumerate()関数

インデックスと要素の両方を取得できます。

```python
fruits = ["りんご", "バナナ", "オレンジ"]

for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
```

### 4. while文の基本

条件が`True`の間、処理を繰り返します。

```python
count = 0

while count < 5:
    print(count)
    count += 1
```

### 5. break文

ループを途中で終了します。

```python
for i in range(10):
    if i == 5:
        break
    print(i)  # 0から4まで表示
```

### 6. continue文

現在の繰り返しをスキップして、次の繰り返しに進みます。

```python
for i in range(10):
    if i % 2 == 0:  # 偶数ならスキップ
        continue
    print(i)  # 奇数だけ表示（1, 3, 5, 7, 9）
```

### 7. else節

ループが正常に終了した場合（`break`されなかった場合）に実行されます。

```python
for i in range(5):
    print(i)
else:
    print("ループが完了しました")

# breakされた場合はelseは実行されない
for i in range(5):
    if i == 3:
        break
    print(i)
else:
    print("これは表示されません")
```

### 8. ネストしたループ

ループの中にループを書くことができます。

```python
# 九九の表
for i in range(1, 10):
    for j in range(1, 10):
        print(f"{i} × {j} = {i * j}")
```

### 9. 無限ループとその回避

`while True:`は無限ループになりますが、`break`で抜けることができます。

```python
while True:
    user_input = input("終了するには 'q' を入力: ")
    if user_input == 'q':
        break
    print("続行します...")
```

## よくある間違い

- `for`文で変数名を定義し忘れる（`for in fruits:` → `for fruit in fruits:`）
- `while`文で条件を更新し忘れて無限ループになる（カウンターを増やすのを忘れる）
- インデントを間違える（ループの中の処理はインデントが必要）
- `range()`の引数を間違える（`range(10)`は0から9まで）
- `break`と`continue`の違いを混同する（`break`は終了、`continue`は次へ）
- 文字列を`for`で回すとき、文字ごとに処理されることを忘れる

## 演習課題

問1. 1から10までの数字を`for`文で表示してください。

```python
# for文とrange()を使う
```

<details>
<summary>解答を表示</summary>

```python
for i in range(1, 11):
    print(i)
```
</details>

問2. リスト`[1, 2, 3, 4, 5]`の各要素を2倍して表示してください。

```python
numbers = [1, 2, 3, 4, 5]
# for文で各要素を2倍して表示
```

<details>
<summary>解答を表示</summary>

```python
numbers = [1, 2, 3, 4, 5]
for n in numbers:
    print(n * 2)
```
</details>

問3. `while`文を使って、1から100までの合計を計算してください。

```python
total = 0
count = 1
# while文で合計を計算
```

<details>
<summary>解答を表示</summary>

```python
total = 0
count = 1
while count <= 100:
    total += count
    count += 1
print(total)  # 5050
```
</details>

問4. 1から20までの数字で、3の倍数だけを表示してください（`continue`を使う）。

```python
# for文とcontinueを使って
```

<details>
<summary>解答を表示</summary>

```python
for i in range(1, 21):
    if i % 3 != 0:
        continue
    print(i)
```
</details>

問5. 九九の表を表示してください（ネストしたループ）。

```python
# ネストしたfor文で九九を表示
```

<details>
<summary>解答を表示</summary>

```python
for i in range(1, 10):
    for j in range(1, 10):
        print(f"{i}×{j}={i*j}", end=' ')
    print()
```
</details>

問6. ユーザーが正しい答えを入力するまで繰り返すプログラムを作成してください：

```python
answer = 42
# while文とinput()を使って
```

<details>
<summary>解答を表示</summary>

```python
answer = 42
while True:
    try:
        n = int(input('答えを入力: '))
    except ValueError:
        print('数値で入力してください')
        continue
    if n == answer:
        print('正解！')
        break
    else:
        print('不正解。もう一度。')
```
</details>

## まとめ

このレッスンでは、繰り返し処理について学びました。

- `for`文でリストや`range()`を繰り返し処理
- `while`文で条件が真の間処理を繰り返し
- `break`と`continue`でループを制御
- ネストしたループや`enumerate()`の使い方

次のレッスンでは、リストとタプルというデータ構造について詳しく学びます。

