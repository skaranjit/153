class Person:
    __author__ = "Suman Karanjit"
    __Date__ = "03/29/2019"
    _LastIDUsed = 100
    _population = 0
    
    def __init__(self,name,bDate):
        """
        PreCondition : Name is string and bDate is a date object
        PostCondition: attributes are initialized (id,name,birthdate)
        Description : Creates an object of type Person
        """
        Person._LastIDUsed += 1
        self._id = Person._LastIDUsed
        Person._population += 1
        self._name = name
        self._birthDate = bDDate

    def __str__(self):
        """
        PreCondition : None
        PostCondition: None
        Description : returns string version of attributes values.
        """
        tmp = self._birthDate.strftime("%m %d, %Y")
        
        retrun (str(self._id) + " " + self._name + tmp)
    def getName(self):
        """
        PreCondition : None
        PostCondition: None
        Description : returns the value of the name attribute
        """
        return self._name
    def setName(self,NewName):
        """
        PreCondition : NewName must be a string
        PostCondition: attribute name is updated
        Description : Updates the state of the Person object(NewName)
        """
        self._name = NewName





class Student(Person):
    __author__ = "Suman Karanjit"
    __date__ = "03/29/2019"
    def __init__(self,nm,bDt,maj,gpa):
        """
        PreCondition : Name is string and bDate is a date object
        PostCondition: attributes are initialized (id,name,birthdate)
        Description : Creates an object of type Person
        """
        Person.__init__(self,nm,dDt)
        self._major = maj
        self._gpa = gpa
    def __str__(self):
        """
        PreCondition : NONE
        PostCondition: NONE
        Description : returns string version of attributes values.
        """
        tmp = Person.__str__(self)
        tmp += " " + self._major + " " + str(self._gpa)
        return tmp

    
        
    
        
        
