class Airline:
    def __init__(self, airline_id,callsign,date_founded,iata_code,airline_name,country_name,status):
        self.airline_id = airline_id
        self.callsign = callsign
        self.date_founded = date_founded   
        self.iata_code = iata_code
        self.airline_name = airline_name
        self.country_name = country_name
        self.status = status
    def getairline_id(self):
        return self.airline_id
    def getcallsign(self):
        return self.callsign
    def getdate_founded(self):
        return self.date_founded
    def getiata_code(self):
        return self.iata_code
    def getairline_name(self):      
        return self.airline_name
    def getcountry_name(self):
        return self.country_name
    def getstatus(self):
        return self.status
    def setairline_id(self,airline_id):
        self.airline_id=airline_id
    def setcallsign(self,callsign):
        self.callsign=callsign
    def setdate_founded(self,date_founded):
        self.date_founded=date_founded
    def setiata_code(self,iata_code):
        self.iata_code=iata_code
    def setairline_name(self,airline_name):
        self.airline_name=airline_name
    def setcountry_name(self,country_name):
        self.country_name=country_name
    def setstatus(self,status):
        self.status=status
    
    
        
    
    
    

