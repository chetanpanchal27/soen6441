class Driver:
    def __init__(self, driverId,driverRef,code, forename, surname,dob,nationality):
        self.driverId=driverId
        self.driverRef=driverRef
        self.code=code
        self.forename=forename
        self.surname=surname
        self.dob=dob
        self.nationality=nationality


    def getdriverId(self):
        return self.driverId
    def setdriverId(self,driverId):
        self.driverId=driverId
    def getdriverRef(self):
        return self.driverRef
    def setdriverRef(self,driverRef):
        self.driverRef=driverRef
    def getdob(self):
        return self.dob
    def setdob(self,dob):
        self.dob=dob
    def getcode(self):
        return self.code
    def setcode(self,code):
        self.code=code
    def getforename(self):
        return self.forename
    def setforename(self,forename):
        self.forename=forename
    def getsurname(self):
        return self.surname
    def setsurname(self,surname):
        self.surname=surname
    def getnationality(self):
        return  self.national
    def setnationality(self,nationality):
        self.nationality=nationality