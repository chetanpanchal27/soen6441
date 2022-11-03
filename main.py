from mapper import getairline_namebyid,add_airline,getallairline,update_airline,delete_airline
from airline import Airline


##get airline by id
id=input("Enter Airline ID: ==> ")
print(getairline_namebyid(id))

