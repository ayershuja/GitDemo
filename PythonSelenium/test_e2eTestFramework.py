import json
import os
import sys
import time

import pytest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pageObjects.shop import ShopPage
from pageObjects.login import LoginPage
test_data_path='../data/test_e2eTestFramework.json'

with open(test_data_path) as f:
    test_data=json.load(f)
    test_list=test_data["data"]


@pytest.mark.smoke
@pytest.mark.parametrize("test_list_item",test_list)
def test_e2e(browserInstance,test_list_item):
    driver=browserInstance
    driver.get("https://rahulshettyacademy.com/loginpagePractise/")
    driver.maximize_window()
    #Login
    loginPage=LoginPage(driver)
    time.sleep(5)
    Shop_page=loginPage.login(test_list_item["userEmail"],test_list_item["userPassword"])
    # Click on Shop
    Shop_page.add_product_to_cart(test_list_item["productName"])
    # Click on checkout page
    checkout_confirmation=Shop_page.gotoCart()
    # checkout
    checkout_confirmation.checkout()
    checkout_confirmation.enter_deliver_address(test_list_item["deliveryAddress"])
    checkout_confirmation.validate_order()

