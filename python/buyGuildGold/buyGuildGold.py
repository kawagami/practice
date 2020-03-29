import pyautogui
import time
import datetime

def clickSpecificPosition(positionX,positionY):
    pyautogui.click(positionX,positionY)
    # print("點擊",positionX,positionY,"了")
    time.sleep(0.7)

def getPosition():
    mousePosition=pyautogui.position()
    print(mousePosition)

def buyGoldLoop(times,recordTime):
    for i in range(times):
        # 點擊旅團金幣
        clickSpecificPosition(1437, 932)
        # 點擊買下旅團金幣
        clickSpecificPosition(955, 663)
        # 點掉買下後特效
        clickSpecificPosition(1437, 932)
    endTime=datetime.datetime.now()
    totalTime=endTime-recordTime
    print(totalTime)

timeNow=datetime.datetime.now()
buyGoldLoop(10,timeNow)