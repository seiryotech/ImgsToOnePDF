import os
import img2pdf
from PIL import Image
from natsort import natsorted
import shutil
import configparser
# import sys

DEBUG_MODE = True

config_ini = configparser.ConfigParser()
config_ini.read('config.ini', encoding='utf-8')

rootFolderPath = config_ini['config']['rootFolderPath']
# 出力したPDFを格納するフォルダ(存在しなければ自動で作成します)
outputFolderName = config_ini['config']['outputFolderName']
# PDF化した後に退避するフォルダ(存在しなければ自動で作成します)
bakFolderName = config_ini['config']['bakFolderName']
# PDF化に失敗した後に格納するフォルダ(存在しなければ自動で作成します)
FailFolderName = config_ini['config']['FailFolderName']

outputFolderPath = rootFolderPath + "\\" + outputFolderName
bakFolderPath = rootFolderPath + "\\" + bakFolderName
failFolderPath = rootFolderPath + "\\" + FailFolderName

if (not os.path.isdir(outputFolderPath)):
    os.makedirs(outputFolderPath)
if (not os.path.isdir(bakFolderPath)):
    os.makedirs(bakFolderPath)
if (not os.path.isdir(failFolderPath)):
    os.makedirs(failFolderPath)

for folderName in os.listdir(rootFolderPath):
    folderPath = rootFolderPath + "\\" + folderName

    if (os.path.isfile(folderPath)) or (folderName == bakFolderName) or (folderName == outputFolderName) or (folderName == FailFolderName):
        continue

    outputPdfPath = outputFolderPath + "\\" + folderName + ".pdf"   # 出力するPDFの名前

    with open(outputPdfPath, "wb") as f:
        convert_target = []
        print(folderPath)
        for j in os.listdir(folderPath):
            convert_target.append(Image.open(folderPath + "\\" + j).filename)

        print('len:{}'.format(len(convert_target)))
        write_target = img2pdf.convert(
            natsorted(convert_target))  # 文字列順に並び替えてPDF変換

        f.write(write_target)

    if (not os.path.isdir(bakFolderPath)):
        shutil.move(folderPath, bakFolderPath)
