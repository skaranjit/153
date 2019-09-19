
from os.path import *
import tkinter as tk
from tkinter import filedialog
import string

def ReadFromFile():
    """
    Ask user to select a file and return list of sentence from file splited from new line.
    """
    root = tk.Tk()
    root.withdraw()
    fileName = filedialog.askopenfilename()
    while not fileName.endswith(".txt"):
        print("Please select the correct text file")
        fileName = filedialog.askopenfilename()
    if isfile(fileName):
        #Do the rest of the processing for this program
        ct = 1
        with open(fileName,"r") as fileObj:    #opens file with read mode as fileObj
            text = fileObj.readlines()
            newList = []
            for sent in text:
                sent = sent.strip('\n')
                wordList = sent.split()
                for words in wordList:
                    newList.append(words.strip("\n")) 
        fileObj.close()
        return(newList)
    else:
        print("File doesn't exist: ", fileName)
def wordDict(tmpList):
    punc = string.punctuation 
    Tupplepunc = tuple(char for char in string.punctuation)
    wordDict = {}
    for word in tmpList:
        word = word.lower()
        if word.strip(punc).isdigit() != True and word.strip(punc) in wordDict.keys() and word.strip(punc) != "":
            wordDict[word.strip(punc)] = wordDict[word.strip(punc)] + 1
        elif word.strip(punc).isdigit() != True and word.strip(punc) not in wordDict.keys() and word.strip(punc) != "":
            wordDict[word.strip(punc)] = 1
    tmpList = [keys for keys in wordDict]
    tmpList.sort()
    #print(tmpList)
    tmpDict = {}
    for word in tmpList:
        value = wordDict[word]
        tmpDict[word] = value
    return tmpDict
               
def puncNumDict(tmpList):
    punc = string.punctuation
    puncDict= {}
    for word in tmpList:
        for char in word:
            if char in punc:
                if char in puncDict.keys():
                    puncDict[char] = puncDict[char] + 1
                else:
                    puncDict[char] = 1
    return puncDict
def CreateMenu(chList, menuTitle):
    """
    This Function will take two parameter,chList( List, List of menu item) and menuTitle( str, Title of Menu). It will then return out the formatted Menu.
    """
    tmpStr = ""
    ct = "1"
    
    for item in chList:
        tmpStr = tmpStr + ct + ". " + item + "\n"
        ct = int(ct) + 1
        ct = str(ct)
    return menuTitle +"\n" + tmpStr
def getValidChoice(NoOfCh, menuStr):
    """
    This function will take two paramenter, NoOfCh(int, len of the menuList) and menuStr( str , Formatted Menu ). It will print out the menu and ask user for the choice. 
    Also will print Invalid and ask for the choice until the choice is valid.Choice needs to be integer less than NoOfCh and greater than zero. At the end it will return choice. 
    """
    print("\n",menuStr)
    choice = input("Enter your choice: " )
    while not choice.isdigit() or (int(choice) <= 0 or int(choice) > NoOfCh):
        print("\nInvalid Choice -- Please Try Again \n")
        print(menuStr)
        choice = input("Enter your choice: " )
    return int(choice)
def PrintReport(myDict,Name):
    print("{:20s}{:10s}".format(Name,"Frequency"))
    x =""
    for keys,values in myDict.items():        
        x += ("{:20s}{:2d}".format(keys,values)) + "\n"
    return x

################################################################################

###############################MAIN#################################################

newList = ReadFromFile()
#print(newList)
optionList = ["Add Word","Delete Word","Add Puncuation","Delete Punctuation","Quit"]
menu = CreateMenu(optionList,"Menu")
mywordDict = wordDict(newList)
print(PrintReport(mywordDict,"Word"))

myPuncDict = puncNumDict(newList)
print(PrintReport(myPuncDict,"Punctuations"))
choice = getValidChoice(len(optionList),menu)

while choice != len(optionList):
    if choice == 1:
        wordstoAdd = input("Enter word: ")
        newList.append(wordstoAdd)
        mywordDict = wordDict(newList)
        print(PrintReport(mywordDict,"Word"))
    elif choice == 2:
        wordstoDelete = input("Enter word to delete: ")
        if wordstoDelete in mywordDict.keys():
            newList = [letter.replace(wordstoDelete,"") for letter in newList]
            mywordDict = wordDict(newList)
            print(PrintReport(mywordDict,"Word"))
        else:
            print("'",wordstoDelete,"'","does not exist.")
            print(PrintReport(mywordDict,"Word"))
    elif choice == 3:
        addPunc = input("Enter Punctuation: ")
        newList.append(addPunc)
        myPuncDict = puncNumDict(newList)
        print(myPuncDict)
        print(PrintReport(myPuncDict,"Punctuations"))
    elif choice == 4:
        delPunc = input("Enter Punctuation: ")
        if delPunc in myPuncDict.keys():
            newList = [word.replace(delPunc,"") for word in newList]
                
            myPuncDict = puncNumDict(newList)
            print(PrintReport(myPuncDict,"Punctuations"))
    choice = getValidChoice(len(optionList),menu)
    
########################################################################
