import os
import shutil
import configparser

DEBUG_MODE = True

config_ini = configparser.ConfigParser()
config_ini.read('config.ini', encoding='utf-8')

rootFolderPath = config_ini['config']['rootFolderPath']
outputFolderName = config_ini['config']['outputFolderName']
outputBakFolderName = config_ini['config']['outputBakFolderName']

outputFolderPath = rootFolderPath + "\\" + outputFolderName
outputBakFolderPath = outputFolderPath + "\\" + outputBakFolderName

if (not os.path.isdir(outputFolderPath)):
    os.makedirs(outputFolderPath)
if (not os.path.isdir(outputBakFolderPath)):
    os.makedirs(outputBakFolderPath)

for file in os.listdir(outputFolderPath):
    filePath = outputFolderPath + "\\" + file

    if not os.path.isfile(filePath):
        continue

    shutil.move(filePath, outputBakFolderPath)
