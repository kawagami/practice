import pyautogui
import time

def clickSpecificPosition(positionX,positionY):
    pyautogui.click(positionX,positionY)
    print("點擊",positionX,positionY,"了")
    time.sleep(0.7)

def getPosition():
    mousePosition=pyautogui.position()
    print(mousePosition)

# getPosition()

def mainBuyWind(times):
    for i in range(times):
        print("第",i,"次")
        # 點擊買金附魔
        clickSpecificPosition(1297, 421)
        # 點擊清風附魔
        clickSpecificPosition(1251, 463)
        # 點擊購買清風附魔
        clickSpecificPosition(955, 665)
        # 點擊掉購買物品過場
        clickSpecificPosition(1336, 896)

mainBuyWind(10)