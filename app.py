from flask import Flask, render_template, abort, request, redirect, url_for, session, flash, jsonify
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from data import (
    lessons, projects, roadmap_phases,
    get_lesson_by_id, get_project_by_id,
    common_mistakes, code_examples,
    get_common_mistakes_by_category, search_code_examples
)
import markdown
import os
import json
from datetime import datetime, timedelta

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
        return {"lessons": {}, "projects": {}, "tasks": {}, "favorites": [], "study_dates": [], "notes": {}}
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
            # 既存データとの互換性のため
            if "favorites" not in data:
                data["favorites"] = []
            if "study_dates" not in data:
                data["study_dates"] = []
            if "notes" not in data:
                data["notes"] = {}
            return data
    except Exception:
        return {"lessons": {}, "projects": {}, "tasks": {}, "favorites": [], "study_dates": [], "notes": {}}


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
    favorites = []
    if current_user.is_authenticated:
        progress_data = load_progress(current_user.email)
        favorites = progress_data.get("favorites", [])

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
                         phase3_progress=phase3_progress,
                         favorites=favorites if current_user.is_authenticated else [])


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
    is_favorite = False
    note = ""
    if current_user.is_authenticated:
        pg = load_progress(current_user.email)
        completed = bool(pg.get("lessons", {}).get(lesson_id))
        favorites = pg.get("favorites", [])
        is_favorite = f"lesson:{lesson_id}" in favorites
        notes = pg.get("notes", {})
        note = notes.get(f"lesson:{lesson_id}", "")

    return render_template('lesson_detail.html', 
                         lesson=lesson, 
                         content=content,
                         prev_lesson=prev_lesson,
                         next_lesson=next_lesson,
                         completed=completed,
                         is_favorite=is_favorite,
                         note=note)


@app.route('/projects')
def projects_list():
    """ミニアプリ一覧"""
    favorites = []
    if current_user.is_authenticated:
        progress = load_progress(current_user.email)
        favorites = progress.get("favorites", [])
    return render_template('projects.html', projects=projects, favorites=favorites if current_user.is_authenticated else [])

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
    is_favorite = False
    note = ""
    if current_user.is_authenticated:
        pg = load_progress(current_user.email)
        completed = bool(pg.get("projects", {}).get(project_id))
        favorites = pg.get("favorites", [])
        is_favorite = f"project:{project_id}" in favorites
        notes = pg.get("notes", {})
        note = notes.get(f"project:{project_id}", "")

    return render_template('project_detail.html',
                           project=project,
                           content=content,
                           prev_project=prev_project,
                           next_project=next_project,
                           completed=completed,
                           is_favorite=is_favorite,
                           note=note)

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


@app.route('/common-mistakes')
def common_mistakes_page():
    """よくあるつまずきポイント集"""
    category = request.args.get('category', '')
    mistakes = get_common_mistakes_by_category(category) if category else common_mistakes
    return render_template('common_mistakes.html', 
                         mistakes=mistakes, 
                         all_mistakes=common_mistakes,
                         all_lessons=lessons,
                         selected_category=category)


@app.route('/dashboard')
@login_required
def dashboard():
    """学習ダッシュボード"""
    progress = load_progress(current_user.email)
    
    # Phase別のレッスン数と完了数
    phase1_lessons = [l for l in lessons if l.get('phase') == 1]
    phase3_lessons = [l for l in lessons if l.get('phase') == 3]
    
    completed_lessons = progress.get("lessons", {})
    completed_projects = progress.get("projects", {})
    
    phase1_completed = sum(1 for l in phase1_lessons if completed_lessons.get(l["id"]))
    phase3_completed = sum(1 for l in phase3_lessons if completed_lessons.get(l["id"]))
    
    phase1_progress = {
        "total": len(phase1_lessons),
        "completed": phase1_completed,
        "percent": int((phase1_completed / len(phase1_lessons) * 100)) if phase1_lessons else 0
    }
    
    phase3_progress = {
        "total": len(phase3_lessons),
        "completed": phase3_completed,
        "percent": int((phase3_completed / len(phase3_lessons) * 100)) if phase3_lessons else 0
    }
    
    # プロジェクト進捗
    projects_completed = sum(1 for p in projects if completed_projects.get(p["id"]))
    projects_progress = {
        "total": len(projects),
        "completed": projects_completed,
        "percent": int((projects_completed / len(projects) * 100)) if projects else 0
    }
    
    # 学習ストリーク（連続学習日数）
    study_dates = progress.get("study_dates", [])
    streak = 0
    if study_dates:
        # 日付文字列を日付オブジェクトに変換してソート
        dates = sorted([datetime.strptime(d, "%Y-%m-%d") for d in study_dates if d])
        today = datetime.now().date()
        check_date = today
        
        # 今日または昨日から逆順にカウント
        for i in range(len(dates) - 1, -1, -1):
            date_obj = dates[i].date()
            if date_obj == check_date or date_obj == check_date - timedelta(days=1):
                streak += 1
                check_date = date_obj - timedelta(days=1)
            else:
                break
    
    # 今日の学習を記録
    today_str = datetime.now().strftime("%Y-%m-%d")
    if today_str not in study_dates:
        study_dates.append(today_str)
        progress["study_dates"] = study_dates
        save_progress(current_user.email, progress)
    
    # 最近完了したレッスン（最新5件）
    recent_completed = []
    for lesson_id, completed in list(completed_lessons.items())[-5:]:
        if completed:
            lesson = get_lesson_by_id(lesson_id)
            if lesson:
                recent_completed.append(lesson)
    recent_completed.reverse()
    
    # 統計
    total_completed_lessons = len([l for l, c in completed_lessons.items() if c])
    total_completed_projects = len([p for p, c in completed_projects.items() if c])
    
    return render_template('dashboard.html',
                         phase1_progress=phase1_progress,
                         phase3_progress=phase3_progress,
                         projects_progress=projects_progress,
                         streak=streak,
                         recent_completed=recent_completed[:5],
                         total_completed_lessons=total_completed_lessons,
                         total_completed_projects=total_completed_projects,
                         all_lessons=lessons,
                         all_projects=projects)


@app.route('/code-examples')
def code_examples_page():
    """コード例検索"""
    query = request.args.get('q', '').strip()
    category = request.args.get('category', '')
    
    if query:
        examples = search_code_examples(query)
    elif category:
        examples = [e for e in code_examples if e.get('category') == category]
    else:
        examples = code_examples
    
    # カテゴリ一覧を取得
    categories = list(set(e.get('category', '') for e in code_examples if e.get('category')))
    
    return render_template('code_examples.html',
                         examples=examples,
                         all_examples=code_examples,
                         all_lessons=lessons,
                         query=query,
                         selected_category=category,
                         categories=categories)


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
    
    # 学習日を記録
    today_str = datetime.now().strftime("%Y-%m-%d")
    study_dates = progress.get("study_dates", [])
    if today_str not in study_dates:
        study_dates.append(today_str)
    progress["study_dates"] = study_dates
    
    save_progress(current_user.email, progress)
    return jsonify({"ok": True, "completed": not current})


@app.route('/api/favorites/toggle', methods=['POST'])
@login_required
def api_favorites_toggle():
    """お気に入りの追加/削除"""
    payload = request.get_json(silent=True) or {}
    item_id = payload.get("item_id")
    kind = payload.get("kind")  # "lesson" | "project"
    if not item_id or kind not in ("lesson", "project"):
        return jsonify({"ok": False, "error": "invalid_parameters"}), 400
    
    progress = load_progress(current_user.email)
    favorites = progress.get("favorites", [])
    favorite_key = f"{kind}:{item_id}"
    
    if favorite_key in favorites:
        favorites.remove(favorite_key)
        is_favorite = False
    else:
        favorites.append(favorite_key)
        is_favorite = True
    
    progress["favorites"] = favorites
    save_progress(current_user.email, progress)
    return jsonify({"ok": True, "is_favorite": is_favorite})


@app.route('/api/notes/save', methods=['POST'])
@login_required
def api_notes_save():
    """ノートの保存"""
    payload = request.get_json(silent=True) or {}
    item_id = payload.get("item_id")
    kind = payload.get("kind")  # "lesson" | "project"
    note = payload.get("note", "").strip()
    
    if not item_id or kind not in ("lesson", "project"):
        return jsonify({"ok": False, "error": "invalid_parameters"}), 400
    
    progress = load_progress(current_user.email)
    notes = progress.get("notes", {})
    note_key = f"{kind}:{item_id}"
    
    if note:
        notes[note_key] = note
    else:
        # 空の場合は削除
        notes.pop(note_key, None)
    
    progress["notes"] = notes
    save_progress(current_user.email, progress)
    return jsonify({"ok": True})


@app.route('/search')
def search_page():
    """検索ページ（レッスン・プロジェクト）"""
    query = request.args.get('q', '').strip()
    category = request.args.get('category', '')  # "lessons" | "projects" | ""
    
    results = {
        "lessons": [],
        "projects": []
    }
    
    if query:
        query_lower = query.lower()
        
        # レッスンを検索
        if not category or category == "lessons":
            for lesson in lessons:
                title_match = query_lower in lesson.get("title", "").lower()
                desc_match = query_lower in lesson.get("description", "").lower() if lesson.get("description") else False
                category_match = query_lower in lesson.get("category", "").lower()
                
                if title_match or desc_match or category_match:
                    results["lessons"].append(lesson)
        
        # プロジェクトを検索
        if not category or category == "projects":
            for project in projects:
                title_match = query_lower in project.get("title", "").lower()
                desc_match = query_lower in project.get("description", "").lower() if project.get("description") else False
                
                if title_match or desc_match:
                    results["projects"].append(project)
    
    return render_template('search.html',
                         query=query,
                         category=category,
                         results=results,
                         all_lessons=lessons,
                         all_projects=projects)


@app.route('/favorites')
@login_required
def favorites_page():
    """お気に入り一覧"""
    progress = load_progress(current_user.email)
    favorites = progress.get("favorites", [])
    
    favorite_lessons = []
    favorite_projects = []
    
    for fav in favorites:
        kind, item_id = fav.split(":", 1)
        if kind == "lesson":
            lesson = get_lesson_by_id(item_id)
            if lesson:
                favorite_lessons.append(lesson)
        elif kind == "project":
            project = get_project_by_id(item_id)
            if project:
                favorite_projects.append(project)
    
    return render_template('favorites.html',
                         favorite_lessons=favorite_lessons,
                         favorite_projects=favorite_projects,
                         all_lessons=lessons,
                         all_projects=projects)

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

