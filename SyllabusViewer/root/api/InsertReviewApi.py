def insertReview(db, request):
    doc_ref = db.collection('reviews').document()
    doc_ref.set({
        "kougiID": request.kougiID,
        "star": int(request.star),
        "title": request.title,
        "text": request.text
})
