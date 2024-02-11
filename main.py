import pyfiglet
text=pyfiglet.figlet_format("CALCULATOR")
print(text)
def add(a,b):
    c=a+b
    return c

def substract(a,b):
    sub=a-b
    return sub

def multiply(a,b):
    multi=a*b
    return multi

def divide(a,b):
    divide=a/b
    return divide

print("SELECT THE OPTION")
print("1. add")
print("2.substract")
print("3.multiply")
print("4.divide")

i=input("enter the the options :")

a=eval(input("enter the first number:"))
b=eval(input("enter the second number :"))

if i=="1":
    print(a,"+",b,"\n","result=",add(a,b))
elif i=="2":
    print(a,"-",b,"\n","result=",substract(a,b))
elif i=="3":
    print(a,"*",b,"\n","result=",multiply(a,b))
elif i=="4":
    print(a,"/",b,"\n","result=",divide(a,b))
else :
    print("invalid output")

def intro():
    print("\n\n\n\n")
    print("*********************************************************************")
    print("-----------------------------DEVELOPED-------------------------------")
    print("---------------------------------BY----------------------------------")
    print("-----------------------------AMAR YADAV------------------------------")
    print("--------------------------------2024---------------------------------")
    print("***********************************************************************")


intro()

