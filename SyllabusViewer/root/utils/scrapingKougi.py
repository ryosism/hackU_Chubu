import requests
from bs4 import BeautifulSoup

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
batch = db.batch()

baseURL = "https://tora-net.sti.chubu.ac.jp/syllabusv3/slbssbdr.do?value(risyunen)=2019&value(semekikn)=1&value(kougicd)={}&value(crclumcd)=01011300002016"

kougicd = str(12547).zfill(5)
URL = baseURL.format(kougicd)
response = requests.get(URL)

soup = BeautifulSoup(response.text, 'html.parser')
kougi = soup.find_all(class_="kougi")

# if len(kougi) == 0:
#     continue

title = kougi[0].prettify().split("\n")[1].strip()
teacher = kougi[3].prettify().split("\n")
teachers = [teacher.strip().replace("\u3000", "") for teacher in teacher if not "<" in teacher][:-1]
tani = kougi[4].prettify().split("\n")[1].strip()
gakunen = kougi[5].prettify().split("\n")[1].strip()
semester = kougi[6].prettify().split("\n")[1].strip()
zikan = kougi[7].prettify().split("\n")[3].split("：")[-1]
# taisyo =

others = [td for td in soup.find_all("td") if td.get("style") == "background-color:; vertical-align:middle"]

# 面倒だけど前後のtdタグと/brタグを削除している、その後結合、<br>タグだけは残すか要考慮
details = []
for detail in others:
    details.append("".join([content.strip() for content in detail.prettify().split("\n")[1:-2] if not "br" in content]))

text, mokuhyo, houhou, hyoka, hyokakizyun = details
import pdb; pdb.set_trace()
