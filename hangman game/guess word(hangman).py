
import os
word = input("write your word , please ? : ")
os.system('cls')
word=word.lower()
a=len(word)
x = ''
i = a

while i > 0:      
    check = 0             
    for char in word:  
          
        if char in x:    
            print (char,end="   ")
            check += 1
               
        else:
            print ("__",end="   ")
        
    print("\n\nYou have (", i , ") times for guess")
               
    if check == a:        
        print ("\n -------- * congratulation You won * ------ \n")
        input ("press enter to exit !\n") 
        break  
                    
    guess = input("guess a character : ")
    print("\n") 
    guess=guess.lower() 
    x += guess                    
    if guess not in  word:  
        i -= 1        
        print("Wrong : ", guess)
        print("\n")      
        if i == 0:           
            print ("\n --------- *sorry You lose * --------")
            input ("press enter to exit !\n")  
