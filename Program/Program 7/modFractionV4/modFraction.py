"""
This is a class called fraction. It will take two number and create a fraction.

"""
__author__="Suman Karanjit"
__date__="03/16/2019"
def myGCD(num1,num2):
        """
        Pre-condition : Rquires two number
        Post-Condition: Return greatest common divisor of two number
        
        This is to calculate greatest common divisor using euclidean Algorithm.
        Source:https://www.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/the-euclidean-algorithm        
        """
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
        return num1

class Fraction:
    
    def __init__(self,numerator = 0,denominator = 1):
        """
        Pre-Condition: Reuires 2 number
        post-condition: Returns string of fraction.

        This is the constructor method to initialize fracList. It will store numerator and demoninator divided by highest factor.
        """
        if denominator == 0 :
            denominator = 1

        highFactor = myGCD(numerator,denominator)

        self._fracList = [int(numerator/highFactor),int(denominator/highFactor)]

    def __add__(self,other):
        """
        Pre-Condition: Reuires 2 Objects. 
        post-condition: returns fraction object

        This is method to add two fraction object and returns sting of sum.
        """

        n1 = self._fracList[0]
        n2 = other._fracList[0]
        d1 = self._fracList[1]
        d2 = other._fracList[1]
        n3 = (n1*d2) + (n2*d1)
        d3 = d1*d2
        return Fraction(n3,d3)

    def __sub__(self,other):
        """
        Pre-Condition: Reuires 2 Objects. 
        post-condition: returns fraction object

        This is method to subtract two fraction object and returns sting of sum.
        """
        n1 = self._fracList[0]
        n2 = other._fracList[0]
        d1 = self._fracList[1]
        d2 = other._fracList[1]
        n3 = n1*d2 - n2*d1
        d3 = d1*d2
        return Fraction(n3,d3)
    
    def __mul__(self,other):
        """
        Pre-Condition: Reuires 2 Objects. 
        post-condition: returns fraction object

        This is method to multiply two fraction object and returns sting of sum.
        """

        n1 = self._fracList[0]
        n2 = other._fracList[0]
        d1 = self._fracList[1]
        d2 = other._fracList[1]
        n3 = n1*n2
        d3 = d1*d2
        return Fraction(n3,d3)
    
    def __truediv__(self,other):
        """
        Pre-Condition: Reuires 2 Objects. 
        post-condition: returns fraction object 

        This is method to divide two fraction object and returns sting of sum.
        """

        n1 = self._fracList[0]
        n2 = other._fracList[0]
        d1 = self._fracList[1]
        d2 = other._fracList[1]
        n3 = n1*d2
        d3 = d1*n2
        return Fraction(n3,d3)
    
    def __lt__(self,other):
        """
        Pre-Condition: Reuires 2 Objects. 
        post-condition: returns Bolean value 

        This is method to compare two fraction object and returns bolean value.
        """
        n1 = self._fracList[0]
        n2 = other._fracList[0]
        d1 = self._fracList[1]
        d2 = other._fracList[1]
        if n1/d1 < n2/d2:
            return True
        else:
            return False
       
    def __gt__(self,other):
        """
        Pre-Condition: Reuires 2 Objects. 
        post-condition: returns Bolean value 

        This is method to compare two fraction object and returns bolean value.
        """
        n1 = self._fracList[0]
        n2 = other._fracList[0]
        d1 = self._fracList[1]
        d2 = other._fracList[1]
        if n1/d1 > n2/d2:
            return True
        else:
            return False
        

    def __eq__(self,other):
        """
        Pre-Condition: Reuires 2 Objects. 
        post-condition: returns Bolean value 

        This is method to compare two fraction object and returns bolean value.
        """

        n1 = self._fracList[0]
        n2 = other._fracList[0]
        d1 = self._fracList[1]
        d2 = other._fracList[1]
        if n1/d1 == n2/d2:
            return True
        else:
            return False
    
    def __str__(self):
        """
        Pre-Condition: None
        Post-Condition: Returns string of fraction

        This will print the fraction in x/y format when object is printed.
        """
        return str(self._fracList[0]) + "/" + str(self._fracList[1])
   
