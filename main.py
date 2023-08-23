# Init project
# This project is about a crawler and crawls in behtarino website (It's a kind of map) And finds all the Schools in Mashhad states and save them in a database.
# Imports
import requests
from bs4 import BeautifulSoup
import sqlite3

#Code
connection = sqlite3.connect('crawler.db')
cursor = connection.cursor()







def init():
    print("Program Initialization.")
    cursor.execute("CREATE TABLE IF NOT EXISTS schools (name TEXT, address TEXT, phone TEXT, website TEXT)")


# # URL of the website you want to crawl
# url = "https://example.com"

# # Send a GET request to the URL
# response = requests.get(url)

# # Parse the HTML content with Beautiful Soup
# soup = BeautifulSoup(response.content, "html.parser")

# # Find and print all the links on the page
# for link in soup.find_all("a"):
#     print(link.get("href"))
    
# for link in soup.
