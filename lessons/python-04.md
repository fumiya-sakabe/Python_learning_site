# 条件分岐（if, elif, else）

## このレッスンのゴール

- `if`文を使って条件に応じた処理を書ける
- `elif`と`else`を使って複数の条件分岐ができる
- 比較演算子（`==`, `!=`, `<`, `>`, `<=`, `>=`）を使える
- 論理演算子（`and`, `or`, `not`）を使って複雑な条件を書ける
- ネストした条件分岐を理解できる

## なぜ重要なのか

条件分岐は、プログラムに「判断力」を与える重要な機能です。

ユーザーの入力に応じて異なる処理を行ったり、データの値によって動作を変えたりするためには必須です。

Webアプリでも、認証状態や権限によって表示を変えたり、フォームの入力チェックを行ったりする際に頻繁に使われます。

ポートフォリオアプリでも、条件分岐は欠かせない機能です。

## 解説

### 1. if文の基本

条件が`True`のときに処理を実行します。

```python
age = 20

if age >= 20:
    print("成人です")
```

コロン（`:`）を忘れずに書きましょう。

### 2. else文

条件が`False`のときに処理を実行します。

```python
age = 18

if age >= 20:
    print("成人です")
else:
    print("未成年です")
```

### 3. elif文

複数の条件を順番にチェックします。

```python
score = 85

if score >= 90:
    print("優秀です")
elif score >= 70:
    print("良好です")
elif score >= 60:
    print("合格です")
else:
    print("不合格です")
```

### 4. 比較演算子

値同士を比較する演算子です。

```python
x = 10
y = 20

print(x == y)  # False（等しい）
print(x != y)  # True（等しくない）
print(x < y)   # True（より小さい）
print(x > y)   # False（より大きい）
print(x <= y)  # True（以下）
print(x >= y)  # False（以上）
```

文字列も比較できます：

```python
name1 = "Alice"
name2 = "Bob"

print(name1 == name2)  # False
print(name1 < name2)   # True（辞書順で比較）
```

### 5. 論理演算子

複数の条件を組み合わせます。

```python
age = 25
has_license = True

# and: 両方の条件がTrue
if age >= 20 and has_license:
    print("運転可能です")

# or: どちらか一方がTrue
if age < 18 or age >= 65:
    print("特別料金が適用されます")

# not: 条件を反転
if not has_license:
    print("免許が必要です")
```

### 6. ネストした条件分岐

条件分岐の中に条件分岐を書くことができます。

```python
age = 25
has_license = True

if age >= 20:
    if has_license:
        print("運転可能です")
    else:
        print("免許が必要です")
else:
    print("20歳未満は運転できません")
```

### 7. in演算子

リストや文字列に要素が含まれているかチェックします。

```python
fruits = ["りんご", "バナナ", "オレンジ"]

if "りんご" in fruits:
    print("りんごがあります")

# 文字列にも使える
text = "Python"
if "Py" in text:
    print("Pyを含んでいます")
```

### 8. 三項演算子（条件式）

短い条件分岐は一行で書けます。

```python
age = 20
status = "成人" if age >= 20 else "未成年"
print(status)
```

## よくある間違い

- コロン（`:`）を忘れる
- インデントが正しくない（Pythonはインデントが重要）
- `=`と`==`を混同する（`=`は代入、`==`は比較）
- 条件式に括弧を付ける（不要だが、可読性のために付けても良い）
- `elif`の代わりに`else if`と書く（Pythonでは`elif`を使う）
- 複数の条件を書くときに`and`や`or`を忘れる
- ブール値と比較するときに`== True`を書く（`if condition:`で十分）

## 演習課題

問1. 年齢に応じて料金を表示するプログラムを作成してください：
   - 12歳未満: 子供料金（500円）
   - 12歳以上18歳未満: 学生料金（800円）
   - 18歳以上65歳未満: 大人料金（1000円）
   - 65歳以上: シニア料金（800円）

   ```python
   age = 25  # 年齢を変更してテスト
   # if文で料金を表示
   ```

<details>
<summary>解答を表示</summary>

```python
age = 25
if age < 12:
    print("子供料金: 500円")
elif age < 18:
    print("学生料金: 800円")
elif age < 65:
    print("大人料金: 1000円")
else:
    print("シニア料金: 800円")
```
</details>

問2. ユーザーの入力（文字列）が「はい」か「いいえ」かで処理を分岐させてください：

   ```python
   answer = "はい"  # または "いいえ"
   # 条件分岐で異なるメッセージを表示
   ```

<details>
<summary>解答を表示</summary>

```python
answer = "はい"
if answer == "はい":
    print("実行します")
elif answer == "いいえ":
    print("中止します")
else:
    print("はい/いいえ で回答してください")
```
</details>

問3. 点数に応じて評価を表示してください：
   - 90点以上: S
   - 80点以上: A
   - 70点以上: B
   - 60点以上: C
   - 60点未満: F

   ```python
   score = 85
   # 評価を表示
   ```

<details>
<summary>解答を表示</summary>

```python
score = 85
if score >= 90:
    print("S")
elif score >= 80:
    print("A")
elif score >= 70:
    print("B")
elif score >= 60:
    print("C")
else:
    print("F")
```
</details>

問4. ユーザー名とパスワードの両方が正しい場合のみ「ログイン成功」と表示するプログラムを作成してください：

   ```python
   username = "admin"
   password = "password123"
   
   input_username = "admin"
   input_password = "password123"
   # ログイン判定
   ```

<details>
<summary>解答を表示</summary>

```python
username = "admin"
password = "password123"
input_username = "admin"
input_password = "password123"

if input_username == username and input_password == password:
    print("ログイン成功")
else:
    print("ログイン失敗")
```
</details>

## まとめ

このレッスンでは、条件分岐について学びました。

- `if`, `elif`, `else`文の使い方
- 比較演算子と論理演算子
- ネストした条件分岐
- `in`演算子や三項演算子

次のレッスンでは、繰り返し処理（`for`と`while`）を学んで、同じ処理を効率的に繰り返す方法を身につけます。

