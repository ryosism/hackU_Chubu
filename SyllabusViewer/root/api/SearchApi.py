import math

def keywordSearch(db, request):
    users_ref = db.collection('kougis')
    docs = users_ref.get()
    result = []
    for doc in docs:
        id = doc.id
        doc = doc.to_dict()
        doc["id"] = id
        if request.form["keyword"] in doc["title"]:
            result.append(doc)

    return result

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
