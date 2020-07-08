import os
import shutil


def isDiamond(root, fileName):
    os.chdir(root)
    print("isDiamond is checking " + root + '\\' + fileName)
    with open(fileName) as file:
        while True:
            line = file.readline()
            if not line:
                break
            if "minecraft:diamond" in line:
                #print(root + "\\" + fileName +" has diamond")
                return True
    return False

def createDir(path):
    os.chdir(path)
    index = -1
    tempword = ''
    folderName = "netherite_"
    while path[index] != '\\':
        tempword+= path[index]
        index-=1

    for char in tempword[::-1]:
        folderName+=char
    newpath = os.path.dirname(path)
    print("this is the new path" + newpath)
    print("New path and folder name " + newpath + '\\' + folderName)
    newDir = newpath + '\\' + folderName
    if not os.path.isdir(newDir):
        shutil.copytree(path, newDir)
    return newDir

def toNetherite(path):
    with open(path, 'r+') as file:
        lineIndex = -1
        lines = file.readlines()
        file.seek(0)
        while True:
            line = file.readline()

            lineIndex+=1
            if not line:
                break
            elif "minecraft:diamond" or ".diamond" in line:
                lines[lineIndex] = lines[lineIndex].replace("minecraft:diamond", "minecraft:netherite")
                lines[lineIndex] = lines[lineIndex].replace('.diamond', '.netherite')
    file.close()
    open(path, 'w').close()
    file = open(path, 'w')
    for line in lines:
        file.write(line)
    file.close()


        # print(root + "\\" + fileName +" has diamond")


def find(path):
    newDirs = []
    for root, dirs, files in os.walk(path, topdown= True):
        for fileName in files:
            if ".properties" in fileName and isDiamond(root, fileName):
                newDir = createDir(root)
                newDirs.append(newDir)
    for folder in newDirs:
        for root, dirs, files in os.walk(folder, topdown=True):
            for fileName in files:
                if ".properties" in fileName and isDiamond(root, fileName):
                    print("here" + root + '\\'+ fileName)
                    toNetherite(root + '\\'+ fileName)
                    break


