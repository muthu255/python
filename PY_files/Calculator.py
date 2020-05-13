from tkinter import *


root=Tk()
root.title('Calulator')
e=Entry(root,width=30,borderwidth=5)
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10) 


def click(num):
    current=e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(num))
    return
def clear():
    e.delete(0,END)
    return
result=0
def add():
    first_arg=e.get()
    global f_num
    f_num=int(first_arg)
    e.delete(0,END)
    
    return
def equal():
    second_arg=e.get()
    e.delete(0,END)
    e.insert(0,f_num+int(second_arg))

b1=Button(root,text='1',padx=40,pady=20,command=lambda : click('1'))
b2=Button(root,text='2',padx=40,pady=20,command=lambda : click('2'))
b3=Button(root,text='3',padx=40,pady=20,command=lambda : click('3'))

b4=Button(root,text='4',padx=40,pady=20,command=lambda : click('4'))
b5=Button(root,text='5',padx=40,pady=20,command=lambda : click('5'))
b6=Button(root,text='6',padx=40,pady=20,command=lambda : click('6'))

b7=Button(root,text='7',padx=40,pady=20,command=lambda : click('7'))
b8=Button(root,text='8',padx=40,pady=20,command=lambda : click('8'))
b9=Button(root,text='9',padx=40,pady=20,command=lambda : click('9'))

b0=Button(root,text='0',padx=40,pady=20,command=lambda : click('0'))

bplus=Button(root,text='+',padx=40,pady=20,command=add)
bequal=Button(root,text='=',padx=90,pady=20,command=equal)
bclear=Button(root,text='clear',padx=90,pady=20,command=clear)

b7.grid(row=1, column=0)
b8.grid(row=1, column=1)
b9.grid(row=1, column=2)

b4.grid(row=2, column=0)
b5.grid(row=2, column=1)
b6.grid(row=2, column=2)

b1.grid(row=3, column=0)
b2.grid(row=3, column=1)
b3.grid(row=3, column=2)

b0.grid(row=4, column=0)

bclear.grid(row=4,column=1,columnspan=2)
bplus.grid(row=5,column=0)
bequal.grid(row=5,column=1,columnspan=2)

root.mainloop()
