# 例外処理（try / except）

## このレッスンのゴール

- `try`/`except`文でエラーを適切に処理できる
- 特定の例外をキャッチできる
- `finally`文でクリーンアップ処理を書ける
- 自分で例外を発生させることができる
- エラーメッセージを読んで、問題を特定できる

## なぜ重要なのか

例外処理は、エラーが発生した際にプログラムを適切に処理するための重要な機能です。

ユーザー入力の検証、ファイル操作、ネットワーク通信など、エラーが発生する可能性がある処理には例外処理が必要です。

Webアプリでも、フォームのバリデーションやAPIのエラーハンドリングで例外処理は欠かせません。

適切な例外処理を書くことで、プログラムの堅牢性とユーザー体験が向上します。

## 解説

### 1. try/except文の基本

エラーが発生する可能性がある処理を`try`ブロックに書きます。

```python
try:
    result = 10 / 0
    print(result)
except:
    print("エラーが発生しました")
```

### 2. 特定の例外をキャッチ

特定の例外だけをキャッチできます。

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("ゼロで割ることはできません")
```

### 3. 複数の例外を処理

複数の例外を別々に処理できます。

```python
try:
    num = int(input("数値を入力: "))
    result = 10 / num
    print(result)
except ValueError:
    print("数値を入力してください")
except ZeroDivisionError:
    print("ゼロで割ることはできません")
except Exception as e:
    print(f"予期しないエラー: {e}")
```

### 4. else節

例外が発生しなかった場合に実行されます。

```python
try:
    result = 10 / 2
except ZeroDivisionError:
    print("ゼロで割ることはできません")
else:
    print(f"計算結果: {result}")  # エラーがなかった場合のみ実行
```

### 5. finally節

例外の有無に関わらず必ず実行されます。

```python
try:
    file = open("example.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("ファイルが見つかりません")
finally:
    if 'file' in locals():
        file.close()  # 必ずファイルを閉じる
```

`with`文を使うと、`finally`は不要です：

```python
try:
    with open("example.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("ファイルが見つかりません")
# ファイルは自動的に閉じられる
```

### 6. 例外情報を取得

`as`キーワードで例外情報を取得できます。

```python
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"エラーが発生しました: {e}")
    print(f"エラーの型: {type(e)}")
```

### 7. 自分で例外を発生させる

`raise`文で例外を発生させます。

```python
def divide(a, b):
    if b == 0:
        raise ValueError("ゼロで割ることはできません")
    return a / b

try:
    result = divide(10, 0)
except ValueError as e:
    print(e)
```

### 8. カスタム例外の作成

自分で例外クラスを定義できます。

```python
class NegativeNumberError(Exception):
    """負の数が渡された場合の例外"""
    pass

def square_root(x):
    if x < 0:
        raise NegativeNumberError("負の数の平方根は計算できません")
    return x ** 0.5

try:
    result = square_root(-1)
except NegativeNumberError as e:
    print(e)
```

### 9. よくある例外

```python
# ZeroDivisionError: ゼロで割る
try:
    10 / 0
except ZeroDivisionError:
    pass

# ValueError: 型変換エラー
try:
    int("文字列")
except ValueError:
    pass

# FileNotFoundError: ファイルが見つからない
try:
    open("存在しないファイル.txt")
except FileNotFoundError:
    pass

# IndexError: インデックスが範囲外
try:
    list = [1, 2, 3]
    print(list[10])
except IndexError:
    pass

# KeyError: 辞書のキーが存在しない
try:
    dict = {"name": "太郎"}
    print(dict["age"])
except KeyError:
    pass
```

### 10. 例外の伝播

例外は、呼び出し元に伝播します。

```python
def function1():
    raise ValueError("エラーです")

def function2():
    function1()  # 例外が発生するが、ここでは処理しない

def function3():
    try:
        function2()
    except ValueError as e:
        print(f"エラーをキャッチ: {e}")

function3()  # "エラーをキャッチ: エラーです"
```

## よくある間違い

- `except:`だけを書く（特定の例外をキャッチすべき）
- 例外を無視してしまう（`except: pass`は避けるべき）
- 必要な例外をキャッチしない（広すぎる例外処理）
- `finally`節の使い方を間違える（クリーンアップ処理を書く）
- 例外情報を無視する（`as e`で例外情報を取得する）
- 例外を再発生させる方法を知らない（`raise`だけを書く）

## 演習課題

問1. ユーザーに数値を入力させて、ゼロ除算エラーを処理してください：

```python
try:
    num = int(input("数値を入力: "))
    result = 10 / num
    print(f"10 / {num} = {result}")
except:
    # 適切な例外処理を実装
    pass
```

<details>
<summary>解答を表示</summary>

```python
try:
    num = int(input("数値を入力: "))
    result = 10 / num
    print(f"10 / {num} = {result}")
except ValueError:
    print("数値を入力してください")
except ZeroDivisionError:
    print("ゼロで割ることはできません")
```
</details>

問2. ファイルを読み込む処理で、`FileNotFoundError`を処理してください：

```python
filename = "example.txt"
try:
    # ファイルを読み込む処理
    pass
except FileNotFoundError:
    print(f"{filename}が見つかりません")
```

<details>
<summary>解答を表示</summary>

```python
filename = "example.txt"
try:
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read())
except FileNotFoundError:
    print(f"{filename}が見つかりません")
```
</details>

問3. リストの範囲外アクセスを処理してください：

```python
numbers = [1, 2, 3]
try:
    index = int(input("インデックスを入力: "))
    print(numbers[index])
except:
    # 適切な例外処理を実装
    pass
```

<details>
<summary>解答を表示</summary>

```python
numbers = [1, 2, 3]
try:
    index = int(input("インデックスを入力: "))
    print(numbers[index])
except ValueError:
    print("数値のインデックスを入力してください")
except IndexError:
    print("範囲外のインデックスです")
```
</details>

問4. カスタム例外を作成して、負の数が渡された場合に例外を発生させてください：

```python
class NegativeError(Exception):
    pass

def factorial(n):
    if n < 0:
        raise NegativeError("負の数の階乗は計算できません")
    # 階乗の計算（簡略化）
    return 1 if n <= 1 else n * factorial(n - 1)
```

<details>
<summary>解答を表示</summary>

```python
class NegativeError(Exception):
    pass

def factorial(n):
    if n < 0:
        raise NegativeError("負の数の階乗は計算できません")
    return 1 if n <= 1 else n * factorial(n - 1)

try:
    print(factorial(-3))
except NegativeError as e:
    print(e)
```
</details>

問5. `try`/`except`/`else`/`finally`を全て使ったプログラムを作成してください：

```python
try:
    # 何かの処理
    pass
except:
    # 例外処理
    pass
else:
    # 正常終了時の処理
    pass
finally:
    # 必ず実行される処理
    pass
```

<details>
<summary>解答を表示</summary>

```python
try:
    with open("data.txt", "r", encoding="utf-8") as f:
        content = f.read()
except FileNotFoundError:
    print("data.txt が見つかりません")
else:
    print("読み込み成功:")
    print(content)
finally:
    print("処理を終了します")
```
</details>

## まとめ

このレッスンでは、例外処理について学びました。

- `try`/`except`文での例外処理
- 特定の例外のキャッチ
- `else`と`finally`節の使い方
- 例外の発生（`raise`）
- カスタム例外の作成
- よくある例外の種類

次のレッスンでは、クラスとオブジェクトについて学び、オブジェクト指向プログラミングの基礎を身につけます。

