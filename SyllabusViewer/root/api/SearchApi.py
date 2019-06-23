def searchApi(db, request):
    users_ref = db.collection('kougis')
    docs = users_ref.get()

    return docs
