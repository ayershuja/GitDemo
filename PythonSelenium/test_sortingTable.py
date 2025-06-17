
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

def test_sort(browserInstance):
    driver= browserInstance
    BrowserSortedList = []

    driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
    driver.maximize_window()

    # Click on column header
    driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()

    VeggeElement = driver.find_elements(By.XPATH, "//tr/td[1]")

    for element in VeggeElement:
        print(element.text)
        BrowserSortedList.append(element.text)

    originalSortedList = BrowserSortedList.copy()

    BrowserSortedList.sort()

    assert originalSortedList == BrowserSortedList

    print(originalSortedList)
    print(BrowserSortedList)
