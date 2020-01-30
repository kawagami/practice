
import bs4
import requests

TargetWeb = "https://www.uukanshu.com/b/88086/"

TextList = list()

WebFile = requests.get(TargetWeb)
if WebFile.status_code == 200:
    print("requests成功")
    soup = bs4.BeautifulSoup(WebFile.text, "lxml")

    NovelList = list()
    for i in soup.select("ul#chapterList")[0].find_all("a"):
        # NovelList現在是所有章節的網址了
        NovelList.append("https://www.uukanshu.com"+i.get("href"))

NovelList.reverse()

for i in NovelList:
    print(i)

for j in NovelList:
    WebFile = requests.get(j)
    if WebFile.status_code == 200:
        print("requests成功")
        soup = bs4.BeautifulSoup(WebFile.text, "lxml")
        # print(len(soup))

        # 取得標題
        TextList.append("\n"+soup.select("h1#timu")[0].text+"\n")
        print("取得標題"+soup.select("h1#timu")[0].text)

        # 取得內文
        for i in soup.select("div#contentbox")[0].select("p"):
            processed_text = str.strip(i.text)
            TextList.append(processed_text+"\n")


def download_to_txt(TargetList):
    with open("雲東流" + '.txt', 'a', encoding='utf8') as tar:
        for i in TargetList:
            tar.write(i)
    print('寫入完成\n')


download_to_txt(TextList)
