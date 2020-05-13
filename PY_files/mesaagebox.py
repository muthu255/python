import tkinter
from tkinter import messagebox

messagebox.showinfo("usernmae","Informative message")
messagebox.showerror("Error", "Error message")
messagebox.showwarning("Warning","Warning message")

answer = messagebox.askokcancelok("Question","Do you want to open this file?")
answer = messagebox.askretrycancel("Question", "Do you want to try that again?")
answer = messagebox.askyesno("Question","Do you like Python?")
answer = messagebox.askyesnocancel("Question", "Continue playing?")
