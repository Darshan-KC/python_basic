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

def numtomonth(num):
    month = {
        1:"January",2:"February",3:"March",4:"April",5: "May",6: "June",7: "July",8: "August",9: "September", 10:"October",11: "November",12: "December"
    }
    return month.get(num)

def readFromFile(file_name):
    with open(file_name,'r') as f:
        data = json.load(f)
    return data

if __name__ == "__main__":
    data = readFromFile("birthday.json")
    
    birthdays = dict()
    result = dict()
    # birthday count 
    for i in range(1,13):
        count = 0
        for x,y in data.items():
            dob = y.split('/')
            if(i == int(dob[1])):
                count +=1
        birthdays[i] = count
    for x,y in birthdays.items():
        if y > 0:
            index = numtomonth(x)
            result[index] = y
    
    # print result
    print(result)