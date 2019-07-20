import math

def keywordSearch(kougiIndex, request):
    keyword = request.keyword
    page = request.page

    JSON = kougiIndex.search(keyword, {
        'hitsPerPage': 20,
        'page': page
    })
    docs = JSON['hits']

    page = JSON["page"]
    nbHits = JSON['nbHits']
    nbPages = JSON['nbPages']
    hitsPerPage = JSON['hitsPerPage']
    resultInfo = {"page": page, "nbHits": nbHits, "nbPages": nbPages, "hitsPerPage": hitsPerPage}

    return docs, resultInfo

def idSearch(db, id):
    users_ref = db.collection('kougis').document(id)
    try:
        doc = users_ref.get().to_dict()
        doc["id"] = id

    except Exception as e:
        doc = {}
        doc["text"] = "ERROR-404"

    return doc

def searchReview(db, id):
    ref = db.collection('reviews').where("kougiID", "==", id)
    reviews = []
    stars = []
    try:
        docs = ref.get()
        for review in docs:
            review = review.to_dict()
            stars.append(int(review["star"]))
            reviews.append(review)

        star = math.ceil(20*sum(stars) / len(stars))

    except Exception as e:
        star = 0
        review = {}
        review["id"] = ""
        review["star"] = 0
        review["title"] = "まだレビューがありません"
        review["text"] = "レビューを登録して他の人に講義を知ってもらおう！"
        reviews.append(review)

    return reviews, star
