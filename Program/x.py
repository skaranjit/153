

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
        for char in word:
            if char in punc:
                word = word.replace(char,"")
        if word.isdigit() != True and word in wordDict.keys() and word != "":
            wordDict[word.strip(punc)] = wordDict[word.strip(punc)] + 1
        elif word.isdigit() != True and word.strip(punc) not in wordDict.keys():
            wordDict[word.strip(punc)] = 1
    print(tmpList)
    tmpList = [keys for keys in wordDict]
    tmpList.sort()
    #print(tmpList)
    tmpDict = {}
    for word in tmpList:
        value = wordDict[word]
        tmpDict[word] = value
    return tmpDict

listn = ReadFromFile()
x = wordDict(listn)
for keys,values in x.items():
    print(keys,values)
