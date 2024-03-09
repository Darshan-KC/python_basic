# Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)
def comparison(p1,p2):
    pass
def start():
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
        return 
    else:
        inputs()

def inputs():
    pass

start()
inputs()