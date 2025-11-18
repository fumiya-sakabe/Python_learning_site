# ブラウザとFlaskの連携（fetchとAPI）

## このレッスンのゴール

- `fetch` を使ってFlaskのAPIとデータをやり取りできる
- JSONの送受信とエラーハンドリングの基本を理解する
- CSRFやCORSなど安全面の注意点を把握する
- 小さなフロントエンドアプリからバックエンドを操作できる

## なぜ重要なのか

FlaskアプリをモダンなUIにしたい場合、非同期通信が欠かせません。  
`fetch` を使えばページ遷移なしで学習記録の保存・チェック機能などを実装できます。

## 解説

### 1. Flask側のJSON API（例）

```python
@app.route('/api/memos', methods=['POST'])
def api_memos():
    payload = request.get_json()
    title = payload.get('title')
    # 保存処理...
    return jsonify({"ok": True, "title": title})
```

### 2. フロント側の`fetch`

```javascript
const form = document.querySelector('#memo-form');
form.addEventListener('submit', async (e) => {
  e.preventDefault();
  const body = {
    title: form.title.value,
    content: form.content.value,
  };
  const res = await fetch('/api/memos', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(body),
  });
  const data = await res.json();
  if (data.ok) {
    alert('保存しました');
  }
});
```

### 3. レスポンスのバリデーション

```javascript
if (!res.ok) {
  throw new Error('サーバーエラー');
}
```

### 4. CSRFへの注意

Flask-WTFや自作CSRFトークンをヘッダーに送る。例：

```javascript
headers: {
  'Content-Type': 'application/json',
  'X-CSRFToken': document.querySelector('meta[name="csrf-token"]').content
}
```

### 5. ローディング表示

```javascript
toggleLoading(true);
try {
  // fetch
} finally {
  toggleLoading(false);
}
```

## よくある間違い

- `fetch` の戻りは常に成功扱いなので `res.ok` を見ない
- JSONを送るのに `JSON.stringify` を忘れる
- `Content-Type` を `application/json` にせずサーバーでパース失敗
- CSRFトークンを送らずPOSTが弾かれる

## 演習課題

1. Flaskで`/api/likes`（POST）を作り、`count`を返却してください。

<details>
<summary>解答を表示</summary>

```python
likes = 0

@app.route('/api/likes', methods=['POST'])
def api_likes():
    global likes
    likes += 1
    return jsonify({"count": likes})
```
</details>

2. ボタンをクリックすると`/api/likes`を呼び出し、最新カウントを表示してください。

<details>
<summary>解答を表示</summary>

```javascript
document.querySelector('#like-btn').addEventListener('click', async () => {
  const res = await fetch('/api/likes', { method: 'POST' });
  const data = await res.json();
  document.querySelector('#like-count').textContent = data.count;
});
```
</details>

3. エラー時にユーザーへメッセージを出す仕組みを追加してください。

<details>
<summary>解答を表示</summary>

```javascript
try {
  const res = await fetch('/api/likes', { method: 'POST' });
  if (!res.ok) throw new Error('サーバーエラー');
} catch (err) {
  document.querySelector('.error').textContent = err.message;
}
```
</details>

4. `fetch` の前にボタンを無効化し、完了後に戻す処理を追加してください。

<details>
<summary>解答を表示</summary>

```javascript
const btn = document.querySelector('#like-btn');
btn.disabled = true;
try {
  // fetch処理
} finally {
  btn.disabled = false;
}
```
</details>

## まとめ

- Flask側にJSON APIを用意し、`fetch` で非同期通信
- `res.ok` や例外処理でエラーハンドリング
- CSRFトークンやローディングUIを忘れずに
- ここまで押さえれば `flask-01` 以降の内容が理解しやすくなります

