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
    print("\n",menuStr)
    choice = input("Enter your choice: " )
    while not choice.isdigit() or int(choice) <= 0 or int(choice) > NoOfCh:
        print("\nInvalid Choice -- Please Try Again \n")
        print(menuStr)
        choice = input("Enter your choice: " )
    return choice


################################Bonus Function#################################
def HandleDeposit(balance):
    """
    This function will take one parameter(balance) which is also integer. It will ask user to enter the deposit amount until it is not integer greater to zero.
    And if so it will add to balance and return balance after adding deposit.O
    """
    deposit = input ("Enter deposit amount : ")
    while not deposit.isdigit() or int(deposit) < 0:
        print("Deposit amount must be only numbers")
        deposit = input ("Enter deposit amount : ")
    deposit = int(deposit)
    balance += deposit
    return balance

def HandleWithdrawl(balance):
    """
    This function will take one parameter(balance) which is also integer. It will ask user to enter the deposit amount until it is not integer equal or greater to zero and also the amoung % 10 is equal to zero.
    Also will check if the withdraw amount is lower than or equal to balance,then it will update balance and return it otherwise it will return error saying Overdraft not allowed.
    """
    WithdrawMoney= input("Enter amount to withdrawl : ")
    while not WithdrawMoney.isdigit() or int(WithdrawMoney) <= 0 or int(WithdrawMoney)%10 != 0:
        print("Withdrawl amount must be only numbers and needs to be multiplication of 10. For Eg: 10,20,30 etc.")
        WithdrawMoney= input("Enter amount to withdrawl : ")       
    WithdrawMoney = int(WithdrawMoney)
    if WithdrawMoney <= balance:
        balance -= WithdrawMoney

    else:
        print("\n{}{}\n".format("Overdraft is not allowed.Your Balance is $",balanceNow))
    
    return balance
        
        
        
        
    

###################################main#########################################
chList = ["Add", "Subtract", "Divide", "MultiPly", "Quit"]
menuTitle = "Main Menu"
menustr = CreateMenu(chList,menuTitle)
#print(menustr)
choice = getValidChoice(len(chList),menustr)


while choice != str(len(chList)):
    if int(choice) == 1:
        print("Your Choice : ",chList[int(choice)-1])
    elif int(choice) == 2:
        print("Your Choice : ",chList[int(choice)-1])
    elif int(choice) == 3:
        print("Your Choice : ",chList[int(choice)-1])
    elif int(choice) == 4:
        print("Your Choice : ",chList[int(choice)-1])
    choice = getValidChoice(len(chList),menustr)
print("\nThank you for Using this program\n")

#################################Bonus############################################################
optionList = ['Deposit','Withdrawal','Print Balance','Quit']
openingBalance = input("Enter opening balance of your checking account: ")

balanceNow = int(openingBalance)
BankMenu = CreateMenu(optionList, "Banking Menu")
#print(BankMenu)
BankChoice = getValidChoice(len(optionList),BankMenu)
while BankChoice != str(len(optionList)):
    if int(BankChoice) == 1:
        balanceNow = HandleDeposit(balanceNow)
    elif int(BankChoice) == 2:
        balanceNow = HandleWithdrawl(balanceNow)
    elif int(BankChoice) == 3:
        print("{}{}\n".format("Your Current balance is : $",balanceNow))
    BankChoice = getValidChoice(len(optionList),BankMenu)
    
print("\nThank You for using our Banking Solution.")

#####################################################################################################################
