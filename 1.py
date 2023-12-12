import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

name = []

with open("people.csv", "r") as file:
    next(file)  # Skip header
    for line in file:
        row = line.rstrip().split(",")
        name.append(row)

url = "https://emn178.github.io/online-tools/crc32.html"
driver.get(url)
time.sleep(2) 


driver.quit()