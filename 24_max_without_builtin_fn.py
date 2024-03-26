# Implement a function that takes as input three variables, and returns the largest of the three. Do this without using the Python max() function!

# Finding max function
def max(l):
    if(l[0]>l[1] and l[0]>l[2]):
        return l[0]
    elif(l[1]>l[2]):
        return l[1]
    else:
        return l[2]

# Main function
if __name__ == "__main__":
    l = list()
    for i in range(3):
        while(True):
            try:
                tem = int(input("Enter number {} : ".format(i+1)))
                break
            except:
                print("Invalid input")
        l.append(tem)
    result = max(l)
    print("The maximum of {}, {} and {} is {}.".format(l[0],l[1],l[2],result))
    