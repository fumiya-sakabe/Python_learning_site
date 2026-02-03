# デバッグの基本（printデバッグ、エラーメッセージの読み方）

## このレッスンのゴール

- `print()`文を使って、デバッグ情報を出力できる
- エラーメッセージを読んで、問題の原因を特定できる
- よくあるエラーの種類と対処法を理解できる
- デバッガーを使わずに問題を解決できる
- エラーハンドリングとデバッグの違いを理解できる

## なぜ重要なのか

デバッグは、プログラミングで最も重要なスキルの一つです。

エラーが発生したときに、エラーメッセージを読んで問題を特定できることは、開発効率に大きく影響します。

実務でも、デバッグに費やす時間は開発時間の多くを占めます。

エラーメッセージを正しく読めることで、問題解決の時間を大幅に短縮できます。

## 解説

### 1. print()デバッグの基本

変数の値を出力して、実行時の状態を確認します。

```python
def calculate_total(price, tax_rate):
    print(f"デバッグ: price={price}, tax_rate={tax_rate}")  # デバッグ出力
    tax = price * tax_rate
    print(f"デバッグ: tax={tax}")  # デバッグ出力
    total = price + tax
    print(f"デバッグ: total={total}")  # デバッグ出力
    return total

result = calculate_total(1000, 0.1)
print(f"結果: {result}")
```

### 2. よくあるエラーの種類

<strong class="term">SyntaxError（構文エラー）</strong>

```python
# コロンを忘れる
if x > 0
    print("正の数")

# 正しい書き方
if x > 0:
    print("正の数")
```

<strong class="term">IndentationError（インデントエラー）</strong>

```python
# インデントが正しくない
def greet():
print("Hello")  # エラー

# 正しい書き方
def greet():
    print("Hello")
```

<strong class="term">NameError（名前エラー）</strong>

```python
# 未定義の変数を使用
print(undefined_variable)  # エラー

# 正しい書き方
variable = "値"
print(variable)
```

<strong class="term">TypeError（型エラー）</strong>

```python
# 異なる型を結合
result = "文字列" + 123  # エラー

# 正しい書き方
result = "文字列" + str(123)
```

<strong class="term">ValueError（値エラー）</strong>

```python
# 型変換エラー
number = int("文字列")  # エラー

# 正しい書き方
number = int("123")
```

<strong class="term">IndexError（インデックスエラー）</strong>

```python
# 範囲外のインデックス
list = [1, 2, 3]
print(list[10])  # エラー

# 正しい書き方
print(list[0])  # または存在確認
if len(list) > 10:
    print(list[10])
```

<strong class="term">KeyError（キーエラー）</strong>

```python
# 存在しないキー
dict = {"name": "太郎"}
print(dict["age"])  # エラー

# 正しい書き方
print(dict.get("age", "不明"))  # デフォルト値を指定
```

### 3. エラーメッセージの読み方

Pythonのエラーメッセージには、問題の場所と原因が書かれています。

```python
# エラーが発生するコード
def divide(a, b):
    return a / b

result = divide(10, 0)
```

エラーメッセージ：

```
ZeroDivisionError: division by zero
  File "example.py", line 3, in divide
    return a / b
  File "example.py", line 5, in <module>
    result = divide(10, 0)
```

- エラーの種類: `ZeroDivisionError`
- エラーの内容: `division by zero`
- エラーが発生した場所: `example.py`の3行目と5行目

### 4. デバッグの手順

1. <strong class="highlight">エラーメッセージを読む</strong>
   - エラーの種類を確認
   - エラーが発生した場所を特定

2. <strong class="highlight">変数の値を確認</strong>
   - `print()`で変数の値を出力
   - 期待値と実際の値が一致するか確認

3. <strong class="highlight">コードの流れを追う</strong>
   - 関数の呼び出し順序を確認
   - 条件分岐の流れを確認

4. <strong class="highlight">最小限のコードで再現</strong>
   - 問題を再現する最小限のコードを作成
   - 原因を絞り込む

### 5. デバッグのテクニック

<strong class="highlight">変数の値を出力</strong>

```python
x = 10
y = 20
print(f"x={x}, y={y}")  # デバッグ出力
result = x + y
print(f"result={result}")  # デバッグ出力
```

<strong class="highlight">関数の入出力を確認</strong>

```python
def add(a, b):
    print(f"add called with: a={a}, b={b}")  # 入力確認
    result = a + b
    print(f"add returns: {result}")  # 出力確認
    return result
```

<strong class="highlight">条件分岐の流れを確認</strong>

```python
age = 20
if age >= 20:
    print("条件: age >= 20 は True")  # デバッグ出力
    print("成人です")
else:
    print("条件: age >= 20 は False")  # デバッグ出力
    print("未成年です")
```

<strong class="highlight">ループの状態を確認</strong>

```python
numbers = [1, 2, 3, 4, 5]
for i, num in enumerate(numbers):
    print(f"ループ {i}: num={num}")  # デバッグ出力
    if num > 3:
        print(f"  条件成立: num > 3")  # デバッグ出力
        break
```

### 6. よくあるエラーの対処法

<strong class="term">AttributeError（属性エラー）</strong>

```python
# Noneに属性アクセス
result = None
print(result.attribute)  # エラー

# 対処法
if result is not None:
    print(result.attribute)
```

<strong class="term">FileNotFoundError（ファイルが見つからない）</strong>

```python
# ファイルが存在しない
with open("存在しないファイル.txt") as f:
    content = f.read()

# 対処法
import os
if os.path.exists("ファイル.txt"):
    with open("ファイル.txt") as f:
        content = f.read()
```

<strong class="term">ImportError（インポートエラー）</strong>

```python
# モジュールが見つからない
import nonexistent_module  # エラー

# 対処法
try:
    import nonexistent_module
except ImportError:
    print("モジュールが見つかりません")
```

### 7. デバッグのベストプラクティス

- <strong class="highlight">エラーメッセージを必ず読む</strong>: エラーの原因が書かれている
- <strong class="highlight">print()で確認する</strong>: 変数の値や実行の流れを確認
- <strong class="highlight">小さくテストする</strong>: 問題を分割して、小さな部分をテスト
- <strong class="highlight">コメントを活用する</strong>: デバッグ用のprint文にコメントを付ける
- <strong class="highlight">ログを使う</strong>: 本格的な開発では`logging`モジュールを使う

### 8. デバッグ用のprint文を削除

デバッグが終わったら、print文を削除またはコメントアウトします。

```python
def calculate_total(price, tax_rate):
    # print(f"デバッグ: price={price}, tax_rate={tax_rate}")  # コメントアウト
    tax = price * tax_rate
    total = price + tax
    return total
```

または、条件付きで出力：

```python
DEBUG = False  # デバッグモード

def calculate_total(price, tax_rate):
    if DEBUG:
        print(f"デバッグ: price={price}, tax_rate={tax_rate}")
    tax = price * tax_rate
    total = price + tax
    return total
```

## よくある間違い

- エラーメッセージを読まずにコードを修正する
- デバッグ用のprint文を削除し忘れる
- エラーハンドリングとデバッグを混同する（エラーハンドリングはエラーを処理、デバッグはエラーを見つける）
- 全ての変数を出力しようとする（必要な箇所だけを出力）
- エラーを無視する（`except: pass`など）

## 演習課題

問1. 以下のコードのエラーを見つけて修正してください：

```python
def add(a, b):
return a + b

result = add(5, 10)
print(result)
```

<details>
<summary>解答を表示</summary>

```python
def add(a, b):
    return a + b

result = add(5, 10)
print(result)
```
</details>

問2. エラーメッセージを読んで、問題を特定してください：

```python
numbers = [1, 2, 3]
print(numbers[10])
```

<details>
<summary>解答を表示</summary>

```
IndexError: list index out of range
```
原因: インデックス10は存在しない（要素数3）。
</details>

問3. print()デバッグを使って、以下の関数の問題を特定してください：

```python
def divide_list(numbers, divisor):
    result = []
    for num in numbers:
        result.append(num / divisor)
    return result

# divide_list([10, 20, 30], 0) を実行するとどうなるか？
```

<details>
<summary>解答を表示</summary>

```python
def divide_list(numbers, divisor):
    result = []
    for num in numbers:
        print(f"num={num}, divisor={divisor}")
        result.append(num / divisor)
    return result

# 問題: divisor が 0 のとき ZeroDivisionError が発生
```
</details>

問4. エラーハンドリングを追加して、エラーメッセージを表示してください：

```python
def read_file(filename):
    with open(filename, "r") as f:
        return f.read()

# 存在しないファイルを読み込む場合のエラーを処理
```

<details>
<summary>解答を表示</summary>

```python
def read_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError as e:
        print(f"{filename} が見つかりません: {e}")
        return None
```
</details>

問5. デバッグ用のprint文を追加して、以下の関数の動作を確認してください：

```python
def find_max(numbers):
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

# print文を追加して、ループの各ステップを確認
```

<details>
<summary>解答を表示</summary>

```python
def find_max(numbers):
    max_num = numbers[0]
    for i, num in enumerate(numbers):
        print(f"i={i}, num={num}, current_max={max_num}")
        if num > max_num:
            print(f"  update: {max_num} -> {num}")
            max_num = num
    return max_num
```
</details>

## まとめ

このレッスンでは、デバッグの基本について学びました。

- `print()`を使ったデバッグ
- よくあるエラーの種類と対処法
- エラーメッセージの読み方
- デバッグの手順とテクニック
- デバッグのベストプラクティス

デバッグは経験を積むことで上達します。エラーが発生したら、エラーメッセージを読んで、一つずつ問題を解決していきましょう。

Phase1のPython基礎学習はこれで完了です。次のPhase2では、実際にミニアプリを作成していきます！

