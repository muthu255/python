import cx_Oracle
import pandas as pd

import tkinter
from tkinter import filedialog
from tkinter import messagebox
from tkinter import *

import json

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
    file_path=filedialog.askopenfilename(initialdir='D:\Studies\SQL_files',title="#Select the Source query",filetypes=(('txt file','*.txt'),('all files','*.*')))
    source=open(file_path).read()
    
    con_string=user_name+'/'+Password+'@localhost/xe'
    con = cx_Oracle.connect(con_string)
    df = pd.read_sql_query(source, con)
    df1=pd.DataFrame(df)
     
    #cur1 = con.cursor()
    
    #cur1.execute(str(source))
    #df1=pd.DataFrame(cur1)
    print(df1)
    #cur1.close()
    con.close()


    #Select the Json file:
    file_path1=filedialog.askopenfilename(initialdir='D:\Studies\SQL_files',title="#Select the Json file",filetypes=(('json file','*.json'),('all files','*.*')))
    with open(file_path1) as f:
        J_data = json.load(f)
    df2=pd.DataFrame(J_data)
    df4=df2.astype(str)
    
    #S-T file:
    df3 = pd.concat([df1, df4]).drop_duplicates(keep=False)
    
    df5=df1.eq(df4,axis='1',level=None)

    
    datatoexcel=pd.ExcelWriter('D:/Studies/SQL_files/emp1.xlsx')
    
    df1.to_excel(datatoexcel,sheet_name='DB_Results',index=False)
    df4.to_excel(datatoexcel,sheet_name='JSON_Results',index=False)

    df3.to_excel(datatoexcel,sheet_name='S-T',index=False)
    #df3.to_excel(datatoexcel,sheet_name='T-S',index=False)
    df5.to_excel(datatoexcel,sheet_name='Comparison',index=False)
    
    print(df3)
    print(df4.dtypes)
    print(df1.dtypes)
    datatoexcel.save()
    print("..............SUCCESS.........")
but=Button(root,text='OK',command=check)
but.grid(row=4,column=5)

