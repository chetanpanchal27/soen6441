import sqlite3
from connectdatabase import connect,close

class Drivermapper:
    def _init_(self):
        self.cursor,self.sqliteConnection=connect()
    
    def add(self,input):
        add = f'INSERT INTO driver(driverId,driverRef,code, forename, surname,dob,nationality) Values("{input.driverId}","{input.driverRef}","{input.code}","{input.forename}","{input.surname}","{input.dob}","{input.nationality}")' 
        self.cursor.execute(add)
        self.sqliteConnection.commit()
        print("Added") 

    def update(self,input):
        getdata=self.getdriverbyId(input.driverId)
        update=f'UPDATE driver SET driverId="{input.driverId}",driverRef="{input.driverRef}",code="{input.code}",forename="{input.forename}",surname="{input.surname}",dob="{input.dob}",nationality="{input.nationality}" WHERE driverId="{input.driverId}"'
        rows = self.cursor.execute(update)
        self.sqliteConnection.commit()
        print("Updated")

    def delete(self,input):
        delete = f'DELETE FROM driver WHERE driverId="{input}"'
        rows = self.cursor.execute(delete)
        self.sqliteConnection.commit()
        print("Deleted from mapper")

    def getall(self):
        get_all = "SELECT * FROM driver"
        rows = self.cursor.execute(get_all).fetchall()
        return rows

    def getdriverbyId(self,input):
        select=f'SELECT * FROM driver WHERE driverId="{input}"'
        self.cursor.execute(select)
        totalRows = self.cursor.fetchone()
        return totalRows

    def getdrivers_raceid(self,input):
        list = f'SELECT DISTINCT driver.forename, driver.surname FROM driver JOIN race_driver ON driver.driverId = race_driver.driverId AND race_driver.raceId = "{input}"' 
        rows = self.cursor.execute(list).fetchall()
        return rows