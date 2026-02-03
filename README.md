# Python学習サイト

初心者向けのPythonとWeb開発の学習プラットフォームです。段階的に学習を進められるカリキュラムと、実践的なプロジェクトを通じてプログラミングスキルを身につけられます。

## 特徴

- **段階的なカリキュラム**: Phase1（Python基礎）→ Phase2（ミニアプリ制作）→ Phase3（Web開発）の3段階で学習
- **実践的なプロジェクト**: 4つのミニアプリプロジェクトで実装力を養成
- **ユーザー進捗管理**: ログイン機能で学習進捗を保存・管理
- **初心者サポート機能**:
  - つまずきポイント集（よくあるエラーと解決方法）
  - コード例検索（カテゴリ別の実装例）
  - 学習ノート機能
  - お気に入り機能
  - 検索機能

## 技術スタック

- **バックエンド**: Flask 3.0.0
- **認証**: Flask-Login
- **マークダウン**: Markdown 3.5.1
- **コードハイライト**: Pygments 2.16.1
- **デプロイ**: Gunicorn 21.2.0

## セットアップ

### 1. リポジトリのクローン

```bash
git clone https://github.com/fumiya-sakabe/Python_learning_site.git
cd Python_learning_site
```

### 2. 仮想環境の作成と有効化

```bash
# macOS/Linux
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

### 3. 依存パッケージのインストール

```bash
pip install -r requirements.txt
```

### 4. アプリケーションの起動

```bash
python app.py
```

ブラウザで `http://localhost:8000` にアクセスしてください。

## プロジェクト構造

```
Python_learning/
├── app.py                 # Flaskアプリケーション本体
├── data.py                # レッスン・プロジェクトデータ
├── requirements.txt       # 依存パッケージ一覧
├── README.md             # このファイル
├── lessons/              # レッスンMarkdownファイル
│   ├── python-*.md       # Phase1: Python基礎レッスン
│   ├── web-*.md          # Phase3: Web基礎レッスン
│   ├── flask-*.md        # Phase3: Flaskレッスン
│   └── project-*.md      # Phase2: プロジェクト課題
├── templates/             # Jinja2テンプレート
│   ├── base.html         # ベーステンプレート
│   ├── index.html        # ホームページ
│   ├── lessons.html      # レッスン一覧
│   ├── lesson_detail.html # レッスン詳細
│   ├── projects.html     # プロジェクト一覧
│   ├── project_detail.html # プロジェクト詳細
│   ├── dashboard.html    # 学習ダッシュボード
│   ├── favorites.html    # お気に入り一覧
│   ├── search.html       # 検索ページ
│   └── ...
├── static/               # 静的ファイル
│   └── css/             # スタイルシート
│       ├── style.css    # メインスタイル
│       └── markdown.css # Markdown表示用スタイル
└── progress/            # ユーザー進捗データ（JSON）
```

## カリキュラム構成

### Phase1: Python基礎（17レッスン）

1. Python開発環境の準備
2. 最初の一歩：printと計算
3. 変数と基本のデータ型
4. 条件分岐
5. 繰り返し処理
6. リストとタプル
7. 辞書と集合
8. 関数の基本
9. モジュールとパッケージ
10. ファイル操作
11. 例外処理
12. クラスとオブジェクト
13. 標準ライブラリ
14. 文字列操作
15. リスト内包表記とジェネレータ
16. パッケージマネージャー
17. デバッグの基本

### Phase2: ミニアプリ制作（4プロジェクト）

1. **ToDoアプリ（CLI）**: 基本的なCRUD操作を学ぶ
2. **タイピングゲーム（CLI）**: ループと時間計測を実践
3. **簡易家計簿（CLI + CSV）**: データ永続化を学ぶ
4. **Webスクレイピング入門**: 外部データ取得の基礎

### Phase3: Web開発（9レッスン）

#### Web基礎
1. HTMLの基本
2. CSSの基本
3. JavaScript超入門
4. ブラウザとFlaskの連携

#### Flask
1. Flask入門
2. テンプレートとフォーム
3. SQLiteでメモアプリ
4. 学習記録アプリ
5. デプロイ

## 主な機能

### ユーザー機能
- **ログイン/ログアウト**: メールアドレスとパスワードで認証
- **進捗管理**: レッスン・プロジェクト・タスクの完了状況を保存
- **学習ダッシュボード**: 進捗状況を視覚的に表示
- **お気に入り**: よく参照するレッスンやプロジェクトを保存
- **学習ノート**: 各レッスン・プロジェクトにメモを追加
- **検索機能**: レッスンとプロジェクトをキーワードで検索

### 学習サポート機能
- **つまずきポイント集**: よくあるエラーと解決方法を解説
- **コード例検索**: カテゴリ別の実装例を検索
- **FAQ**: よくある質問と回答

## デプロイ

### Renderでのデプロイ

1. GitHubリポジトリにプッシュ
2. Renderで「New Web Service」を選択
3. リポジトリを接続
4. 設定を入力：
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
5. 環境変数を設定（必要に応じて）:
   - `FLASK_SECRET_KEY`: セキュアなシークレットキー

詳細は `lessons/flask-05.md` を参照してください。

## 開発

### ローカル開発

```bash
# 開発モードで起動（デバッグ有効）
python app.py
```

### 本番環境

```bash
# Gunicornで起動
gunicorn app:app
```

## ライセンス

このプロジェクトは学習目的で作成されています。

## 貢献

バグ報告や機能要望は、GitHubのIssuesでお願いします。

## 作者

fumiya-sakabe

---

**注意**: このサイトは学習用のプロジェクトです。本番環境で使用する場合は、セキュリティ設定（SECRET_KEY、パスワードハッシュ化など）を適切に設定してください。
