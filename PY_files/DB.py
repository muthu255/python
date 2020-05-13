
import cx_Oracle
import tkinter
import pandas as pd
from tkinter import filedialog
from tkinter import messagebox

root=tkinter.Tk()
root.withdraw()
messagebox.showinfo('SOURCE','#Select the Source query')
file_path=filedialog.askopenfilename()
messagebox.showinfo('TARGET','#Select the Target query')
file_path1=filedialog.askopenfilename()





#print(file_path)
#print(file_path1)
source=open(file_path).read()
print("============SRC_QUERY============")
print(source)
target=open(file_path1).read()
print("============TGT_QUERY============")
print(target)

con = cx_Oracle.connect('SYSTEM/muthu255@localhost/xe')
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






