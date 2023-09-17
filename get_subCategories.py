from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import requests
import time
import sys

import sqlite3

url = 'https://www.behtarino.com'

def open_browser():
    status = "not found"
    connection = sqlite3.connect('crawler.db')
    cursor = connection.cursor()
    categoriesList = cursor.execute("SELECT name FROM categories").fetchall()
    print("Crawling on categories started")
    sub_categories = []
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(2)
    driver.find_element(By.CLASS_NAME, 'go862738768').click()
    time.sleep(2)
    driver.find_element(By.NAME, 'more-horizontal').click()
    time.sleep(2)
    driver.find_element(By.CLASS_NAME, 'go931307338').click()
    time.sleep(1)
    first_category_name = driver.find_element(By.CLASS_NAME, 'go931307338').text

    for i in categoriesList:
        if i[0] == first_category_name:
            status = "found"
    if(status == "found"):
        category_id = cursor.execute("Select id FROM categories WHERE name = ?", (first_category_name,)).fetchone()



open_browser()
