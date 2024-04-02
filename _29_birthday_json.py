# In this exercise, modify your program from Part 1 to load the birthday dictionary from a JSON file on disk, rather than having the dictionary defined in the program.

# Bonus: Ask the user for another scientist’s name and birthday to add to the dictionary, and update the JSON file you have on disk with the scientist’s name. If you run the program multiple times and keep adding new names, your JSON file should keep getting bigger and bigger.

# import json to manipulate json data
import json

birthday = {
        "ram" : "2000/01/03",
        "hari" : "1999/08/16",
        "sita" : "2002/09/22",
        "gita" : "2003/09/23",
    }
# json_data = json.dumps(birthday)
# with open("birthday.json","w") as f:
#     # f.write(json_data)
#     json.dump(birthday,f)

def ReadFromFile(file,name):
    with open(file,'r') as f:
        data = json.load(f)
        name = name.lower()
        result = data.get(name)
        if(result == None):
            print("\n{} is not in the file.\n".format(name))
        else:
            print("\nThe birthday of {} is on {}.\n".format(name.capitalize(),result))
def WriteIntoFile(name,data):
    pass

if __name__ == "__main__":
    while(True):
        print("Enter one of the following options : ")
        print("* Enter 1 to read data from file.")
        print("* Enter 2 to write data into the file.")
        print("* Enter 3 to exit this.")
        try:
            choice = int(input("Enter your choice : "))
            if(choice > 3 or choice <1):
                raise("Number out of options.")
            else:
                if(choice == 3):
                    break
                elif(choice == 1):
                    name = input("Enter the name of the person you want to get birthday: ")
                    ReadFromFile("birthday.json",name)
                else:
                    pass
        except Exception as e:
            print("Error => ",e)