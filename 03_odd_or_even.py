# Tasks:
# 1. Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user
# 2. If the number is a multiple of 4, print out a different message.
# 3. Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.

def task1():
    num = int(input("Enter a number : "))
    if(num % 2 == 0):
        print("The number {} is even.".format(num))
    else:
        print("The number {} is odd.".format(num))
    
def task2():
    num = int(input("Enter a number : "))
    if(num % 4 == 0):
        print("The number {} is a multiple of 4.".format(num))
    else:
        print("The number {} isn't the multiple of 4.".format(num))

def task3():
    num = int(input("Enter a number : "))
    check = int(input("Enter a number for divident : "))
    if(num % check == 0):
        print("{} perfectly divides the number {}".format(check,num))
    else:
        print("{} doesn't perfectly divide the number {}.".format(check,num))
        
print("Enter the option 1,2,3 for different operations : ")
print("1. Check odd or not.")
print("2. Check multiple of 4. ")
print("3. num1 divides num2 or not.")
choice = int(input("Enter your choice : "))

if(choice == 1):
    task1()
elif(choice == 2):
    task2()
elif(choice == 3):
    task3()
else:
    print("Invalid chioce")