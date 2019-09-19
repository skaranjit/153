"""
This program will ask for the file name from user and if the file is present relatively, it will read data from the file and print out the formatted report.
"""
__author__="Suman Karanjit"
__date__="1/25/2019"
from os.path import *
import os

fileName = input("Enter name of the file {eg:'data.txt'}: ")
"""
#Note to self: To check what files are present in current or working directory.
path = '.'    #to define path to the current directory or working directory
 
files = os.listdir(path)    #get the list of files in the working directory 
for name in files:
    print(name)
"""
if isfile(fileName):
    #Do the rest of the processing for this program
    professorNameList = []
    classNameList = []
    StuList = []
    ct = 1
    with open(fileName,"r") as fileObj:    #opens file with read mode as fileObj
        print("Class Report: /n")       # Heading for the report
        for tmpLine in fileObj:
    
            if len(tmpLine) > 1:                
                tmpList = tmpLine.split("\n")
                for item in tmpList:
                    if len(item) == 0:          #if there are any empty items in list, it will remove it 
                        tmpList.remove(item)
                        
                    else:
                        if (ct-1)%3 == 0 or ct == 1 :       # it will be true only if CT belongs to [1,4,7,10,....] sequence
                            professorNameList.append(item)
                            print("Name:",professorNameList[0])             
                            professorNameList = []
                        elif (ct-2)%3 == 0 or ct == 2:  #It will run only if ct belongs in [2,5,8,...] sequence
                            classNameList.append(item)
                            print("Class:",classNameList[0])  
                            classNameList = []
                        elif ct%3 == 0:             # it will run only if ct belongs in [ 3,6,9,12,.....] sequence
                            
                            stuList = item.split(",")
                            stuList.sort()
                            
                            print("Student List: \n", stuList)
                            print("*"*150, "\n"*3)
                            stuList = []
                ct += 1
    fileObj.close()
else:
    print("File doesn't exist: ", fileName)
    
