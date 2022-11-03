import sqlite3,csv

def readSqliteTable():
    try:
        sqliteConnection = sqlite3.connect('app_soen.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

       # sqlite_select_query = """SELECT * from airline"""
        #cursor.execute(sqlite_select_query)
        
        file = open('E:\@Concordia\APP\support\Airlines.csv')
        contents = csv.reader(file)
        insert_records = "INSERT INTO airline (airline_id,callsign,date_founded,iata_code,airline_name,country_name,status) VALUES(?, ?,?, ?,?, ?,?)"
 
        cursor.executemany(insert_records, contents)
        select_all = "SELECT * FROM airline"
        rows = cursor.execute(select_all).fetchall()
 
# Output to the console screen
        for r in rows:

            print("dd",r)
        
        
        records = cursor.fetchall()

        # print("Total rows are:  ", len(records))
        # print("Printing each row")
        # for row in records:
        #     print("h")
        #     print("Name: ", row[0])
           
        #     print("\n")

        # cursor.close()

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")

readSqliteTable()
