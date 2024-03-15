# Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.

# Extras:

# Write two different functions to do this - one using a loop and constructing a list, and another using sets.

list = [1, 2, 4, 1, 2 , 9, 4,5, 6]
list1 = list()
# using loop 
for x in list:
    if(x in list1):
        continue
    list1.append(x)
print(list1)