import math

def equation(a,b,c):

    dd = float ((b*b) - (4 * a * c))

    if  (dd) == 0 :
        x = ((-1)*b) / (2 * a)
        print("root :" , x )

    if (dd) > 0 :
        x = ((-b) + ((dd)**(1/2))) / (2 * a)
        y = ((-b) - ((dd)**(1/2))) / (2 * a)
        print("first root : ", x , "    second root : ", y )
 
    if (dd) < 0 :
        print(" equation don't have any root ")



x=1
i=1
while x>0:
    
    if i==1:
        print(" format : ax^2 + bx + c   ")
        a=int(input("insert a : "))
        b=int(input("insert b : "))
        c=int(input("insert c : "))
        equation (a,b,c)
        i=int(input("if you want start it , please insert 1 : "))

    else :
        print("Good Bye !")
        break







