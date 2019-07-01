import requests
from bs4 import BeautifulSoup

baseURL = "https://tora-net.sti.chubu.ac.jp/syllabusv3/slbssbdr.do?value(risyunen)=2019&value(semekikn)=1&value(kougicd)={}&value(crclumcd)=01011100002019"

# for idx in range(1):
#     kougicd = str(idx).zfill(5)
#     URL = baseURL.format(kougicd)
#     response = requests.get(URL)
#     print(response)

kougicd = str(11319).zfill(5)
URL = baseURL.format(kougicd)
response = requests.get(URL)

soup = BeautifulSoup(response.text, 'html.parser')
kougi = soup.find_all(class_="kougi")
if len(kougi) == 0:
    continue

for label in kougi:
    title = kougi[0].prettify().split("\n")[1].strip()
    teacher = kougi[3].prettify().split("\n")[3].strip().replace("\u3000", " ")
    gakunen = kougi[5].prettify().split("\n")[1].strip()
    semester = kougi[6].prettify().split("\n")[1].strip()
    

    # tani = kougi[4].prettify().split("\n")[1].strip()
