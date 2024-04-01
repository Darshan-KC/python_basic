# In this exercise, modify your program from Part 1 to load the birthday dictionary from a JSON file on disk, rather than having the dictionary defined in the program.

# Bonus: Ask the user for another scientist’s name and birthday to add to the dictionary, and update the JSON file you have on disk with the scientist’s name. If you run the program multiple times and keep adding new names, your JSON file should keep getting bigger and bigger.

with open("birthday.json","a+") as f:
    birthday = {
        "ram" : "2000/01/03",
        "hari" : "1999/08/16",
        "sita" : "2002/09/22",
        "gita" : "2003/09/23",
    }
    f.write(str(birthday))
