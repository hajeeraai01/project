from tkinter import*
import mysql.connector
app= Tk()
app.title("my second python gui")
app.geometry("500x200+500+100")
app.config(bg="yellow")
#app.state("zoomed")

def MyDBConnection():
    dbcon=mysql.connector.connect(
    host="192.168.1.240",
    user="AIBATCH01",
    password="AI@123",
    database="ai_hajeera"
    )

    return dbcon
     #print(dbcon)

def Insert():
    Name=(inputbox.get())
    English=(inputbox1.get())
    Tamil=(inputbox2.get())
    Maths=(inputbox3.get())
    Science=(inputbox4.get())
    Social=(inputbox5.get())

    e_con= MyDBConnection()
    result=e_con.cursor()
    statement="insert into studentmark(Name,English,Tamil,Maths,Science,Social)values(%s,%s,%s,%s,%s,%s);"
    valuepass=(Name,English,Tamil,Maths,Science,Social)
    result.execute(statement,valuepass)
    e_con.commit()
    print(result.rowcount, " row inserted")

def Update():
    Name=(inputbox.get())
    #English=(inputbox1.get())
    Tamil=(inputbox2.get())
    #Maths=(inputbox3.get())
    #Science=(inputbox4.get())
    #Social=(inputbox5.get())
    #Sno=(inputbox7.get())
    e_con= MyDBConnection()
    result=e_con.cursor()
    statement="Update studentmark set Tamil=(%s) where Name=(%s);"
    valuepass=(Tamil,Name)
    result.execute(statement,valuepass)
    e_con.commit()
    print(result.rowcount, " row updated")


def Delete():
    Name=(inputbox.get())
    #English=(inputbox1.get())
    
    
    #Tamil=(inputbox2.get())
    #Maths=(inputbox3.get())
    #Science=(inputbox4.get())
    #Social=(inputbox5.get())
    #Sno=(inputbox7.get())
    e_con= MyDBConnection()
    result=e_con.cursor()
    statement="Delete from studentmark  where Name=(%s);"
    valuepass=(Name,)
    result.execute(statement,valuepass)
    e_con.commit()
    print(result.rowcount, " row deleted")


lblTitle6=Label(app,text="studentmarklist",bg="orange")
lblTitle6.grid(row=0, column=4,padx=40,pady=40)

lblTitle=Label(app,text="Name",bg="green")
lblTitle.grid(row=0,column=1,padx=40,pady=40)

inputbox=Entry(app,width=30)
inputbox.grid(row=0,column=2)


lblTitle1=Label(app,text="English",bg="green")
lblTitle1.grid(row=1,column=1,padx=40,pady=40)

inputbox1=Entry(app,width=30)
inputbox1.grid(row=1,column=2)


lblTitle2=Label(app,text="Tamil",bg="green")
lblTitle2.grid(row=2,column=1,padx=40,pady=40)

inputbox2=Entry(app,width=30)
inputbox2.grid(row=2,column=2)

lblTitle3=Label(app,text="Maths",bg="green")
lblTitle3.grid(row=3,column=1,padx=40,pady=40)

inputbox3=Entry(app,width=30)
inputbox3.grid(row=3,column=2)

lblTitle4=Label(app,text="Science",bg="green")
lblTitle4.grid(row=4,column=1,padx=40,pady=40)

inputbox4=Entry(app,width=30)
inputbox4.grid(row=4,column=2)

lblTitle5=Label(app,text="Social",bg="green")
lblTitle5.grid(row=5,column=1,padx=40,pady=40)

inputbox5=Entry(app,width=30)
inputbox5.grid(row=5,column=2)

lblTitle7=Label(app,text="Sno",bg="purple",fg="white")
lblTitle7.grid(row=7,column=1,padx=40,pady=40)

inputbox7=Entry(app,width=30)
inputbox7.grid(row=7,column=2,padx=40,pady=40)

clickme=Button(app, text="Insert",bg="pink",command=Insert)
clickme.grid(row=0,column=3,padx=10,pady=10)


clickme=Button(app, text="Update",bg="pink",command=Update)
clickme.grid(row=1,column=3,padx=10,pady=10)

clickme=Button(app, text="Delete",bg="pink",command=Delete)
clickme.grid(row=2,column=3,padx=10,pady=10)

clickme=Button(app, text="Reset",bg="pink")
clickme.grid(row=3,column=3,padx=10,pady=10)




app.mainloop()