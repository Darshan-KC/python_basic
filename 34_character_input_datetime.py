# Implement the same exercise as Exercise 1 (Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old), except don’t explicitly write out the year. Use the built-in Python datetime library to make the code you write work during every year, not just the one we are currently in.
import datetime

if __name__ == "__main__":
    name = input("Enter your name : ")
    while(True):
        try:
            age = int(input("Enter your age : "))
            if(age > 0 and age < 100):
                break
            else:
                print("Invalid age.")
        except:
            print("Enter valid age.")
            
    now = datetime.datetime.now()
    
    print("{} will turn 100 in year {}.".format(name.capitalize(),now.year + (100 -age)))