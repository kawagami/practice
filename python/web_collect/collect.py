import requests
from bs4 import BeautifulSoup

web = "https://www.ffxs.info/book/16-8905-1.html"


def get_text(web):
    r = requests.get(web)
    if r.status_code == 200:
        soup = BeautifulSoup(r.text, 'lxml')
        text = soup.select("div.content")[0].text.replace(" ", "\n")
        text2 = text.replace("。", "。\n")
        text3 = text2.replace("？", "？\n")
        textList = text3.split()
        return textList

# 將網址放入引數，回傳小說內文list
# textList = get_text(web)
# for i in textList:
#     print(i)

def download_novel(textList):
    with open('novelTest.txt', 'w', encoding='utf8') as novelTest:
        for i in textList:
            novelTest.write(i+"\n")

def get_chaper():
    titleList = list()
    # 目錄頁面
    titleWeb = "https://www.ffxs.info/trxs/8905.html"
    r = requests.get(titleWeb)
    if r.status_code == 200:
        soup = BeautifulSoup(r.text, 'lxml')
        # print(type(soup.select("ul.clearfix")[0]))
        for i in soup.select("ul.clearfix")[0].select("li"):
            titleList.append("https://www.ffxs.info"+i.a.get('href'))
    # 回傳目錄章節list
    return titleList


# 取得所有章節的內文
titleList = get_chaper()
novelList = list()
times = 0
for i in titleList:
    outputNovelList = get_text(i)
    novelList.extend(outputNovelList)
    times += 1
    print("第", times, "次")
download_novel(novelList)
