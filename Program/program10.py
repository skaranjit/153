__author__= "Suman Karanjit"
__date__ = "04/21/2019"
"""
Description : This program will run from the command line. It will take as many string as an arguments and print out the formatted list o
validSSNS, palindromes,at least two uppercase,at least one even digit and ends with s or s Lists.
Pre-Condition:  User need to enter at least one arguments including the file name.
Post-Condition: None
"""

import sys
def isValidSSN(ssn):
    """
    Description: returns true if the string in is in this format: ###-##-#### otherwise returns false
    Pre-Condition: SSN needs to be string seperated by '-'
    Post-Condition: None
    """
    if len(ssn) == 11:   ###Checks if the entered number length is 11
        if ssn[3] == '-' and ssn [6] == '-': ##Check if hyphens are in correct place
            if ssn[0:3].isdigit() and\
               ssn[4:6].isdigit() and\
               ssn[7:11].isdigit(): ###Checks digits are in correct place
                if int(ssn[0]) != 0: ##checks if the first number is not '0'
                    return True
                else: return False
            else: return False
        else: return False
    else:
        return False


def isPalindrome(word):
    """
    Description: Returns True if the string is a palindrome otherwise returns False
    PreCondition: Word needs to be a string.
    PostCondition: None
    """
    reversedWord = word[::-1]
    flag = False
    if reversedWord.lower() == word.lower():
        flag = True
    return flag

def hasUpperCase(word):
    """
    Description: Returns True if the string has at least two uppercase letters otherwise returns False.
    Pre-Condition: word needs to be a string.
    Post-Condition: None
    """
    flag = False
    ct = 0
    for char in word:
        if char.isupper():
            ct +=1
    if ct >= 2:
        flag = True
    return flag

def hasEvenDigit(num):
    """
    Description: Returns True if the string contains at least one even digit otherwise returns False
    Pre-Condition: Num needs to be a string.
    Post-Condition: None
    """
    flag = False
    for char in num:
        if char.isdigit():
            char = int(char)
            if char % 2 == 0:
                flag = True
    return flag

def endsWithS(word):
    """
    Description : Returns True if the word ends with an s or an S otherwise returns False
    Pre-Condition: word needs to be string
    Post-Condition: None
    """
    flag = False
    if word.lower().endswith('s'):
        flag = True

    return flag

def printReport(ssnList,palinList,upperList,evenList,Slist):
    tmp = "Valid SSns:\n"+ " "*10 + str(ssnList) + "\n" 
    tmp += "Plindromes:\n" + " "*10 + str(palinList) + "\n"
    tmp += "At Least two UpperCase:\n" + " "*10 +str(upperList)+ "\n"
    tmp += "At Least one even digit:\n"+ " "*10 +str(evenList)+ "\n"
    tmp += "Ends with s or S:\n"  + " "*10 +str(Slist)+ "\n"
    return tmp

def checkList(tmpList):
    if tmpList == []:
        tmpList = "None Found"
    else:
        tmpList = tmpList
    return tmpList
def main():
    script = sys.argv[0]
    ssnList = []
    palinList = []
    upperList = []
    evenList = []
    Slist = []
    if len(sys.argv) > 1:
        for ct in range(len(sys.argv)-1):
            ct += 1
            st = sys.argv[ct]
            if isValidSSN(st):
                ssnList.append(st)
            if isPalindrome(st):
                palinList.append(st)
            if hasUpperCase(st):
                upperList.append(st)
            if hasEvenDigit(st):
                evenList.append(st)
            if endsWithS(st):
                Slist.append(st)
        print(printReport(checkList(ssnList),checkList(palinList),\
                          checkList(upperList),checkList(evenList)\
                          ,checkList(Slist)))
    else:
        print("You need to enter the correct arguments as following to execute:\n\
python program10.py xxx-xx-xxxx xxx xxxxx xx xxx xxxx\n\
eg: python program10.py 504 111-22-3333  313 HEllO by2e 11 cdc 232 toys abba ")
        
        
        

if __name__ == '__main__':
    main()
    
    

