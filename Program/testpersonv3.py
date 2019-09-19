"""
This program will call the class module to create object. It will also call getter and setter to access the values of the object created.At last it will ask user for id, firstname, lastname, birth year
bith month, and birth day and will create a object calling the class from moduleperson.
"""
__author__ = "Suman Karanjit"
__date__ ="02/27/2019"

from modPerson import Person
from datetime import *
p1 = Person(111,"Joe", "Jones", date(2010,1,1) )
p2 = Person(222,"Sally", "Smith", date(1990, 9, 30) )
print("Person 1: ", p1)
print("Testing getters for Person 1")
idNum = p1.getIdNum(); print("ID Number: ", idNum)
fName = p1.getFirstName();  print("First name: ", fName)
lName = p1.getLastName(); print("Last name: ", lName)
bDay = p1.getBirthDate( );  print("Birthdate: ", bDay)
print("Person 2: ", p2)
print("\nTesting setters for Person 2")
p2.setIdNum("123")
p2.setFirstName("Joseph")
p2.setLastName("Johnson")
p2.setBirthDate( date(2000,10,31))
print("After changing p2’s first name to Joseph, last name to Johnson, and birthdate to 10/31/2000")
print(p2)
###############################################
def validateNum(num):
    try:
        num = int(num)
        return True
    except:
        return False
def ValidateMonth(Mon):
   
    if validateNum(Mon):
        Mon = int(Mon)
        if Mon < 13 and Mon > 0:
            return True
        else:
            return False
    else:
        return False
def ValidateYear(year):
    if validateNum(year):
        year = int(year)
    else: return False
    nowYear = int(datetime.now().strftime("%Y"))
    if year in range(1,nowYear):
        return True
    else:
        return False

def ValidateDay(day,year,month):
    if validateNum(day):
        day = int(day)
        year = int(year)
        month = int(month)
    else:
        return False
    try:
        date_correct = date(year,month,day)
        return True
    except:
        return False
        
    
print("\n\n")

PersonID = input("Enter an ID:")
while validateNum(PersonID) == False:
    print("Invalid ID")
    PersonID = input("Enter an ID:")
PersonID = int(PersonID)

fName = input("Enter First Name: ")
lName = input("Enter Last Name: ")

BirthYear = input("Enter your birth Year: ")
while ValidateYear(BirthYear) == False:
    print("Invalid Birth Year")
    BirthYear = input("Enter your birth Year: ")
BirthYear = int(BirthYear)
    
BirthMonth = input("Etner your birth Month: ")
while ValidateMonth(BirthMonth) == False:
    print("Invalid Birth Month")
    BirthMonth = input("Enter your birth Month: ")
BirthMonth = int(BirthMonth)

birthDay = input("Enter you birth day: ")
while ValidateDay(birthDay,BirthYear,BirthMonth) == False:
    print("Invalid Birth Day")
    birthDay = input("Enter your birth Day: ")
birthDay= int(birthDay)



p3 = Person(PersonID,fName,lName,date(BirthYear,BirthMonth,birthDay))
print(p3)
    
