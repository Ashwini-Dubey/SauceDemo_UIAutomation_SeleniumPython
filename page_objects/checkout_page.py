from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class CheckoutPage:

    checkout_page_product_name = (By.XPATH,"//div[@class='inventory_item_name']")
    checkout_page_checkout_button = (By.ID,"checkout")
    checkout_page_information_fname = (By.ID,"first-name")
    checkout_page_information_lname = (By.ID, "last-name")
    checkout_page_information_postal = (By.ID, "postal-code")
    checkout_page_step_one_continue_button = (By.ID,"continue")
    checkout_page_step_two_finish_button = (By.ID,"finish")
    checkout_page_success_order = (By.XPATH,"//h2[text()='Thank you for your order!']")

    def __init__(self, driver):
        self.driver = driver

    def checkout_click_checkout_added_product(self):
        ##assert "Backpack" in CheckoutPage.checkout_page_product_name
        return self.driver.find_element(*CheckoutPage.checkout_page_checkout_button).click()

    def checkout_information_fname(self):
        assert "checkout" in self.driver.current_url
        return self.driver.find_element(*CheckoutPage.checkout_page_information_fname)

    def checkout_information_lname(self):
        return self.driver.find_element(*CheckoutPage.checkout_page_information_lname)

    def checkout_information_postal(self):
        return self.driver.find_element(*CheckoutPage.checkout_page_information_postal)

    def checkout_step_one_click_continue_button(self):
        return self.driver.find_element(*CheckoutPage.checkout_page_step_one_continue_button).click()

    def checkout_step_two_click_finish(self):
        assert "checkout-step-two.html" in self.driver.current_url
        return self.driver.find_element(*CheckoutPage.checkout_page_step_two_finish_button).click()

    def checkout_order_success(self):
        assert "checkout-complete" in self.driver.current_url
        success_message = WebDriverWait(self.driver,10).until(EC.presence_of_element_located(CheckoutPage.checkout_page_success_order))

        assert "Thank you for your order" in success_message.text


