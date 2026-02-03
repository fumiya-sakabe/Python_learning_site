# ミニアプリ: タイピングゲーム（CLI）

## このプロジェクトのゴール

- `random`と時間計測を使ってゲームを作れる
- ループ・条件分岐・関数分割の実践
- スコア集計とランキング保存（任意）

## 概要

出題された文字列を素早く正確に入力してスコアを競うCLIゲームを作成します。

## 要件

- ランダムなお題（英単語/文章）を出題
- 制限時間または出題数で終了
- 正答数、ミスタイプ数、WPM（words per minute）などを表示
- （任意）結果を`results.csv`へ保存し、トップ5を表示

## 実装ステップ

1. お題リストを用意（配列または外部ファイル）
2. `time.time()`で開始/終了を計測
3. 判定とスコア算出
4. ランキング保存/読み込み

## サンプルコード（最小）

```python
import random
import time

WORDS = [
    'python', 'keyboard', 'function', 'variable', 'condition', 'flask', 'sqlite'
]


def play(rounds: int = 5):
    correct = 0
    mistakes = 0
    start = time.time()

    for _ in range(rounds):
        w = random.choice(WORDS)
        print(f"\nお題: {w}")
        typed = input('入力> ').strip()
        if typed == w:
            print('✅ 正解!')
            correct += 1
        else:
            print(f'❌ 不正解: {typed}')
            mistakes += 1

    elapsed = time.time() - start
    wpm = correct / (elapsed / 60) if elapsed > 0 else 0
    print(f"\n正解: {correct}, ミス: {mistakes}, 経過秒: {elapsed:.1f}, WPM: {wpm:.1f}")


if __name__ == '__main__':
    play()
```

## 演習課題

1. 制限時間（例: 30秒）で終了するモードを追加してください。

<details>
<summary>💡 解答を見る</summary>

解答：

制限時間モードを追加するには、ループ内で経過時間をチェックし、制限時間を超えたら終了します。

実装例：

```python
def play_time_limit(time_limit: int = 30):
    """制限時間モード（デフォルト30秒）"""
    correct = 0
    mistakes = 0
    start = time.time()

    while True:
        # 制限時間を超えたら終了
        if time.time() - start > time_limit:
            break
        
        w = random.choice(WORDS)
        print(f"\n残り時間: {time_limit - (time.time() - start):.1f}秒")
        print(f"お題: {w}")
        typed = input('入力> ').strip()
        
        if typed == w:
            print('✅ 正解!')
            correct += 1
        else:
            print(f'❌ 不正解: {typed}')
            mistakes += 1

    elapsed = time.time() - start
    wpm = correct / (elapsed / 60) if elapsed > 0 else 0
    print(f"\n時間切れ!")
    print(f"正解: {correct}, ミス: {mistakes}, 経過秒: {elapsed:.1f}, WPM: {wpm:.1f}")

# 使用例
play_time_limit(30)  # 30秒制限
```

ポイント：
- `time.time() - start`で経過時間を計算
- ループ内で制限時間を超えたら`break`で終了
- 終了後にスコアを集計して表示

</details>

2. ミスタイプ数に応じて減点するスコア式を導入してください。

<details>
<summary>💡 解答を見る</summary>

解答：

正答数に加点し、ミスタイプ数に応じて減点するスコア式を導入します。

実装例：

```python
def play(rounds: int = 5):
    correct = 0
    mistakes = 0
    start = time.time()

    for _ in range(rounds):
        w = random.choice(WORDS)
        print(f"\nお題: {w}")
        typed = input('入力> ').strip()
        if typed == w:
            print('✅ 正解!')
            correct += 1
        else:
            print(f'❌ 不正解: {typed}')
            mistakes += 1

    elapsed = time.time() - start
    wpm = correct / (elapsed / 60) if elapsed > 0 else 0
    
    # スコア計算（正答1問10点、ミス1回-2点）
    score = correct * 10 - mistakes * 2
    if score < 0:
        score = 0  # スコアは0以下にならない
    
    print(f"\n正解: {correct}, ミス: {mistakes}, 経過秒: {elapsed:.1f}, WPM: {wpm:.1f}")
    print(f"スコア: {score}点")

# 使用例
play(5)
```

ポイント：
- `score = correct * 10 - mistakes * 2`のような式でスコアを計算
- スコアが0以下にならないように調整
- 正答数とミス数を両方表示して、スコア計算の根拠を明確に

</details>

3. お題を外部ファイル（`words.txt`）から読み込めるようにしてください。

<details>
<summary>💡 解答を見る</summary>

解答：

外部ファイルからお題リストを読み込むことで、プログラムを変更せずにお題を追加・変更できます。

実装例：

```python
WORDS = []  # グローバル変数

def load_words(filename: str = 'words.txt'):
    """外部ファイルからお題リストを読み込む"""
    global WORDS
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            WORDS = [line.strip() for line in f if line.strip()]
        if not WORDS:
            print(f"⚠️ {filename}が空です。デフォルトのお題を使用します。")
            WORDS = ['python', 'keyboard', 'function', 'variable']
    except FileNotFoundError:
        print(f"⚠️ {filename}が見つかりません。デフォルトのお題を使用します。")
        WORDS = ['python', 'keyboard', 'function', 'variable']

# 起動時に読み込む
if __name__ == '__main__':
    load_words()
    if WORDS:
        play()
    else:
        print("お題が読み込めませんでした。")
```

`words.txt`の例：
```
python
keyboard
function
variable
condition
flask
sqlite
```

ポイント：
- `line.strip()`で行の前後の空白を削除
- `if line.strip()`で空行をスキップ
- ファイルが見つからない場合のエラーハンドリング
- ファイルが空の場合のデフォルト値設定

</details>

4. 成績を`results.csv`に追記して、最新TOP5を表示してください。

<details>
<summary>💡 解答を見る</summary>

解答：

成績をCSVファイルに保存し、スコア順でTOP5を表示します。

実装例：

```python
import csv
from datetime import datetime

RESULTS_FILE = 'results.csv'

def save_result(correct: int, mistakes: int, wpm: float, score: int):
    """成績をCSVに追記"""
    timestamp = datetime.now().isoformat()
    result = {
        'timestamp': timestamp,
        'correct': correct,
        'mistakes': mistakes,
        'wpm': wpm,
        'score': score
    }
    
    # ファイルが存在するかチェック
    file_exists = os.path.exists(RESULTS_FILE)
    
    with open(RESULTS_FILE, 'a', encoding='utf-8', newline='') as f:
        fieldnames = ['timestamp', 'correct', 'mistakes', 'wpm', 'score']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        
        # ファイルが新規作成ならヘッダーを書き込み
        if not file_exists:
            writer.writeheader()
        
        writer.writerow(result)

def show_top5():
    """TOP5の成績を表示"""
    try:
        with open(RESULTS_FILE, 'r', encoding='utf-8', newline='') as f:
            reader = csv.DictReader(f)
            results = []
            for row in reader:
                # 文字列を数値に変換
                row['score'] = int(row['score'])
                row['correct'] = int(row['correct'])
                row['mistakes'] = int(row['mistakes'])
                row['wpm'] = float(row['wpm'])
                results.append(row)
        
        # スコア順でソートしてTOP5を取得
        top5 = sorted(results, key=lambda r: r['score'], reverse=True)[:5]
        
        print("\n🏆 TOP5ランキング:")
        for i, r in enumerate(top5, 1):
            print(f"{i}. スコア: {r['score']}点 | 正解: {r['correct']} | ミス: {r['mistakes']} | WPM: {r['wpm']:.1f}")
    except FileNotFoundError:
        print("まだ成績が記録されていません。")

def play(rounds: int = 5):
    # ... 既存のコード ...
    
    # 成績を保存
    save_result(correct, mistakes, wpm, score)
    
    # TOP5を表示
    show_top5()
```

ポイント：
- `csv.DictWriter`で辞書をCSVに追記
- ファイルが新規作成の場合のみヘッダーを書き込み
- `sorted(..., key=lambda r: r['score'], reverse=True)[:5]`でスコア順のTOP5を取得
- CSVから読み込む際は文字列を数値に変換

</details>







