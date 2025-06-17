import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# if we wanna use VPN and dont wanna update chrome browser automatically, we can use Service class




driver= webdriver.Firefox()
driver.get("https://rahulshettyacademy.com")
driver.maximize_window()
print(driver.title)
print(driver.current_url)






time.sleep(2)