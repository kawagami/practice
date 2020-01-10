
import pyperclip
import datetime
import time
import requests
import bs4

target_website = r"https://www.wnacg.org/photos-index-aid-92711.html"


def f2_show_website_file_name(target_website):
    # 顯示在copy_list的檔案名稱
    htmlfile = requests.get(target_website)
    if htmlfile.status_code == 200:
        soup = bs4.BeautifulSoup(htmlfile.text, 'lxml')
        print(soup.h2.text)
    else:
        print("error!")


f2_show_website_file_name(target_website)
