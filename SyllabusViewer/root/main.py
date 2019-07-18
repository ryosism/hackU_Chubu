# -*- coding: utf-8 -*-
import os
from flask import *  # 必要なライブラリのインポート

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from firebase_admin import db
from flask_bootstrap import Bootstrap

from api import SearchApi, SearchApiRequest, InsertReviewApi, InsertReviewApiRequest
from utils.parser import *
from algoliasearch.search_client import SearchClient

client = SearchClient.create(os.environ["ALGOLIA_APP_ID"], os.environ["ALGOLIA_API_KEY"])
kougiIndex = client.init_index('SyllabusViewer_kougis')
reviewIndex = client.init_index('SyllabusViewer_reviews')

cred = credentials.ApplicationDefault()
firebase_admin.initialize_app(cred, {
  'projectId': 'syllubusviewer',
})
db = firestore.client()

app = Flask(__name__)  # アプリの設定
bootstrap = Bootstrap(app)


@app.route("/", methods=["GET", "POST"])  # どのページで実行する関数か設定
def top():
    return render_template("top.html")


@app.route("/about", methods=["GET", "POST"])  # どのページで実行する関数か設定
def about():
    return render_template("about.html")


@app.route("/searchResult", methods=["GET", "POST"])
def searchResult():
    if request.method == "GET":
        keyword = ""
    else:
        try:
            keyword = str(request.form["keyword"])
        except Exception as e:
            keyword = ""

    searchApiRequest = SearchApiRequest.SearchApiRequest(keyword = keyword, count = 10, tags = [])
    result, resultInfo = parseSearchResults(SearchApi.keywordSearch(kougiIndex, request))

    return render_template("searchResult.html", keyword = keyword, result = result, resultInfo = resultInfo)


@app.route("/kougiDetail/<id>", methods=["GET", "POST"])
def kougiDetial(id):
    kougi = SearchApi.idSearch(db, id)

    if kougi["text"] == "ERROR-404":
        return render_template("404.html")
    if request.method == "GET":
        reviews, star = SearchApi.searchReview(db, id)

        return render_template("kougiDetail.html", kougi = kougi, reviews = reviews, star = int(star))

    else:
        kougiID = request.form["id"]
        try:
            star = request.form["star"]
        except Exception as e:
            star = 3
        try:
            title = request.form["title"]
        except Exception as e:
            title = "無題"
        try:
            text = request.form["text"]
        except Exception as e:
            text = ""

        insertReviewApiRequest = InsertReviewApiRequest.InsertReviewApiRequest(kougiID = kougiID, star = star, title = title, text = text)
        InsertReviewApi.insertReview(db, insertReviewApiRequest)

        reviews, star = SearchApi.searchReview(db, id)

        return redirect('/kougiDetail/{}'.format(id), code=303)

if __name__ == "__main__":  # 実行されたら
    app.run(debug=True, host='0.0.0.0', port=8888, threaded=True)  # デバッグモード、localhost:8
