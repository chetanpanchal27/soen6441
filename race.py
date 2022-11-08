class Race:
    def __init__(self, raceId,year,round,name,date,time,circuitId):
        self.raceId=raceId
        self.year=year
        self.round=round
        self.name=name
        self.date=date
        self.time=time
        self.circuitId=circuitId
    def getraceId(self):
        return self.raceId
    def setraceId(self,raceId):
        self.raceId=raceId
    def getyear(self):
        return self.year
    def setyear(self,year):
        self.year=year
    def getround(self):
        return self.round
    def setround(self,round):
        self.round=round
    def getname(self):
        return self.name
    def setname(self,name):
        self.name=name
    def getdate(self):
        return self.date
    def setdate(self,date):
        self.date=date
    def gettime(self):
        return self.time
    def settime(self,time):
        self.time=time
    def getcircuitId(self):
        return self.circuitId
    def setcircuitId(self,circuitId):
        self.circuitId=circuitId
        
            
        