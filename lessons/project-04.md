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
<summary>解答を表示</summary>

- 一覧で`a[href]`を収集→`urljoin`で絶対URL化→各詳細ページを`fetch`→`parse_detail`で抽出
</details>

2. 連続アクセスしないように、1〜2秒のランダムスリープを入れてください。

<details>
<summary>解答を表示</summary>

- `time.sleep(random.uniform(1,2))`を各リクエスト間に挿入
</details>

3. 例外処理とリトライ（最大3回）を導入してください。

<details>
<summary>解答を表示</summary>

- `for attempt in range(3):
    try: ...; break
  except requests.RequestException: time.sleep(1)`
</details>

4. 取得結果をCSVだけでなくJSONにも保存してください。

<details>
<summary>解答を表示</summary>

- `json.dump(data, open('items.json','w',encoding='utf-8'), ensure_ascii=False, indent=2)`
</details>
