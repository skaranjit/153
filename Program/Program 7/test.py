def myGCD(num1,num2):
    if num1 == 0:
        return num2
    elif num2 == 0:
        return num1
    else:
        while num2 != 0 :
            quotient = num1//num2
            remainder = num1 % num2
            
            num1 = num2
            num2 = remainder
            
            print(num1,num2)
       
        return num1


num1 = 400
num2 = -300

print(myGCD(num1,num2))
