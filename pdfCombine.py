
import os
import img2pdf
from PIL import Image
from natsort import natsorted
import shutil

rootFolderPath = r"XXXXXXXXXXx"  # 変換したい画像ファイルがある
outputFolderName = "result"  # 出力したPDFを格納するフォルダ
bakFolderName = "bak"  # PDF化した後に退避するフォルダ

for folderName in os.listdir(rootFolderPath):
    folderPath = rootFolderPath + "\\" + folderName
    outputFolderPath = rootFolderPath + "\\" + outputFolderName
    bakfolderPath = rootFolderPath + "\\" + bakFolderName

    if (os.path.isfile(folderPath)) or (folderName == bakFolderName) or (folderName == outputFolderName):
        continue

    outputPdfPath = outputFolderPath + "\\" + folderName + ".pdf"   # 出力するPDFの名前

    with open(outputPdfPath, "wb") as f:
        convert_target = []
        for j in os.listdir(folderPath):
            convert_target.append(Image.open(folderPath + "\\" + j).filename)

        write_target = img2pdf.convert(
            natsorted(convert_target))  # 文字列順に並び替えてPDF変換

        f.write(write_target)
    shutil.move(folderPath, bakfolderPath)
