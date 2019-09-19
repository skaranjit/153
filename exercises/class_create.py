#Class : collection of attributes and methods

class Room:
    #construtor method
    def __init__(self,roomNum,length,width,height,rmType):
        self._roomNum = roomNum   #Underscore makes the parameter private.
        self._length = length   
        self._width = width
        self._height = height
        self._rmType = rmType
        

    def __str__(self):
        tmp = str(self._length)
        
        return tmp
    ###Retrueve a private attribute --- use a getter
    def getRoomNum(self):
        return self._roomNum

    ###Change the value of a private attribute -- use a setter

    def setRoomNum(self):
        self._roomNum = newRoomNum

#use the Room Class:
br161 = Room (161,45,20,13,"classroom")
br165 = Room(165,40,20,30,"lab")
print(br165)
print(br161)
roomNum = br161.getRoomNum()
print(roomNum)
