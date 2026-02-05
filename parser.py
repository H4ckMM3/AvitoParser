import requests
from bs4 import BeautifulSoup
from urllib3 import response
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import CITY, CATEGORY, MIN_PRICE, MAX_PRICE
from config import AVITO_URL

def get_listings():
    
    option = Options()
    option.add_argument("--headless")
    option.add_argument("--disable-gpu")
    option.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=option)
    listings = []
    try:
        driver.get(AVITO_URL)
        
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[data-marker='item']")))
        
        items = driver.find_elements(By.CSS_SELECTOR, "div[data-marker='item']")
        
        for item in items:
            try:
                link_element = item.find_element(By.CSS_SELECTOR, "a[href]")
                link = link_element.get_attribute("href")
                
                try:
                    price_element = item.find_element(By.CSS_SELECTOR, "span[data-marker='item-price-value']")
                    price = price_element.text.strip() if price_element.text else ""
                except:
                    price = "Цена не найдена или не указана"
                    
                try:
                    title_element = item.find_element(By.CSS_SELECTOR, "h2[itemprop='name']")
                    title = title_element.text.strip() if title_element.text else ""
                except:
                    title = "Заголовок не найден или не указан"
                    
                listings.append({
                    "title": title,
                    "price": price,
                    "link": link
                })
            except Exception as e:
                continue
        return listings
    finally:
        driver.quit()


        

    


        