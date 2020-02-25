
# 將下載器下載的zip檔案整理好
# 改名、往上拉一層、刪除空白資料夾

import os
import glob
import shutil
import send2trash
import zipfile

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


def Achive_Folder_To_ZIP(sFilePath):
    """
    input : Folder path and name
    output: using zipfile to ZIP folder
    """
    zf = zipfile.ZipFile(sFilePath + '.ZIP', mode='w')  # 只儲存不壓縮
    # zf = zipfile.ZipFile(sFilePath + '.ZIP', mode = 'w', compression = zipfile.ZIP_DEFLATED)#預設的壓縮模式
    os.chdir(sFilePath)
    # print sFilePath
    for root, folders, files in os.walk(".\\"):
        for sfile in files:
            aFile = os.path.join(root, sfile)
            # print aFile
            zf.write(aFile)
    zf.close()
    print(os.path.basename(sFilePath), "壓縮完成")


# 將目標資料夾底下的資料夾都壓縮成zip檔案
dir_wait_to_process = r"G:\H\test"

# 歷遍目標資料夾檢查底下要壓縮的資料夾
dir_list = os.listdir(dir_wait_to_process)
# dir_list = os.listdir(test_dir)

need_to_zip = list()
for i in dir_list:
    # mer為路徑+檔名
    mer = os.path.join(dir_wait_to_process, i)
    # 如果是資料夾就加入list
    if os.path.isdir(mer):
        # 取得要壓縮的資料夾的路徑加入need_to_zip數列
        need_to_zip.append(mer)

# for i in need_to_zip:
#     # 在這階段i是整個路徑 a是資料夾名稱
#     a = os.path.basename(i)
#     print(a)

# print(len(need_to_zip))
# 將要壓縮的資料夾依照名稱壓縮成同名的壓縮檔


# 在test資料夾測試功能
test_dir = r"C:\test"
dir_wait_to_process = r"G:\H\test"
dir_list_test = os.listdir(dir_wait_to_process)

need_to_zip_test = list()
for i in dir_list_test:
    # mer為路徑+檔名
    mer_test = os.path.join(dir_wait_to_process, i)
    # 如果是資料夾就加入list
    if os.path.isdir(mer_test):
        # 取得要壓縮的資料夾的路徑加入need_to_zip數列
        need_to_zip_test.append(mer_test)

# 在這裡做檢查重複、壓縮檔案、移除資料夾
for i in need_to_zip_test:
    # 在這階段i是整個資料夾絕對路徑 a是資料夾名稱
    a = os.path.basename(i)
    # print(a)
    # 檢查是否存在同名的壓縮檔

    # b是檔案所在的路徑
    b = os.path.dirname(i)
    # c是在資料夾下的同名rar檔案
    c = os.path.join(b, a+".zip")
    # c存在就跳過本次迴圈
    if os.path.exists(c):
        print("有", c, "了")
        continue
    # 呼叫函數執行壓縮
    print(os.path.basename(i), "開始壓縮")
    Achive_Folder_To_ZIP(i)
    # 壓縮後c存在的話將資料夾丟入垃圾桶
    if os.path.exists(c):
        # print("可以丟", i, "進垃圾桶了")
        send2trash.send2trash(i)
        print(os.path.basename(i), "丟進垃圾桶了")

# print(len(need_to_zip_test))
