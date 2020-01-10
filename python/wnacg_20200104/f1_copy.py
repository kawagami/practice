

import pyperclip
import datetime
import time
import requests
import bs4


def f2_show_website_file_name(target_website):
    # 顯示在copy_list的檔案名稱
    htmlfile = requests.get(target_website)
    if htmlfile.status_code == 200:
        soup = bs4.BeautifulSoup(htmlfile.text, 'lxml')
        print(soup.h2.text)
    else:
        print("error!")


def f1_copy_website(copy_list):
    """預計設定成無限迴圈但是想不出好的break條件"""
    """目前先設計成跑10秒"""
    # 紀錄複製的網址
    # pyperclip.paste()
    # 紀錄網址的列表
    print("開始複製網址")
    # 取得現在時間的變數
    time_start = datetime.datetime.now()
    # 取得區間為10秒的變數
    ten_second = datetime.timedelta(seconds=10)
    # 取得10秒後時間的變數
    ten_second_after = time_start+ten_second
    # 當現在的時間小於函數開始後10秒的時候就會繼續while迴圈
    # 白話一點就是會運行10秒
    while datetime.datetime.now() < ten_second_after:
        if pyperclip.paste() in copy_list:
            pass
        # 檢查是否wnacg的網址
        elif "wnacg" in pyperclip.paste():
            copy_list.append(pyperclip.paste())
            print(pyperclip.paste(), "加入列表")
            # 將最新加入的網址資訊顯示
            f2_show_website_file_name(copy_list[-1])
        time.sleep(0.1)
        # print(ten_second_after-datetime.datetime.now())
    # 當函數結束時顯示字串
    print("複製網址結束")


# global copy_list
target_website = list()
f1_copy_website(target_website)
# print(target_website)


def f3_path1_check_direct_download():
    # 檢查能否直接下載
    pass


def f4_path1_direct_download():
    # 直接下載
    pass


def f5_path2_crawler_onebyone():
    # 抓取網頁顯示的每一頁圖片資訊
    pass


def f6_path2_download_onebyone():
    # 抓取網頁顯示的每一頁圖片資訊
    pass
