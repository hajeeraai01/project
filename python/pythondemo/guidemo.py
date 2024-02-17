from tkinter import*
app= Tk()
app.title("my first python gui app")
app.geometry("500x200+500+100")
app.config(bg="lavender")
#app.state("zoomed")

def addition():
    a=int(inputbox1.get())
    b=int(inputbox2.get())
    c=a+b
    #print(c)
    labeloutput.config(text=c)

def subtraction():
    a=int(inputbox1.get())
    b=int(inputbox2.get())
    c=a-b
    #print(c)
    labeloutput.config(text=c)


def multiplication():
    a=int(inputbox1.get())
    b=int(inputbox2.get())
    c=a*b
    #print(c)
    labeloutput.config(text=c)

def divition():
    a=int(inputbox1.get())
    b=int(inputbox2.get())
    c=a/b
    #print(c)
    labeloutput.config(text=c)
    

def modlus():
    a=int(inputbox1.get())
    b=int(inputbox2.get())
    c=a%b
    #print(c)
    labeloutput.config(text=c)

def power():
    a=int(inputbox1.get())
    b=int(inputbox2.get())
    c=a**b
    #print(c)
    labeloutput.config(text=c)

def floordivition():
    a=int(inputbox1.get())
    b=int(inputbox2.get())
    c=a//b
    #print(c)
    labeloutput.config(text=c)


def assign():
    a=int(inputbox1.get())
    
    c=a=2
    
    labeloutput.config(text=c)




lblTitle=Label(app,text="Arithmatic opertion",bg="purple")
lblTitle.grid(row=0,column=1,padx=40,pady=40)

inputbox1=Entry(app,width=30)
inputbox1.grid(row=0,column=2)

lblTitle1=Label(app,text="Arithmatic opertion",bg="purple")
lblTitle1.grid(row=1,column=1,padx=40,pady=40)

inputbox2=Entry(app,width=30)
inputbox2.grid(row=1,column=2)


clickme=Button(app, text="+",bg="yellow",command=addition)
clickme.grid(row=2,column=1,padx=10,pady=10)

clickme=Button(app, text="-",bg="yellow",command=subtraction)
clickme.grid(row=2,column=2,padx=10,pady=10)
             
clickme=Button(app, text="*",bg="yellow",command=multiplication)
clickme.grid(row=2,column=3,padx=10,pady=10)
             
clickme=Button(app, text="/",bg="yellow",command=divition)
clickme.grid(row=2,column=4,padx=10,pady=10)            

clickme=Button(app, text="%",bg="yellow",command=modlus)
clickme.grid(row=2,column=5,padx=10,pady=10)            


clickme=Button(app, text="**",bg="yellow",command=power)
clickme.grid(row=2,column=6,padx=10,pady=10)            


clickme=Button(app, text="//",bg="yellow",command=floordivition)
clickme.grid(row=2,column=7,padx=10,pady=10) 


#clickme=Button(app, text="//",bg="yellow",command=floordivition)
#clickme.grid(row=2,column=7,padx=10,pady=10) 


#clickme=Button(app, text="+=",bg="yellow",command=plusequal)
#clickme.grid(row=2,column=8,padx=10,pady=10)            

#clickme=Button(app, text="-=",bg="yellow",command=minusequal)
#clickme.grid(row=2,column=9,padx=10,pady=10)            

#clickme=Button(app, text="*=",bg="yellow",command=multiplequal)
#clickme.grid(row=2,column=10,padx=10,pady=10)            

#clickme=Button(app, text="/=",bg="yellow",command=divitionequal)
#clickme.grid(row=3,column=1,padx=10,pady=10)            

#clickme=Button(app, text="%=",bg="yellow",command=modlusequal)
#clickme.grid(row=3,column=2,padx=10,pady=10)            

#clickme=Button(app, text="//=",bg="yellow",command=floorequal)
#clickme.grid(row=3,column=3,padx=10,pady=10)            

#clickme=Button(app, text="**=",bg="yellow",command=multiplemultipleequal)
#clickme.grid(row=3,column=4,padx=10,pady=10)        

#clickme=Button(app, text="&=",bg="yellow",command=andequal)
#clickme.grid(row=3,column=5,padx=10,pady=10)        


#clickme=Button(app, text="|=",bg="yellow",command=notequal)
#clickme.grid(row=2,column=13,padx=10,pady=10)        

#clickme=Button(app, text="^=",bg="yellow",command=powerequal)
#clickme.grid(row=2,column=13,padx=10,pady=10)        


#clickme=Button(app, text=">>=",bg="yellow",command=greaterequal)
#clickme.grid(row=2,column=13,padx=10,pady=10)        

#clickme=Button(app, text="<<=",bg="yellow",command=lessequal)
#clickme.grid(row=2,column=13,padx=10,pady=10)        

labeloutput=Label(app,text="result",bg="purple")
labeloutput.grid(row=5,column=1,padx=40,pady=40)
             
labeloutput=Label(app,text="",bg="green",width=40)
labeloutput.grid(row=5,column=2)

app.mainloop()