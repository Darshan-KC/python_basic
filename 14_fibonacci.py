# Write a program that asks the user how many Fibonnaci numbers to generate and then generates them. Take this opportunity to think about how you can use functions. Make sure to ask the user to enter the number of numbers in the sequence to generate.(Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the sequence is the sum of the previous two numbers in the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)

def fibonacci(n:int)->int:
    if(n==1 or n==2):
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

try:
    n = int(input("Enter a numbers of fibonnaci that you want to generate : "))
    if(n<1):
        print("Number is less than 1.")
    else:
        for x in range(1,n+1):
            print(fibonacci(x),end=" ")
except:
    print("Invalid number")