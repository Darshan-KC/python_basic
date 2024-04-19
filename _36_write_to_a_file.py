# Take the code from the How To Decode A Website exercise and instead of printing the results to a screen, write the results to a txt file. In your code, just make up a name for the file you are saving to.

# Extras:

# Ask the user to specify the name of the output file that will be saved.

import requests
from bs4 import BeautifulSoup

def scraping_and_writing(url,file_name):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text,"html.parser")
        paragraphs = soup.find_all('p')
        data = [x.get_text() for x in paragraphs]
        data_text = "\n\n".join(data)
        with open(file_name,"w", encoding="utf-8") as f:
            f.write(data_text)
        print("Successfully scrap and write data into the file ",file_name)
    else:
        print("Failed to retrieve data from the URL. Status code:", response.status_code)
        
if __name__ == "__main__":
    base_url = "https://www.nytimes.com/"
    
    file_name = input("Enter file name (e.g., abc.txt): ")
    
    if file_name.endswith((".txt", ".json", ".html", ".htm")):
        scraping_and_writing(base_url, file_name)
    else:
        print("Invalid file format. Please provide a file name with .txt, .json, .html, or .htm extension.")
        