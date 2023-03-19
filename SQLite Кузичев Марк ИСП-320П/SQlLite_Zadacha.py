import sqlite3
from sqlite3 import Error

def sql_connection():
    try:
        con = sqlite3.connect('Vologda.db')
        return con
 
    except Error:
        print(Error)

def sql_tabel_town(con):
    cursorObj = con.cursor()
    cursorObj.execute("CREATE TABLE if not exists street(id integer PRIMARY KEY, name_street text)")
    con.commit()

def sql_insert_street(con, data):
    cursorObj = con.cursor()
    cursorObj.executemany('INSERT INTO street(id, name_street) VALUES(?, ?)', data)
    con.commit()


data = [(1, "Некрасова"),(2, "Гоголя"),(3, "Горького"),(4, "Северная"),(5, "Мальцева")]

con = sql_connection()

sql_tabel_town(con)
sql_insert_street(con, data)

con.close()