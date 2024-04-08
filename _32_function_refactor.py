# In this exercise, we will be stretching our functions muscle by refactoring an existing code snippet into using functions.

# Here is the code snippet to refactor (taken from a correct but very repeated solution to exercise 24 on this website):

# print(" --- --- ---")
# print("|   |   |   |")
# print(" --- --- ---")
# print("|   |   |   |")
# print(" --- --- ---")
# print("|   |   |   |")
# print(" --- --- ---")
# Hint: Think about a way to refactor this using functions where generating an 8x8 or a 19x19 grid is a single change to a function call!

def display_structure(n):
    print(" _ _ _"*n)
    for i in range(n):
        print("|",end="")
        print("     |"*n)
        print(" _ _ _"*n)

if __name__ == "__main__":
    while(True):
        try:
            n = int(input("Enter the size of the structure: "))
            break
        except TypeError as error:
            print("!!!\t Error : " + error)
            print("Please enter a valid integer.")
            
    display_structure(n)


    