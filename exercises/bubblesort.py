myList = [(1,3),(1,7),(3,4,6),(3,2,2)]
passCt=1
for i in range( len(myList),1,-1):
    for j in range (i-1):
        if myList[j][len(myList[j])-1] > myList[j+1][len(myList[j])-1]:
            tmp = myList[j]
            myList[j] = myList[j+1]
            myList[j+1] = tmp
    print("Pass ",passCt,myList)
    passCt+=1
print(myList)

