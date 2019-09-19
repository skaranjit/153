from modAccount import *
import datetime
from datetime import timedelta



####################Account########################################

Myaccount = Account ("Generic",200.00,datetime.date(2018,9,9))
print(Myaccount)

#######################Saving Accounts################################

SavingAccount= CDSavingAcct("Savings",200.00,datetime.date(2018,9,9),datetime.date(2018,10,9))
print(SavingAccount)
Interest = SavingAccount.computeInterest()
print("Interest= ", round(Interest,2))
print("After Interest:")
print(SavingAccount)
SavingAccount.closeAcct() #Will close saving account
print("\nAfter Closing account:",SavingAccount)
##############################Checking Account#########################

checkingAccount = CheckingAcct("Checking",400.00,datetime.date(2018,9,20))
print(checkingAccount)

checkingAccount.deposit(1200)    #Deposit in checking account
print("After Deposit:",checkingAccount)
print(checkingAccount.withdrawal(200)) #When current balance is more than withdraw amount
print(checkingAccount.withdrawal(2000)) #When Current balance is less than withdrawal amount.



###################Test Get Method##############################
print("The following will print from get methods:\n")
print("Account Type:"+Myaccount.getAcctType(),\
      "\nAccount Number:"+ str(Myaccount.getAcctNum()),\
      "\nOpening Balance:"+str(Myaccount.getOpenBalance()),\
      "\nCurrent Balance:"+str(Myaccount.getCurBalance()),\
      "\nDate Opened:"+str(Myaccount.getDateOpened()),\
      "\nNumber of Saving Accounts:"+str(Myaccount.getNumSavingsAccts()),\
      "\nNumber of Checking Accounts:"+str(Myaccount.getNumCheckingAccts()),\
      "\nTotal Assets:"+str(round(Myaccount.getTotalAssets(),2)))

print("\nThe following will print after calling set methods:\n")
SavingAccount.setCurBalance(40)
print(SavingAccount)
SavingAccount.computeInterest()
print("The following will print after computing Interest:\n")
print(SavingAccount)
print("The following will print after updating totalAssets:\n")
Myaccount.updateTotalAssets(checkingAccount,SavingAccount)
print("Total Assets:"+ str(round(Myaccount.getTotalAssets(),2)))


