from datetime import *
class Vehicle:
    _numVehicles = 1
    def __init__(self,VIN,Vtype,yearManufactured,color):
        self._numV = Vehicle._numVehicles
        Vehicle._numVehicles += 1
        self._VIN = VIN
        self._Vtype = Vtype
        self._yearManf = yearManufactured
        self._color = color

    def getNumVehicles():
        return Vehicle._numVehicles
    def getVIN(self):
        return self._VIN
    def getVtype(self):
        return self._Vtype
    def getyearManf(self):
        return self._yearManf
    def getColor(self):
        return slef._color

    def calcVehicleAge(self):
        nowYears = nowYear = int(datetime.now().strftime("%Y"))
        return (nowYears - self._yearManf)
    def __str__(self):
        return "Number of Vehicles: " +str(self._numV) + "\n" \
               + "VIN: " + str(self._VIN)+ "\n" + \
               "Type: " + self._Vtype + " \n" + \
               "Year Manufactured: " +str(self._yearManf) + "\n" + \
               "Color: " + self._color + " \n" + \
               "Vehicle Age: "+ str(Vehicle.calcVehicleAge(self))




class Car(Vehicle):
    _numMake = 1
    def __init__(self,tmpVIN,tmpType,tmpYear,tmpColor,tmpMake):
        self._numMake = Car._numMake
        Car._numMake += 1
        self._Vmake = tmpMake
        Vehicle.__init__(self,tmpVIN,tmpType,tmpYear,tmpColor)
        
    


    def getType(slef):
        return self._Vmake
    def getNumMake():
        return Car._numMake
    def __str__(self):
        tmp = Vehicle.__str__(self)
        tmp = tmp + "\n" + "Make: " + self._Vmake +\
              "\n" + "Number of " + self._Vmake + ": " + str(self._numMake)
        return tmp


V1 = Vehicle(1234,"CAR",1991,"RED")
H1 = Car(12345,"CAR",1991,"RED","Honda")
print(V1,H1)
    
    
