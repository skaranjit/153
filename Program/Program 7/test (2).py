"""
This is a class called fraction. It will take two number and create a fraction.

"""
__author__="Suman Karanjit"
__date__="03/16/2019"

class Fraction:
    def myGCD(num1,num2):
        """
        Pre-condition : Rquires two number
        Post-Condition: None
        
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

    def __init__(self,numerator = 0,denominator = 1):
        """
        Pre-Condition: Reuires 2 number
        post-condition: Denominator should not be negative

        This is the constructor method to initialize fracList. It will store numerator and demoninator divided by highest factor.
        """
        if denominator == 0 :
            denominator = 1

        highFactor = Fraction.myGCD(numerator,denominator)

        self._fracList = [numerator/highFactor,denominator/highFactor]

    def __add__(self,other):
        """
        Pre-Condition: Reuires 2 number
        post-condition: Denominator should not be negative

        This is the constructor method to initialize fracList. It will store numerator and demoninator divided by highest factor.
        """

        n1 = self._fracList[0]
        n2 = other._fracList[0]
        d1 = self._fracList[1]
        d2 = other._fracList[1]
        n3 = n1*d2 + n2*d1
        d3 = d1*d2
        highFactor = Fraction.myGCD(n3,d3)
        return str(int(n3/highFactor)) + "/" + str(int(d3/highFactor))

    def __sub__(self,other):
        """
        Pre-Condition: Reuires 2 number
        post-condition: Denominator should not be negative

        This is the constructor method to initialize fracList. It will store numerator and demoninator divided by highest factor.
        """

        n1 = self._fracList[0]
        n2 = other._fracList[0]
        d1 = self._fracList[1]
        d2 = other._fracList[1]
        n3 = n1*d2 - n2*d1
        d3 = d1*d2
        highFactor = Fraction.myGCD(n3,d3)
        return str(int(n3/highFactor)) + "/" + str(int(d3/highFactor))
    
    def __mul__(self,other):
        """
        Pre-Condition: Reuires 2 number
        post-condition: Denominator should not be negative

        This is the constructor method to initialize fracList. It will store numerator and demoninator divided by highest factor.
        """

        n1 = self._fracList[0]
        n2 = other._fracList[0]
        d1 = self._fracList[1]
        d2 = other._fracList[1]
        n3 = n1*n2
        d3 = d1*d2
        highFactor = Fraction.myGCD(n3,d3)
        return str(int(n3/highFactor)) + "/" + str(int(d3/highFactor))
    
    def __truediv__(self,other):
        """
        Pre-Condition: Reuires 2 number
        post-condition: Denominator should not be negative

        This is the constructor method to initialize fracList. It will store numerator and demoninator divided by highest factor.
        """

        n1 = self._fracList[0]
        n2 = other._fracList[0]
        d1 = self._fracList[1]
        d2 = other._fracList[1]
        n3 = n1*d2
        d3 = d1*n2
        highFactor = Fraction.myGCD(n3,d3)
        return str(int(n3/highFactor)) + "/" + str(int(d3/highFactor))
    
    def __lt__(self,other):
        n1 = self._fracList[0]
        n2 = other._fracList[0]
        d1 = self._fracList[1]
        d2 = other._fracList[1]
        if n1/d1 < n2/d2:
            return True
        else:
            return False
       
    def __gt__(self,other):
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
        Pre-Condition: Reuires 2 number
        post-condition: Denominator should not be negative

        This is the constructor method to initialize fracList. It will store numerator and demoninator divided by highest factor.
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
        Post-Condition: should change integer to string

        This will print the fraction in x/y format.
        """
        return str(int(self._fracList[0])) + "/" + str(int(self._fracList[1]))
   
