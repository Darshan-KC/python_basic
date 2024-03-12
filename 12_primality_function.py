# Ask the user for a number and determine whether the number is prime or not.
import math

def Prime(n :int ) ->bool:
    k=math.sqrt(n)
    k=math.floor(k)
    i=2
    while i<=k:
        if(n%i == 0):
            return False
        i+=1
    return True

try:
    n = int(input("Enter a number : "))
    if(Prime(n)):
        print("{} is a prime number.".format(n))
    else:
        print("{} is not a prime number.".format(n))
except:
    print("Invalid input!")
    