# stone , paper , scissor

import random
comp = random.randint(0 , 2)
user = int(input(" 0.stone\n 1.paper\n 2.scissor\nEnter num :"))

def game1(comp, user):
    if(comp == user):
        return 0
    
    if((comp == 0 and user == 1) or (comp == 1 and user == 2) or (comp == 2 and user == 0)):
        return 1
    
    return -1

play = game1(comp, user)
print("user:",user)
print("comp:",comp)

if(play == 0):
    print("Game Draw!!")
elif(play == 1):
    print("You Won!!")
else:
    print("You Lose!!")