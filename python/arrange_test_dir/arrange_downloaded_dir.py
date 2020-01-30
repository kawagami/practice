
# 將下載器下載的zip檔案整理好
# 改名、往上拉一層、刪除空白資料夾

import os
import glob
import shutil
import send2trash

time = 0
list_test_dir = list()

ori_dir = r"G:\H\test"
pattern = r"G:\H\test\*\*.zip"

for i in glob.iglob(pattern):
    list_test_dir.append(i)

for i in list_test_dir:
    for a, b, c in os.walk(os.path.dirname(i)):
        time += 1
        print("root：", a, "\nupperdir：", os.path.basename(a), "\nfile：", c)
        shutil_a = os.path.join(a, c[0])
        shutil_b = os.path.join(ori_dir, os.path.basename(a)+".zip")
        print("等待處理的zip檔案", shutil_a)
        print("預計處理完的路徑", shutil_b)
        if os.path.exists(shutil_b):
            print(os.path.basename(shutil_b), "已經存在")
        else:
            shutil.move(shutil_a, shutil_b)
            send2trash.send2trash(a)
            print("移動", os.path.basename(shutil_b), "結束")
        print("-"*160)

print(time)
