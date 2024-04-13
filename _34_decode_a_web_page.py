# Use the BeautifulSoup and requests Python packages to print out a list of all the article titles on the New York Times homepage.
import requests # Enter command pip install request
from bs4 import BeautifulSoup as bs # Enter command pip install bs4

url = "https://www.nytimes.com/"
response = requests.get(url)
soup = bs(response.content,"html.parser")
print(soup.find_all('article'))