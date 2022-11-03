from mapper import getairline_namebyid,add_airline,getallairline,update_airline,delete_airline
from airline import Airline

##add airline
# id=input("Enter Airline ID: ==> ")
# callsign=input("Enter Airline callsign: ==> ")
# date_founded=input("Enter Airline date_founded: ==> ")
# iata_code=input("Enter Airline iata_code: ==> ")
# airline_name=input("Enter Airline airline_name: ==> ")
# country_name=input("Enter Airline country_name: ==> ")
# status=input("Enter Airline status: ==> ")

# add = Airline(id,callsign,date_founded,iata_code,airline_name,country_name,status)
# add_airline(add)

# #getallairline
# allairlines=getallairline()
# print("All Airlines==> ",allairlines)

#update airline
# id=input("Enter Airline ID: ==> ")
# obj=getairline_namebyid(id)
# print("Airline ==> ",obj)
# callsign=input("Enter Airline callsign: ==> ")
# date_founded=input("Enter Airline date_founded: ==> ")
# iata_code=input("Enter Airline iata_code: ==> ")
# airline_name=input("Enter Airline airline_name: ==> ")
# country_name=input("Enter Airline country_name: ==> ")
# status=input("Enter Airline status: ==> ")
# aobj = Airline(id,callsign,date_founded,iata_code,airline_name,country_name,status)
# update_airline(aobj)

#delete airline
id=input("Enter Airline ID: ==> ")
delete_airline(id)


