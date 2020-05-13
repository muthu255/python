import sqlite3
from sqlite3 import OperationalError
import cx_Oracle



con = cx_Oracle.connect('SYSTEM/muthu255@localhost/xe')
c = con.cursor()

fd = open('D:\Studies\Python\dept.txt', 'r')
sqlFile = fd.read()
fd.close()

# all SQL commands (split on ';')
sqlCommands = sqlFile.split(';')
print(sqlCommands)

for commands in sqlCommands:
    df=c.execute(commands)
    print(df)
    

