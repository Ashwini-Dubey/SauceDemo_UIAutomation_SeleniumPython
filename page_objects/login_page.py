#page_objects/login_page.py
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:


    login_page_username = (By.ID,"user-name")
    login_page_password = (By.ID,"password")
    login_page_login_button = (By.ID,"login-button")

    def __init__(self, driver):
        self.driver = driver

    def enter_email(self):
        return self.driver.find_element(*LoginPage.login_page_username)

    def enter_password(self):
        return self.driver.find_element(*LoginPage.login_page_password)

    def click_login_button(self):
        return self.driver.find_element(*LoginPage.login_page_login_button).click()





