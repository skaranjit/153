from os.path import *

fileName = input("enter name of the file")
path = '.'
 
files = os.listdir(path)
for name in files:
    print(name)

if isfile(fileName):
    #Do the rest of the processing for this program
    fileObj = open(fileName, "r")
    for tmpLine in fileObj:
        tmpList = tmpLine.split(" ")
        print(tmpList)
    fileObj.close()
else:
    print("File doesn't exist: ", fileName)
    
