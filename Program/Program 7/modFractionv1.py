"""
This is a class called fraction. It will take two number and create a fraction.

"""
__author__="Suman Karanjit"
__date__="03/16/2019"

def calcHCF(x,y):
    if x < y:
        lownum = x
    else:
        lownum = y
    for i in range(1,lownum+1):
        if (x%i == 0) and (y%i == 0):
            gcd = i
    return gcd
        



print(calcHCF(60,68))

print(calcHCF(60,60))

print(calcHCF(50,60))
print(calcHCF(24,0))


print("3/4 = ", int(3/calcHCF(3,4)) ,"/" ,+ int(4/calcHCF(3,4)))
