AskUser = input("Enter Number or type 'Done' to quit: ")
NumList = []
Positive = []
oddNum = []
while AskUser.lower() != "done":
    if AskUser.isdigit() or (AskUser.startswith("-") and AskUser[1:].isdigit()):
        AskUser = int(AskUser)
        NumList.append(AskUser)
        if AskUser >= 0:
            Positive.append(AskUser)
        if AskUser%2 !=0:
            oddNum.append(AskUser)
            
    else:
        print("Only numbers or type done to exit")
    
    AskUser = input("Enter Number or type 'Done' to quit: ")

if Positive != []:
    print("Maximum:", max(Positive))

if oddNum != []:
    oddNum.sort(reverse = True)
    print("Odd Numbers:",oddNum)
