
while True:
    i=int(input("for check please insert number  1  :"))
    if i==1:
        size=input("enter size of any side of triangle (format: a,b,c): ")

        a,b,c=size.split(",")

        if int(a) + int(b) > int(c) :
            if int(a) + int(c) > int(b):
                if int(c) +int(b) > int(a):
                    print("it can be a triangle!")
                else:
                    print("it can't be a triangle!") 
            else:
                print("it can't be a triangle!")         

        else :
            print("it can't be a triangle!")

    if i !=1:
        break        