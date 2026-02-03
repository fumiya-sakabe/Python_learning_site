lessons = [
    # Phase1：Python基礎
    {"id": "python-01", "title": "Python開発環境の準備", "category": "basic", "level": "初級", "phase": 1},
    {"id": "python-02", "title": "最初の一歩：printと計算", "category": "basic", "level": "初級", "phase": 1},
    {"id": "python-03", "title": "変数と基本のデータ型（int, float, str, bool）", "category": "basic", "level": "初級", "phase": 1},
    {"id": "python-04", "title": "条件分岐（if, elif, else）", "category": "basic", "level": "初級", "phase": 1},
    {"id": "python-05", "title": "繰り返し処理（for, while）", "category": "basic", "level": "初級", "phase": 1},
    {"id": "python-06", "title": "リストとタプル", "category": "basic", "level": "初級", "phase": 1},
    {"id": "python-07", "title": "辞書と集合", "category": "basic", "level": "初級", "phase": 1},
    {"id": "python-08", "title": "関数の基本（引数・戻り値）", "category": "basic", "level": "初級", "phase": 1},
    {"id": "python-09", "title": "モジュールとパッケージ", "category": "basic", "level": "初級", "phase": 1},
    {"id": "python-10", "title": "ファイル操作（読み書き）", "category": "basic", "level": "初級", "phase": 1},
    {"id": "python-11", "title": "例外処理（try / except）", "category": "basic", "level": "初級", "phase": 1},
    {"id": "python-12", "title": "クラスとオブジェクト（入門）", "category": "basic", "level": "中級", "phase": 1},
    {"id": "python-13", "title": "標準ライブラリに触れてみる（datetime, randomなど）", "category": "basic", "level": "初級", "phase": 1},
    # 初心者向け追加レッスン
    {"id": "python-14", "title": "文字列操作の基礎（format, f-string, 文字列メソッド）", "category": "basic", "level": "初級", "phase": 1},
    {"id": "python-15", "title": "リスト内包表記とジェネレータ", "category": "basic", "level": "中級", "phase": 1},
    {"id": "python-16", "title": "パッケージマネージャー（pip）の使い方", "category": "basic", "level": "初級", "phase": 1},
    {"id": "python-17", "title": "デバッグの基本（printデバッグ、エラーメッセージの読み方）", "category": "basic", "level": "初級", "phase": 1},
    # Phase3：Web基礎（HTML/CSS/JS）
    {"id": "web-01", "title": "HTMLの基本（構造とよく使うタグ）", "category": "web-foundation", "level": "初級", "phase": 3},
    {"id": "web-02", "title": "CSSの基本（レイアウトとデザイン）", "category": "web-foundation", "level": "初級", "phase": 3},
    {"id": "web-03", "title": "JavaScript超入門（DOMとイベント）", "category": "web-foundation", "level": "初級", "phase": 3},
    {"id": "web-04", "title": "ブラウザとFlaskの連携（fetchとAPI）", "category": "web-foundation", "level": "中級", "phase": 3},
    # Phase3：Webアプリ（Flask）
    {"id": "flask-01", "title": "Flask入門（Hello Worldとルーティング）", "category": "web-app", "level": "中級", "phase": 3},
    {"id": "flask-02", "title": "テンプレートとフォーム", "category": "web-app", "level": "中級", "phase": 3},
    {"id": "flask-03", "title": "SQLiteでメモアプリ", "category": "web-app", "level": "中級", "phase": 3},
    {"id": "flask-04", "title": "学習記録アプリ", "category": "web-app", "level": "中級", "phase": 3},
    {"id": "flask-05", "title": "Webアプリのデプロイ", "category": "web-app", "level": "中級", "phase": 3},
]

projects = [
    # Phase2：ミニアプリ
    {"id": "project-01", "title": "コマンドラインTodoリスト", "description": "基本文法の総復習として作る小さなアプリ。リスト操作、関数、ファイル操作の実践"},
    {"id": "project-02", "title": "タイピングゲーム", "description": "繰り返し処理とランダム機能を使って、インタラクティブなゲームを作成"},
    {"id": "project-03", "title": "簡易家計簿（CLI＋CSV保存）", "description": "CSVファイルの読み書きとデータ管理を学ぶ実践的なアプリ"},
    {"id": "project-04", "title": "Webスクレイピング入門", "description": "requestsとBeautifulSoupを使って、Webからデータを取得する方法を学ぶ"},
]

roadmap_phases = [
    {
        "name": "Phase1：Python基礎",
        "duration": "3〜4週間",
        "description": "Pythonの基本的な文法から始めて、プログラミングの基礎をしっかりと身につけます。",
        "items": [
            "開発環境の準備",
            "Pythonの基本文法（変数、型、条件分岐、ループなど）",
            "リストや辞書などのデータ構造",
            "関数、クラス、例外処理",
            "ファイル操作、標準ライブラリの使い方"
        ]
    },
    {
        "name": "Phase2：ミニアプリ制作",
        "duration": "3週間",
        "description": "小さくても「最後まで動くもの」を作ることで、学んだ文法が「使えるスキル」に変わります。",
        "items": [
            "Todoリスト（CLI）",
            "タイピングゲーム",
            "簡易家計簿アプリ",
            "Webスクレイピング"
        ]
    },
    {
        "name": "Phase3：Webアプリ開発",
        "duration": "3〜4週間",
        "description": "Flaskを使ったWebアプリケーション開発を学び、実際にデプロイして公開できるようになります。",
        "items": [
            "Webの仕組み（HTTP、リクエスト/レスポンス）",
            "Flaskの基本（ルーティング、テンプレート）",
            "フォーム入力、DB保存（SQLite）",
            "メモアプリ、学習記録アプリの制作",
            "PythonAnywhereやRenderなどでのデプロイ"
        ]
    },
    {
        "name": "Phase4：ポートフォリオ制作",
        "duration": "3〜4週間",
        "description": "転職活動でアピールできる、あなただけのポートフォリオアプリを作成します。",
        "items": [
            "自分でテーマを選んでWebアプリを企画",
            "要件定義、画面設計",
            "実装、デプロイ、GitHub公開",
            "ポートフォリオページ用の説明文章を書く"
        ]
    }
]


# ===== データ検索・フィルタリング関数 =====

def get_lesson_by_id(lesson_id: str) -> dict | None:
    """レッスンIDでレッスンを取得"""
    for lesson in lessons:
        if lesson["id"] == lesson_id:
            return lesson
    return None


def get_lessons_by_category(category: str) -> list:
    """カテゴリでレッスンをフィルタリング"""
    return [lesson for lesson in lessons if lesson.get("category") == category]


def get_lessons_by_level(level: str) -> list:
    """レベルでレッスンをフィルタリング"""
    return [lesson for lesson in lessons if lesson.get("level") == level]


def get_project_by_id(project_id: str) -> dict | None:
    """プロジェクトIDでプロジェクトを取得"""
    for project in projects:
        if project["id"] == project_id:
            return project
    return None


def get_phase_by_name(phase_name: str) -> dict | None:
    """フェーズ名でフェーズを取得"""
    for phase in roadmap_phases:
        if phase["name"] == phase_name:
            return phase
    return None


# ===== 表示関数 =====

def display_all_lessons():
    """すべてのレッスンを表示"""
    print("\n=== レッスン一覧 ===")
    for lesson in lessons:
        print(f"ID: {lesson['id']}")
        print(f"  タイトル: {lesson['title']}")
        print(f"  カテゴリ: {lesson.get('category', 'N/A')}")
        print(f"  レベル: {lesson.get('level', 'N/A')}")
        print()


def display_all_projects():
    """すべてのプロジェクトを表示"""
    print("\n=== プロジェクト一覧 ===")
    for project in projects:
        print(f"ID: {project['id']}")
        print(f"  タイトル: {project['title']}")
        print(f"  説明: {project.get('description', 'N/A')}")
        print()


def display_roadmap():
    """ロードマップを表示"""
    print("\n=== 学習ロードマップ ===")
    for i, phase in enumerate(roadmap_phases, 1):
        print(f"{i}. {phase['name']}")
        print(f"   期間: {phase['duration']}")
        print()


# ===== JSON出力関数 =====

def export_to_json():
    """データをJSON形式で出力"""
    import json
    data = {
        "lessons": lessons,
        "projects": projects,
        "roadmap_phases": roadmap_phases
    }
    return json.dumps(data, ensure_ascii=False, indent=2)


# ===== 初心者向けサポートデータ =====

# よくあるつまずきポイント集
common_mistakes = [
    {
        "id": "mistake-01",
        "title": "代入演算子（=）と比較演算子（==）を混同する",
        "category": "basic",
        "wrong_code": "if x = 5:\n    print('5です')",
        "correct_code": "if x == 5:\n    print('5です')",
        "explanation": "`=` は「代入」、`==` は「等しいか比較」です。条件分岐では必ず `==` を使います。",
        "related_lessons": ["python-04"]
    },
    {
        "id": "mistake-02",
        "title": "インデント（字下げ）を忘れる",
        "category": "basic",
        "wrong_code": "if x > 0:\nprint('正の数です')  # エラー！",
        "correct_code": "if x > 0:\n    print('正の数です')  # 4スペース字下げ",
        "explanation": "Pythonではインデントが構文の一部です。`if` や `for` の後に続くコードは必ず字下げが必要です。",
        "related_lessons": ["python-04", "python-05"]
    },
    {
        "id": "mistake-03",
        "title": "文字列と数値を連結しようとする",
        "category": "basic",
        "wrong_code": "age = 20\nmessage = '年齢は' + age + '歳です'  # エラー！",
        "correct_code": "age = 20\nmessage = '年齢は' + str(age) + '歳です'\n# または f-string: message = f'年齢は{age}歳です'",
        "explanation": "文字列と数値は直接連結できません。`str()` で数値を文字列に変換するか、f-stringを使います。",
        "related_lessons": ["python-03", "python-14"]
    },
    {
        "id": "mistake-04",
        "title": "リストのコピーと参照を混同する",
        "category": "basic",
        "wrong_code": "a = [1, 2, 3]\nb = a\nb.append(4)\nprint(a)  # [1, 2, 3, 4] ← aも変わってしまう！",
        "correct_code": "a = [1, 2, 3]\nb = a.copy()  # または b = a[:]\nb.append(4)\nprint(a)  # [1, 2, 3] ← aは変わらない",
        "explanation": "`b = a` は参照をコピーするだけなので、`b`を変更すると`a`も変わります。独立したコピーが必要な場合は `.copy()` を使います。",
        "related_lessons": ["python-06"]
    },
    {
        "id": "mistake-05",
        "title": "ループ中にリストの要素を削除する",
        "category": "basic",
        "wrong_code": "numbers = [1, 2, 3, 4, 5]\nfor n in numbers:\n    if n % 2 == 0:\n        numbers.remove(n)  # 予期しない結果になる！",
        "correct_code": "numbers = [1, 2, 3, 4, 5]\nnumbers = [n for n in numbers if n % 2 != 0]  # リスト内包表記\n# または: numbers = list(filter(lambda n: n % 2 != 0, numbers))",
        "explanation": "ループ中にリストを変更すると、インデックスがずれて予期しない動作になります。リスト内包表記や`filter()`を使うのが安全です。",
        "related_lessons": ["python-05", "python-06", "python-15"]
    },
    {
        "id": "mistake-06",
        "title": "関数内でグローバル変数を変更しようとする",
        "category": "basic",
        "wrong_code": "x = 10\ndef change_x():\n    x = 20  # これは新しいローカル変数を作るだけ\nchange_x()\nprint(x)  # 10 のまま",
        "correct_code": "x = 10\ndef change_x():\n    global x  # グローバル変数を使う宣言\n    x = 20\nchange_x()\nprint(x)  # 20",
        "explanation": "関数内でグローバル変数を変更する場合は、`global` 宣言が必要です。宣言しないと新しいローカル変数が作られます。",
        "related_lessons": ["python-08"]
    },
    {
        "id": "mistake-07",
        "title": "辞書のキーにリストを使おうとする",
        "category": "basic",
        "wrong_code": "d = {}\nd[[1, 2]] = 'value'  # エラー！リストはキーにできない",
        "correct_code": "d = {}\nd[tuple([1, 2])] = 'value'  # タプルはキーにできる\n# または: d['1,2'] = 'value'  # 文字列をキーにする",
        "explanation": "辞書のキーは「変更不可能（immutable）」な値しか使えません。リストは変更可能なので使えませんが、タプルや文字列なら使えます。",
        "related_lessons": ["python-06", "python-07"]
    },
    {
        "id": "mistake-08",
        "title": "ファイルを開いた後、閉じ忘れる",
        "category": "basic",
        "wrong_code": "f = open('data.txt', 'r')\ndata = f.read()\n# 閉じ忘れ → リソースリークの可能性",
        "correct_code": "with open('data.txt', 'r') as f:\n    data = f.read()\n# withブロックを出ると自動で閉じられる",
        "explanation": "`with` 文を使うと、ファイルが自動的に閉じられます。`open()` だけを使う場合は `close()` を忘れがちなので、`with` を使うのが推奨です。",
        "related_lessons": ["python-10"]
    },
    {
        "id": "mistake-09",
        "title": "例外処理で `except:` を広く使いすぎる",
        "category": "basic",
        "wrong_code": "try:\n    result = 10 / 0\nexcept:  # すべての例外を捕捉してしまう\n    print('エラー')",
        "correct_code": "try:\n    result = 10 / 0\nexcept ZeroDivisionError:  # 特定の例外だけ\n    print('ゼロで割れません')\nexcept Exception as e:  # その他の例外\n    print(f'エラー: {e}')",
        "explanation": "`except:` だけだと、バグや予期しないエラーまで隠してしまいます。できるだけ具体的な例外を指定しましょう。",
        "related_lessons": ["python-11"]
    },
    {
        "id": "mistake-10",
        "title": "変数名のタイプミスや未定義変数を使う",
        "category": "basic",
        "wrong_code": "name = '太郎'\nprint(nmae)  # タイプミス → NameError!",
        "correct_code": "name = '太郎'\nprint(name)  # 正しい変数名",
        "explanation": "変数を使う前に必ず定義されているか確認しましょう。IDEの自動補完を使うとタイプミスを防げます。",
        "related_lessons": ["python-03"]
    }
]

# コード例検索データ
code_examples = [
    {
        "id": "example-01",
        "title": "リストに要素を追加する",
        "keywords": ["リスト", "追加", "append", "insert", "要素"],
        "category": "list",
        "description": "リストに新しい要素を追加する方法",
        "code": "# append: 末尾に追加\nnumbers = [1, 2, 3]\nnumbers.append(4)\nprint(numbers)  # [1, 2, 3, 4]\n\n# insert: 指定位置に挿入\nnumbers.insert(1, 10)\nprint(numbers)  # [1, 10, 2, 3, 4]\n\n# extend: 別のリストを結合\nnumbers.extend([5, 6])\nprint(numbers)  # [1, 10, 2, 3, 4, 5, 6]",
        "related_lessons": ["python-06"]
    },
    {
        "id": "example-02",
        "title": "ファイルを読み込む",
        "keywords": ["ファイル", "読み込み", "read", "ファイル操作", "読み取り"],
        "category": "file",
        "description": "テキストファイルの内容を読み込む方法",
        "code": "# ファイル全体を読み込む\nwith open('data.txt', 'r', encoding='utf-8') as f:\n    content = f.read()\n    print(content)\n\n# 1行ずつ読み込む\nwith open('data.txt', 'r', encoding='utf-8') as f:\n    for line in f:\n        print(line.strip())  # strip()で改行を削除\n\n# すべての行をリストで取得\nwith open('data.txt', 'r', encoding='utf-8') as f:\n    lines = f.readlines()",
        "related_lessons": ["python-10"]
    },
    {
        "id": "example-03",
        "title": "ファイルに書き込む",
        "keywords": ["ファイル", "書き込み", "write", "保存", "出力"],
        "category": "file",
        "description": "テキストファイルにデータを書き込む方法",
        "code": "# ファイルに書き込む（上書き）\nwith open('output.txt', 'w', encoding='utf-8') as f:\n    f.write('Hello, World!\\n')\n    f.write('こんにちは\\n')\n\n# ファイルに追記する\nwith open('output.txt', 'a', encoding='utf-8') as f:\n    f.write('追加の行\\n')",
        "related_lessons": ["python-10"]
    },
    {
        "id": "example-04",
        "title": "辞書の値を取得する",
        "keywords": ["辞書", "dict", "値", "取得", "キー"],
        "category": "dict",
        "description": "辞書から値を安全に取得する方法",
        "code": "# 基本的な取得（キーが存在しないとエラー）\nd = {'name': '太郎', 'age': 20}\nname = d['name']  # '太郎'\n\n# get()メソッド（キーがなくてもエラーにならない）\nage = d.get('age', 0)  # 'age'がない場合は0を返す\ncity = d.get('city', '不明')  # 'city'がない場合は'不明'\n\n# キーの存在確認\nif 'name' in d:\n    print(d['name'])",
        "related_lessons": ["python-07"]
    },
    {
        "id": "example-05",
        "title": "エラーをキャッチする",
        "keywords": ["エラー", "例外", "try", "except", "エラー処理"],
        "category": "error",
        "description": "例外処理でエラーを安全に処理する方法",
        "code": "# 基本的な例外処理\ntry:\n    result = 10 / 0\nexcept ZeroDivisionError:\n    print('ゼロで割ることはできません')\n\n# 複数の例外を処理\ntry:\n    number = int(input('数値を入力: '))\n    result = 100 / number\nexcept ValueError:\n    print('数値を入力してください')\nexcept ZeroDivisionError:\n    print('ゼロは入力できません')\n\n# エラー情報を取得\ntry:\n    x = int('abc')\nexcept ValueError as e:\n    print(f'エラー: {e}')",
        "related_lessons": ["python-11"]
    },
    {
        "id": "example-06",
        "title": "リストから条件に合う要素だけ抽出する",
        "keywords": ["リスト", "フィルタ", "条件", "抽出", "filter"],
        "category": "list",
        "description": "条件に一致する要素だけを取り出す方法",
        "code": "# リスト内包表記（推奨）\nnumbers = [1, 2, 3, 4, 5, 6]\neven_numbers = [n for n in numbers if n % 2 == 0]\nprint(even_numbers)  # [2, 4, 6]\n\n# filter()関数を使う\nnumbers = [1, 2, 3, 4, 5, 6]\neven_numbers = list(filter(lambda n: n % 2 == 0, numbers))\nprint(even_numbers)  # [2, 4, 6]\n\n# 文字列のリストから長さでフィルタ\nwords = ['apple', 'pen', 'computer', 'cat']\nlong_words = [w for w in words if len(w) > 3]\nprint(long_words)  # ['apple', 'computer']",
        "related_lessons": ["python-05", "python-06", "python-15"]
    },
    {
        "id": "example-07",
        "title": "文字列を数値に変換する",
        "keywords": ["文字列", "数値", "変換", "int", "float"],
        "category": "string",
        "description": "文字列を数値型に変換する方法",
        "code": "# 文字列を整数に変換\nstr_num = '123'\nint_num = int(str_num)\nprint(int_num)  # 123\nprint(type(int_num))  # <class 'int'>\n\n# 文字列を浮動小数点数に変換\nstr_float = '3.14'\nfloat_num = float(str_float)\nprint(float_num)  # 3.14\n\n# 数値を文字列に変換\nnumber = 456\nstr_number = str(number)\nprint(str_number)  # '456'",
        "related_lessons": ["python-03"]
    },
    {
        "id": "example-08",
        "title": "ループでインデックス（番号）も一緒に取得する",
        "keywords": ["ループ", "インデックス", "番号", "enumerate", "for"],
        "category": "loop",
        "description": "リストの要素とインデックスを同時に取得する方法",
        "code": "# enumerate()を使う（推奨）\nfruits = ['apple', 'banana', 'orange']\nfor index, fruit in enumerate(fruits):\n    print(f'{index}: {fruit}')\n# 出力:\n# 0: apple\n# 1: banana\n# 2: orange\n\n# インデックスを1から始める\nfor index, fruit in enumerate(fruits, start=1):\n    print(f'{index}: {fruit}')\n# 出力:\n# 1: apple\n# 2: banana\n# 3: orange",
        "related_lessons": ["python-05", "python-06"]
    },
    {
        "id": "example-09",
        "title": "辞書をループで処理する",
        "keywords": ["辞書", "ループ", "items", "キー", "値"],
        "category": "dict",
        "description": "辞書のキーと値をループで取り出す方法",
        "code": "# キーのみ\nperson = {'name': '太郎', 'age': 20, 'city': '東京'}\nfor key in person:\n    print(key)\n\n# 値のみ\nfor value in person.values():\n    print(value)\n\n# キーと値の両方（推奨）\nfor key, value in person.items():\n    print(f'{key}: {value}')\n# 出力:\n# name: 太郎\n# age: 20\n# city: 東京",
        "related_lessons": ["python-05", "python-07"]
    },
    {
        "id": "example-10",
        "title": "文字列を分割・結合する",
        "keywords": ["文字列", "分割", "結合", "split", "join"],
        "category": "string",
        "description": "文字列を分割したり、リストを結合して文字列にする方法",
        "code": "# 文字列を分割（split）\ntext = 'apple,banana,orange'\nfruits = text.split(',')\nprint(fruits)  # ['apple', 'banana', 'orange']\n\n# デフォルトは空白で分割\nwords = 'hello world python'.split()\nprint(words)  # ['hello', 'world', 'python']\n\n# リストを文字列に結合（join）\nfruits = ['apple', 'banana', 'orange']\ntext = ','.join(fruits)\nprint(text)  # 'apple,banana,orange'\n\ntext_with_space = ' '.join(fruits)\nprint(text_with_space)  # 'apple banana orange'",
        "related_lessons": ["python-03", "python-14"]
    }
]


def get_common_mistakes_by_category(category: str = None) -> list:
    """カテゴリでつまずきポイントをフィルタリング"""
    if category:
        return [m for m in common_mistakes if m.get("category") == category]
    return common_mistakes


def search_code_examples(query: str) -> list:
    """キーワードでコード例を検索"""
    if not query:
        return code_examples
    query_lower = query.lower()
    results = []
    for example in code_examples:
        # タイトル、キーワード、説明で検索
        if (query_lower in example["title"].lower() or
            query_lower in example["description"].lower() or
            any(query_lower in kw.lower() for kw in example.get("keywords", []))):
            results.append(example)
    return results


if __name__ == "__main__":
    # デモ実行
    display_roadmap()
    display_all_lessons()
    display_all_projects()
    
    print("\n=== JSON形式の出力 ===")
    print(export_to_json())

