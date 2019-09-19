"""
This program will ask user to open the file and if the file is a text file, it will read data from the file and print out the formatted report otherwise will ask user to select text file to process.
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
    print("Please select the correct text file")
    fileName = filedialog.askopenfilename()



#fileName = input("Enter name of the file {eg:'data.txt'}: ")
"""
#Note to self: To check what files are present in current or working directory.
path = '.'    #to define path to the current directory or working directory
 
files = os.listdir(path)    #get the list of files in the working directory 
for name in files:
    print(name)
"""
if isfile(fileName):
    #Do the rest of the processing for this program
    ct = 1
    with open(fileName,"r") as fileObj:    #opens file with read mode as fileObj
        print("\n \n Class Report: \n")       # Heading for the report
        for tmpLine in fileObj:
            if len(tmpLine) > 1:                
                tmpList = tmpLine.split("\n")
                tmpListnew = []
                for item in tmpList:
                    if len(item) != 0:#It will ignore empty item and append the item to new List.
        
                        tmpListnew.append(item)
                for item in tmpListnew:
                    StuList = []
                    if (ct-1)%3 == 0:       # it will be true only if CT belongs to [1,4,7,10,....] sequence
                        print("Name:",item)
                    elif (ct-2)%3 == 0:  #It will run only if ct belongs in [2,5,8,...] sequence
                        print("Class:",item)
                    elif ct%3 == 0:             # it will run only if ct belongs in [ 3,6,9,12,.....] sequence
                        stuList = item.split(", ")
                        stuList.sort()
                        print("Student List: \n", stuList)
                        print("*"*160, "\n"*2)
                    ct += 1
        fileObj.close()
else:
    print("File doesn't exist: ", fileName)
    
