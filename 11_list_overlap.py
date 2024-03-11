# Take two lists, say for example these two:

# 	a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# 	b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and write a program that returns a list that contains only the elements that are common between the lists (without duplicates).
import random
n1 = random.randint(1,20)
list1 = [x for x in range(1,n1)]
while(True):
    n2 = random.randint(1,20)
    if(n1!= n2):
        break

list2 = [x for x in range(1,n2)]

list3 = list(set(list1).intersection(set(list2)))

print("List 1 is : ",list1)
print("List 2 is : ",list2)
print("Result list is : ",list3)
    