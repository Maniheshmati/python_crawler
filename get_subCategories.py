from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import sqlite3

# Define constants
URL = 'https://www.behtarino.com'


def open_browser():
    # Initialize variables
    category_id = None
    status = "not found"

    # Connect to the database
    connection = sqlite3.connect('crawler.db')
    cursor = connection.cursor()

    # Fetch category and sub-category lists
    categories_list = [row[0] for row in cursor.execute("SELECT name FROM categories").fetchall()]
    sub_categories_list = [row[0] for row in cursor.execute("SELECT name FROM sub_categories_level_1").fetchall()]
    print("Crawling on categories started")

    # Initialize WebDriver
    driver = webdriver.Chrome()
    driver.get(URL)
    time.sleep(2)

    # Interact with elements
    driver.find_element(By.CLASS_NAME, 'go862738768').click()
    time.sleep(2)
    driver.find_element(By.NAME, 'more-horizontal').click()
    time.sleep(2)
    driver.find_element(By.CLASS_NAME, 'go931307338').click()
    time.sleep(2)
    # Find the list of category elements
    found_categories_list = driver.find_elements(By.CLASS_NAME, 'go839650805')

    # Initialize variables
    category_id = None

    # Iterate through the found categories
    for i, category_element in enumerate(found_categories_list):
        category_name = category_element.text

        # Check if the category name exists in the database
        if category_name in categories_list:
            # Retrieve the category ID from the database
            category_id = cursor.execute("SELECT id FROM categories WHERE name = ?", (category_name,)).fetchone()[0]

            # Click on the category element (assuming this is how you navigate to sub-categories)
            category_element.click()

            # Now you can write code to find sub-categories within this category
            sub_categories_list = driver.find_elements(By.CLASS_NAME, 'go2478805746')
            for j, sub_category_element in enumerate(sub_categories_list):
                sub_category_name = sub_category_element.text

                # Check for duplicates
                cursor.execute("SELECT name FROM sub_categories_level_1 WHERE category = ?", (category_id,))
                existing_sub_categories = set(row[0] for row in cursor.fetchall())

                # Check if the sub-category is not already in the database
                if sub_category_name not in existing_sub_categories:
                    # Insert into database
                    cursor.execute("INSERT INTO sub_categories_level_1 (name, category) VALUES (?, ?)",
                                   (sub_category_name, category_id))
                    connection.commit()
                    existing_sub_categories.add(sub_category_name)

        else:
            continue

    print("Crawling on sub_categories finished")

