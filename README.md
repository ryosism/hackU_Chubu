# HackU_Chubu

# Syllabus Viewer
シラバスビューワー(仮プロダクト名)

## Requirements
- Flask==1.0.3
- firebase-admin==2.17.0
- Flask-Bootstrap4==4.0.2
- gunicorn==19.9.0
- google-cloud-firestore==1.2.0

These requirements are included in `requirements.txt`


## installation
- Type `pip install -t lin -r requirements.txt`
- Launch `python main.py`

- Note: Googleのサービスアカウントの.jsonファイルが求められるので、\\
パスを指定してあげる `export GOOGLE_APPLICATION_CREDENTIALS=PATH_TO_JSON` と動くよ
