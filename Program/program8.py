import datetime
from datetime import timedelta
class Account:
    _lastAcctNumUsed = 102459
    _numSavingsAccts = 0
    _numCheckingAccts = 0
    _totalAssets = 0
    def __init__(self,acctType,openBal,dateOpened):
        """
        PreCondition : acctType is string, openBal is a float number and dateOpened is a date object.
        PostCondition: attributes are initialized ( acctNum, acctType,openBal,CurBal, DateOpened)
        Description:Creates an object type Account
        """
        Account._lastAcctNumUsed += 1
        self._acctNum = Account._lastAcctNumUsed
        self._acctType = acctType
        self._openBal = openBal
        self._curBal = openBal
        self._dateOpened = dateOpened
        self._totalInterestEarned = 0
    def __str__(self):
        """
        PreCondition : None
        PostCondition: None
        Description: Returns string version of attribures values.
        """
        return ("Account Number: {:>31d}\nAccount Type: {:>33s}\nDate Opened:{:24s} {:}\nOpening Balance: {:>30.2f}\nCurrent Balance: {:>30.2f}\n"\
                .format(self._acctNum,self._acctType," ",self._dateOpened,self._openBal,self._curBal))
    def getAcctType(self):
        """
        PreCondition : None
        PostCondition: None
        Description: Returns the value(string) of the acctType attribute
        """
        return self._acctType
    def getOpenBalance(self):
        """
        PreCondition : None
        PostCondition: None
        Description: Returns the value(float) of the openBal attribute
        """
        return self._openBal
    def getCurBalance(self):
        """
        PreCondition : None
        PostCondition: None
        Description: Returns the value(float) of the curBal attribute
        """
        return self._curBal
    def getDateOpened(self):
        """
        PreCondition : None
        PostCondition: None
        Description: Returns the value(dateObject) of the dateOpened attribute
        """
        return self._dateOpened
    def getAcctNum(self):
        """
        PreCondition : None
        PostCondition: None
        Description: Returns the value(integer) of acctNum attribute
        """
        return self._acctNum
    def getNumSavingsAccts(self):
        """
        PreCondition : None
        PostCondition: None
        Description: Returns the value of NumSavingsAccts(number of saving accounts in integer) attribute
        """
        return Account._numSavingsAccts
    def getNumCheckingAccts(self):
        """
        PreCondition : None
        PostCondition: None
        Description: Returns the value of numCheckingAccts (number of checking accounts in integer)attribute
        """
        return Account._numCheckingAccts
    def getTotalAssets(self):
        """
        PreCondition : None
        PostCondition: None
        Description: Returns the value of totalAssets attribute
        """
        return Account.__totalAssets   
    def setCurBalance(self,newBalance):
        """
        PreCondition : newBalance must be a float number.
        PostCondition: attribute curBal is updated to newBalance
        Description: Updates the state of the Account object curBal to newBalance.
        """
        self._curBal = newBalance
    def updateTotalAssets(self,chekcing,saving):
        totalAssets = self._curBalace + checking._curBalance + saving._curBalance


class CDSavingAcct(Account):
    _CDIntRate = 0.10
    def __init__(self, acctType,openBal,dateOpened,maturityDate):
        """
        PreCondition : acctType is string, openBal is a float number and dateOpened & maturityDate are date object
        PostCondition: attributes are initialized ( acctNum, acctType,openBal,CurBal, DateOpened, maturityDate)
        Description: Creates an object of type CDSavings Account.
        """
        Account.__init__(self,acctType,openBal,dateOpened)
        self._maturityDate = maturityDate
        Account._numSavingsAccts += 1
    
    def __str__(self):
        """
        PreCondition : None
        PostCondition: None
        Description: Returns string version of attribures values.
        """
        tmp = "\n" +Account.__str__(self) \
              + "Total Interest Earned:{:>25.2f}".format(self._totalInterestEarned) +"\n"
        return tmp
    def computeInterest(self):
        """
        PreCondition : None
        PostCondition: Updates curBal and totalInterestEarned attributes.
        Description: calculates and returns amount of interest and also updates curBalace and totalInterestEarned by adding amount of interest
        """
        I = (self._curBal * CDSavingAcct._CDIntRate)
        self._curBal += I
        self._totalInterestEarned += I
        return I
    def closeAcct(self):
        """
        PreCondition : None
        PostCondition: None
        Description: Returns string version of attribures values.
        """
        today = datetime.date.today()
        if self._maturityDate<=today:
            Account._numSavingsAccts -= 1
            Account._totalAssets -= self._curBal
            self._totalInterestEarned = 0
            self._curBal = 0
            self._openBal = 0
            print("Account Closed sucessfull")
            
        else:
            print ("Not able to close your saving account at this time. You will need to wait untill",\
                   self._maturityDate," to be able to close your account.\n \n NOT ALLOWED!")
            
            
            
class CheckingAcct(Account):
    
    def __init__(self,acctType,openBal,dateOpened):
        Account.__init__(self,acctType,openBal,dateOpened)
        self._totalDepositAmts = 0
        self._totalWithdrawalAmts = 0
        Account._numCheckingAccts += 1

    def __str__(self):
        return "\n" + Account.__str__(self)\
               +"Total Deposit: {:>32.2f}\nTotal WithDrawal:{:>30.2f}\n"\
               .format(self._totalDepositAmts,self._totalWithdrawalAmts)
    def updateCurrentBalance(self,amt):
        if amt >= 0:
            self._curBal += amt
        else:
            self._curBal += amt
    def deposit(self,amt):
        self._totalDepositAmts += amt
        CheckingAcct.updateCurrentBalance(self,amt)
    def withdrawal(self,amt):
        if amt<=self._curBal:
            self._totalWithdrawalAmts += amt
            CheckingAcct.updateCurrentBalance(self,-amt)
            return "\nSuccessful"
        else:
            return "\nUnsuccessful"    
        
