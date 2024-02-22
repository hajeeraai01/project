from tkinter import *
import mysql.connector

win=Tk()

win.title("MYSQL DB Demo")
win.geometry("300x300")

class manipulationwindow:
    def __init__(self):
        frametop=Frame(win,bg="black",width=800,height=300,padx=10,pady=10)
        frametop.pack(side=TOP)
        btninsert=Button(frametop,text="INSERT").pack(padx=10,pady=10)
        btnupdate=Button(frametop,text="UPDATE").pack(padx=10,pady=10)
        btndelete=Button(frametop,text="DELETE").pack(padx=10,pady=10)
        




run=manipulationwindow()
win.mainloop()