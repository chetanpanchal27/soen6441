import sqlite3
from connectdatabase import connect,close


        
def getairline_namebyid(input):
    cursor,sqliteConnection=connect()    
    select = 'SELECT * FROM airline where airline_id=='+input
    rows = cursor.execute(select).fetchall()
    return rows

def add_airline(input):
    pass
def getallairline():
    pass
def update_airline(input):
    pass
def delete_airline(input):
    pass


   
    