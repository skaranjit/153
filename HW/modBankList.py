class Account:
    def __init__(self,tmpAcctNum,tmpBankName,tmpAcctType,tmpBalance):
        self._tmpList = [tmpAcctNum,tmpBankName,tmpAcctType,tmpBalance]
    def __str__(self):
        tmp = "{:20s}{:<4d}".format("Account Name",self._tmpList[0]) + "\n"\
              "{:20s}{:20s}".format("Bank:",self._tmpList[1]) + "\n"\
              "{:20s}{:20s}".format("Account Type",self._tmpList[2]) + "\n"\
              "{:20s}{:.2f}".format("Balance:",self._tmpList[3])
        return tmp
    def computeInterest(self,rate = 5, time =2):
        principle=self._tmpList[3]
        self._tmpList[3] = principle*(1+(rate*time)/100)
        return (self._tmpList[3]-principle)
    def getaccountNum(self):
        return self._tmpList[0]
    def getbankName(self):
        return self._tmpList[1]
    def getaccountType(self):
        return self._tmpList[2]
    def getbalance(self):
        return self._tmpList[3]

    def setaccountNum(self,newaccountNum):
        self._tmpList[0] = newaccountNum
    def setbankName(self,newbankName):
        self._tmpList[1] = newbankName
    def setaccountType(self,newaccountType):
        self._tmpList[2] = newaccountType
    def setbalance(self,newbalance):
        self._tmpList[3] = newbalance
    
        
########################
a1 = Account(111,"NORWEST","CHECKING",123.45)
print(a1)
Interest = a1.computeInterest(6,2)
print(Interest)
balance = a1.getbalance()
print(balance)

a1.setbalance(200)
print("After Changing balance:", a1)
