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

PID = input("Enter an ID:")
while not PID.isdigit():
    print("Invalid ID")
    PID = input("Enter an ID:")
PID = int(PID)
fName = input("Enter First Name: ")
lName = input("Enter Last Name: ")
BirthYear = input("Enter your birth Year: ")
while not BirthYear.isdigit():
    print("Invalid Birth Year")
    BirthYear = input("Enter your birth Year: ")
BirthYear = int(BirthYear)
    
BirthMonth = input("Etner your birth Month: ")
while not BirthMonth.isdigit():
    print("Invalid Birth Month")
    BirthMonth = input("Enter your birth Month: ")
BirthMonth = int(BirthMonth)
BirthDay = input("Enter you birth day: ")
while not BirthDay.isdigit():
    print("Invalid Birth Day")
    BirthDay = input("Enter your birth Day: ")
BirthDay= int(BirthDay)


p3 = Person(PID,fName,lName,date(BirthYear,BirthMonth,BirthDay))
print(p3)
    
