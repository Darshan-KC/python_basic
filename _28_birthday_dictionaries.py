# we will keep track of when our friend’s birthdays are, and be able to find that information based on their name. Create a dictionary (in your file) of names and birthdays. When you run your program it should ask the user to enter a name, and return the birthday of that person back to them. 
# The interaction should look something like this:
# Welcome to the birthday dictionary. We know the birthdays of:
# Albert Einstein
# Benjamin Franklin
# Ada Lovelace
# >>> Who's birthday do you want to look up?
# Benjamin Franklin
# >>> Benjamin Franklin's birthday is 01/17/1706.

birthday = {
    "ram" : "2000/01/03",
    "hari" : "1999/08/16",
    "sita" : "2002/09/22",
    "gita" : "2003/09/23",
}

print("Welcome to the birthday dictionary. We know the birthdays of : ")
for key in birthday:
    print(key.capitalize())
    
name = input("Who's birthday do you want to look up? ")
name = name.lower()
result = birthday.get(name)
if(result == None):
    print("\n!!!Enter the name that is given!!!\n")
else:
    print("{}'s birthday is {}.".format(name.capitalize(),result))