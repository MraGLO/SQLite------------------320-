import sqlite3 as sql3
 
from sqlite3 import Error
 
def sql_connection(): # функция подключение к бд 
 
    try:
        con = sql3.connect('mydatabase.db')
        return con
 
    except Error:
        print(Error)
 
def sql_table(con): # Создание таблицы
    cursorObj = con.cursor()
    cursorObj.execute("CREATE TABLE  employees(id integer PRIMARY KEY, name text, salary real, department text, position text, hireDate text)")
    con.commit()


def sql_insert(con, entities): # вставка информации в таблицу
    cursorObj = con.cursor()
    cursorObj.execute('INSERT INTO employees(id, name, salary, department, position, hireDate) VALUES(?, ?, ?, ?, ?, ?)', entities)
    con.commit()


def sql_update(con): # обновление информации
    cursorObj = con.cursor()
    cursorObj.execute('UPDATE employees SET name = "Rogers" where id = 2')
    con.commit()

def sql_fetch(con): # получение информации из бд
    cursorObj = con.cursor()
    cursorObj.execute('SELECT * FROM employees')
    rows = cursorObj.fetchall()
    for row in rows:
        print(row)
    print(len(row)) # вывод количества строк

def sql_fetch_Where(con): # получение информации из бд с where
    cursorObj = con.cursor()
    cursorObj.execute('SELECT id, name FROM employees WHERE salary > 800.0')
    rows = cursorObj.fetchall()
    for row in rows:
        print(row)

def sql_fetch_Table(con): # вывод таблиц
    cursorObj = con.cursor()
    cursorObj.execute('SELECT name from sqlite_master where type= "table"')
    print(cursorObj.fetchall())


def sql_fetch_delete(con):
    cursorObj = con.cursor()
    cursorObj.execute('DROP table if exists employees')
    con.commit()


 
entities = (2, 'Andrew', 800, 'IT', 'Tech', '2018-02-06')
con = sql_connection()

sql_table(con)
sql_insert(con, entities)
sql_fetch(con)
sql_update(con)
sql_fetch(con)
sql_fetch_Where(con)
sql_fetch_Table(con)
sql_fetch_delete(con)


con.close()
