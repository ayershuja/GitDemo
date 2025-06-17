import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj =Service("C:/Users/ayers/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe")
driver= webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

radioBtns=driver.find_elements(By.CSS_SELECTOR,"div[id='radio-btn-example'] input[type='radio']")

print(len(radioBtns))

radioBtns[1].click()
assert radioBtns[1].is_selected()

for radioBtn in radioBtns:
    if radioBtn.get_attribute("value") =="radio3":
        radioBtn.click()
        assert radioBtn.is_selected()
        break

assert driver.find_element(By.ID,"displayed-text").is_displayed()
driver.find_element(By.ID,"hide-textbox").click()
assert not driver.find_element(By.ID,"displayed-text").is_displayed()





time.sleep(2)
