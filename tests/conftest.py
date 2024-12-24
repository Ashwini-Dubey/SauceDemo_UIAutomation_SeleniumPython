#tests/conftest.py

import pytest
from selenium import webdriver

def pytest_addoption(parser):

    parser.addoption(
        "--browser_name", action="store", default="Chrome"
    )

@pytest.fixture(scope="function")
def browser_setup(request):

    browser_name = request.config.getoption("browser_name").lower()
    if browser_name == "chrome":
        driver = webdriver.Chrome()
    elif browser_name == "firefox":
        driver = webdriver.Firefox()
    elif browser_name == "safari":
        driver = webdriver.Safari()

    driver.get("https://www.saucedemo.com/")
    driver.implicitly_wait(10)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()


