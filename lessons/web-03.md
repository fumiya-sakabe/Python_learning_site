# JavaScript超入門（DOMとイベント）

## このレッスンのゴール

- JavaScriptの読み込み方法と基本構文を理解する
- DOM要素の取得・書き換え・イベント登録ができる
- フォーム入力のバリデーションや簡単なインタラクションを実装できる

## なぜ重要なのか

Flaskだけではクライアント側のインタラクションが弱くなりがちです。  
JavaScriptの最低限を理解しておけば、フォームUX改善や非同期通信の準備ができます。

## 解説

### 1. 読み込み

```html
<script src="{{ url_for('static', filename='js/main.js') }}" defer></script>
```

`defer` を付けるとHTML解析後に実行され、DOM操作が安全。

### 2. 変数と関数

```javascript
const message = 'こんにちは';
function greet(name) {
  return `${message}、${name}さん`;
}
console.log(greet('太郎'));
```

### 3. DOM取得と操作

```javascript
const title = document.querySelector('h1');
title.textContent = 'ようこそ！';
title.classList.add('highlight');
```

### 4. イベント

```javascript
const button = document.querySelector('#cta');
button.addEventListener('click', () => {
  alert('クリックされました');
});
```

### 5. フォームバリデーション

```javascript
const form = document.querySelector('#contact-form');
form.addEventListener('submit', (e) => {
  const email = form.email.value.trim();
  if (!email.includes('@')) {
    e.preventDefault();
    alert('正しいメールアドレスを入力してください');
  }
});
```

## よくある間違い

- `<script>` を `<head>` に置いて `defer` を付け忘れ、DOMが未読込でエラー
- `querySelectorAll` はNodeListを返すので `forEach` で回す必要を忘れる
- `preventDefault()` を使わずバリデーション前にフォームが送信される

## 演習課題

1. ボタンを押すたびにカウンターの数字が1増えるUIを作ってください。

<details>
<summary>解答を表示</summary>

```html
<p>クリック数: <span id="count">0</span></p>
<button id="increment">増やす</button>
<script>
  const countEl = document.getElementById('count');
  const btn = document.getElementById('increment');
  let count = 0;
  btn.addEventListener('click', () => {
    count += 1;
    countEl.textContent = count;
  });
</script>
```
</details>

2. タブ切り替えを実装し、クリックしたタブのみ内容を表示してください。

<details>
<summary>解答を表示</summary>

```javascript
const tabs = document.querySelectorAll('[data-tab]');
const panels = document.querySelectorAll('[data-panel]');
tabs.forEach(tab => {
  tab.addEventListener('click', () => {
    const target = tab.dataset.tab;
    panels.forEach(panel => {
      panel.hidden = panel.dataset.panel !== target;
    });
  });
});
```
</details>

3. フォームで空欄があれば送信を止め、エラーメッセージを表示してください。

<details>
<summary>解答を表示</summary>

```javascript
form.addEventListener('submit', (e) => {
  const name = form.name.value.trim();
  if (!name) {
    e.preventDefault();
    document.querySelector('.error').textContent = '名前は必須です';
  }
});
```
</details>

4. ライト/ダークモード切り替えボタンを実装し、`body` にクラスを付け替えてください。

<details>
<summary>解答を表示</summary>

```javascript
const toggle = document.querySelector('#theme-toggle');
toggle.addEventListener('click', () => {
  document.body.classList.toggle('dark');
});
```
</details>

## まとめ

- JavaScriptはブラウザ上で動くスクリプト言語
- DOM操作とイベントができれば基本的なUI操作が可能
- 次のレッスンでfetchとAPI連携を学び、Flaskとつなげましょう

