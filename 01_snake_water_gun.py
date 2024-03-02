# Snake water gun game is a game which requires two players both have to select something from snake or water or gun. 
# snake wins over water , gun win over snake and water wins over gun. ultimately the player with maximum points wins the game.
import random

# To take computer input
def computer_choice(c):
    if(c==0):
        return "s"
    elif(c==1):
        return "w"
    else:
        return "g"

# To take user input
def user_choice():
    choice=input("Input your choice (snake / water / gun): ")
    choice=choice.lower()
    if(choice=="snake"):
        return "s"
    elif(choice=="water"):
        return "w"
    elif(choice=="gun"):
        return "g"
    else:
        print("!!! Invalid input !!!\n")
        a=user_choice()
        return a

# Compare user and computer choice
def compare(u,c):
    # user wining condition
    if(u=="g" and c=="s"):
        return 1
    elif(u=="w" and c=="g"):
        return 1
    elif(u=="s" and c=="w"):
        return 1
    # draw condition
    elif(u=="g" and c=="g"):
        return 0
    elif(u=="w" and c=="w"):
        return 0
    elif(u=="s" and c=="s"):
        return 0
    # computer wining condition
    elif(u=="s" and c=="g"):
        return -1
    elif(u=="g" and c=="w"):
        return -1
    else:
        return -1
    
#Getting full meaning e.g. s => snake
def full(x):
    if(x=="s"):
        return "Snake"
    elif(x=="w"):
        return "Water"
    else:
        return "Gun"
    
#display output
def output(result,user,computer):
    if(result==1):
        print("!!!  CONGRATULATION YOU WIN THE MATCH    !!!")
        print(f"You choose {user} and computer choose {computer}")
        return
    elif(result==0):
        print("!!!  THE GAME IS DRAW    !!!")
        print(f"You choose {user} and computer choose {computer}")
        return
    else:
        print("!!!  COMPUTER WON THE GAME   !!!")
        print(f"You choose {user} and computer choose {computer}")
        return
    
cmptr = random.randint(0,2)
computer=computer_choice(cmptr)
user=user_choice()
result=compare(user,computer)
computer=full(computer)
user=full(user)
output(result,user,computer)