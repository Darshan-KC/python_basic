# Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only the first and last elements of the given list. For practice, write this code inside a function.
a = [5, 10, 15, 20, 25]

lst = list()
n = len(a)
i = 0
for x in range(n):
    if(x==0 or x==(n-1)):
        lst.append(a[x])
        

print(lst)