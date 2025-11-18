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


if __name__ == "__main__":
    # デモ実行
    display_roadmap()
    display_all_lessons()
    display_all_projects()
    
    print("\n=== JSON形式の出力 ===")
    print(export_to_json())

