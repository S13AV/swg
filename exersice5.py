#SNAKE WATER GAME
import random as r
import time as t
print("welcome to SNAKE WATER GUN GAME")
t.sleep(1.2)
n = r.randint(1,3)
a = int(input( ("Enter your number \'(1=Snake|2=Water|3=Gun)\': ")))
if a == n:
    print("Draw ,i guess")
elif a ==1 and n ==3:
    print("Bro get a life you cant even win against a bot")
elif a==2 and n == 3:
    print("Congratulations you win")
elif a== 1 and n==2:
    print("Congratulations you win")
elif a == 3 and n ==2:
    print("Bro get a life you cant even win against a bot")
elif a == 3 and n==1:
    print("Congratulations you win")
else:
    print("Are you blind or are you a idiot")
    

    
