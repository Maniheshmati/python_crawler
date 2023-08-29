from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import requests
import time

url = 'https://www.behtarino.com'
def open_browser():
    print("Crawling on categories started")
    categories = []
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(chrome_options)
    driver.get(url)
    time.sleep(2)
    driver.find_element(By.CLASS_NAME, 'go862738768').click()
    driver.find_element(By.NAME, 'more-horizontal').click()
    time.sleep(2)
    div_elements = driver.find_elements(By.CLASS_NAME, 'go1407998477')
    for i in div_elements:
        categories.append(i.text)
        
    print("Crawling on categories finished :) \n")
    return categories
        

    
    
open_browser()