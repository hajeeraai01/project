from tkinter import *
import mysql.connector

win=Tk()

win.title("Insert into mysql db demo")
win.geometry("300x300")
class frameDBoperations:
    def __init__(self):
        frametop=Frame(win, bg="black",width=800, height=300, padx=10,pady=10)
        frametop.pack(side = TOP)
        btninsert=Button(frametop,text="INSERT", command=self.frameLeft).pack(padx=10, pady=10)
        btnupdate=Button(frametop,text="UPDATE", command=self.rightFrame).pack(padx=10, pady=10)
        btndelete=Button(frametop,text="DELETE").pack(padx=10, pady=10)

    def frameLeft(self):

        frameleft=Frame(win, bg="red",width=500, height=500, padx=30,pady=30)
        frameleft.pack(side = LEFT)


        lbl_Title_of_operation=Label(frameleft,text="Name")
        lbl_Title_of_operation.grid(row=0,columnspan=5)


        lblname=Label(frameleft,text="Name")
        lblname.grid(row=2,column=1,padx=30,pady=10)

    
        lblname=Label(frameleft,text="Hajeera")
        lblname.grid(row=3,column=1,padx=30,pady=10)

    def rightFrame(self):
        neww=Tk()
        neww.title("update into mysql db demo")
        neww.geometry("500x500")
        frameright=Frame(neww, bg="red",width=500,height=500,padx=30,pady=30 )
        frameright.pack(side=RIGHT)

        lbl_Title_of_Operation1=Label(frameright, text="Insert into MySQL DB Demo")
        lbl_Title_of_Operation1.grid(row=0,columnspan=5)

        lblName1=Label(frameright,text="Name")
        lblName1.grid(row=2,column=1,padx=30,pady=10)
        lblHajeera1=Label(frameright,text="Hajeera")
        lblHajeera1.grid(row=3,column=1,padx=30,pady=10)

        neww.mainloop()

run=frameDBoperations()
# run.rightFrame()
win.mainloop()  
        

