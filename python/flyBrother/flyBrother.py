import pyautogui
import time

def clickSpecificPosition(positionX,positionY):
    pyautogui.click(positionX,positionY)
    print("點擊",positionX,positionY,"了")

def getPosition():
    mousePosition=pyautogui.position()
    # str1="pyautogui.click"
    # print(str1,mousePosition,sep="")
    print(mousePosition)

getPosition()

# 點擊白毛
clickSpecificPosition(954, 432)

# 換角間隔
time.sleep(1)

# 點擊技能三
clickSpecificPosition(1378, 913)

# 點擊確認
clickSpecificPosition(1554, 894)

# 施放時間
time.sleep(6)

# 點擊奶騎
clickSpecificPosition(838, 423)

# 換角間隔
time.sleep(1)

# 點擊奶騎左邊一格
clickSpecificPosition(721, 435)

# 移動時間
time.sleep(1)

# 點擊奶騎技能2
clickSpecificPosition(1462, 801)

# 奶騎技能2選擇白毛
clickSpecificPosition(959, 435)

# 點擊確認
clickSpecificPosition(1554, 894)

# # 施放時間
time.sleep(6)

# 點擊維拉
clickSpecificPosition(842, 666)

# 換角間隔
time.sleep(1)

# 點擊技能三
clickSpecificPosition(1378, 913)

# 技能三點擊維拉
clickSpecificPosition(842, 666)

# 點擊確認
clickSpecificPosition(1554, 894)

# # 施放時間
time.sleep(8)

# 點擊愛麗絲
clickSpecificPosition(949, 661)

# 換角間隔
time.sleep(1)

# 點擊愛麗絲右上那格
clickSpecificPosition(1073, 552)

# # 移動時間
time.sleep(1)

# 點擊愛麗絲技能2
clickSpecificPosition(1462, 801)

# 愛麗絲技能2選擇白毛
clickSpecificPosition(959, 432)

# 點擊確認
clickSpecificPosition(1554, 894)

# 施放時間
time.sleep(5)

# 點擊大爆發傳送位置
clickSpecificPosition(1184, 196)

# 施放時間
time.sleep(3)

# 點擊海恩往上的位置
clickSpecificPosition(958, 131)

# # 移動時間
time.sleep(1)

# 點擊海恩技能2
clickSpecificPosition(1462, 801)

# 海恩技能2選擇白毛
clickSpecificPosition(1183, 412)

# 點擊確認
clickSpecificPosition(1554, 894)

# # 施放時間
time.sleep(4)

# 點擊傳送位置
clickSpecificPosition(1623, 432)