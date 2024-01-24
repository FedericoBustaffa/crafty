from selenium import webdriver
from selenium.webdriver.common.by import By
import time

base_url = "https://bitinfocharts/bitcoin/address/"
headers = {
    "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    + " (KHTML, like Gecko) Chrome/61.0.3163.100Safari/537.36"
}

driver = webdriver.Chrome()
driver.get(base_url + "1257To3UPv8yDWaz23jovVCTTEJNi5NpRc")
time.sleep(5)
driver.quit()
