import os
import shutil


def isDiamond(root, fileName):
    os.chdir(root)
    with open(fileName) as file:
        while True:
            line = file.readline()
            if not line:
                break
            if "minecraft:diamond" in line:
                #print(root + "\\" + fileName +" has diamond")
                return True
    return False

def createDir(root):
    os.chdir(root)
    index = -1
    tempword = ''
    folderName = "netherite_"
    while root[index] != '\\':
        tempword+= root[index]
        index-=1

    for char in tempword[::-1]:
        folderName+=char
    newpath = os.path.dirname(root)
    print("this is the new path" + newpath)
    print("New path and folder name " + newpath + '\\' + folderName)
    newDir = newpath + '\\' + folderName
    if not os.path.isdir(newDir):
        os.mkdir(path= newDir)

class newItemCreation:

    def __init__(self, rootFolder):
        self.root = rootFolder


    def find(self):
        for root, dirs, files in os.walk(self.root, topdown= True):
            for fileName in files:
                if ".properties" in fileName:
                    if isDiamond(root, fileName):
                        createDir(root)





    def copy(self, fileName):
        fileopen = open(fileName, 'r')

