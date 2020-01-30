
import bs4
import requests

TargetWeb = "https://www.uukanshu.com/b/88086/7121.html"
soup = ""
NovelList = list()

WebFile = requests.get(TargetWeb)
if WebFile.status_code == 200:
    print("requests成功")
    soup = bs4.BeautifulSoup(WebFile.text, "lxml")
    # print(len(soup))

    # 取得標題
    NovelList.append("\n"+soup.select("h1#timu")[0].text+"\n")

    # 取得內文
    for i in soup.select("div#contentbox")[0].select("p"):
        processed_text = str.strip(i.text)
        NovelList.append(processed_text+"\n")


def download_to_txt(TargetList):
    with open("雲東流" + '.txt', 'a', encoding='utf8') as tar:
        for i in TargetList:
            tar.write(i)
    print('寫入完成\n')


download_to_txt(NovelList)
