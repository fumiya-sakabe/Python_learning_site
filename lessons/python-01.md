# Python開発環境の準備

## このレッスンのゴール

- Pythonを自分のPCにインストールできる
- 仮想環境を作成して、プロジェクトごとに環境を分けられる
- コードを書くエディタ（VS Code や Cursor）を用意できる
- ターミナルから Python を実行できる

## なぜ重要なのか

プログラミング学習は、「環境構築でつまずいて終わる」というパターンが非常に多いです。

最初に環境をきちんと整えておくと、今後の学習がスムーズに進みます。

また、仮想環境を使う習慣を最初から身につけることで、実務に近い形で学ぶことができます。

ポートフォリオ制作や実際の開発現場でも、環境を適切に管理することは必須のスキルです。

## 解説

### 1. Pythonのインストール

公式サイトからインストーラをダウンロードしてインストールします。

- Python公式サイト: https://www.python.org/
- すでにインストール済みの場合はバージョンを確認しましょう。

<strong class="highlight">Windowsの場合:</strong>
```bash
python --version
```

<strong class="highlight">macOS/Linuxの場合:</strong>
```bash
python3 --version
```

推奨バージョン: Python 3.11以上

インストールが完了したら、再度バージョンを確認して正しくインストールされたか確認しましょう。

### 2. 仮想環境の作成

プロジェクトごとに独立した環境を作成することで、パッケージの競合を避けることができます。

仮想環境を使うことで、異なるプロジェクトで異なるバージョンのパッケージを使い分けることができます。

```bash
python -m venv venv
```

または、macOS/Linuxの場合：

```bash
python3 -m venv venv
```

これで、プロジェクトフォルダ内に`venv`という名前の仮想環境が作成されます。

### 3. 仮想環境の有効化

仮想環境を作成したら、有効化する必要があります。

<strong class="highlight">Windowsの場合:</strong>
```bash
venv\Scripts\activate
```

<strong class="highlight">macOS/Linuxの場合:</strong>
```bash
source venv/bin/activate
```

有効化に成功すると、ターミナルのプロンプトの前に`(venv)`と表示されます。

```bash
(venv) $ python --version
```

仮想環境を無効化するには：

```bash
deactivate
```

### 4. パッケージのインストール

必要なパッケージをインストールするには、`pip`を使用します。

```bash
pip install flask
```

または、`requirements.txt`がある場合は：

```bash
pip install -r requirements.txt
```

インストールされたパッケージを確認するには：

```bash
pip list
```

### 5. エディタの設定

Pythonの開発には、適切なエディタを使用することが重要です。

推奨エディタ：
- <strong class="term">Visual Studio Code</strong>: 無料で高機能、拡張機能が豊富（本教材ではVS Codeを前提に解説します）

VS Codeをインストールしたら、Python拡張機能を入れておくと補完やデバッグが使いやすくなります。

### 6. Visual Studio Code の初期設定（無料）

1. VS Code公式サイト https://code.visualstudio.com/ からダウンロード＆インストール  
2. 起動後、左サイドバー「Extensions」から以下をインストール  
   - `Python`（Microsoft）  
   - `Pylance`（推奨）  
   - `Black Formatter`（必要に応じて）
3. コマンドパレット（`⌘⇧P` / `Ctrl+Shift+P`）→ `Python: Select Interpreter` → プロジェクトの `venv` 内の Python を選択
4. `.py` ファイルを開いて右上の「Run」ボタン、または内蔵ターミナルで `python file.py`

#### VS Codeを日本語化したい場合

1. コマンドパレットで `Configure Display Language` を実行  
2. `Language Pack for Japanese (日本語)` をインストール  
3. `ja` を選択し、再起動するとメニューなどが日本語表示になります

#### 便利な設定

- `設定 > 検索` で「format on save」をON（`editor.formatOnSave: true`）
- `settings.json` で `"[python]": {"editor.defaultFormatter": "ms-python.black-formatter"}` を設定するとBlackで整形

## よくある間違い

- 仮想環境を作成しても有効化し忘れる（プロンプトに`(venv)`が表示されていない）
- システムのPythonと仮想環境のPythonを混同する
- 仮想環境を作成する場所を間違える（プロジェクトフォルダ内で実行する）
- エディタとPythonの連携がうまくいかない（エディタ側でPythonインタープリターを正しく指定する必要がある）
- パッケージをシステムに直接インストールしてしまう（必ず仮想環境を有効化してからインストールする）

## 演習課題

問1. Pythonが正しくインストールされているか確認し、バージョンを表示してください。

<details>
<summary>解答を表示</summary>

```bash
python --version   # または macOS/Linuxでは python3 --version
```

出力例: `Python 3.11.x`
</details>

問2. 新しいフォルダを作成し、その中で仮想環境を作成して有効化してください。

<details>
<summary>解答を表示</summary>

```bash
mkdir myproject && cd myproject
python -m venv venv          # macOS/Linux は python3 -m venv venv
# 有効化
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

プロンプト先頭に`(venv)`が表示されていればOKです。
</details>

問3. 仮想環境が有効化されていることを確認し（プロンプトに`(venv)`が表示される）、`pip list`コマンドで現在インストールされているパッケージを確認してください。

<details>
<summary>解答を表示</summary>

```bash
(venv) pip list
```

初期状態ではほとんど空（`pip`, `setuptools`, `wheel`など）です。
</details>

問4. 簡単なテスト用パッケージ（例：`requests`）をインストールし、`pip list`で確認してください。

<details>
<summary>解答を表示</summary>

```bash
(venv) pip install requests
(venv) pip list | grep requests   # Windowsは findstr requests
```

`requests 2.x.x`のように表示されればOKです。
</details>

問5. エディタでPythonファイルを作成し、以下のコードを実行してみてください：

```python
print("Hello, Python!")
```

<details>
<summary>解答を表示</summary>

```bash
(venv) python hello.py
```

出力: `Hello, Python!`
</details>

## まとめ

このレッスンでは、Python開発環境の準備について学びました。

- Pythonのインストール方法
- 仮想環境の作成と有効化
- パッケージのインストール方法
- エディタの選び方

これらの準備が整ったら、次のレッスンでPythonの基本的な文法を学んでいきましょう。
