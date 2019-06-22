def searchApi(db, request):
    users_ref = db.collection('kougis')
    docs = users_ref.get()

    for doc in docs:
        print('{} => {}'.format(doc.id, doc.to_dict()))

    result = doc

    return result
