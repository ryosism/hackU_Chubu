from flask import *  # 必要なライブラリのインポート

app = Flask(__name__)  # アプリの設定


@app.route("/")  # どのページで実行する関数か設定
def top():
    return "Hello, World!"  # Hello, World! を出力


@app.route("/search")
def search():
    return "Search result here."


@app.route("/detail")
def detial():
    return "A detail of syllabus here."


if __name__ == "__main__":  # 実行されたら
    app.run(debug=True, host='0.0.0.0', port=8888, threaded=True)  # デバッグモード、localhost:8
