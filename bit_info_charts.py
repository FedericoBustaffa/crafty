from selenium import webdriver
from selenium.webdriver.common.by import By
import time


base_url = "https://bitinfocharts.com/bitcoin/address/"
headers = {
    "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    + " (KHTML, like Gecko) Chrome/61.0.3163.100Safari/537.36"
}

driver = webdriver.Chrome()
driver.get(base_url + "15GWLfGNuqbSvP7EqYAvwhEs99vjgUXksC")
smalls = driver.find_elements(By.TAG_NAME, "small")
for s in smalls:
    print(s.text)

driver.quit()
