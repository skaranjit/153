"""
This program will ask for the file name from user and if the file is present relatively, it will read data from the file and print out the formatted report.
"""
__author__="Suman Karanjit"
__date__="1/25/2019"
from os.path import *
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

fileName = filedialog.askopenfilename()

while not fileName.endswith(".txt"):
    fileName = filedialog.askopenfilename()


if isfile(fileName):
    #Do the rest of the processing for this program
    fileObj= open(fileName,"r")
    totLinestmp = fileObj.readlines()
    print(totLinestmp)
    totLines = []
    for item in totLinestmp:
        if item.endswith("\n"):
            item=item.replace("\n","")
        if item != "":
            totLines.append(item)
    print(totLines)
            
    for ct in range(0,len(totLines)-2,3):
        stuList = (totLines[ct+2]).split(',')
        stuList.sort()
        print("Name :", totLines[ct])
        print("Class :", totLines[ct+1])
        print("StuList : \n", stuList)
        print("=" *70)
    fileObj.close()
else:
    print("File doesn't exist: ", fileName)
    
