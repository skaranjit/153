"""
This Program contains two functions #CreateMenu and #getValidChoice. It also contain the List to provide to the function to return the formatted Menu. The functions are described below. 
"""
__author__ = "Suman Karanjit"
__date__ = "02/06/2019"
chList = ["Add", "Subtract", "Divide", "MultiPly", "Quit"]
menuTitle = "Main Menu"

optionList = ["Deposit","Withdrawal","Quit"]


def CreateMenu(chList, menuTitle):
    """
    This Function will take two parameter,chList( List, List of menu item) and menuTitle( str, Title of Menu). It will then print out the formatted Menu.
    """
    tmpStr = ""
    ct = "1"
    
    for item in chList:
        tmpStr = tmpStr + ct + ". " + item + "\n"
        ct = int(ct) + 1
        ct = str(ct)
    return menuTitle +"\n" + tmpStr

menustr = CreateMenu(chList,menuTitle)
menuStr = CreateMenu(optionList, "Banking Menu")

print(menustr)
print(menuStr)
def getValidChoice(NoOfCh, menuStr):
    """
    This function will take two paramenter, NoOfCh(int, len of the menuList) and menuStr( str , Formatted Menu ). It will print out the menu and ask user for the choice. Until and unless user select number for quit it will ask to enter choice.
    Also will print Invalid and ask for the choice while the choice is not valid.Choice needs to be integer less than NoOfCh and greater that zero
    """
    print(menuStr)
    menuStrList = menuStr.split("\n")
    menuList = []
    for ct in range(1,len(menuStrList)-1):
        menuItem = menuStrList[ct].split()
        menuList.append(menuItem[1])
    choice = input("Enter your choice: " )
    while choice != str(NoOfCh):
        while not choice.isdigit() or int(choice) <= 0 or int(choice) > NoOfCh or choice == str(NoOfCh):
            print("\nInvalid Choice -- Please Try Again \n")
            print(menuStr)
            choice = input("Enter your choice: " )
                
        print("You Choose: ",menuList[int(choice)-1], "\n\n")
        print(menuStr)
    
        choice = input("Enter your choice: " )
    print("\n")
    return "Thank You For Using Program"
print(getValidChoice(len(chList),menustr))
print(getValidChoice(len(optionList),menuStr))

    
    
    


