#tests/test_login.py

import pytest

from ..utilities.base_class import BaseClass
from ..page_objects.login_page import LoginPage
from ..page_objects.products_page import ProductsPage
from ..test_data.login_page_data import LoginPageData



class TestLogin(BaseClass):


    def test_login(self,login_data):

        log = self.get_logger()
        log.info("Initiating the login for SauceDemo")

        self.user_login(login_data["Username"], login_data["Password"])

        if login_data["Username"] == "locked_out_user":
            assert not "inventory.html" in self.driver.current_url
            log.info("Login failed for locked_out_user")
        else :
            assert "inventory.html" in self.driver.current_url
            log.info(f"Login successful for {login_data["Username"]}")

    @pytest.fixture(params=LoginPageData.login_page_data)
    def login_data(self,request):
        return request.param


