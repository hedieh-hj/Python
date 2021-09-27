import math

def summ ():
    a=input("number one : ")
    b=input("number two : ")
    c=int (a) + int (b)
    print("sum = ", c)


def subb():
    a=input("number one : ")
    b=input("number two : ")
    c=int (a) - int (b)
    print("sub = ", c)

def mul():
    a=input("number one : ")
    b=input("number two : ")
    c=int (a) * int (b)
    print("multiplication = ", c) 

def div():
    a=input("number one : ")
    b=input("number two : ")
    c=int (a) / int (b)
    print("division = ", c) 


def radicall():
    a=input("number : ")
    c=int (a)**(1/2)
    print("radical = ", c) 

def sin():
    a=int(input("degree : "))
    math.radians=a/360 *2 *math.pi
    c=math.sin (math.radians)
    print("sinus = ", float(c))


def cos():
    a=int(input("degree : "))
    math.radians=a/360 *2 *math.pi
    c=math.cos (math.radians)
    print("cosine = ", float(c))  

def tan():
    a=int(input("degree : "))
    math.radians=a/360 *2 *math.pi
    c=math.tan (math.radians)
    print("tangent = ", float(c))

def cot():
    a=int(input("degree : "))
    math.radians=a/360 *2 *math.pi
    c=math.atan (math.radians)
    print("cotangent = ", float(c))

def fac():
    a=int(input("number : "))
    c=math.factorial(a)
    print("factorial = ", c)     

def menu ():
    print("\n*********** calculator ************")
    print("""
    1.sum
    2.sub
    3.multiplication
    4.division
    5.radical
    6.sinus
    7.cosine
    8.tangent
    9.cotangent
    10.factorial
    11.exit
    """)
i=1
while i>0:
        
            menu()
            text=input("what do you want to do insert number :")

            if int(text)==1:
                summ ()
        

            if int(text)==2:
                subb()
                

            if int(text)==3:
                mul()
                

            if int(text)==4:
                div()
                

            if int(text)==5:
                radicall()
                


            if int(text)==6:
                sin()
                

            if int(text)==7:
                cos()
                

            if int(text)==8:
                tan()
                

            if int(text)==9:
                cot()
                


            if int(text)==10:
                fac() 
                

            if int(text)==11:
                print("Good Bye")
                break

        








 