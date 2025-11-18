# ミニアプリ: 簡易家計簿（CLI＋CSV保存）

## このプロジェクトのゴール

- CSVを使ったデータ永続化を実装できる
- 追加・一覧・集計（合計/カテゴリ別）を実装できる
- 入出力と検証の基本を身につける

## 概要

CLIで収支を登録し、`records.csv`に保存します。カテゴリ別の合計を表示し、月次レポートも作成します。

## 要件

- フィールド: `id, date(YYYY-MM-DD), category, memo, amount(int)`
- コマンド: 追加、一覧、合計、カテゴリ別、削除
- 既定は当日の日付、金額は数値必須

## サンプルCSV

```csv
id,date,category,memo,amount
1,2025-01-01,food,ランチ,-800
2,2025-01-01,income,給与,250000
```

## 実装ステップ

1. CSVの読み書きユーティリティを作成
2. 入力検証（空文字/数値/日付形式）
3. 一覧と合計の実装
4. カテゴリ別集計

## 演習課題

1. 収支の追加機能を実装してください（CSVへ追記）。

<details>
<summary>解答を表示</summary>

- `csv.DictWriter`で行を追記
- `id`は最大ID+1で採番
</details>

2. 日付範囲でフィルタして一覧/合計を出せるようにしてください。

<details>
<summary>解答を表示</summary>

- `start<=date<=end`でフィルタ（`datetime.strptime`で比較）
</details>

3. カテゴリ別に合計を出力してください。

<details>
<summary>解答を表示</summary>

- `collections.defaultdict(int)`で`sum_by_cat[cat]+=amount`
</details>

4. 月次レポート（指定月の合計とカテゴリ別）を表示してください。

<details>
<summary>解答を表示</summary>

- `YYYY-MM`でstartswith判定し、合計とカテゴリ別を計算
</details>

5. 削除機能（指定IDを除外して再保存）を実装してください。

<details>
<summary>解答を表示</summary>

- レコードを読み込み→IDでフィルタ→上書き保存
</details>
