sum = 0
numFound = 0
for ct in range(2,21,3):
    sum+=ct;
    if (ct % 2 ==0) or (ct % 5 == 0):
        numFound += 1
    print("numFound: ", numFound)
    print("ct: ", ct)
    print("sum: ",sum)
    
print(numFound)
