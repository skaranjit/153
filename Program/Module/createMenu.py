chList = ["Add", "Subtract", "Divide", "MultiPly", "Quit"]
menuTitle = "Main Menu"

optionList = ["Deposit","Withdrawal","Quit"]


def CreateMenu(chList, menuTitle):
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

