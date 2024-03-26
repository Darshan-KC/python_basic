# Implement a function that takes as input three variables, and returns the largest of the three. Do this without using the Python max() function!
def max():
    pass

if __name__ == "__main__":
    l = list()
    for i in range(3):
        try:
            tem = int(input("Enter number {}".format(i+1)))
        except:
            print("Invalid input")
    