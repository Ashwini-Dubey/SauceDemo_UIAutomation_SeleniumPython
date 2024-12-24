#utilities/base_class.py
import logging
import inspect
import pytest
from ..page_objects.login_page import LoginPage

@pytest.mark.usefixtures("browser_setup")
class BaseClass:

    def get_logger(self):

        logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_name)
        file_handler = logging.FileHandler("../logs/log_file.log")
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        logger.setLevel(logging.DEBUG)
        return logger

    def user_login(self,username,password):
        log = self.get_logger()
        log.info(f"Attempting to log in with username: {username}")

        login_page = LoginPage(self.driver)
        login_page.enter_email().send_keys(username)
        login_page.enter_password().send_keys(password)
        login_page.click_login_button()

        log.info("Login action performed.")






