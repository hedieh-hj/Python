from os import read
from os import write
import pyfiglet

def read():
    if x==1:

        ff = open('translate.txt', 'r')
        num = ff.read().split('\n')
        a=len(num)

        for i in range(a):

            if i%2 == 0:
                dic={}
                dic['eng']=num[i]

            if i%2 != 0:
                dic['per']=num[i]
                temp.append(dic)

        ff.close()
        
    else:
        print('We can\'t found translate.txt')


#ff=open ("translate.txt","r")
#print(ff.read())
x=1
i=1

while(1):

    temp=[]
    read()


    if i==1:
        result = pyfiglet.figlet_format(" translate ")
        print(result)
        choose=int(input("enter the number of your choice ?\n\n1.persian to english \n2.english to persian \n3.add word\n"))

        if choose==1 :
            
            #read()
            org="per"
            tra="eng"
            
            list1=input("\nenter your sentece (without . ): ").split( )
            list2=[]
            
            
            for i in list1:
                text=i
                for y in range (len(temp)):
                    if temp[y][org]==i:
                        text = temp[y][tra]
                        #print("testttt : ",text)
                        break
                         
                list2.append(text)

            print("\nTranslate : " + " " .join(list2))

            

            i=int(input("\nif you want start it again , please insert 1 : "))


###################################################################

        if choose==2 :
        
            #read()
            org="eng"
            tra="per"
            
            list1=input("\nenter your sentece (without . ): ").split( )
            list2=[]
            
            
            for i in list1:
                text=i
                for y in range (len(temp)):
                    if temp[y][org]==i:
                        text = temp[y][tra]
                        #print("testttt : ",text)
                        break
                         
                list2.append(text)

            print('Translate: ' + ' '.join(list2))

            

            i=int(input("if you want start it again , please insert 1 : "))


###########################################################################
        if choose==3:

            pass
            

            i=int(input("if you want start it again , please insert 1 : "))

##########################################################################
    else :
        print("Good Bye !")
        input("press enter for exit!")
        break