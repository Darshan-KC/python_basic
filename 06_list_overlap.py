# Take two lists, say for example these two:

#   a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#   b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.

# Extras:

# Randomly generate two lists to test this
# Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)

import random
n1 = random.randint(1,20)
n2 = random.randint(1,20)

l1 = l2 = list()

i = 0
while(i<n1):
    tem = random.randint(1,20)
    l1.append(tem)
    i+=1

i = 0
while(i<n2):
    tem = random.randint(1,20)
    l2.append(tem)
    i+=1
    
print("First list is ",l1)

print("Second list is ",l2)

intersection = list(set(l1).intersection(set(l2)))

print("The intersection is ",intersection)