"""
This person module is a class to create an object. It have all data private. It provide getter and setter method for user to acess amd change the values.
"""
__author__ = "Suman Karanjit"
__date__ ="02/27/2019"
from datetime import *

class Person:
    #construtor method
    def __init__(self,idNum,fName,lName,birthDate):
        self._idNum = idNum   #Underscore makes the parameter private.
        self._fName = fName   
        self._lName = lName
        self._birthDate = birthDate     
    def __str__(self):
        tmp = str(self._idNum) + " " + self._fName + " " + self._lName\
              + "\n" + self._birthDate.strftime("%b %d, %Y")        
        return tmp
    ###Retrueve a private attribute --- use a getter
    def getIdNum(self):
        return self._idNum
    def getFirstName(self):
        return self._fName
    def getLastName(self):
        return self._lName
    def getBirthDate(self):
        return self._birthDate
    ###Change the value of a private attribute -- use a setter

    def setIdNum(self,newID):
        self._idNum = newID
    def setFirstName(self,newfName):
        self._fName = newfName
    def setLastName(self,newlName):
        self._lName = newlName
    def setBirthDate(self,newBDate):
        self._birthDate = newBDate

