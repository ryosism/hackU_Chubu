def keywordSearch(db, request):
    users_ref = db.collection('kougis')
    docs = users_ref.get()
    result = []
    for doc in docs:
        id = doc.id
        doc = doc.to_dict()
        doc["id"] = id
        print("{} = {}".format(request.form["keyword"], doc["title"]))
        if request.form["keyword"] in doc["title"]:
            result.append(doc)

    return result

def idSearch(db, id):
    users_ref = db.collection('kougis').document(id)
    try:
        doc = users_ref.get().to_dict()

    except Exception as e:
        doc = {}
        doc["text"] = "ERROR-404"

    return doc
