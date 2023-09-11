import sqlite3

def save_categories(categories):
    connection = sqlite3.connect('crawler.db')
    cursor = connection.cursor()
    for category in categories:
        # Check if the cetogory is already in the table
        cursor.execute("""
            SELECT * FROM categories WHERE name = ?
        """, (category,))
        if cursor.fetchone():
            continue
        else:
            cursor.execute("""
                Insert INTO categories(name) VALUES(?)
            """, (category,))
        
    connection.commit()
    connection.close()
    
    print("Saves in table Categories \n")
    
def save_subCategories(subCategories):
    pass

def save_provinces(provinces):
    pass

def save_cities(cities):
    pass

def save_neighborhoods(neighborhoods):
    pass