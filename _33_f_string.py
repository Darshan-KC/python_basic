# Implement the same exercise as Exercise 1 (Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old), except use f-strings instead of the + operator to print the resulting output message.
def output(name,age):
    age = 100 - age
    print(f"{name} will turn 100 after {age} years.")

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
            
    output(name,age)