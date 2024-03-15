# Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.

# Extras:

# Write two different functions to do this - one using a loop and constructing a list, and another using sets.

list0 = [1, 2, 4, 1, 2 , 9, 4,5, 6]

# using loop 
list1 = list()
for x in list0:
    if(x in list1):
        continue
    list1.append(x)
list1.sort()
print(list1)

# using set 
tem = set(list0)
list0 = list(tem)
print(list0)