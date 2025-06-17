import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

service_obj =Service("C:/Users/ayers/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe")
driver= webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()

driver.find_element(By.CSS_SELECTOR,".search-keyword").send_keys("ber")
time.sleep(2)

#Validation: List showing same
ExpectedList=['Cucumber - 1 Kg','Raspberry - 1/4 Kg','Strawberry - 1/4 Kg']
Actuallist=[]

results=driver.find_elements(By.XPATH,"//*[@class='products']/div")
print(len(results))
count= len(results)
assert count >0
for result in results:
    Actuallist.append(result.find_element(By.XPATH, "h4").text)
    result.find_element(By.XPATH,"div/button").click()

assert Actuallist == ExpectedList

driver.find_element(By.CSS_SELECTOR,"img[alt='Cart']").click()
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()


#Sum Validation

prices=driver.find_elements(By.XPATH,".//table[@id='productCartTables']//td[5]/p")
sum=0

for price in prices:
    sum= sum+int(price.text)

print(sum)

totalAmount= int(driver.find_element(By.CSS_SELECTOR,".totAmt").text)
print(totalAmount)

assert sum == totalAmount

driver.find_element(By.CSS_SELECTOR,".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR,".promoBtn").click()
wait=WebDriverWait(driver,10)
wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR,".promoInfo")))
print(driver.find_element(By.CSS_SELECTOR,".promoInfo").text)
assert driver.find_element(By.CSS_SELECTOR,".promoInfo").text== "Code applied ..!"


#Validation :Total After Discount amount less than Total Amount

discountedPrice=float(driver.find_element(By.CSS_SELECTOR,".discountAmt").text)
assert discountedPrice < totalAmount