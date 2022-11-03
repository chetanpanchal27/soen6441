import sqlite3
from connectdatabase import connect,close


        
def getairline_namebyid(input):
    cursor,sqliteConnection=connect()    
    select = 'SELECT * FROM airline where airline_id=='+input
    rows = cursor.execute(select).fetchall()
    return rows

def add_airline(input):
    cursor,sqliteConnection=connect()    
    add = f'INSERT INTO airline(airline_id,callsign,date_founded,iata_code,airline_name,country_name,status) VALUES("{input.airline_id}","{input.callsign}","{input.date_founded}","{input.iata_code}","{input.airline_name}","{input.country_name}","{input.status}")'
    rows = cursor.execute(add)
    sqliteConnection.commit()
    print("Added")

def getallairline():
    cursor,sqliteConnection=connect()    
    get_all = 'SELECT * FROM airline'
    rows = cursor.execute(get_all).fetchall()
    return rows

def update_airline(input):
    cursor,sqliteConnection=connect()    
    update = f'UPDATE airline SET callsign="{input.callsign}",date_founded="{input.date_founded}",iata_code="{input.iata_code}",airline_name="{input.airline_name}",country_name="{input.country_name}",status="{input.status}" WHERE airline_id="{input.airline_id}"'
    rows = cursor.execute(update)
    sqliteConnection.commit()
    print("Updated")

def delete_airline(input):
    cursor,sqliteConnection=connect()    
    delete = 'DELETE FROM airline WHERE airline_id="'+input+'"'
    rows = cursor.execute(delete)
    sqliteConnection.commit()
    print("Deleted")



   
    