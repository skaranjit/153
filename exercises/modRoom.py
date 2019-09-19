class Room:
    __author__ = "Suman Karanjit"
    __date__ = "3/20/2019"
    def __init__(self,l,w):
        """
        PreCondition: l and w are positive and numeric
        PostCondition: length and width are updated.
        Description: Creates an object of type room and initializes the private attributes.
        
        """
        self._length = l
        self._width = w

    def getWidth(self):
        """
        PreCondition: None
        PostCondition: None
        Description:Retrieves the private width attribute
        """
        return self._witdh
    def setLen(self,newLength):
        """
        PreCondition: newLength is a positive number
        PostCondition: length is updated 
        Description: Sets length attribute to newLength.
        """
        self._length = newLength

    
