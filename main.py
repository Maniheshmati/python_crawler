# Init project
# This project is about a crawler and crawls in behtarino website (It's a kind of map) And finds all the Schools in Mashhad states and save them in a database.
# Imports
import requests
from bs4 import BeautifulSoup
import sqlite3
import shapely

#Code
connection = sqlite3.connect('crawler.db')
cursor = connection.cursor()

# cursor.execute("""CREATE TABLE IF NOT EXISTS provinces(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name TEXT NOT NULL
#     )""");
# connection.commit()
# cursor.execute("""CREATE TABLE IF NOT EXISTS cities(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name TEXT NOT NULL,
#     provinve_id INTEGER NOT NULL,
#     FOREIGN KEY (provinve_id) REFERENCES provinces(id)
#     )""");
# connection.commit()
# cursor.execute("""CREATE TABLE IF NOT EXISTS neighborhoods(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name TEXT NOT NULL,
#     city_id INTEGER NOT NULL,
#     FOREIGN KEY (city_id) REFERENCES cities(id))""");
# connection.commit()


while True:

    def init(category, neighbor, city):
        
        url = f"https://www.behtarino.com/r/{category}/{city}/{neighbor}"
        print(url)
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        
        schools = soup.find_all("h3")
        
        for school in schools:
            print(school.text)
        
        print("Crawling finished \n")



    def crawl_menu():
        city = input("Enter city name: ")
        neighborhood = input("Enter neighborhood name: ")
        category = input("Enter category name: ")
        city = city.replace(" ", "-")
        neighborhood = neighborhood.replace(" ", "-")
        category = category.replace(" ", "-")
        
        if city == "" or neighborhood == "" or category == "":
            print("Please fill the inputs...")
            crawl_menu()
        else:
            print("Crawling started...")
            init(category=category, neighbor=neighborhood, city=city)
        
    def start_menu():
        print("1. Crawl")
        print("2. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            crawl_menu()
        elif choice == 2:
            exit()
        else:
            print("Invalid choice")
            start_menu()
            

    start_menu()