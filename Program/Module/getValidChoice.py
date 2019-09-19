def getValidChoice(NoOfCh, menuStr):
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
    
    
    
