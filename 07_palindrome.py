# Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)

str = input("Enter a string : ")
str1 = str[::-1]
if str == str1:
    print("{} is a palindrome string.".format(str))
else:
    print("{} isn't a palindrome string.".format(str))