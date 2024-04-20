# Given a .txt file that has a list of a bunch of names, count how many of each name there are in the file, and print out the results to the screen. I have a .txt file for you, if you want to use it!

# Extra:

# Instead of using the .txt file from above (or instead of, if you want the challenge), take this .txt file, and count how many of each “category” of each image there are.

import requests

response = requests.get("https://www.practicepython.org/assets/Training_01.txt")
# print(response.content)
content = response.text

lst = content.split("\n")

lst_category = list()

for x in lst:
    tem = x.split("/")
    if len(tem) > 3:
       lst_category.append(tem[2])
    
set_category = set(lst_category)
# print(set_category)
print("The number of categories are ",len(set_category))
