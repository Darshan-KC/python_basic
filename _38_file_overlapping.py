# Given two .txt files that have lists of numbers in them, find the numbers that are overlapping. One .txt file has a list of all prime numbers under 1000, and the other .txt file has a list of happy numbers up to 1000.

import requests

first_url = "https://www.practicepython.org/assets/primenumbers.txt"
second_url = "https://www.practicepython.org/assets/happynumbers.txt"

first_response = requests.get(first_url)
second_response = requests.get(second_url)

first_content = first_response.text
second_content = second_response.text

first_lst = first_content.split("\n")
second_lst = second_content.split("\n")

overlap = set(first_lst).intersection(second_lst)
print("The number of overlapping numbers is ",len(overlap))