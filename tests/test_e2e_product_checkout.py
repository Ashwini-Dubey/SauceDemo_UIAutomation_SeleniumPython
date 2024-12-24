#tests/test_login.py

import pytest

from ..page_objects.checkout_page import CheckoutPage
from ..utilities.base_class import BaseClass
from ..page_objects.login_page import LoginPage
from ..page_objects.products_page import ProductsPage
from ..test_data.login_page_data import LoginPageData
from ..test_data.checkout_page_data import CheckoutPageData



class TestProducts(BaseClass):

    def test_products(self,login_data,checkout_data):
        log = self.get_logger()
        log.info("Initiating the Products Page for SauceDemo")

        products_page = ProductsPage(self.driver)
        checkout_page = CheckoutPage(self.driver)

        log.info("Initiating the login")
        self.user_login(login_data["Username"], login_data["Password"])
        log.info("Getting the list of all the products")
        products_page.product_page_get_products()
        log.info("Adding the product to the cart")
        products_page.product_page_add_products()
        log.info("Check cart with the added product")
        products_page.click_products_page_cart_icon()
        assert "cart.html" in self.driver.current_url
        log.info("Checking out the added product")
        checkout_page.checkout_click_checkout_added_product()
        log.info("Checkout Step 1")
        checkout_page.checkout_information_fname().send_keys(checkout_data["FirstName"])
        checkout_page.checkout_information_lname().send_keys(checkout_data["LastName"])
        checkout_page.checkout_information_postal().send_keys(checkout_data["PostalCode"])
        checkout_page.checkout_step_one_click_continue_button()
        log.info("Checkout Step 2")
        checkout_page.checkout_step_two_click_finish()
        log.info("Final Stage of checkout")
        checkout_page.checkout_order_success()


    @pytest.fixture(params=LoginPageData.login_page_data)
    def login_data(self, request):
        return request.param

    @pytest.fixture(params=CheckoutPageData.checkout_page_data)
    def checkout_data(self, request):
        return request.param




