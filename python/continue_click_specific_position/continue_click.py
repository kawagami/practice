import pyautogui
import datetime
import time


def GetPosition():
    print(pyautogui.position())


def ClickSpecificPosition(second):
    start_position = pyautogui.position()
    # 取得現在時間的變數
    time_start = datetime.datetime.now()
    # 取得區間為10秒的變數
    ten_second = datetime.timedelta(seconds=second)
    # 取得10秒後時間的變數
    ten_second_after = time_start+ten_second
    # 特定位置
    # 吃鑰匙
    target_position = (1504, 827)
    # 當現在的時間小於函數開始後10秒的時候就會繼續while迴圈
    # 白話一點就是會運行10秒
    while datetime.datetime.now() < ten_second_after:
        pyautogui.click(target_position)
        time.sleep(0.1)
        print("還剩", ten_second_after-datetime.datetime.now(), "秒")
    pyautogui.moveTo(start_position)


# GetPosition()
ClickSpecificPosition(22)
