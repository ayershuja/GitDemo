import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj =Service("C:/Users/ayers/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe")
driver= webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/client")
driver.maximize_window()
driver.find_element(By.LINK_TEXT,"Forgot password?").click()
driver.find_element(By.XPATH,"//input[@type='email']").send_keys("demo@gmail.com")
driver.find_element(By.CSS_SELECTOR,"form div:nth-child(2) input").send_keys("Hello@1234")
driver.find_element(By.CSS_SELECTOR,"#confirmPassword").send_keys("Hello@1234")
driver.find_element(By.CSS_SELECTOR,"form div:nth-child(4) button").click()



time.sleep(2)