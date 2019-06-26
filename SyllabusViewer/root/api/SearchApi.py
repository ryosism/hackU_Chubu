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
    ref = db.collection('kougis').where("id", "==", id)
    doc = users_ref.get().to_dict()
