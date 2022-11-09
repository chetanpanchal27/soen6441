import sqlite3
from connectdatabase import connect,close

class Racemapper:
    def __init__(self):
        self.cursor,self.sqliteConnection=connect()

   
    def add(self,input):
        add=f'INSERT INTO race(raceId,year,round,circuitId,name,date,time) Values("{input.raceId}","{input.year}","{input.round}","{input.circuitId}","{input.name}","{input.date}","{input.time}")'
        self.cursor.execute(add)
        self.sqliteConnection.commit()
        print("Race Added(DB)")
        close()

    def update(self,input):
        update= f'UPDATE race SET raceId="{input.raceId}",year="{input.year}",round="{input.round}",name="{input.name}",date="{input.date}",time="{input.time}",circuitId="{input.circuitId}" WHERE raceId="{input.raceId}"'
        rows = self.cursor.execute(update)
        self.sqliteConnection.commit()
        print("Race Updated(DB)")
        close()

    def delete(self,input):
        delete=f'DELETE FROM race WHERE raceId="{input}"'
        d=self.cursor.execute(delete)
        print(d.arraysize)
        self.sqliteConnection.commit()
        print("Race Deleted(DB)")
        close()

    def getall(self):
        get_all = "SELECT * FROM race"
        rows = self.cursor.execute(get_all).fetchall()
        close()
        return rows
        

    def getracebyId(self,input):
        select=f'SELECT * FROM race WHERE raceId="{input}"'
        self.cursor.execute(select)
        totalRows = self.cursor.fetchone()
        close()
        return totalRows

    def getrace_driverid(self,input):
        list = f'SELECT DISTINCT race.name FROM race JOIN race_driver ON race.raceId = race_driver.raceId AND race_driver.driverId = "{input}"' 
        rows = self.cursor.execute(list).fetchall()
        print(rows)
        close()
        return rows