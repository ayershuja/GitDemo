from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait



from pageObjects.checkout_confirmation import Checkout_Confirmation


class ShopPage:

    def __init__(self,driver):
        self.driver=driver
        self.shop_link= (By.XPATH, "//a[contains(text(),'Shop')]")
        self.product_cart= (By.XPATH, "//div[@class='card h-100']")
        self.checkout_button= (By.CSS_SELECTOR, "a[class*='btn-primary']")


    def add_product_to_cart(self,Productname):

        self.driver.find_element(*self.shop_link).click()

        # Collect Information of Product
        products = self.driver.find_elements(*self.product_cart)
        print(len(products))

        for phone in products:
            print(phone.text)
            product_name = phone.find_element(By.XPATH, "div/h4/a").text

            if product_name == Productname:
                phone.find_element(By.XPATH, "div/button").click()

    def gotoCart(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "a[class*='btn-primary']")))
        self.driver.find_element(*self.checkout_button).click()
        checkout_confirmation=Checkout_Confirmation(self.driver)
        return checkout_confirmation