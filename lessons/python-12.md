# クラスとオブジェクト（入門）

## このレッスンのゴール

- クラスを定義して、オブジェクトを作成できる
- メソッドと属性を使って、オブジェクトの振る舞いを定義できる
- コンストラクタ（`__init__`）を使って、初期化ができる
- インスタンス変数とクラス変数の違いを理解できる
- 簡単なクラスを使ったプログラムを書ける

## なぜ重要なのか

クラスとオブジェクトは、オブジェクト指向プログラミングの基礎です。

実務では、コードを整理し、再利用可能にするためにクラスが頻繁に使われます。

Webアプリでも、データベースのモデル、フォーム、ビューなど、多くのものがクラスとして定義されます。

ポートフォリオアプリでも、ユーザー、記事、コメントなどの概念をクラスとして表現することで、コードが整理されます。

## 解説

### 1. クラスの定義

`class`キーワードでクラスを定義します。

```python
class Person:
    pass

# オブジェクト（インスタンス）を作成
person1 = Person()
person2 = Person()
```

### 2. 属性の追加

オブジェクトに属性を追加できます。

```python
class Person:
    pass

person = Person()
person.name = "太郎"
person.age = 25

print(person.name)  # "太郎"
```

### 3. メソッドの定義

クラス内でメソッドを定義できます。

```python
class Person:
    def greet(self):
        print("Hello!")

person = Person()
person.greet()  # "Hello!"
```

### 4. コンストラクタ（`__init__`）

オブジェクトの初期化を行うメソッドです。

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        print(f"私は{self.name}、{self.age}歳です")

person = Person("太郎", 25)
person.introduce()  # "私は太郎、25歳です"
```

### 5. インスタンス変数

`self`を使って、インスタンス変数を定義します。

```python
class Person:
    def __init__(self, name):
        self.name = name  # インスタンス変数
    
    def get_name(self):
        return self.name

person1 = Person("太郎")
person2 = Person("花子")

print(person1.get_name())  # "太郎"
print(person2.get_name())  # "花子"
```

### 6. クラス変数

クラス全体で共有される変数です。

```python
class Person:
    species = "Homo sapiens"  # クラス変数
    
    def __init__(self, name):
        self.name = name  # インスタンス変数

person1 = Person("太郎")
person2 = Person("花子")

print(person1.species)  # "Homo sapiens"
print(person2.species)  # "Homo sapiens"
print(Person.species)   # "Homo sapiens"
```

### 7. プライベート変数（慣習）

Pythonでは、アンダースコア（`_`）でプライベートであることを示します。

```python
class Person:
    def __init__(self, name):
        self.name = name  # 公開
        self._age = 25    # プライベート（慣習上）
        self.__secret = "秘密"  # よりプライベート（名前修飾）
```

### 8. 文字列表現（`__str__`）

オブジェクトを文字列として表現します。

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"Person(name={self.name}, age={self.age})"

person = Person("太郎", 25)
print(person)  # "Person(name=太郎, age=25)"
```

### 9. 実践例：計算機クラス

```python
class Calculator:
    def __init__(self):
        self.result = 0
    
    def add(self, value):
        self.result += value
        return self
    
    def subtract(self, value):
        self.result -= value
        return self
    
    def multiply(self, value):
        self.result *= value
        return self
    
    def get_result(self):
        return self.result

calc = Calculator()
result = calc.add(10).multiply(2).subtract(5).get_result()
print(result)  # 15
```

## よくある間違い

- `self`を忘れる（メソッドの第一引数は必ず`self`）
- `__init__`の名前を間違える（`_init_`や`init`ではない）
- インスタンス変数を`self`なしで参照する（エラーになる）
- クラス変数とインスタンス変数を混同する
- `__str__`と`__repr__`の違いを理解しない（`__str__`は表示用、`__repr__`はデバッグ用）

## 演習課題

問1. `Student`クラスを作成して、名前と年齢を持つ学生を表現してください：

```python
class Student:
    def __init__(self, name, age):
        # ここを実装
        pass
    
    def introduce(self):
        # 自己紹介文を表示
        pass
```

<details>
<summary>解答を表示</summary>

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        print(f"私は{self.name}、{self.age}歳です")

s = Student("太郎", 20)
s.introduce()
```
</details>

問2. `Rectangle`クラスを作成して、幅と高さから面積と周囲の長さを計算してください：

```python
class Rectangle:
    def __init__(self, width, height):
        # ここを実装
        pass
    
    def area(self):
        # 面積を返す
        pass
    
    def perimeter(self):
        # 周囲の長さを返す
        pass
```

<details>
<summary>解答を表示</summary>

```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)
```
</details>

問3. `BankAccount`クラスを作成して、残高の管理機能を実装してください：

```python
class BankAccount:
    def __init__(self, initial_balance=0):
        # ここを実装
        pass
    
    def deposit(self, amount):
        # 預金
        pass
    
    def withdraw(self, amount):
        # 引き出し
        pass
    
    def get_balance(self):
        # 残高を返す
        pass
```

<details>
<summary>解答を表示</summary>

```python
class BankAccount:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance
    
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("入金額は正の数で")
        self.balance += amount
    
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("出金額は正の数で")
        if amount > self.balance:
            raise ValueError("残高不足")
        self.balance -= amount
    
    def get_balance(self):
        return self.balance
```
</details>

問4. `__str__`メソッドを実装して、オブジェクトを文字列として表示してください：

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        # ここを実装
        pass
```

<details>
<summary>解答を表示</summary>

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"Person(name={self.name}, age={self.age})"
```
</details>

問5. クラス変数を使って、作成されたインスタンスの数を数えてください：

```python
class Person:
    count = 0  # クラス変数
    
    def __init__(self, name):
        self.name = name
        # カウンターを増やす
        pass
```

<details>
<summary>解答を表示</summary>

```python
class Person:
    count = 0
    
    def __init__(self, name):
        self.name = name
        Person.count += 1

p1 = Person("太郎")
p2 = Person("花子")
print(Person.count)  # 2
```
</details>

## まとめ

このレッスンでは、クラスとオブジェクトの基礎について学びました。

- クラスの定義とインスタンスの作成
- コンストラクタ（`__init__`）での初期化
- メソッドと属性の定義
- インスタンス変数とクラス変数
- `__str__`メソッドでの文字列表現

次のレッスンでは、標準ライブラリについて学び、Pythonの便利な機能を活用する方法を身につけます。

