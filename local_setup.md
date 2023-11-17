# セットアップ手順
## 事前準備

### プロジェクトの準備
以下のコマンドでサンプル コードをローカルにクローンしてください。

```cli
git clone https://github.com/marumaru1019/openai-client.git
```

### 5 章文章検索アプリのデプロイ
[5 章文章検索アプリ](https://github.com/Azure-Samples/jp-azureopenai-samples/tree/main/5.internal-document-search) をセットアップガイドに従って自分のサブスクリプションにデプロイしてください。


## 実行

### 5 章: 文章検索アプリと APIM のつなぎこみ
1. api management を作成して下さい。
    以下の項目にないものは、デフォルトの設定にしてください。

    | 設定名 | 設定値 |
    | ---- | ---- |
    | サブスクリプション | 5 章をデプロイしたのと同じサブスクリプション |
    | リソースグループ | 任意 (5 章をデプロイしたのと同じである必要なし) |
    | リージョン | Japan East |
    | リソース名 | 任意 |
    | 組織名 | 任意 |
    | 管理者のメールアドレス | 任意 |
    | 価格レベル | 任意 |
    | 仮想ネットワーク | なし |

1. 左のナビゲーション メニューから「API > Add API > App Service」を選択してください。
![image](https://github.com/marumaru1019/github-image/assets/70362624/55a46c57-16ee-4c12-808f-1480bd66b0cc)
1. Browse から 5 章でデプロイした App Service を選択してください。
![image](https://github.com/marumaru1019/github-image/assets/70362624/472dc0de-ebab-4780-8b62-88c23ad51813)
1. All APIs から該当の API を選択して、Subscription Required をオフにしてください。

### ローカルでのアプリケーションの起動
1. サンプル コードをクローンしたディレクトリまで移動してください。
    ```
    cd /path/to/openai-client
    ```
1. Python の仮想環境を作成して、アクティベートしてください。
    ```
    python -m venv .venv(任意の環境名)
    ```
1. 作成した仮想環境をアクティベートしてください。
    ```
    .venv\Scripts\activate
    ```
1. 必要なライブラリをインストールしてください。
    ```
    pip install -r requirements.txt
    ```
1. `.env-sample` を `.env` という名前でコピーして、中身を自身の環境変数で置き換えてください。
    ```
    cp .env-sample .env
    ```
1. アプリケーションを起動してください。
    ```
    python -m streamlit run app.py --server.port 8000
    ```
1. ブラウザで http://localhost:8000 にアクセスしてください。
![image](https://github.com/marumaru1019/kagawa-iris-classification/assets/70362624/3af500ba-7607-467c-aac5-f2156e4df8d3)


## 動作確認
1. ブラウザで http://localhost:8000 にアクセスしてください。
1. テキストボックスに「就業規則とは何ですか？」と入力して、Ctrl + Enter してください。
1. 以下のように返答が返ってきていれば成功です。
![image](https://github.com/marumaru1019/github-image/assets/70362624/b8fdcfcc-a7a0-4a58-8c5a-37aa4caa8ca2)