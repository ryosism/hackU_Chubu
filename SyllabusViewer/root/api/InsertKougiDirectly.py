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
    "title": "資格英語A(英検)",
    "text": "日本英語検定協会が実施する「英語検定試験」（英検）は日本で広く受け入れられている英語能力試験の1つである。「資格英語Ａ（英検）」では，この英検の2級合格を目指すとともに，英検合格に向けての学習を通して，実用的な英語能力を身に付けることを目標とする。",
    "teacher": "三島 恵理子",
    "hyoka": "英検のテスト結果が重要な評価基準だが，英検が不合格でも一次試験の結果も考慮する。また，語彙テスト, 出席状況, 授業への貢献度, 課題なども成績評価に関わってくる。",
    "hyokakizyun": "英検のテスト結果（60％）、語彙テスト・課題・平常点（20%)、まとめのテスト（20%)を総合的に評価する。"
})
