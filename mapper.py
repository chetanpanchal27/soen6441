import sqlite3
from connectdatabase import connect,close
from driver import Driver

#driver table
def adddriver(input):
    cursor,sqliteConnection=connect()
    add = f'INSERT INTO driver(driverId,driverRef,code, forename, surname,dob,nationality) Values("{input.driverId}","{input.driverRef}","{input.code}","{input.forename}","{input.surname}","{input.dob}","{input.nationality}")' 
    cursor.execute(add)
    sqliteConnection.commit()
    print("Added") 
    
def getdrivers():
    cursor,sqliteConnection=connect()    
    get_all = "SELECT * FROM driver"
    rows = cursor.execute(get_all).fetchall()
    return rows

def deletedriver(input):
    cursor,sqliteConnection=connect()    
    delete = f'DELETE FROM driver WHERE driverId="{input}"'
    rows = cursor.execute(delete)
    sqliteConnection.commit()
    print("Deleted")

def updatedriver(input):
    cursor,sqliteConnection=connect()    
    update=f'UPDATE driver SET driverId="{input.driverId}",driverRef="{input.driverRef}",code="{input.code}",forename="{input.forename}",surname="{input.surname}",dob="{input.dob}",nationality="{input.nationality}" WHERE driverId="{input.driverId}"'
    rows = cursor.execute(update)
    sqliteConnection.commit()
    print("Updated")

def getdriverbyId(input):
    cursor,sqliteConnection=connect()
    select=f'SELECT * FROM driver WHERE driverId="{input}"'
    cursor.execute(select)
    totalRows = cursor.fetchone()
    #rows = cursor.execute(select).fetchall()
    return totalRows

#season table
def allseasonsbyyear(input):
    cursor,sqliteConnection=connect()
    select=f'SELECT * FROM season WHERE year="{input}"'
    rows = cursor.execute(select).fetchall()
    return rows

def addseason(input):
    cursor,sqliteConnection=connect()
    add = f'INSERT INTO season(year,url) Values("{input.year}","{input.url}")'
    cursor.execute(add)
    sqliteConnection.commit()
    print("Added")

def getseasons():
    cursor,sqliteConnection=connect()
    get_all = "SELECT * FROM season"
    rows = cursor.execute(get_all).fetchall()
    return rows

def deleteseason(input):
    cursor,sqliteConnection=connect()
    delete = f'DELETE FROM season WHERE year="{input}"'
    rows = cursor.execute(delete)
    sqliteConnection.commit()
    print("Deleted")

def updateseason(input):
    cursor,sqliteConnection=connect()
    update= f'UPDATE season SET year="{input.year}",url="{input.url}" WHERE year="{input.year}"'
    print(update)
    rows = cursor.execute(update)
    sqliteConnection.commit()
    print("Updated")

def addrace(input):
    cursor,sqliteConnection=connect()
    add=f'INSERT INTO race(raceId,year,round,circuitId,name,date,time) Values("{input.raceId}","{input.year}","{input.round}","{input.circuitId}","{input.name}","{input.date}","{input.time}")'
    cursor.execute(add)
    sqliteConnection.commit()
    print("Added")

def getraces():
    cursor,sqliteConnection=connect()
    get_all = "SELECT * FROM race"
    rows = cursor.execute(get_all).fetchall()
    return rows

def deleterace(input):
    cursor,sqliteConnection=connect()
    delete=f'DELETE FROM race WHERE raceId="{input}"'
    rows = cursor.execute(delete)
    sqliteConnection.commit()
    print("Deleted")

def updaterace(input):
    cursor,sqliteConnection=connect()
    update= f'UPDATE race SET raceId="{input.raceId}",year="{input.year}",round="{input.round}",circuitId="{input.circuitId}",name="{input.name}",date="{input.date}",time="{input.time}" WHERE raceId="{input.raceId}"'
    print(update)
    rows = cursor.execute(update)
    sqliteConnection.commit()
    print("Updated")

    

def getdrivers_raceid(input):
    cursor,sqliteConnection=connect()
   # list=f'SELECT * FROM driver WHERE driverId=(SELECT driverId FROM race_driver WHERE raceId="{input}")'
    list = f'SELECT DISTINCT driver.forename, driver.surname FROM driver JOIN race_driver ON driver.driverId = race_driver.driverId AND race_driver.raceId = "{input}"' 
    #print(list)
    rows = cursor.execute(list).fetchall()
    #print(rows)
    return rows

def getrace_driverid(input):
    cursor,sqliteConnection=connect()
    list = f'SELECT DISTINCT race.name FROM race JOIN race_driver ON race.raceId = race_driver.raceId AND race_driver.driverId = "{input}"' 
    rows = cursor.execute(list).fetchall()
    print(rows)
    return rows
def getraces_season(input):
    cursor,sqliteConnection=connect()
    list =f'SELECT race.name FROM race JOIN season ON race.year = season.year AND season.year = "{input}"'
    rows = cursor.execute(list).fetchall()
    return rows


        





   
