import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from firebase_admin import db

cred = credentials.ApplicationDefault()
firebase_admin.initialize_app(cred, {
  'projectId': 'syllubusviewer',
})
db = firestore.client()

doc_ref = db.collection('kougis').document()
doc_ref.set({
    "title": "",
    "text": "",
    "teacher": "",
    "hyoka": "",
    "hyokakizyun": "",
    "gakunen": "",
    "semester": "",
    "zikan": "",
    "taisyo": ""
})
