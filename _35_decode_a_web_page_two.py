# Using the requests and BeautifulSoup Python libraries, print to the screen the full text of the article on this website: https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture

# The article is long, so it is split up between 4 pages. Your task is to print out the text to the screen so that you can read the full article without having to click any buttons.

# (Hint: The post here describes in detail how to use the BeautifulSoup and requests libraries through the solution of the exercise posted here.)

# This will just print the full text of the article to the screen. It will not make it easy to read
import requests
from bs4 import BeautifulSoup

base_url = "https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture"
urls = [
    "https://www.vanityfair.com/style/fashion",
    "https://www.vanityfair.com/style/style",
    "https://www.vanityfair.com/style/celebrity",
    "https://www.vanityfair.com/style/beauty",
    "https://www.vanityfair.com/style/royals",
]
response = requests.get(base_url)