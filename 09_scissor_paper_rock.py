# Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)
import random

def computer():
    tem = random.randint(1,3)
    if(tem == 1):
        return 's'
    elif(tem == 2):
        return 'p'
    return 'r'

def abbr(x):
    if(x == 's'):
        return "Scissor"
    elif(x == 'p'):
        return "Paper"
    else:
        return "Rock"
    
def display(result,usr,com):
    usr = abbr(usr)
    com = abbr(com)
    if(result == 0):
        print("The game is dram. You choose {} and computer choose {}. ".format(usr,com))
    elif(result == 1):
        print("$$$$ CONGRATULATIONS! You won the game.  $$$$$$.\n You choose {} whereas computer choose {}.".format(usr,com))
    else:
        print("**** BAD LUCK! You loose. *****\n You choose {} whereas computer choose {}.".format(usr,com))
    return
    
def comparison(p1,p2):
    if(p1 == p2):
        return 0
    elif(p1 == 's' and p2 == 'p'):
        return 1
    elif(p1 == 's' and p2 == 'r'):
        return -1
    elif(p1 == 'p' and p2 == 's'):
        return -1
    elif(p1 == 'p' and p2 == 'r'):
        return 1
    elif(p1 == 'r' and p2 == 's'):
        return 1
    elif(p1 == 'r' and p2 == 'p'):
        return -1
    
    
def start():
    while(True):
        print("\n\n")
        print("*"*10," Welcome to the Rock Paper Scissor game. ","*"*10)
        print("\n\n\nThis match is between you and the computer")
        print("\nEnter one of the following options of your choice: \n")
        print("1. Enter 1 to start the game.")
        print("2. Enter 2 to quit the game.")
        while(True):
            choice = input("\n\nEnter your choice: ")
            if(choice == '1' or choice == '2'):
                break
            else:
                print("\n\t!!!! Invalid input. Please enter the correct input. !!!!!")
        if(choice == '2'):
            break
        else:
            inputs()
    return

def inputs():
    while(True):
        print("\nEnter your input : ")
        print("1. Enter s for scissor.")
        print("2. Enter p for paper.")
        print("3. Enter r for rock.")
        usr = input("Enter your choice : ")
        usr = usr.lower()
        if(usr == 's' or usr == 'p' or usr == 'r'):
            break
        else:
            print("\n\t!!!! Invalid input. Please enter the correct input. !!!!!")
        
    com = computer()
    
    result = comparison(usr,com)
    
    display(result,usr,com)
        
    
    

start()