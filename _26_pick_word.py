# In this exercise, the task is to write a function that picks a random word from a list of words from the SOWPODS dictionary. Download this file and save it in the same directory as your Python code. This file is Peter Norvig’s compilation of the dictionary of words used in professional Scrabble tournaments. Each line in the file contains a single word.
import random

def readFromFile(file,line):
    with open(file,"r") as f:
        for i in range(line+1):
            if(i == line):
                return f.readline().strip()
            f.readline()
    return None

def countLines(file):
    count = 0
    with open(file,"r") as f:
        for i in f:
            count += 1
    return count

if __name__ == "__main__":
    file = "sowpods.txt"
    n = countLines(file)
    m = random.randint(0,n)
    print(f"Random word is {readFromFile(file,m)}")