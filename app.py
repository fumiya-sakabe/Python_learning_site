from flask import Flask, render_template, abort, request, redirect, url_for, session, flash, jsonify
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from data import (
    lessons, projects, roadmap_phases,
    get_lesson_by_id, get_project_by_id
)
import markdown
import os
import json

app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_SECRET_KEY", "dev-secret-key")

login_manager = LoginManager()
login_manager.login_view = "login"
login_manager.init_app(app)

DATA_USERS = {
    "user@example.com": {"password": "testpass", "name": "受講生"}
}

PROGRESS_DIR = "progress"
os.makedirs(PROGRESS_DIR, exist_ok=True)

PHASE3_OVERVIEW_POINTS = [
    "静的なHTMLを正しく構造化して情報を整理する",
    "CSSでレイアウトとレスポンシブ対応を行い、見た目を整える",
    "JavaScriptでDOM操作やフォームバリデーションを実装する",
    "Flaskとfetch APIを組み合わせて双方向なWebアプリを作る"
]

PHASE3_TIMELINE = [
    {"step": 1, "title": "HTMLの骨組み理解", "lessons": ["web-01"], "description": "セマンティックタグでページを構造化"},
    {"step": 2, "title": "CSSでデザイン", "lessons": ["web-02"], "description": "ボックスモデルとレスポンシブの基礎"},
    {"step": 3, "title": "JavaScriptで動きを付ける", "lessons": ["web-03"], "description": "DOM操作とイベントでUIを強化"},
    {"step": 4, "title": "fetchでAPI連携", "lessons": ["web-04"], "description": "Flask APIとデータ交換"},
    {"step": 5, "title": "Flask基本機能", "lessons": ["flask-01", "flask-02"], "description": "テンプレートとフォーム処理"},
    {"step": 6, "title": "DB・アプリ構築", "lessons": ["flask-03", "flask-04"], "description": "SQLiteでCRUDアプリを実装"},
    {"step": 7, "title": "デプロイ", "lessons": ["flask-05"], "description": "本番公開と運用のポイント"}
]

PHASE3_PRACTICAL_TASKS = [
    {"id": "task-responsive", "title": "レスポンシブ対応済み", "description": "CSSメディアクエリでスマホ表示を最適化"},
    {"id": "task-form-validation", "title": "フォームバリデーション実装", "description": "JavaScriptで未入力チェックやエラーメッセージ表示"},
    {"id": "task-fetch-api", "title": "fetch + Flask API連携", "description": "非同期通信でデータ保存・取得ができる"},
    {"id": "task-ui-polish", "title": "サンプルデザイン再現", "description": "提供されたデザインをHTML/CSSで忠実に再現"}
]


class User(UserMixin):
    def __init__(self, email: str, name: str):
        self.id = email
        self.email = email
        self.name = name


@login_manager.user_loader
def load_user(user_id: str):
    data = DATA_USERS.get(user_id)
    if not data:
        return None
    return User(email=user_id, name=data.get("name", user_id))


def load_progress(email: str):
    path = os.path.join(PROGRESS_DIR, f"{email}.json")
    if not os.path.exists(path):
        return {"lessons": {}, "projects": {}}
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {"lessons": {}, "projects": {}}


def save_progress(email: str, progress: dict):
    path = os.path.join(PROGRESS_DIR, f"{email}.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(progress, f, ensure_ascii=False, indent=2)

@app.route('/')
def index():
    """トップページ（LP的なページ）"""
    return render_template('index.html')


@app.route('/roadmap')
def roadmap():
    """学習ロードマップ"""
    return render_template('roadmap.html', phases=roadmap_phases)


@app.route('/lessons')
def lessons_list():
    """レッスン一覧"""
    # フェーズごとにレッスンを分類
    phase1_lessons = [lesson for lesson in lessons if lesson.get('phase') == 1]
    phase3_lessons = [lesson for lesson in lessons if lesson.get('phase') == 3]
    progress_data = None
    if current_user.is_authenticated:
        progress_data = load_progress(current_user.email)

    phase3_total = len(phase3_lessons)
    phase3_completed = 0
    if progress_data:
        completed_map = progress_data.get("lessons", {})
        phase3_completed = sum(1 for lesson in phase3_lessons if completed_map.get(lesson["id"]))
    phase3_progress = {
        "show": bool(progress_data),
        "completed": phase3_completed,
        "total": phase3_total,
        "percent": int((phase3_completed / phase3_total) * 100) if phase3_total else 0
    }

    tasks_progress = progress_data.get("tasks", {}) if progress_data else {}
    phase3_tasks = []
    for task in PHASE3_PRACTICAL_TASKS:
        item = task.copy()
        item["completed"] = bool(tasks_progress.get(task["id"]))
        phase3_tasks.append(item)

    return render_template('lessons.html', 
                         phase1_lessons=phase1_lessons,
                         phase3_lessons=phase3_lessons,
                         all_lessons=lessons,
                         phase3_overview=PHASE3_OVERVIEW_POINTS,
                         phase3_timeline=PHASE3_TIMELINE,
                         phase3_tasks=phase3_tasks,
                         phase3_progress=phase3_progress)


@app.route('/lessons/<lesson_id>')
def lesson_detail(lesson_id):
    """レッスン詳細（Markdown表示）"""
    lesson = get_lesson_by_id(lesson_id)
    if not lesson:
        abort(404)
    
    # 前後のレッスンを取得
    current_phase = lesson.get('phase')
    phase_lessons = [lesson_item for lesson_item in lessons if lesson_item.get('phase') == current_phase]
    
    # 現在のレッスンのインデックスを見つける
    current_index = None
    for i, lesson_item in enumerate(phase_lessons):
        if lesson_item['id'] == lesson_id:
            current_index = i
            break
    
    prev_lesson = None
    next_lesson = None
    
    if current_index is not None:
        # 前のレッスン
        if current_index > 0:
            prev_lesson = phase_lessons[current_index - 1]
        # 次のレッスン
        if current_index < len(phase_lessons) - 1:
            next_lesson = phase_lessons[current_index + 1]
    
    # Markdownファイルを読み込む
    markdown_path = f"lessons/{lesson_id}.md"
    content = ""
    if os.path.exists(markdown_path):
        with open(markdown_path, 'r', encoding='utf-8') as f:
            content = f.read()
        # MarkdownをHTMLに変換
        content = markdown.markdown(content, extensions=['extra', 'codehilite'])
    else:
        content = "<p>Markdownファイルが見つかりませんでした。</p>"
    
    completed = False
    if current_user.is_authenticated:
        pg = load_progress(current_user.email)
        completed = bool(pg.get("lessons", {}).get(lesson_id))

    return render_template('lesson_detail.html', 
                         lesson=lesson, 
                         content=content,
                         prev_lesson=prev_lesson,
                         next_lesson=next_lesson,
                         completed=completed)


@app.route('/projects')
def projects_list():
    """ミニアプリ一覧"""
    return render_template('projects.html', projects=projects)

@app.route('/projects/<project_id>')
def project_detail(project_id):
    """ミニアプリ詳細（Markdown表示: lessons/project-xx.md）"""
    project = get_project_by_id(project_id)
    if not project:
        abort(404)
    markdown_path = f"lessons/{project_id}.md"
    content = ""
    if os.path.exists(markdown_path):
        with open(markdown_path, 'r', encoding='utf-8') as f:
            content = f.read()
        content = markdown.markdown(content, extensions=['extra', 'codehilite'])
    else:
        content = "<p>Markdownファイルが見つかりませんでした。</p>"
    # 前後ナビ（projects配列順）
    ids = [p['id'] for p in projects]
    prev_project = None
    next_project = None
    if project_id in ids:
        idx = ids.index(project_id)
        if idx > 0:
            prev_project = get_project_by_id(ids[idx - 1])
        if idx < len(ids) - 1:
            next_project = get_project_by_id(ids[idx + 1])
    completed = False
    if current_user.is_authenticated:
        pg = load_progress(current_user.email)
        completed = bool(pg.get("projects", {}).get(project_id))

    return render_template('project_detail.html',
                           project=project,
                           content=content,
                           prev_project=prev_project,
                           next_project=next_project,
                           completed=completed)

@app.route('/phase2')
def phase2():
    """Phase2ページ（ミニアプリ制作の概要と導線）"""
    phase2_info = None
    for ph in roadmap_phases:
        if 'Phase2' in ph.get('name', ''):
            phase2_info = ph
            break
    return render_template('phase2.html',
                           phase=phase2_info,
                           projects=projects)


@app.route('/portfolio')
def portfolio():
    """最終ポートフォリオ課題"""
    return render_template('portfolio.html')


@app.route('/faq')
def faq():
    """よくある質問"""
    return render_template('faq.html')


@app.errorhandler(404)
def not_found(error):
    """404エラーハンドラー"""
    return render_template('404.html'), 404

@app.route('/api/progress/toggle', methods=['POST'])
@login_required
def api_progress_toggle():
    payload = request.get_json(silent=True) or {}
    item_id = payload.get("item_id")
    kind = payload.get("kind")  # "lesson" | "project" | "task"
    if not item_id or kind not in ("lesson", "project", "task"):
        return jsonify({"ok": False, "error": "invalid_parameters"}), 400
    progress = load_progress(current_user.email)
    if kind == "lesson":
        key = "lessons"
    elif kind == "project":
        key = "projects"
    else:
        key = "tasks"
    current = bool(progress.get(key, {}).get(item_id))
    progress.setdefault(key, {})[item_id] = not current
    save_progress(current_user.email, progress)
    return jsonify({"ok": True, "completed": not current})

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email', '').strip().lower()
        password = request.form.get('password', '')
        record = DATA_USERS.get(email)
        if record and record['password'] == password:
            user = User(email=email, name=record.get("name", email))
            login_user(user)
            flash('ログインしました。', 'success')
            next_url = request.args.get('next') or url_for('index')
            return redirect(next_url)
        flash('メールアドレスまたはパスワードが正しくありません。', 'error')
    return render_template('login.html')

@app.route('/logout')
def logout():
    if current_user.is_authenticated:
        logout_user()
        flash('ログアウトしました。', 'success')
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=8000)

