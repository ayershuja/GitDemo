from selenium.webdriver.common.by import By

from pageObjects.shop import ShopPage


class LoginPage:
    def __init__(self,driver):
      self.driver=driver
      self.username_input=  (By.ID, "username")
      self.password_input= (By.ID, "password")
      self.login_button= (By.ID, "signInBtn")


    def login(self,username,password):
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.login_button).click()
        Shop_page = ShopPage(self.driver)
        return Shop_page


    def getTitle(self):
        return self.driver.title