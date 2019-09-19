"""
This Program contains two functions #CreateMenu and #getValidChoice. It also contain the List to provide to the function to return the formatted Menu. The functions are described below. 
"""
__author__ = "Suman Karanjit"
__date__ = "02/06/2019"





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
    print(menuStr)
    choice = input("Enter your choice: " )
    while not choice.isdigit() or int(choice) <= 0 or int(choice) > NoOfCh:
        print("\nInvalid Choice -- Please Try Again \n")
        print(menuStr)
        choice = input("Enter your choice: " )
    return choice


#main
chList = ["Add", "Subtract", "Divide", "MultiPly", "Quit"]
menuTitle = "Main Menu"

optionList = ["Deposit","Withdrawal","Quit"]
menustr = CreateMenu(chList,menuTitle)
menuStr = CreateMenu(optionList, "Banking Menu")
print(menustr)
print(menuStr)
choice = getValidChoice(len(chList),menustr)
#BankChoice = getValidChoice(len(optionList),menuStr)

while choice != str(len(chList)):
    print("Your Choice : ",chList[int(choice)-1])
    choice = getValidChoice(len(chList),menustr)
print("Thank you for Using this program")
