# Write a function that takes an ordered list of numbers (a list where the elements are in order from smallest to largest) and another number. The function decides whether or not the given number is inside the list and returns (then prints) an appropriate boolean.

# Extras:

# Use binary search.

def binarySearch(lst,l,r,n):
    if(l>r):
        print("Invalid list index.")
        return False
    elif(l==r):
        if(lst[l] == n):
            return True
        else:
            return False
    else:
        m = (l + r)//2
        if(lst[m] == n):
            return True
        elif(n <= lst[m]):
            return binarySearch(lst,l,m-1,n)
        else:
            return binarySearch(lst,m+1,r,n)
            

# Main program
if __name__ == "__main__":
    lst = [1,9,2,5,4,6,7]
    # Sort list
    lst.sort()
    print(lst)
    try:
        n = int(input("Enter the number to search in the list : "))
        result = binarySearch(lst,0,(len(lst) - 1),n)
        if(result):
            print("{} is present in the list.".format(n))
        else:
            print("{} isn't present in the list.".format(n))
        
    # Handle invalid input 
    except ValueError:
        print("Invalid input")
        
    # Handle other exception 
    except Exception as e:
        print("An error occurred : ",e)