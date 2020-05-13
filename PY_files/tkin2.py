from tkinter import *
import tkinter.messagebox as messagebox

root=Tk()

root.title('Main Window')

#root.geometry('400x400')

def check():
    ans=entry.get()
    entry.delete(0,END)
    messagebox.showinfo('Hello',ans)
lbl=Label(root,text='Enter your name')
lbl.pack(side=LEFT)
entry=Entry(root,show='#')#password encrpt
entry.pack(side=LEFT)

but=Button(root,text='click',command=check)
but.pack(side=BOTTOM)
