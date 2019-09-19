__author__="Suman Karanjit"
__date__="04/29/2019"

"""
Description = This program will find the binary number that is divisible by given number and also finds the even between user input whose every digit is even.
"""

def isDivisibleByNum(tmpList,num):
    """
    Pre-Condition: tmpList should be a list of string of binary number and num should be a integer
    Post-Condition: None
    Description: Returns a list of string of binary digits which is divisible by given number.
    """
    result = []
    for binaryNum in tmpList:
        try:
            binaryNum.isdigit()
            tmpdec =0
            decNum = 0            
        except:
            return "Error: Needs to be a string of binary digit",binaryNum,"not a binary digit."
        for ct in range(len(binaryNum)-1,-1,-1):
            if (binaryNum[ct] != "1") and (binaryNum[ct] != "0"):
                return "Error: Needs to be a binary digit.",binaryNum," not a binary digit."
            if binaryNum[ct]=="1":
                decNum += 2**tmpdec
            tmpdec+=1
        if decNum%num==0:
            result.append(binaryNum)
    return result

def findEvenDigits(lowBound,highBound):
    """
    Pre-Condition: lowBound and highBound needs to be a integer.LowBound needs to be lower integer than highBound
    Post-Condition: None
    Description: Returns a list of numbers whose each digit is even.
    """
    result = []
    try:
        lowBound = int(lowBound)
        highBound = int(highBound)
    except:
        return "Error, parameters needs to be a number"
    for ct in range(lowBound,highBound+1,1):
        ct = str(ct)
        flag = 0
        for digit in ct:
            if int(digit)%2 == 0:
                flag += 1
        if flag >= len(ct):
            result.append(int(ct))
        ct = int(ct)
        ct+=1
    return result
        
############Main###############################                
tmpList = ["0100","1111","0000","0011","1010","1001","0101","1001"]
resultList = isDivisibleByNum(tmpList,4)
print(resultList)
evenDigits = findEvenDigits(10,"62")
print(evenDigits)
                    
                    
