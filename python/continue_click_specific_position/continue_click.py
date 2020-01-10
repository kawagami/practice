import pyautogui
import datetime
import time

start_position = pyautogui.position()
# 取得現在時間的變數
time_start = datetime.datetime.now()
# 取得區間為10秒的變數
ten_second = datetime.timedelta(seconds=5)
# 取得10秒後時間的變數
ten_second_after = time_start+ten_second
# 當現在的時間小於函數開始後10秒的時候就會繼續while迴圈
# 白話一點就是會運行10秒
while datetime.datetime.now() < ten_second_after:
    pyautogui.click(1468, 381)
    time.sleep(0.1)
    print("還剩", ten_second_after-datetime.datetime.now(), "秒")

pyautogui.moveTo(start_position)
