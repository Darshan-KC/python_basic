# Take a list, say for example this one:

#   a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# and write a program that prints out all the elements of the list that are less than 5.

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# print("The numbers less than 5 are :")
# for x in a:
#     if(x < 5):
#         print(x,end=" ")

# Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list. Write this in one line of Python.

b = [x for x in a if x < 5]
print(b)
# Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user.

num = int(input("Enter a number : "))
c = [x for x in a if x < num]
print(c)