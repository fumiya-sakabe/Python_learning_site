# モジュールとパッケージ

## このレッスンのゴール

- モジュールをインポートして、他のファイルのコードを使える
- 自分でモジュールを作成できる
- パッケージの構造を理解できる
- 標準ライブラリのモジュールを使える
- サードパーティのパッケージをインストールできる

## なぜ重要なのか

モジュールとパッケージは、コードを整理し、再利用するための重要な機能です。

実務では、コードを複数のファイルに分割して管理することが一般的です。

Webアプリでも、機能ごとにモジュールを分けることで、コードの保守性が向上します。

標準ライブラリやサードパーティのパッケージを活用することで、開発効率が大幅に向上します。

## 解説

### 1. モジュールのインポート

他のファイルのコードを使うためにインポートします。

```python
import math

result = math.sqrt(16)
print(result)  # 4.0
```

### 2. 特定の関数やクラスをインポート

必要な部分だけをインポートできます。

```python
from math import sqrt, pi

result = sqrt(16)
print(pi)  # 3.141592653589793
```

### 3. エイリアス（別名）を使う

`as`キーワードで別名を付けることができます。

```python
import math as m

result = m.sqrt(16)
```

### 4. 全てをインポート（非推奨）

`from module import *`は避けるべきです（名前の衝突が起きやすい）。

```python
# 非推奨
from math import *

# 推奨
import math
# または
from math import sqrt, pi
```

### 5. 自分でモジュールを作成

`my_module.py`というファイルを作成します。

```python
# my_module.py
def greet(name):
    return f"Hello, {name}!"

PI = 3.14159

class Calculator:
    def add(self, a, b):
        return a + b
```

別のファイルからインポート：

```python
import my_module

result = my_module.greet("太郎")
calc = my_module.Calculator()
```

### 6. モジュールの`__name__`

モジュールが直接実行されたか、インポートされたかを判定できます。

```python
# my_module.py
def greet(name):
    return f"Hello, {name}!"

if __name__ == "__main__":
    # このファイルが直接実行された場合のみ実行
    print(greet("World"))
```

### 7. パッケージの構造

パッケージは複数のモジュールを含むフォルダです。

```
my_package/
    __init__.py
    module1.py
    module2.py
    subpackage/
        __init__.py
        module3.py
```

### 8. `__init__.py`ファイル

パッケージであることを示すために`__init__.py`が必要です（Python 3.3以降は空でも可）。

```python
# my_package/__init__.py
from .module1 import function1
from .module2 import Class1

__all__ = ['function1', 'Class1']
```

### 9. 相対インポートと絶対インポート

```python
# 絶対インポート
from my_package.module1 import function1

# 相対インポート（同じパッケージ内）
from .module2 import Class1
from ..parent_package import something
```

### 10. よく使う標準ライブラリモジュール

```python
# datetime: 日付と時刻
from datetime import datetime
now = datetime.now()

# random: 乱数
import random
number = random.randint(1, 10)

# os: オペレーティングシステム関連
import os
current_dir = os.getcwd()

# sys: システム固有のパラメータ
import sys
print(sys.version)

# json: JSONデータの処理
import json
data = json.loads('{"name": "太郎"}')
```

### 11. サードパーティパッケージのインストール

`pip`を使ってインストールします。

```bash
pip install requests
```

Pythonコードから使用：

```python
import requests
response = requests.get("https://api.example.com")
```

## よくある間違い

- モジュール名と変数名が衝突する（変数名にモジュール名を使わない）
- 循環インポート（モジュールAがBをインポートし、BがAをインポートする）
- インポートパスが間違っている（相対パスと絶対パスの違いを理解する）
- `__init__.py`を忘れる（パッケージとして認識されない）
- `from module import *`を使う（名前の衝突が起きやすい）
- モジュールの実行とインポートを混同する（`if __name__ == "__main__"`を使う）

## 演習課題

問1. `math`モジュールを使って、円の面積を計算する関数を作成してください：

```python
import math

def circle_area(radius):
    # ここを実装（面積 = π * r^2）
    pass
```

<details>
<summary>解答を表示</summary>

```python
import math

def circle_area(radius):
    return math.pi * radius ** 2
```
</details>

問2. `datetime`モジュールを使って、現在の日時を表示してください：

```python
from datetime import datetime
# 現在の日時を表示
```

<details>
<summary>解答を表示</summary>

```python
from datetime import datetime
print(datetime.now())
# 例: 2025-11-16 21:30:00.123456
```
</details>

問3. `random`モジュールを使って、1から100までのランダムな数値を生成してください：

```python
import random
# ランダムな数値を生成
```

<details>
<summary>解答を表示</summary>

```python
import random
print(random.randint(1, 100))
```
</details>

問4. 自分でモジュール`utils.py`を作成し、便利な関数を定義して別のファイルからインポートしてください：

```python
# utils.py
def multiply(a, b):
    return a * b

# main.py
from utils import multiply
result = multiply(3, 4)
```

<details>
<summary>解答を表示</summary>

```python
# utils.py
def multiply(a, b):
    return a * b

# main.py
from utils import multiply
print(multiply(3, 4))  # 12
```
</details>

問5. パッケージ構造を作成して、複数のモジュールを整理してください：

```
myapp/
    __init__.py
    utils.py
    models.py
```

<details>
<summary>解答を表示</summary>

```python
# myapp/__init__.py
from .utils import multiply

# 使い方
from myapp import multiply
print(multiply(2, 5))  # 10
```
</details>

## まとめ

このレッスンでは、モジュールとパッケージについて学びました。

- モジュールのインポート方法
- 自分でモジュールを作成する方法
- パッケージの構造と`__init__.py`
- 標準ライブラリの活用
- サードパーティパッケージのインストール

次のレッスンでは、ファイル操作について学び、データを永続化する方法を身につけます。

