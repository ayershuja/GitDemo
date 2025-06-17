import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

chrome_options=webdriver.ChromeOptions()
chrome_options.add_argument("headless")

service_obj =Service("C:/Users/ayers/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe")
driver= webdriver.Chrome(service=service_obj, options=chrome_options)
driver.implicitly_wait(5)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")
driver.get_screenshot_as_file("screenshot.png")


time.sleep(4)