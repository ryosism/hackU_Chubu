from flask import *  # 必要なライブラリのインポート

app = Flask(__name__)  # アプリの設定


@app.route("/", methods=["GET", "POST"])  # どのページで実行する関数か設定
def top():
    return render_template("top.html")


@app.route("/searchResult", methods=["GET", "POST"])
def searchResult():
    return render_template("searchResult.html")


@app.route("/kougiDetail", methods=["GET", "POST"])
def kougiDetial():
    return render_template("kougiDetail.html")


if __name__ == "__main__":  # 実行されたら
    app.run(debug=True, host='0.0.0.0', port=8888, threaded=True)  # デバッグモード、localhost:8
