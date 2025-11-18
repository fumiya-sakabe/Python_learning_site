# HTMLの基本（構造とよく使うタグ）

## このレッスンのゴール

- HTMLの役割と基本構造（`<!DOCTYPE html>`〜`</html>`）を理解する
- よく使うタグ（`h1`、`p`、`a`、`img`、`ul/li` など）を使い分けられる
- セマンティックタグ（`header`、`main`、`footer` など）の意味を理解する
- シンプルなLPやプロフィールページを自力で組み立てられる

## なぜ重要なのか

FlaskでHTMLテンプレートを扱う前に、HTMLそのものを理解していないとレイアウトや情報設計で迷子になります。  
また、セマンティックなタグを使うことでアクセシビリティやSEOにも好影響があります。

## 解説

### 1. HTML文書の骨組み

```html
<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <title>ページタイトル</title>
</head>
<body>
  <!-- ここにコンテンツ -->
</body>
</html>
```

### 2. 見出し・段落・リンク

```html
<h1>メイン見出し</h1>
<h2>セクション見出し</h2>
<p>これは段落です。<a href="https://example.com">リンク</a>も書けます。</p>
```

### 3. 画像とリスト

```html
<img src="images/logo.png" alt="ロゴ">

<ul>
  <li>箇条書き1</li>
  <li>箇条書き2</li>
</ul>
```

### 4. セマンティックレイアウト

```html
<header>ヘッダー</header>
<nav>ナビゲーション</nav>
<main>
  <section>
    <h2>セクション</h2>
  </section>
</main>
<footer>フッター</footer>
```

### 5. フォームの基本

```html
<form action="/contact" method="post">
  <label>名前: <input type="text" name="name"></label>
  <label>メール: <input type="email" name="email"></label>
  <button type="submit">送信</button>
</form>
```

## よくある間違い

- `lang` や `meta charset` を忘れて文字化けする
- すべて `div` で書いてセマンティクスが失われる
- 画像の `alt` 属性を空にしてしまいアクセシビリティが落ちる
- `form` の `method` や `name` 属性を付け忘れてサーバーで値が取れない

## 演習課題

1. ヒーロー見出しとCTAボタンを持つLPを作ってください。

<details>
<summary>解答を表示</summary>

```html
<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <title>シンプルLP</title>
</head>
<body>
  <header>
    <h1>Python×Webでキャリアを始めよう</h1>
    <p>基礎からデプロイまで一続きで学ぶカリキュラム</p>
    <a href="#signup">今すぐ体験</a>
  </header>
</body>
</html>
```
</details>

2. プロフィールセクションを作り、画像＋自己紹介＋SNSリンクを並べてください。

<details>
<summary>解答を表示</summary>

```html
<section class="profile">
  <img src="me.jpg" alt="プロフィール写真">
  <h2>山田太郎</h2>
  <p>文系出身。PythonでWebアプリを開発中。</p>
  <ul>
    <li><a href="https://github.com/example">GitHub</a></li>
    <li><a href="https://twitter.com/example">X</a></li>
  </ul>
</section>
```
</details>

3. `header/nav/main/footer` を使ったレイアウトを作り、`main` 内に2つの `section` を用意してください。

<details>
<summary>解答を表示</summary>

```html
<header>サイトタイトル</header>
<nav>
  <a href="#about">About</a>
  <a href="#features">Features</a>
</nav>
<main>
  <section id="about">
    <h2>このサイトについて</h2>
  </section>
  <section id="features">
    <h2>特徴</h2>
  </section>
</main>
<footer>© 2025</footer>
```
</details>

4. 問い合わせフォーム（名前、メール、質問内容、送信ボタン）を作ってください。

<details>
<summary>解答を表示</summary>

```html
<form action="/contact" method="post">
  <label>名前<input type="text" name="name" required></label>
  <label>メール<input type="email" name="email" required></label>
  <label>質問<textarea name="message" rows="4"></textarea></label>
  <button type="submit">送信</button>
</form>
```
</details>

## まとめ

- HTMLはWebページの骨格を作る言語で、構造と意味を正しく伝えることが大切
- 見出し・文章・リスト・リンク・画像を組み合わせて情報を整理
- セマンティックタグを意識するとアクセシビリティとSEOが向上
- 次はCSSでデザインを整えていきましょう

