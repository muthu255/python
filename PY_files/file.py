import cx_Oracle
import tkinter
from tkinter import filedialog

root=tkinter.Tk()


root.withdraw()

file_path=filedialog.askopenfilename()

print(file_path)

con = cx_Oracle.connect('SYSTEM/muthu255@localhost/xe')
cur = con.cursor()
cur1=con.cursor()
res=cur.execute(open('D:/Studies/Python/practice/SQL_Dept.txt','r'))

for i in res:
    print(i)


