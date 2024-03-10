# Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.
import random

print("#############\tWelcome to the number guessing game. \t##############")
def intro():
    pass

num = random.randint(1,9)
while(True):
    count = 0
    print("Enter one of the following options:")
    print("1. Enter 1 to start or replay the game")
    print("2. Enter 2 to exit the game")
    try:
        choice = int(input("Enter your choice : "))
        if(choice == 2):
            break
    except:
        print("!!! Invalid input !!!. Enter correct option")
        continue
    while(True):
        try:
            man = int(input("Enter your guess (1 to 9) : "))
            count += 1
            if(man >0 and man < 10):
                if(man == num):
                    print("\n******* CONGRATULATIONS! You guess the correct number in {} attemps. ***********\n".format(count))
                    break
                elif((man - num) <=3 and (man - num) > 0):
                    print("Your guess is too close. But you guess a bit greater number.")
                elif((num - man) <= 3 and (num - man) > 0):
                    print("Your guess is too close. But you guess a bit smaller number.")
                elif((num - man) <=6 and (num - man) > 0):
                    print("Your guess is close. But you guess smaller number.")
                elif((man - num) <=6 and (man - num) > 0):
                    print("Your guess is close. But you guess greater number.")
                else:
                    print("Your aren't close")
            else:
                print("Enter number between 1 and 9")
                continue
        except:
            print("!!! Invalid input !!!.")
    

print("\n##########\t Thank you for playing number guessing game. \t ##############")