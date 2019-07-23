# HackU_Chubu

# Syllabus Viewer
中部大学のシラバスを超軽量で閲覧でき、匿名のレビューもつけられるビューワー

## Requirements
- Flask==1.0.3
- firebase-admin==2.17.0
- Flask-Bootstrap4==4.0.2
- gunicorn==19.9.0
- google-cloud-firestore==1.2.0
- algoliasearch>=2.0,<3.0

These requirements are included in `requirements.txt`

- `npm install algoliasearch --save`
- `npm install firebase --save`
をfunctionの中で実行

## installation
- Type `pip install -t lin -r requirements.txt`
- Launch `python main.py`

- Note: Googleのサービスアカウントの.jsonファイルが求められるので、  
パスを指定してあげる `export GOOGLE_APPLICATION_CREDENTIALS=PATH_TO_JSON` と動くよ  
あと、firebase cloudfunctionでalgoliaを使っているから、`firebase functions:config:set algolia.app_id=`
などしてあげる必要あり
