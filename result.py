import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

name = []

with open("people.csv", "r") as file:
    next(file)  
    for line in file:
        row = line.rstrip().split(",")
        name.append(row[0]) 

def get_crc32_hash(text):
    driver.get("https://emn178.github.io/online-tools/crc32.html")
    time.sleep(2)

    input_element = driver.find_element("id", "inputText")
    input_element.clear()
    input_element.send_keys(text)

    crc32_button = driver.find_element("id", "crc32")
    crc32_button.click()

    time.sleep(2)
    result_element = driver.find_element("id", "result")
    return result_element.text

salaries_df = pd.read_excel("salary.xlsx", sheet_name="Sheet1")

total_salaries = []

for person in name:
    crc32_hash = get_crc32_hash(person)
    person_entry = salaries_df[salaries_df['A'] == crc32_hash]
    if not person_entry.empty:
        total_salary = person_entry['B'].sum() 
        total_salaries.append((person, total_salary))

for person, total_salary in total_salaries:
    print(f"{person}: Total Salary = {total_salary}")

driver.quit()