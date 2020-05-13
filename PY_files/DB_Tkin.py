import cx_Oracle
import tkinter
import pandas as pd
from tkinter import filedialog
from tkinter import messagebox
from tkinter import *

root=tkinter.Tk()


root.title('DataBase')

e1=Entry(root,width=20,borderwidth=5,)
e1.grid(row=2,column=4,columnspan=3,padx=10,pady=10)

e2=Entry(root,width=20,borderwidth=5,show='*')
e2.grid(row=3,column=4,columnspan=5,padx=10,pady=10)

lb1=Label(root,text='USER NAME :').grid(row=2,column=3)
lb2=Label(root,text='PASSWORD :').grid(row=3,column=3)

def check():
    user_name=e1.get()
    Password=e2.get()
    #Select the Source query')
    file_path=filedialog.askopenfilename(initialdir='D:\Studies\Python\practice',title="#Select the Source query",filetypes=(('txt file','*.txt'),('all files','*.*')))
    #Select the Target query')
    file_path1=filedialog.askopenfilename(initialdir='D:\Studies\Python\practice',title="#Select the Target query",filetypes=(('SQL file','*.sql'),('all files','*.*')))

    #print(file_path)
    #print(file_path1)
    source=open(file_path).read()
    print("============SRC_QUERY============")
    print(source)
    target=open(file_path1).read()
    print("============TGT_QUERY============")
    print(target)
    con_string=user_name+'/'+Password+'@localhost/xe'
    print(con_string)
    con = cx_Oracle.connect(con_string)
    cur1 = con.cursor()
    cur2 = con.cursor()
    cur1.execute(str(source))
    cur2.execute(str(target))
    print("============SRC_QUERY============")
    for i in cur1:
        print(i)
    print("============SRC_QUERY============")
    for i in cur2:
        print(i)
    df1=pd.DataFrame(cur1)
    df2=pd.DataFrame(cur2)
    cur1.close()
    cur2.close()
    con.close()
but=Button(root,text='OK',command=check)
but.grid(row=4,column=5)

