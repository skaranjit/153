from modAccount import *
a1 = Account("generic", date(2019,3,28), 100)
s1 = CDSavingsAcct(date(2019,3,15), 200,date(2019,3,1))
s2 = CDSavingsAcct(date(2019,2,28), 200,date(2019,3,1))
c1 = CheckingAcct(date(2019,3,28),300)
print("account: ", a1) 
print("savings: ", s1)
print("checking: ", c1)
print(Account.getTotalAssets()) #should be 600
s1.closeAcct() #should print a message that it cannot be closed 
s2.closeAcct( )
print('\n***CLOSE', Account.getTotalAssets())#should be 400

c1.deposit(100)
print('\n***DEPOSIT', c1, "\n", Account.getTotalAssets()) #should be 500

c1.deposit(100)
print('\n***DEPOSIT', c1, "\n", Account.getTotalAssets()) #should be 600

c1.withdrawal(10000)
print('\n***WITHDR', c1, "\n",Account.getTotalAssets()) #should be 600

c1.withdrawal(100)
print('\n***WITHDR', c1, "\n", Account.getTotalAssets()) #should be 500

c1.withdrawal(100)
print('\n***WITHDR', c1,"\n", Account.getTotalAssets()) #should be 400
