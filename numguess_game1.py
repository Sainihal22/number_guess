import random
import math

ch='y'

print("\n *************** WELCOME TO NUMBER GUESSING GAME *************** \n ")

while (ch=='y' or ch=='Y' ):
    
    lw=int(input("  ENTER THE LOWER BOUND : "))
    up=int(input("  ENTER THE UPPER BOUND : "))
    guessnum=random.randint(lw,up)
    
    x=round(math.log(up-lw+1,2))
    
    print("\n  YOU JUST HAVE ",x," CHANCES ")
    
    c=0
    
    while(c<x) :
        
        c=c+1
        
        num=int(input("  ENTER THE NUMBER : "))
        
        if num==guessnum :
            
            print("\n  YOU GUESSED IT IN",c,"CHANCES ")
            break
        
        elif num < guessnum :
            
            print("  NUMBER IS TOO LOW !!!! ")
        
        elif num > guessnum : 
            
            print("  NUMBER IS TOO HIGH !!!! ")
    
    else :
        
        print("\n  BETTER LUCK NEXT TIME !!!! ")
        print("\n  THE NUMBER IS : ",guessnum)
    
    ch=input("  DO YOU WANT TO CONTINUE ? (Y/N) : ")
    