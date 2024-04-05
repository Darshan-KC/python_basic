# In the previous exercise we saved information about famous scientists’ names and birthdays to disk. In this exercise, load that JSON file from disk, extract the months of all the birthdays, and count how many scientists have a birthday in each month.

# Your program should output something like:

# {
# 	"May": 3,
# 	"November": 2,
# 	"December": 1
# }

#import
from collections import Counter
import json

def readFromFile(file_name):
    with open(file_name,'r') as f:
        data = json.load(f)

if __name__ == "__main__":
    pass