
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
#import time

chrome_options = Options()

chrome_options.add_argument("--headless")
chrome_options.add_argument("--start-maximized");

url = "https://gtiit-grades.technion.ac.il/"
path = "chromedriver.exe"
driver = webdriver.Chrome(executable_path=path)
driver.get(url)

driver.implicitly_wait(40)

driver.find_element(By.ID, "username").send_keys("yang.bai")
driver.find_element(By.ID, "password").send_keys("Origin949491")

login = driver.find_element(By.ID, "tsc_send")
login.click()

driver.implicitly_wait(40)
h = driver.page_source
f=open('./2.html',mode="w",encoding="utf-8")

f.write(h)




