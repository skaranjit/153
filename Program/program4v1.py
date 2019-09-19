"""
This program will display a menu to the user and ask for the choice . User can add employee or print out the report from the menu. It will take only integers as a choice.
The program stores data into dictionary with the ID as the Key. User can change the value of the specific id if they want to but will need to know the ID.

"""
__author__ = "Suman Karanjit"
__date__ = "02/10/2019"

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
    while not choice.isdigit() or int(choice) <= 0 or int(choice) > NoOfCh:
        print("\nInvalid Choice -- Please Try Again \n")
        print(menuStr)
        choice = input("Enter your choice: " )
    return int(choice)

def getValidNumber(userInput):
    """
    This function will check and reuturn if the user input in number or not. If not integer it will keep asking user to enter valid one else will return the integer.
    
    """
    while not userInput.isdigit():
        userInput = input("Only Integer!. Enter valid number:")
    return int(userInput)

def isfloat(value):
    """
    Check if the user input can be float or not. Returns ture or False.
    """
    try:
        float(value)
        return True
    except ValueError:
        return False

def getValidName(name):
    """
    Check if the name is valid or not
    """
    if name.startswith(' '): return False
    if " " in name:
        nameList = name.split(" ")
        for item in nameList:
            for char in item:
                if not char.isalpha() or char == "":
                    return False
    else:
        for char in name:
            if not char.isalpha():
                print("x")
                return False
            
def addEmployee(empDict):
    """
    It will take dictionary and ask user for the details if valid it will add it to the dictionary and returns it.
    """
    id = input("Enter Your ID:")
    id = getValidNumber(id)
    
    while id in empDict:
        print("Duplicate ID found")
        print("ID: ",id)
        print("Name: ", empDict[id][0])
        change = input("Would you like to Override this ID? 'Y' or 'N': ")
        while not (change.lower() == "y" or change.lower() == "n"):
            print("Please enter either 'Y' or 'N'")
            print("ID: ",id)
            print("Name: ", empDict[id][0])
            change = input("Would you like to Override this ID? 'Y' or 'N': ")
            
        if change.lower() == 'y':
            empDict.pop(id,None)
            id = id
        else:
            id = input("Enter Your ID:")
            id = getValidNumber(id)
    name = input("Enter Full Name: ")
    while getValidName(name) == False:
        print("Invalid Name!")
        name = input("Enter Full Name: ")
    payrate = input("Enter Payrate: ")
    while isfloat(payrate) == False:
        print("Please enter valid number like: 10 , 10.5")
        payrate = input("Enter Payrate: ")
    payrate =float(payrate)
    hours = input("Enter Hours: ")
    while isfloat(hours) == False:
        print("Please enter valid number like: 40 , 40.5")
        hours = input("Enter Hours: ")
    hours = float(hours)
    if hours > 40:
        grossPay= (40*payrate)+((hours-40)*payrate*1.5)
    else:
        grossPay = hours * payrate
    empDict[id] = [name, payrate, hours,grossPay]
    return empDict



def PrintReport(empDict):
    print("{:>50s}".format("\n\nEmployee Roster\n\n"))
    print("{:10s}{:30s}{:15s}{:15s}{:15s}".format("ID","Name","PayRate","Hours","Gross Pay"))
    print("="*82)
    nameList=[]
    for key in empDict:            
        nameList.append((empDict[key][0].split(" ")))
    nameList.sort(key = lambda name: name[1])
    newNameList = []
    for item in nameList:
        name = item[0] + " " + item[1]
        newNameList.append(name)
    for name in newNameList:
        for key,values in empDict.items():
            payrate =  values[1]  
            hours = values[2]
            if name in values[0]:
                if values[2] > 40:
                    grosspay =  (40*payrate)+((values[2]-40)*payrate*1.5)
                else:
                    grosspay = hours * payrate
                print("{:<10}{:30s}{:15.2f}{:15.1f}{:15.2f}".format(key,name,values[1],values[2],grosspay))
        
    
#########################################main#######################################################################
Dict = {}
from os.path import *
import tkinter as tk
from tkinter import filedialog

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
        for tmpLine in fileObj:
            if len(tmpLine) > 1:                
                tmpList = tmpLine.split("\n")
                tmpListnew = []
                for item in tmpList:
                    if len(item) != 0:#It will ignore empty item and append the item to new List.
                        tmpListnew.append(item)
                value = []
                for item in tmpListnew:
                    value = item.split(", ")
                    key = int(value[0])
                    name = value[1]
                    payrate = float(value[2])
                    hours = float(value[3])
                    Dict[key] = [name,payrate,hours]
        print(Dict)
        fileObj.close()
else:
    print("File doesn't exist: ", fileName)
    

optionList = ["Add employee","Print Employee Report","Quit"]
menu = CreateMenu(optionList,"Employee Menu")
choice = getValidChoice(len(menu),menu)
while choice != 3:
    if choice == 1:
        
        empDict = addEmployee(Dict)
        print(empDict, "\n")
    else:
        PrintReport(Dict)
    choice = getValidChoice(len(menu),menu)
print("Thank You for Using this Program")


