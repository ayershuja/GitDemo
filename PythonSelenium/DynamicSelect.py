import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj =Service("C:/Users/ayers/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe")
driver= webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.maximize_window()

driver.find_element(By.ID,"autosuggest").send_keys("Uni")
time.sleep(2)
countries= driver.find_elements(By.CSS_SELECTOR,"li[class='ui-menu-item'] a")


for country in countries:
    if country.text=="United States (USA)":
        country.click()
        break
assert driver.find_element(By.ID,"autosuggest").get_attribute("value") == "United States (USA)"

#assert "United States (USA)" in verify_country

time.sleep(2)