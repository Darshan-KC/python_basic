# Let’s continue building Hangman. In the game of Hangman, a clue word is given by the program that the player has to guess, letter by letter. The player guesses one letter at a time until the entire word has been guessed. (In the actual game, the player can only guess 6 letters incorrectly before losing).

# Let’s say the word the player has to guess is “EVAPORATE”.

# >>> Welcome to Hangman!
# _ _ _ _ _ _ _ _ _
# >>> Guess your letter: S
# Incorrect!
# >>> Guess your letter: E
# E _ _ _ _ _ _ _ E
# ...

import _26_pick_word as pick
import random

def intro():
    print("*********************************************************************")
    print("###########\t WELCOME TO THE NUMBER GUESSING GAME \t#############")
    print("*********************************************************************\n")

def output(word,guess):
    print("\n************************************************************************")
    print("#########\t CONGRATULATIONS! YOU HAVE GUESS THE WORD \t##########")
    print("#######\t You guess the word [{}] in {} attempts. \t########".format(word,guess))

def display(l):
    word_str = " ".join(l)
    print(word_str)

if __name__ == "__main__":
    # Display intro
    intro()
    guessCount = 0
    count = 0
    file = "sowpods.txt"
    
    # pick word
    n = pick.countLines(file)
    m = random.randint(0,n)
    word = pick.readFromFile(file,m)
    tem = list()
    for i in range(len(word)):
        tem.append("_")
    word_str = " ".join(tem)
    
    # Checking 
    while(count<len(word)):
        usr = input("Guess your letter : ")
        guessCount +=1
        usr = usr.upper()
        if usr in word:
            for i in range(len(word)):
                if(word[i] == usr):
                    count +=1
                    tem[i] = usr
        word_str = " ".join(tem)
        
        # Display the word
        display(tem)
    
    # Display the result
    output(word,guessCount)
    
    