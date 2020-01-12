import requests
import bs4

target_website = r"https://www.wnacg.org/photos-index-aid-92810.html"


def dict_test(target_website):
    wnacg_dict = {}
    # 顯示在copy_list的檔案名稱
    htmlfile = requests.get(target_website)
    if htmlfile.status_code == 200:
        soup = bs4.BeautifulSoup(htmlfile.text, 'lxml')
        # print(soup.h2.text)
        wnacg_dict[soup.h2.text] = soup
        # wnacg_dict[soup.h2.text] = "應該是成功"
        print(wnacg_dict)
    else:
        print("error!")


dict_test(target_website)
