import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

service_obj =Service("C:/Users/ayers/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe")
driver= webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)
driver.get("https://the-internet.herokuapp.com/windows")
driver.maximize_window()

driver.find_element(By.LINK_TEXT,"Click Here").click()
windowOpened=driver.window_handles
driver.switch_to.window(windowOpened[1])
print(driver.find_element(By.XPATH,"//h3").text)
driver.close()
driver.switch_to.window(windowOpened[0])
print(driver.find_element(By.XPATH,"//h3").text)

assert driver.find_element(By.XPATH,"//h3").text == "Opening a new window"
time.sleep(2)
