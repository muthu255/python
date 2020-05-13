from tkinter import *
import tkinter.messagebox as messagebox
root=Tk()

root.title('Main Window')

root.geometry('400x400')

chk1=IntVar()
chk2=IntVar()
chk3=IntVar()

def check():
    if chk1.get()==1:
        messagebox.showinfo('Hello', 'you have enterd for c')
    elif chk2.get()==1:
        messagebox.showinfo('Hello', 'you have enterd for Java')
    elif chk3.get()==1:
        messagebox.showinfo('Hello', 'you have enterd for Python')
    else:
        pass


        

chkbtn1=Checkbutton(root,text='C',variable=chk1,onvalue=1,offvalue=0)
chkbtn2=Checkbutton(root,text='Java',variable=chk2,onvalue=1,offvalue=0)
chkbtn3=Checkbutton(root,text='Python',variable=chk3,onvalue=1,offvalue=0)

chkbtn1.pack()
chkbtn2.pack()
chkbtn3.pack()

but=Button(root,text='click',command=check)
but.pack()
root.mainloop()
