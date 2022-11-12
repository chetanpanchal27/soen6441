import sqlite3

def connect():
    try:
        sqliteConnection = sqlite3.connect('demo.db',check_same_thread=False)
        cursor = sqliteConnection.cursor()
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")
        return cursor,sqliteConnection   
    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
def close():
    try:
        sqliteConnection = sqlite3.connect('demo.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")
        return cursor   
    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
    if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")