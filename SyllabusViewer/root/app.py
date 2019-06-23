from flask import *  # 必要なライブラリのインポート

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from firebase_admin import db
from flask_bootstrap import Bootstrap

from api import SearchApi, SearchApiRequest
from utils.parser import *

cred = credentials.Certificate('../secrets/syllubusviewer-firebase-adminsdk-sxbfc-60c38042a5.json')
firebase_admin.initialize_app(cred)
db = firestore.client()

app = Flask(__name__)  # アプリの設定
bootstrap = Bootstrap(app)


@app.route("/", methods=["GET", "POST"])  # どのページで実行する関数か設定
def top():
    return render_template("top.html")


@app.route("/searchResult", methods=["GET", "POST"])
def searchResult():
    searchApiRequest = SearchApiRequest.SearchApiRequest(keyword = "C言語応用", tags = [])
    result = parseSearchResults(SearchApi.searchApi(db, request))

    return render_template("searchResult.html", result = result)


@app.route("/kougiDetail", methods=["GET", "POST"])
def kougiDetial():
    return render_template("kougiDetail.html")


if __name__ == "__main__":  # 実行されたら
    app.run(debug=True, host='0.0.0.0', port=8888, threaded=True)  # デバッグモード、localhost:8
