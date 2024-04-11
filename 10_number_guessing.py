# Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.
import random

def intro():
    print("#############\tWelcome to the number guessing game. \t##############")


old_num = -1


while(True):
    count = 0
    print("Enter one of the following options:")
    print("1. Enter 1 to start or replay the game")
    print("2. Enter 2 to exit the game")
    try:
        choice = int(input("Enter your choice : "))
        if(choice == 2):
            break
        elif(choice != 1):
            print("\n!!!Enter the choice either 1 or 2.!!!\n")
            continue
    except:
        print("!!! Invalid input !!!. Enter correct option")
        continue
    
    # computer choice or secret number
    num = random.randint(1,9)
    
    # Checking whether new random number is equal to old number or not
    while(old_num == num):
        num = random.randint(1,9)
    old_num = num
    
    # Logic of guessing game
    while(True):
        try:
            man = int(input("Enter your guess (1 to 9) : "))
            if(man >0 and man < 10):
                count += 1
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