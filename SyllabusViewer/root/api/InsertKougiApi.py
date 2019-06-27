def insertKougi(db, request):
    doc_ref = db.collection('kougis').document()
    doc_ref.set({
        "title": request.title,
        "text": request.text,
        "teacher": request.teacher,
        "hyoka": request.hyoka,
        "hyokakizyun": request.hyokakizyun
})
