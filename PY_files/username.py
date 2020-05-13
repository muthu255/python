import tkinter
from tkinter import filedialog
from tkinter import *

root=tkinter.Tk()
root.title('Enter your database crendtials')

e1=Entry(root,width=20,borderwidth=5,)
e1.grid(row=2,column=4,columnspan=3,padx=10,pady=10)

e2=Entry(root,width=20,borderwidth=5,show='*')
e2.grid(row=3,column=4,columnspan=5,padx=10,pady=10)

lb1=Label(root,text='USER NAME :').grid(row=2,column=3)
lb2=Label(root,text='PASSWORD :').grid(row=3,column=3)

def check():
    user_name=e1.get()
    Password=e2.get()
    print('USER NAME :',user_name)
    print('PASSWORD :',Password)


but=Button(root,text='OK',command=check)
but.grid(row=4,column=5)


