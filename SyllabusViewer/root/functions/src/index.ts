import * as functions from 'firebase-functions';
import * as algoliasearch from 'algoliasearch';
import * as admin from 'firebase-admin';
admin.initializeApp();

const env = functions.config();

// Algolia Clientの初期化
const client = algoliasearch(env.algolia.appid, env.algolia.apikey);
// 作成したAlgoliaのIndex名を入れる
const index = client.initIndex('SyllabusViewer');

exports.insertKougi = functions.firestore
    .document('kougis/{kougiID}')
    .onCreate((snap, context) => {
        const kougi = snap.data();

        // kougiIDをurlの引数から拾ってくる
        const objectID = context.params.kougiID;

    return index.addObject({objectID, kougi});
});
