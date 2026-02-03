# 文字列操作の基礎（format, f-string, 文字列メソッド）

## このレッスンのゴール

- 文字列のフォーマット方法（`.format()`、f-string）を理解できる
- 文字列のメソッドを使って、操作や検索ができる
- 文字列のスライスを使って、部分文字列を取得できる
- 正規表現の基本（検索・置換）ができる
- 実践的な文字列処理プログラムを書ける

## なぜ重要なのか

文字列操作は、プログラミングで最も頻繁に使われる操作の一つです。

ユーザー入力の検証、データの整形、ファイル名の処理、ログメッセージの生成など、多くの場面で文字列操作が必要です。

Webアプリでも、フォームの入力チェック、URLの解析、HTMLの生成などで文字列操作は欠かせません。

ポートフォリオアプリでも、データの表示や整形に文字列操作が必要です。

## 解説

### 1. 文字列のフォーマット（.format()）

変数を文字列に埋め込みます。

```python
name = "太郎"
age = 25

# 位置指定
message = "私は{}、{}歳です".format(name, age)
print(message)  # "私は太郎、25歳です"

# インデックス指定
message = "私は{0}、{1}歳です。{0}はPythonを学習中です".format(name, age)

# キーワード指定
message = "私は{name}、{age}歳です".format(name="太郎", age=25)

# フォーマット指定
pi = 3.14159
print("円周率は{:.2f}です".format(pi))  # "円周率は3.14です"
```

### 2. f-string（Python 3.6以降）

最も読みやすく、推奨される方法です。

```python
name = "太郎"
age = 25

# 基本的な使い方
message = f"私は{name}、{age}歳です"
print(message)  # "私は太郎、25歳です"

# 式を埋め込める
x = 10
print(f"{x}の2倍は{x * 2}です")  # "10の2倍は20です"

# フォーマット指定
pi = 3.14159
print(f"円周率は{pi:.2f}です")  # "円周率は3.14です"

# 複数行の文字列
message = f"""
名前: {name}
年齢: {age}
"""
```

### 3. 文字列のメソッド

よく使う文字列のメソッド：

```python
text = "  Python学習中  "

# 大文字・小文字
print(text.upper())  # "  PYTHON学習中  "
print(text.lower())  # "  python学習中  "
print(text.capitalize())  # "  python学習中  "

# 空白の削除
print(text.strip())  # "Python学習中"
print(text.lstrip())  # "Python学習中  "
print(text.rstrip())  # "  Python学習中"

# 置換
print(text.replace("Python", "JavaScript"))  # "  JavaScript学習中  "

# 分割
text2 = "りんご,バナナ,オレンジ"
fruits = text2.split(",")
print(fruits)  # ["りんご", "バナナ", "オレンジ"]

# 結合
fruits = ["りんご", "バナナ", "オレンジ"]
text3 = ",".join(fruits)
print(text3)  # "りんご,バナナ,オレンジ"

# 検索
text4 = "Pythonは楽しい"
print(text4.startswith("Python"))  # True
print(text4.endswith("楽しい"))  # True
print(text4.find("楽しい"))  # 7（インデックス）
print(text4.count("n"))  # 2（出現回数）

# チェック
text5 = "abc123"
print(text5.isalpha())  # False（文字のみか）
print(text5.isdigit())  # False（数字のみか）
print(text5.isalnum())  # True（英数字のみか）
```

### 4. 文字列のスライス

リストと同じようにスライスできます。

```python
text = "Python学習中"

print(text[0:6])  # "Python"（0から5まで）
print(text[:6])  # "Python"（最初から5まで）
print(text[6:])  # "学習中"（6から最後まで）
print(text[-1])  # "中"（最後の文字）
print(text[::-1])  # "中習学nohtyP"（逆順）
```

### 5. 正規表現の基本

`re`モジュールを使って正規表現で文字列を処理します。

```python
import re

text = "電話番号: 090-1234-5678"

# パターンの検索
pattern = r"\d{3}-\d{4}-\d{4}"
match = re.search(pattern, text)
if match:
    print(match.group())  # "090-1234-5678"

# 全てのマッチを検索
pattern = r"\d+"
matches = re.findall(pattern, text)
print(matches)  # ['090', '1234', '5678']

# 置換
result = re.sub(r"\d+", "X", text)
print(result)  # "電話番号: X-X-X"

# マッチオブジェクト
pattern = r"(\d{3})-(\d{4})-(\d{4})"
match = re.search(pattern, text)
if match:
    print(match.group(0))  # 全体: "090-1234-5678"
    print(match.group(1))  # 1番目のグループ: "090"
    print(match.group(2))  # 2番目のグループ: "1234"
```

### 6. エスケープシーケンス

特殊文字を表現する方法です。

```python
# 改行
text = "1行目\n2行目"
print(text)

# タブ
text = "列1\t列2\t列3"
print(text)

# 引用符
text = "彼は\"こんにちは\"と言った"
text2 = '彼は\'こんにちは\'と言った'

# バックスラッシュ
text = "C:\\Users\\name"  # Windowsパス
text2 = r"C:\Users\name"  # raw文字列（エスケープ不要）
```

### 7. 文字列の検証

よく使う検証パターン：

```python
def is_email(email):
    """簡単なメールアドレス検証"""
    return "@" in email and "." in email.split("@")[1]

def is_phone(phone):
    """電話番号の検証（ハイフンあり）"""
    import re
    pattern = r"\d{3}-\d{4}-\d{4}"
    return bool(re.match(pattern, phone))
```

## よくある間違い

- f-stringで変数名を間違える（エラーになる）
- 文字列のイミュータブル性を忘れる（元の文字列は変更されない）
- 文字列と数値を直接結合しようとする（型変換が必要）
- 正規表現の特殊文字をエスケープしない（`\`が必要）
- 文字列のエンコーディングを意識しない（UTF-8を使う）
- `.format()`とf-stringを混同する（f-stringの方が推奨）

## 演習課題

問1. f-stringを使って自己紹介文を作成してください：

```python
name = "太郎"
age = 25
hobby = "読書"
# 自己紹介文を表示
```

<details>
<summary>解答を表示</summary>

```python
name = "太郎"
age = 25
hobby = "読書"
print(f"私は{name}、{age}歳です。趣味は{hobby}です。")
```
</details>

問2. 文字列のメソッドを使って、以下の処理を行ってください：
- 文字列の前後の空白を削除
- 文字列を大文字に変換
- 文字列内の特定の文字を置換

```python
text = "  Pythonは楽しい  "
# 各処理を実行
```

<details>
<summary>解答を表示</summary>

```python
text = "  Pythonは楽しい  "
print(text.strip())
print(text.upper())
print(text.replace("楽しい", "面白い"))
```
</details>

問3. カンマ区切りの文字列を分割して、各要素を処理してください：

```python
data = "りんご,バナナ,オレンジ,ぶどう"
# 分割して各要素を表示
```

<details>
<summary>解答を表示</summary>

```python
data = "りんご,バナナ,オレンジ,ぶどう"
for item in data.split(','):
    print(item)
```
</details>

問4. 正規表現を使って、文字列からメールアドレスらしき文字列を抽出してください：

```python
import re
text = "連絡先: taro@example.com または hanako@test.co.jp"
# メールアドレスを抽出
```

<details>
<summary>解答を表示</summary>

```python
import re
text = "連絡先: taro@example.com または hanako@test.co.jp"
pattern = r"[\w.+-]+@[\w-]+\.[\w.-]+"
print(re.findall(pattern, text))
```
</details>

問5. 文字列のスライスを使って、ファイル名から拡張子を取得してください：

```python
filename = "document.pdf"
# 拡張子を取得
```

<details>
<summary>解答を表示</summary>

```python
filename = "document.pdf"
print(filename.split('.')[-1])  # pdf
# もしくはスライス
print(filename[filename.rfind('.')+1:])
```
</details>

## まとめ

このレッスンでは、文字列操作の基礎について学びました。

- 文字列のフォーマット（`.format()`, f-string）
- 文字列のメソッド（`.strip()`, `.split()`, `.replace()`など）
- 文字列のスライス
- 正規表現の基本（`re`モジュール）
- エスケープシーケンス

文字列操作は頻繁に使われるので、しっかりとマスターしておきましょう。

