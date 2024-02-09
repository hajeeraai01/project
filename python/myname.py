"""
def myname():
    print("this is azar")
    print("hello")
    name="azar1"
    lname="hs"
    if name=="azar":
        print("your name is azar")
        print("hello")
    print("skippedd the name is mismatch")
    for x in name:
        print(x)
    myname()
    """

def myname1():
    print("i am azar")
    myname1()
    myname1()
    myname1()


def myname2():
    name="azar"
    lname="hs"
    year=2024
    print("hi..!",name)
    print("hi..!",name,lname)
    print("hi..!",name,lname, "welcome to year of",year)

    print("-------------")
    print("printing value using concatenation")
    print("hi..!"+ name)
    print("hi..!"+ name+" "+lname)
    print("hi..!"+ name+" "+lname + "welcome to year of" + str(year))



    myname2("azar","hs",2024)
    name="suriya"
    lname="karthik"
    year=2024
    myname2(name,lname,year)
    
