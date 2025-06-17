import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj =Service("C:/Users/ayers/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe")
driver= webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR,"input[name='name']").send_keys("Ayer Shuja")
driver.find_element(By.XPATH,"//*[@name='email']").send_keys("ayer.shuja@gmail.com")
driver.find_element(By.ID,"exampleInputPassword1").send_keys("ayersh")
driver.find_element(By.CSS_SELECTOR,"#inlineRadio1").click()

#Static Dropdown
Dropdown=Select(driver.find_element(By.ID,"exampleFormControlSelect1"))
Dropdown.select_by_index(1)
Dropdown.select_by_visible_text("Male")


driver.find_element(By.ID,"exampleCheck1").click()
driver.find_element(By.XPATH,"(//input[@name='name'])[2]").click()

driver.find_element(By.XPATH,"//*[@type='submit']").click()
message=driver.find_element(By.CLASS_NAME,"alert-dismissible").text



print(message)

assert "Success" in message

time.sleep(2)