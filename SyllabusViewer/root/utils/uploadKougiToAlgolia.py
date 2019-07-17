import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from firebase_admin import db

from algoliasearch.search_client import SearchClient
import algoliaSecret

client = SearchClient.create(algoliaSecret.algolia_app_id, algoliaSecret.algolia_api_key)
kougiIndex = client.init_index('SyllabusViewer_kougis')

cred = credentials.ApplicationDefault()
firebase_admin.initialize_app(cred, {
  'projectId': 'syllubusviewer',
})
db = firestore.client()

users_ref = db.collection('kougis')
docs = users_ref.get()

objectBatch = []
count = 0

for doc in docs:
    id = doc.id
    doc = doc.to_dict()
    doc["objectID"] = id

    objectBatch.append(doc)
    if len(objectBatch) > 200:
        res = kougiIndex.save_objects(objectBatch)
        objectBatch = []
        count += 200
        print("{} documents were added.".format(count))

res = kougiIndex.save_objects(objectBatch)
print("all {} documents were added.".format(count))
