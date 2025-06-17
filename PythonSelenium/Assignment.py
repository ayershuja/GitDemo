import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

service_obj =Service("C:/Users/ayers/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe")
driver= webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.maximize_window()

driver.find_element(By.LINK_TEXT,"Free Access to InterviewQues/ResumeAssistance/Material").click()
windowOpened=driver.window_handles
driver.switch_to.window(windowOpened[1])
wait=WebDriverWait(driver,10)
wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR,".inner-box h1")))
print(driver.find_element(By.CSS_SELECTOR,".inner-box h1").text)
assert driver.find_element(By.CSS_SELECTOR,".inner-box h1").text == "DOCUMENTS REQUEST"
print("Changed to New Window, New Window assertion passed")

PhraseStr=driver.find_element(By.CSS_SELECTOR,"#interview-material-container p:nth-child(2)").text
SpiltedStr=PhraseStr.split(" ")
print(SpiltedStr)
print(SpiltedStr[4])
Email=SpiltedStr[4]
Pass="password"
#print(driver.find_element(By.CSS_SELECTOR,"#interview-material-container p:nth-child(2)").text)

driver.switch_to.window(windowOpened[0])
wait.until(expected_conditions.visibility_of_element_located((By.ID,"username")))
driver.find_element(By.ID,"username").send_keys(Email)
assert driver.find_element(By.ID,"username").get_attribute('value') == Email
print(Email,"is Entered in Username Field Sucesfully")

driver.find_element(By.ID,"password").send_keys(Pass)
driver.find_element(By.ID,"signInBtn").click()

wait.until(expected_conditions.visibility_of_element_located((By.XPATH,".//div[@class='alert alert-danger col-md-12']")))
message=driver.find_element(By.XPATH,".//div[@class='alert alert-danger col-md-12']").text
assert message == "Incorrect username/password."
print(message)
