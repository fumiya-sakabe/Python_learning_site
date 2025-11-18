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
<summary>解答を表示</summary>

- ループ内で`if time.time() - start > 30: break`
- スコア計測はそのまま、終了後に集計
</details>

2. ミスタイプ数に応じて減点するスコア式を導入してください。

<details>
<summary>解答を表示</summary>

- `score = correct * 10 - mistakes * 2` のような式を導入し表示
</details>

3. お題を外部ファイル（`words.txt`）から読み込めるようにしてください。

<details>
<summary>解答を表示</summary>

- 起動時に`with open('words.txt') as f: WORDS = [line.strip() for line in f if line.strip()]`
</details>

4. 成績を`results.csv`に追記して、最新TOP5を表示してください。

<details>
<summary>解答を表示</summary>

- `csv.DictWriter`で`{timestamp, correct, mistakes, wpm, score}`を追記
- 読み込み後に`sorted(..., key=lambda r: r['score'], reverse=True)[:5]`
</details>
