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
batch = db.batch()

baseURL = "https://tora-net.sti.chubu.ac.jp/syllabusv3/slbssbdr.do?value(risyunen)=2019&value(semekikn)=1&value(kougicd)={}&value(crclumcd)=01011300002019"

numberOfBatch = 0

for idx in range(29968, 100000, 1):
    kougicd = str(idx).zfill(5)
    print("will search kougicd = {}".format(kougicd))
    URL = baseURL.format(kougicd)
    response = requests.get(URL)

    soup = BeautifulSoup(response.text, 'html.parser')
    kougi = soup.find_all(class_="kougi")

    if len(kougi) == 0:
        continue

    title = kougi[0].prettify().split("\n")[1].strip()
    teacher = kougi[3].prettify().split("\n")
    teachers = [teacher.strip().replace("\u3000", "") for teacher in teacher if not "<" in teacher][:-1]
    tani = kougi[4].prettify().split("\n")[1].strip()
    gakunen = kougi[5].prettify().split("\n")[1].strip()
    semester = kougi[6].prettify().split("\n")[1].strip()
    try:
        zikan = kougi[7].prettify().split("\n")[3].split("：")[-1]
    except Exception as e:
        zikan = ""

    # taisyo =

    others = [td for td in soup.find_all("td") if td.get("style") == "background-color:; vertical-align:middle"]

    # 面倒だけど前後のtdタグと/brタグを削除している、その後結合、<br>タグだけは残すか要考慮
    details = []
    for detail in others:
        details.append("".join([content.strip() for content in detail.prettify().split("\n")[1:-2] if not "br" in content]))

    text, mokuhyo, houhou, hyoka, hyokakizyun = details

    keikakuhyo = soup.find_all("table", class_="syllkmok")

    cmd = "ref_{} = db.collection('kougis').document()".format(kougicd); exec(cmd)

    data = {
        "title": title,
        "text": text,
        "teacher": teachers,
        "hyoka": hyoka,
        "hyokakizyun": hyokakizyun,
        "gakunen": gakunen,
        "semester": semester,
        "zikan": zikan,

        "tani": tani,
        "mokuhyo": mokuhyo,
        "kougicd": kougicd

        # "taisyo": ""
    }
    # import pdb; pdb.set_trace()
    cmd = "batch.set(ref_{}, data)".format(kougicd); exec(cmd)

    print("kougicd = {} was set".format(kougicd))
    numberOfBatch += 1
    # if numberOfBatch%200 == 0:
    batch.commit()
        # numberOfBatch = 0
