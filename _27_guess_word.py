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

def check():
    pass

def userInput():
    usr = input("Guess your letter : ")
    
def display(usr = None):
    n = len(word)
    if(usr == None):
        print("_ "*n)
    else:
        i = 0
        if(usr in word):
            count +=1
            for i in range(n):
                if(word[i] == usr):
                    print(word[i].upper())
                else:
                    print("_ ")
    print(word)

if __name__ == "__main__":
    # Display intro
    intro()
    global word
    global count
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
    print(word_str)
    
    display()
    # while(count!=len(word)):
    #     userInput()
    