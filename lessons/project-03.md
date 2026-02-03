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
<summary>💡 解答を見る</summary>

解答：

収支データをCSVファイルに追記します。`id`は既存の最大IDに1を足して採番します。

実装例：

```python
import csv
from datetime import datetime

FILE = 'records.csv'

def load_records():
    """CSVから記録を読み込む"""
    records = []
    try:
        with open(FILE, 'r', encoding='utf-8', newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                row['id'] = int(row['id'])
                row['amount'] = int(row['amount'])
                records.append(row)
    except FileNotFoundError:
        pass
    return records

def get_next_id(records):
    """次のIDを取得（最大ID+1）"""
    if not records:
        return 1
    return max(r['id'] for r in records) + 1

def add_record(date: str, category: str, memo: str, amount: int):
    """収支を追加（CSVへ追記）"""
    records = load_records()
    new_id = get_next_id(records)
    
    new_record = {
        'id': new_id,
        'date': date,
        'category': category,
        'memo': memo,
        'amount': amount
    }
    
    file_exists = os.path.exists(FILE)
    with open(FILE, 'a', encoding='utf-8', newline='') as f:
        fieldnames = ['id', 'date', 'category', 'memo', 'amount']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()
        writer.writerow(new_record)
    
    print(f"✅ 追加しました: ID={new_id}, {date}, {category}, {memo}, {amount}円")

# 使用例
add_record('2025-01-01', 'food', 'ランチ', -800)
add_record('2025-01-01', 'income', '給与', 250000)
```

ポイント：
- `csv.DictWriter`で行を追記（`'a'`モード）
- `get_next_id()`で最大IDを取得して+1
- ファイルが新規作成の場合のみヘッダーを書き込み

</details>

2. 日付範囲でフィルタして一覧/合計を出せるようにしてください。

<details>
<summary>💡 解答を見る</summary>

解答：

指定した日付範囲の記録だけをフィルタリングして、一覧表示や合計を計算します。

実装例：

```python
from datetime import datetime

def filter_by_date_range(records, start_date: str = None, end_date: str = None):
    """日付範囲でフィルタ"""
    if not start_date and not end_date:
        return records
    
    filtered = []
    for r in records:
        record_date = datetime.strptime(r['date'], '%Y-%m-%d').date()
        
        if start_date:
            start = datetime.strptime(start_date, '%Y-%m-%d').date()
            if record_date < start:
                continue
        
        if end_date:
            end = datetime.strptime(end_date, '%Y-%m-%d').date()
            if record_date > end:
                continue
        
        filtered.append(r)
    
    return filtered

def list_records(start_date: str = None, end_date: str = None):
    """一覧を表示"""
    records = load_records()
    filtered = filter_by_date_range(records, start_date, end_date)
    
    if not filtered:
        print("該当する記録がありません。")
        return
    
    print(f"\n記録一覧 ({len(filtered)}件):")
    for r in filtered:
        print(f"ID={r['id']}, {r['date']}, {r['category']}, {r['memo']}, {r['amount']:,}円")

def calculate_total(start_date: str = None, end_date: str = None):
    """合計を計算"""
    records = load_records()
    filtered = filter_by_date_range(records, start_date, end_date)
    total = sum(r['amount'] for r in filtered)
    print(f"\n合計: {total:,}円 ({len(filtered)}件)")
    return total

# 使用例
list_records('2025-01-01', '2025-01-31')  # 1月分のみ
calculate_total('2025-01-01', '2025-01-31')
```

ポイント：
- `datetime.strptime()`で文字列を日付オブジェクトに変換
- `start <= date <= end`の範囲でフィルタリング
- `start_date`や`end_date`が`None`の場合は制限なし

</details>

3. カテゴリ別に合計を出力してください。

<details>
<summary>💡 解答を見る</summary>

解答：

`collections.defaultdict`を使って、カテゴリごとの合計金額を計算します。

実装例：

```python
from collections import defaultdict

def calculate_by_category(records):
    """カテゴリ別の合計を計算"""
    sum_by_cat = defaultdict(int)
    
    for r in records:
        category = r['category']
        amount = r['amount']
        sum_by_cat[category] += amount
    
    return dict(sum_by_cat)

def show_category_summary(start_date: str = None, end_date: str = None):
    """カテゴリ別の合計を表示"""
    records = load_records()
    filtered = filter_by_date_range(records, start_date, end_date)
    category_totals = calculate_by_category(filtered)
    
    if not category_totals:
        print("該当する記録がありません。")
        return
    
    print("\nカテゴリ別合計:")
    for category, total in sorted(category_totals.items()):
        print(f"  {category}: {total:,}円")

# 使用例
show_category_summary()  # 全期間
show_category_summary('2025-01-01', '2025-01-31')  # 1月分のみ
```

ポイント：
- `defaultdict(int)`で、存在しないキーでも0を返す辞書を作成
- `sum_by_cat[cat] += amount`でカテゴリごとに合計を累積
- `dict()`に変換して通常の辞書として返す

</details>

4. 月次レポート（指定月の合計とカテゴリ別）を表示してください。

<details>
<summary>💡 解答を見る</summary>

解答：

指定した年月（例：`2025-01`）の記録をフィルタリングして、合計とカテゴリ別の集計を表示します。

実装例：

```python
def monthly_report(year_month: str):
    """月次レポートを表示（例: '2025-01'）"""
    records = load_records()
    
    # 年月でフィルタ（YYYY-MMで始まる日付）
    monthly_records = [r for r in records if r['date'].startswith(year_month)]
    
    if not monthly_records:
        print(f"{year_month}の記録がありません。")
        return
    
    print(f"\n📊 {year_month}の月次レポート")
    print("=" * 50)
    
    # 合計
    total = sum(r['amount'] for r in monthly_records)
    print(f"合計: {total:,}円 ({len(monthly_records)}件)")
    
    # カテゴリ別
    category_totals = calculate_by_category(monthly_records)
    print("\nカテゴリ別:")
    for category, amount in sorted(category_totals.items(), key=lambda x: abs(x[1]), reverse=True):
        print(f"  {category}: {amount:,}円")
    
    # 収入と支出を分ける
    income = sum(r['amount'] for r in monthly_records if r['amount'] > 0)
    expense = sum(r['amount'] for r in monthly_records if r['amount'] < 0)
    
    print(f"\n収入: {income:,}円")
    print(f"支出: {abs(expense):,}円")
    print(f"差額: {income + expense:,}円")  # 収入 + 支出（負の値）

# 使用例
monthly_report('2025-01')
```

ポイント：
- `r['date'].startswith(year_month)`で年月でフィルタリング
- 合計とカテゴリ別の両方を表示
- 収入（正の値）と支出（負の値）を分けて表示

</details>

5. 削除機能（指定IDを除外して再保存）を実装してください。

<details>
<summary>💡 解答を見る</summary>

解答：

指定したIDの記録を除外して、残りの記録をCSVに上書き保存します。

実装例：

```python
def delete_record(record_id: int):
    """指定IDの記録を削除"""
    records = load_records()
    
    # 指定IDを除外
    before_count = len(records)
    records = [r for r in records if r['id'] != record_id]
    after_count = len(records)
    
    if before_count == after_count:
        print(f"⚠️ ID {record_id} が見つかりませんでした。")
        return False
    
    # 上書き保存
    with open(FILE, 'w', encoding='utf-8', newline='') as f:
        fieldnames = ['id', 'date', 'category', 'memo', 'amount']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        
        for r in records:
            writer.writerow(r)
    
    print(f"✅ ID {record_id} を削除しました。")
    return True

# 使用例
delete_record(1)  # ID=1の記録を削除
```

ポイント：
- リスト内包表記で指定IDを除外：`[r for r in records if r['id'] != record_id]`
- `'w'`モードで上書き保存（`'a'`ではない）
- 削除前後で件数を比較して、削除できたか確認
- ヘッダーも含めて全て書き直す

</details>







