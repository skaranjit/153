tmpList = [i for i in range(1,101)]
guess = 76
def mysearch(tmpList, numtoFind):
    mIn = 1
    Max = 100
    while numtoFind != guess:
        if numtoFind not in tmpList:
            print("not in list")
        elif numtoFind > guess:
            print("Higher!")
            tmpList = [i for i in range(mIn,numtoFind)]
            Max = numtoFind
            print(tmpList)
        elif numtoFind < guess:
            print("Lower")
            tmpList = [i for i in range(numtoFind+1, Max)]
            mIn = numtoFind+1
            print(tmpList)
        numtoFind = int(input("Enter your guess"))
        
    return numtoFind

numtoFind = int(input("Enter your guess"))
print(mysearch(tmpList,numtoFind))
