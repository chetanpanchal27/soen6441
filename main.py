# from mapper import getrace_driverid,getdriverbyId,getdrivers_raceid,getdrivers_racename
from MySQLdb import Date
from race import Race
from season import Season
from mapper import addrace, addseason, deleterace, deleteseason, getrace_driverid,adddriver,deletedriver, getseasons,updatedriver,getdriverbyId,getraces_season, updaterace, updateseason
from driver import Driver
##get driver by id
#id=input("Driver ID: ==> ")
# print(getdriverbyId(id))

# drivers=getdrivers_raceid(1)
# print(drivers)
#drivers=getdrivers_racename("Australian Grand Prix")
#print(drivers)
# drivers=getdrivers_raceid(input("Enter Race ID: "))
# print(drivers)

# race=getrace_driverid(2)
#print(race)

#driver added
# id=input("ENter Driver Id: ")
# dref=input("Enter driver reference: ")
# code=input("Enter code: ")
# fname=input("Enter forename: ")
# sname=input("Enter surname: ")
# dob=input("Enter dob: ")
# nat=input("Enter nationality: ")
# d=Driver(id,dref,code,fname,sname,dob,nat)
# adddriver(d)

#remove driver
# id=input("Enter Driver Id: ")
# deletedriver(id)

#update driver
# id=input("ENter Driver Id: ")
# dref=input("Enter driver reference: ")
# code=input("Enter code: ")
# fname=input("Enter forename: ")
# sname=input("Enter surname: ")
# dob=input("Enter dob: ")
# nat=input("Enter Nationality: ")
# d=Driver(id,dref,code,fname,sname,dob,nat)
# updatedriver(d)

#get driver by id
# id=input("Driver ID: ==> ")
# print(getdriverbyId(id))

