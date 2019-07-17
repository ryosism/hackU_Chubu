const functions = require('firebase-functions')
const admin = require('firebase-admin')
admin.initializeApp(functions.config().firebase)
const algoliasearch = require('algoliasearch')

const ALGOLIA_ID = functions.config().algolia.app_id
const ALGOLIA_ADMIN_KEY = functions.config().algolia.api_key
const ALGOLIA_SEARCH_KEY = functions.config().algolia.search_key

// Algolia Clientの初期化
const client = algoliasearch(ALGOLIA_ID, ALGOLIA_ADMIN_KEY)
// 作成したAlgoliaのIndex名を入れる
const kougiIndex = client.initIndex('SyllabusViewer_kougis');
const reviewIndex = client.initIndex('SyllabusViewer_reviews');

exports.insertKougi = functions.firestore
    .document('kougis/{kougiID}')
    .onCreate((snap, context) => {
        const kougi = snap.data();

        // kougiIDをurlの引数から拾ってくる
        const objectID = context.params.kougiID;

    return kougiIndex.addObject({objectID, kougi});
});

exports.insertReview = functions.firestore
    .document('reviews/{reviewID}')
    .onCreate((snap, context) => {
        const review = snap.data();

        // reviewIDをurlの引数から拾ってくる
        const objectID = context.params.reviewID;

    return reviewIndex.addObject({objectID, review});
});
