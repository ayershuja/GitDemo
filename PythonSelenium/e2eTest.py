import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

service_obj =Service("C:/Users/ayers/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe")
driver= webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
driver.implicitly_wait(4)


#Click on Shop
driver.find_element(By.XPATH,"//a[contains(text(),'Shop')]").click()


#Collect Information of Product
products=driver.find_elements(By.XPATH,"//div[@class='card h-100']")
print(len(products))

for phone in products:
    print(phone.text)
    product_name=phone.find_element(By.XPATH,"div/h4/a").text

    if product_name=="Blackberry":
        phone.find_element(By.XPATH,"div/button").click()


#Click on checkout page
wait=WebDriverWait(driver,10)
wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR,"a[class*='btn-primary']")))
driver.find_element(By.CSS_SELECTOR,"a[class*='btn-primary']").click()


#checkout
driver.find_element(By.XPATH,"//*[@class='btn btn-success']").click()

#Location
driver.find_element(By.ID,"country").send_keys("Ind")
wait.until(expected_conditions.visibility_of_element_located((By.LINK_TEXT,"India")))
driver.find_element(By.LINK_TEXT,"India").click()

#Click on checkbox for "I Agree"
wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//div[@class='checkbox checkbox-primary']")))
driver.find_element(By.XPATH,"//div[@class='checkbox checkbox-primary']").click()

#Click on purchase
driver.find_element(By.CSS_SELECTOR,"input[type='submit']").click()

#Validation
sucess_Message=driver.find_element(By.CSS_SELECTOR,"input[class*='btn-success']").text
wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR,"input[class*='btn-success']")))
assert sucess_Message in "Success! Thank you!"


