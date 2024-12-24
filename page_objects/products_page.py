#page_objects/products_page.py
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductsPage:

    products_page_products_list = (By.XPATH, "//div/div/div[@class='inventory_item_label']")
    products_page_products_add_to_cart_button = (By.XPATH,"//div/div/div/div/div/button[text()='Add to cart']")
    products_page_products_remove_button = (By.XPATH, "//div/div/div/div/div/button[text()='Remove']")
    products_page_cart_icon = (By.CSS_SELECTOR,".shopping_cart_link")

    def __init__(self, driver):
        self.driver = driver

    def product_page_get_products(self):
        productsList= self.driver.find_elements(*ProductsPage.products_page_products_list)
        print(productsList)

    def product_page_add_products(self):
        productsList= self.driver.find_elements(*ProductsPage.products_page_products_list)
        for products in productsList:
            if products.text == "Backpack":
                ProductsPage.products_page_products_add_to_cart_button.click()
                assert "Remove" in ProductsPage.products_page_products_remove_button.text
                break

    def click_products_page_cart_icon(self):
        return self.driver.find_element(*ProductsPage.products_page_cart_icon).click()










