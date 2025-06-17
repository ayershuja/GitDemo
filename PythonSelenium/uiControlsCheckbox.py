import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj =Service("C:/Users/ayers/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe")
driver= webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()


CheckboxExample=driver.find_elements(By.XPATH,"//div[@id='checkbox-example']//input[@type='checkbox']")

print(len(CheckboxExample))

for checkbox in CheckboxExample:
    if checkbox.get_attribute("value") =="option2":
        checkbox.click()
        assert checkbox.is_selected()
        break



time.sleep(2)