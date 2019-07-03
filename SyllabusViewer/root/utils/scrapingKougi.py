import requests
from bs4 import BeautifulSoup

baseURL = "https://tora-net.sti.chubu.ac.jp/syllabusv3/slbssbdr.do?value(risyunen)=2019&value(semekikn)=1&value(kougicd)={}&value(crclumcd)=01011300002016"

# for idx in range(1):
#     kougicd = str(idx).zfill(5)
#     URL = baseURL.format(kougicd)
#     response = requests.get(URL)
#     print(response)

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

import pdb; pdb.set_trace()
