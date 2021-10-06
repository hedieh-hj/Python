import random
from termcolor import colored 
y=1
while True:
    if y==1:

        list=["rock","paper","scissors"]
        i=0
        count1=0
        count2=0

        counter=int(input("how many rounds do you play ? : "))

        select=int(input("\n\n*******rock 👊  paper 🤚 scissors ✌*******\n\nif you want to play with bot enter number 1 (solo):\nif you want to play with your friends enter number 2 (duo):\n"))
        while True:

            if select==1 :
                print("\nscore player : ", count1 ,  "\nscore bot  : " , count2 )
                player1=input("\nwrite your choice  (rock 👊  paper 🤚 scissors ✌) = ")
                player2=random.choice(list)
                print("bot choice (rock 👊  paper 🤚 scissors ✌) = " , player2)

                if player1=="rock" or player1=="paper" or player1=="scissors":

                    if (player1=="rock" and player2=="scissors" ) or (player1=="paper" and player2=="rock") or (player1=="scissors" and player2=="paper"):
                        count1+=1
                        i+=1
                        if count1==counter :
                            print(colored("\n*** winner = player ***\n", 'green'))
                            
                            break

                    elif (player2=="rock" and player1=="scissors" ) or (player2=="paper" and player1=="rock") or (player2=="scissors" and player1=="paper"):
                        count2+=1
                        i+=1   
                        if count2==counter:
                            print(colored("\n*** winner = bot ***", 'green'))
                            
                            break

                else:
                    print(colored ("\nyou write a illegal word ! try again...\n" , 'red') )      

            if select==2 :

                print("\nscore player 1 : ", count1 ,  "\nscore player 2 : " , count2 )
                player1=input("\nwrite your choice player 1  (rock 👊  paper 🤚 scissors ✌) = ")

                if player1=="rock" or player1=="paper" or player1=="scissors"  :
                    flag = 1
                    winflag = 1
                    while flag == 1:
                                
                        player2=input("write your choice player 2  (rock 👊  paper 🤚 scissors ✌) = ")

                        if player2=="rock" or player2=="paper" or player2=="scissors":
                            flag = 0
                            if (player1=="rock" and player2=="scissors" ) or (player1=="paper" and player2=="rock") or (player1=="scissors" and player2=="paper"):
                                count1+=1
                                i+=1
                                if count1==counter :
                                    print(colored("\n*** winner = player 1 ***\n", 'green'))
                                    winflag = 0
                                    break
                                

                            elif (player2=="rock" and player1=="scissors" ) or (player2=="paper" and player1=="rock") or (player2=="scissors" and player1=="paper"):
                                count2+=1
                                i+=1   
                                if count2==counter:
                                    print(colored("\n*** winner = player 2 ***\n", 'green')) 
                                    winflag = 0
                                    break   

                        else:
                            print(colored ("\nyou write a illegal word player 2 ! try again...\n" , 'red') )

                    if winflag == 0:
                        break        
                        

                else:
                    print(colored ("\nyou write a illegal word player 1 ! try again...\n" , 'red') )

        y=int(input (" do you want to play it again ? yes=1  no=2 : "))

    else :
        print("Good bye !")
        input()
        break            