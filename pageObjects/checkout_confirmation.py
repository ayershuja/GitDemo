from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Checkout_Confirmation:
        def __init__(self, driver):
            self.driver=driver
            self.checkout_button= (By.XPATH, "//*[@class='btn btn-success']")
            self.country_input = (By.ID, "country")
            self.country_option = (By.XPATH, "//*[@class='suggestions']//li[1]/a")
            self.checkboxes = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
            self.submit_button = (By.CSS_SELECTOR, "input[type='submit']")
            self.success_message = (By.CSS_SELECTOR, "input[class*='btn-success']")


        def checkout(self):
            self.driver.find_element(*self.checkout_button).click()

        def enter_deliver_address(self,countryName):
            wait = WebDriverWait(self.driver, 10)
            self.driver.find_element(*self.country_input).send_keys(countryName)
            wait.until(expected_conditions.visibility_of_element_located(self.country_option))
            self.driver.find_element(*self.country_option).click()
            wait.until(expected_conditions.visibility_of_element_located(self.checkboxes))
            self.driver.find_element(*self.checkboxes).click()
            self.driver.find_element(*self.submit_button).click()

        def validate_order(self):
            wait = WebDriverWait(self.driver, 10)
            sucess_Message = self.driver.find_element(*self.success_message).text
            wait.until(expected_conditions.visibility_of_element_located(self.success_message))
            assert sucess_Message in "Success! Thank you!"