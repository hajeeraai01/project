"""
def myfunction():
    a=1+2+1+2
    print(a)
    if a==3:
        print("A is 3")
        x="hajeera is a good girl"
        for x1 in x:
            print(x1)
        x=x.split(" ")    
        for x2 in x:
            print(x2)
    elif a==6:
        print("A is greater then")        
    y=input("enter the value").split()
    print(y) 
           
myfunction()
"""
x1=("humera","shabeen","irfana","rameez","amthul")
print(x1)
print(type(x1))
for value in x1:
        print(value)
        if value=="irfana":
           continue
        print(value)     

x1="humera shabeen irfana rameez amthul"
print(x1)
print(type(x1))
x1=x1.split(" ")
print(x1)
print(type(x1))


x1[0]="jothika" 
print(x1) 


x1="humera shabeen irfana rameez amthul"
x1=x1.replace("humera","humera az")
print(x1)



      


