# ミニアプリ: Webスクレイピング入門

## このプロジェクトのゴール

- `requests`と`BeautifulSoup`を使ってHTMLを取得・解析できる
- 必要なデータを抽出してCSV/JSONに保存できる
- 簡単なレート制限・例外処理を実装できる

## 注意

- 利用規約/robots.txtを必ず確認してください
- アクセスの礼儀（短いディレイ、過剰リクエスト禁止）

## 準備

```bash
pip install requests beautifulsoup4
```

## サンプルコード（最小）

```python
import time
import csv
import requests
from bs4 import BeautifulSoup

URL = 'https://example.com'


def fetch(url: str) -> str:
    headers = {'User-Agent': 'Mozilla/5.0'}
    r = requests.get(url, headers=headers, timeout=10)
    r.raise_for_status()
    return r.text


def parse(html: str):
    soup = BeautifulSoup(html, 'html.parser')
    # 例: タイトル一覧を抽出
    return [h.get_text(strip=True) for h in soup.select('h2')]


def main():
    html = fetch(URL)
    items = parse(html)
    with open('items.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['title'])
        for t in items:
            writer.writerow([t])

if __name__ == '__main__':
    main()
```

## 演習課題

1. 一覧ページから詳細ページのリンクを辿って、詳細情報（例: 著者・日付）も取得してください。

<details>
<summary>💡 解答を見る</summary>

解答：

一覧ページから詳細ページへのリンクを収集し、各詳細ページを取得して詳細情報を抽出します。

実装例：

```python
from urllib.parse import urljoin

def fetch_list_page(url: str):
    """一覧ページを取得"""
    html = fetch(url)
    soup = BeautifulSoup(html, 'html.parser')
    
    # 詳細ページへのリンクを収集
    detail_links = []
    for link in soup.select('a[href]'):
        href = link.get('href')
        if href:
            # 相対URLを絶対URLに変換
            absolute_url = urljoin(url, href)
            detail_links.append(absolute_url)
    
    return detail_links

def parse_detail(html: str):
    """詳細ページから情報を抽出"""
    soup = BeautifulSoup(html, 'html.parser')
    
    # 例: タイトル、著者、日付を抽出
    title = soup.select_one('h1').get_text(strip=True) if soup.select_one('h1') else 'N/A'
    author = soup.select_one('.author').get_text(strip=True) if soup.select_one('.author') else 'N/A'
    date = soup.select_one('.date').get_text(strip=True) if soup.select_one('.date') else 'N/A'
    
    return {
        'title': title,
        'author': author,
        'date': date
    }

def scrape_with_details(list_url: str):
    """一覧ページから詳細ページを辿って情報を取得"""
    detail_links = fetch_list_page(list_url)
    
    results = []
    for detail_url in detail_links:
        html = fetch(detail_url)
        detail_info = parse_detail(html)
        detail_info['url'] = detail_url
        results.append(detail_info)
    
    return results

# 使用例
results = scrape_with_details('https://example.com/list')
for r in results:
    print(f"タイトル: {r['title']}, 著者: {r['author']}, 日付: {r['date']}")
```

ポイント：
- `soup.select('a[href]')`でリンクを収集
- `urljoin(base_url, relative_url)`で相対URLを絶対URLに変換
- 各詳細ページを`fetch`して`parse_detail`で情報を抽出
- セレクタ（`.author`, `.date`など）は対象サイトに合わせて調整

</details>

2. 連続アクセスしないように、1〜2秒のランダムスリープを入れてください。

<details>
<summary>💡 解答を見る</summary>

解答：

各リクエストの間にランダムなスリープを入れて、サーバーに負荷をかけないようにします。

実装例：

```python
import random
import time

def fetch_with_delay(url: str, delay_min: float = 1.0, delay_max: float = 2.0):
    """リクエストの間にランダムスリープを入れる"""
    headers = {'User-Agent': 'Mozilla/5.0'}
    r = requests.get(url, headers=headers, timeout=10)
    r.raise_for_status()
    
    # 1〜2秒のランダムスリープ
    sleep_time = random.uniform(delay_min, delay_max)
    time.sleep(sleep_time)
    
    return r.text

def scrape_with_delay(list_url: str):
    """遅延を入れてスクレイピング"""
    detail_links = fetch_list_page(list_url)
    
    results = []
    for i, detail_url in enumerate(detail_links, 1):
        print(f"処理中 ({i}/{len(detail_links)}): {detail_url}")
        
        html = fetch_with_delay(detail_url)  # 遅延あり
        detail_info = parse_detail(html)
        results.append(detail_info)
    
    return results

# 使用例
results = scrape_with_delay('https://example.com/list')
```

ポイント：
- `random.uniform(1, 2)`で1〜2秒のランダムな時間を生成
- `time.sleep()`で処理を一時停止
- 各リクエストの後にスリープを入れる
- 進行状況を表示して、ユーザーに待っていることを伝える

</details>

3. 例外処理とリトライ（最大3回）を導入してください。

<details>
<summary>💡 解答を見る</summary>

解答：

ネットワークエラーやタイムアウトなどの例外をキャッチし、最大3回までリトライします。

実装例：

```python
def fetch_with_retry(url: str, max_attempts: int = 3):
    """リトライ機能付きのリクエスト"""
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    for attempt in range(max_attempts):
        try:
            r = requests.get(url, headers=headers, timeout=10)
            r.raise_for_status()
            return r.text
        except requests.RequestException as e:
            if attempt < max_attempts - 1:
                print(f"⚠️ リクエストエラー（{attempt + 1}回目）: {e}")
                print(f"   1秒後にリトライします...")
                time.sleep(1)
            else:
                print(f"❌ 最大リトライ回数に達しました: {url}")
                raise  # 最後の試行でも失敗したら例外を再発生
    
    return None

def scrape_with_retry(list_url: str):
    """リトライ機能付きでスクレイピング"""
    detail_links = fetch_list_page(list_url)
    
    results = []
    for detail_url in detail_links:
        try:
            html = fetch_with_retry(detail_url)
            if html:
                detail_info = parse_detail(html)
                results.append(detail_info)
        except Exception as e:
            print(f"⚠️ {detail_url} の処理をスキップしました: {e}")
            continue  # エラーがあっても続行
    
    return results

# 使用例
results = scrape_with_retry('https://example.com/list')
```

ポイント：
- `for attempt in range(max_attempts)`で最大3回まで試行
- `try/except requests.RequestException`でネットワークエラーをキャッチ
- リトライ前に1秒スリープしてサーバー負荷を軽減
- 最後の試行でも失敗した場合は例外を再発生
- 1つのURLでエラーがあっても、他のURLの処理は続行

</details>

4. 取得結果をCSVだけでなくJSONにも保存してください。

<details>
<summary>💡 解答を見る</summary>

解答：

取得したデータをCSVとJSONの両方の形式で保存します。

実装例：

```python
import json

def save_to_csv(results, filename: str = 'items.csv'):
    """CSV形式で保存"""
    if not results:
        return
    
    with open(filename, 'w', encoding='utf-8', newline='') as f:
        fieldnames = list(results[0].keys())  # 最初の要素のキーを取得
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(results)
    
    print(f"✅ CSVに保存しました: {filename}")

def save_to_json(results, filename: str = 'items.json'):
    """JSON形式で保存"""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    
    print(f"✅ JSONに保存しました: {filename}")

def main():
    html = fetch(URL)
    items = parse(html)
    
    # CSVとJSONの両方で保存
    save_to_csv(items, 'items.csv')
    save_to_json(items, 'items.json')

# 使用例
results = scrape_with_retry('https://example.com/list')
save_to_csv(results, 'results.csv')
save_to_json(results, 'results.json')
```

ポイント：
- `json.dump()`でJSON形式で保存
- `ensure_ascii=False`で日本語を正しく保存
- `indent=2`で見やすい形式に整形
- CSVとJSONの両方で保存することで、用途に応じて使い分け可能

</details>







