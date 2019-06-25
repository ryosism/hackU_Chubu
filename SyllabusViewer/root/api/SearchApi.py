def searchApi(db, request):
    users_ref = db.collection('kougis')
    docs = users_ref.get()
    result = []
    for doc in docs:
        doc = doc.to_dict()
        print("{} = {}".format(request.form["keyword"], doc["title"]))
        if request.form["keyword"] in doc["title"]:
            result.append(doc)

    return result
