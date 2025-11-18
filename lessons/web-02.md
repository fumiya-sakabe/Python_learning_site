# CSSの基本（レイアウトとデザイン）

## このレッスンのゴール

- CSSの仕組み（セレクタ、プロパティ、継承）を理解する
- ボックスモデルとレイアウト（Flexbox/グリッド）の基礎を押さえる
- レスポンシブデザインの考え方を知る
- HTMLで作ったLPをスタイリングできる

## なぜ重要なのか

Flaskでテンプレートを構築しても、スタイルが整っていないとユーザー体験は向上しません。  
また、CSSを理解すれば、フロントエンドエンジニアとの連携もスムーズになります。

## 解説

### 1. CSSの適用方法

```html
<link rel="stylesheet" href="/static/css/style.css">
```

```css
h1 {
  color: #1a1a1a;
}
```

### 2. セレクタと基本プロパティ

```css
/* クラス */
.hero {
  text-align: center;
  padding: 60px 20px;
}

/* 子孫セレクタ */
.hero h1 {
  font-size: 2.4rem;
}
```

### 3. ボックスモデル

```css
.card {
  border: 1px solid #ddd;
  padding: 16px;
  margin: 12px;
  box-shadow: 0 4px 12px rgba(0,0,0,0.08);
}
```

### 4. Flexbox

```css
.features {
  display: flex;
  gap: 24px;
}

.features .item {
  flex: 1;
}
```

### 5. レスポンシブ（メディアクエリ）

```css
@media (max-width: 768px) {
  .features {
    flex-direction: column;
  }
}
```

### 6. グローバルスタイル

```css
:root {
  --primary: #1f7aec;
}

body {
  font-family: "Noto Sans JP", sans-serif;
  color: #333;
  line-height: 1.6;
}
```

## よくある間違い

- CSSファイルを読み込むパスを間違える（Flaskでは `url_for('static', filename='css/style.css')`）
- 幅と余白の関係を理解せずレイアウトが崩れる
- メディアクエリを書いたのに指定順序で上書きされて効かない
- 同じスタイルを何度も書いて管理が大変になる

## サンプルデザイン課題

以下の仕様でヒーローセクションを再現してみましょう。

- 背景は `#1f7aec → #7f68f6` の斜めグラデーション
- 最大幅 1200px、中央寄せ、上下100pxの余白
- タイトル36px・太字、サブタイトル18px/80%の白
- Primaryボタン、Outlineボタンの2種類（ホバー時にシャドウ）
- 横幅768px以下ではPaddingとフォントを少し小さくし、ボタンを縦積み

ヒント:

```css
.hero {
  background: linear-gradient(135deg, #1f7aec, #7f68f6);
  color: #fff;
  padding: 100px 20px;
  text-align: center;
}
.hero-buttons {
  display: flex;
  gap: 16px;
  justify-content: center;
  flex-wrap: wrap;
}
.hero .btn-outline {
  background: transparent;
  border: 2px solid #fff;
  color: #fff;
}
@media (max-width: 768px) {
  .hero {
    padding: 70px 16px;
  }
  .hero-buttons {
    flex-direction: column;
  }
}
```

完成したらスクリーンショットを撮影し、学習記録やポートフォリオに添付すると実績になります。

## 演習課題

1. `.hero` セクションを中央揃えし、背景をグラデーションにしてください。

<details>
<summary>解答を表示</summary>

```css
.hero {
  text-align: center;
  padding: 80px 20px;
  color: #fff;
  background: linear-gradient(135deg, #1f7aec, #7f68f6);
}
```
</details>

2. 3つのカードを横並びにし、スマホでは縦並びにしてください。

<details>
<summary>解答を表示</summary>

```css
.cards {
  display: flex;
  gap: 20px;
}
.card {
  flex: 1;
}
@media (max-width: 768px) {
  .cards {
    flex-direction: column;
  }
}
```
</details>

3. ナビゲーションで現在のページを強調表示してください。

<details>
<summary>解答を表示</summary>

```css
.nav a {
  padding: 8px 16px;
  border-radius: 999px;
}
.nav a.active {
  background: var(--primary);
  color: #fff;
}
```
</details>

4. `section` にスクロールマージンを設定し、アンカーリンク時に上部が隠れないようにしてください。

<details>
<summary>解答を表示</summary>

```css
section {
  scroll-margin-top: 80px;
}
```
</details>

## まとめ

- CSSは見た目とレイアウトを定義する言語
- ボックスモデルとFlexboxを押さえると多くのUIが組める
- メディアクエリでレスポンシブ対応
- 次はJavaScriptでインタラクションを加えましょう

