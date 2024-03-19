# Create a program that will play the “cows and bulls” game with the user. The game works like this:

# Randomly generate a 4-digit number. Ask the user to guess a 4-digit number. For every digit that the user guessed correctly in the correct place, they have a “cow”. For every digit the user guessed correctly in the wrong place is a “bull.” Every time the user makes a guess, tell them how many “cows” and “bulls” they have. Once the user guesses the correct number, the game is over. Keep track of the number of guesses the user makes throughout teh game and tell the user at the end.

import random

# Intro
def welcome():
    print("\n\t########################################################")
    print("\n\n\t*******\t Welcome to the COWS AND BULLS game\t********\n\n")
    print("\n\t########################################################\n")

# Computer input
def computer():
    com = list()
    for i in range(4):
        tem = random.randint(0,9)
        if(len(com) > 0):
            while(tem in com):
                tem = random.randint(0,9)
        com.append(tem)
        # com.append(random.randint(0,9))
    # print(com)
    return com

# User input
def user():
    usr = list()
    while(True):
        tem = input("Enter your guess : ")
        if(len(tem) == 4):
            try:
                tem = int(tem)
                break
            except:
                print("Invalid input")
        else:
            print("Guess should be of 4 digits number.")
            
    for _ in range(4):
        x = tem % 10
        usr.insert(0,x)
        tem = tem // 10
    return usr

# Main logic
def compare(comptr,usr):
    count = 1
    cow = 0
    bull = 0
    while(True):
        for x in range(4):
            if comptr[x] in usr:
                if(comptr[x] == usr[x]):
                    cow += 1
                else:
                    bull +=1
        else:
            if(bull >1):
                b = "bulls"
            else:
                b = "bull"
            if(cow > 1):
                c = "cows"
            else:
                c = "cow"
            print("{0} {1} and {2} {3}".format(cow,c,bull,b))
        
        if(comptr == usr):
            return count
        else:
            usr = user()
            count += 1
            cow = bull = 0
            
            
            
# Output function
def output(result,com):
    print("\n\t######\t CONGRATULATIONS. You complete the game in {} steps.\t#######".format(result))
    print("\t#######\t         Computer choice was {}                     \t#######".format(com))
    print("\n\t*************************************************************************\t")

# Main method
if __name__ == "__main__":
    welcome()
    comptr = computer()
    usr = user()
    result = compare(comptr,usr)
    output(result,comptr)