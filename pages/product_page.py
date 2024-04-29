from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from pages.cart_page import CartPage

class ProductPageLocators:
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, "input[value='Do koszyka']")
    NUMBER_OF_PRODUCTS_IN_THE_CART = (By.XPATH, "//*[@id='shopping_cart']/a/span[2]")
    CART_BTN = (By.XPATH, "//li[@id='shopping_cart']//a[@title='Pokaż mój koszyk']")

class ProductPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def add_to_the_cart(self):
        try:
            add_to_cart_btn = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(ProductPageLocators.ADD_TO_CART_BTN))
            add_to_cart_btn.click()
            # Czas na dodanie produktu do koszyka
            WebDriverWait(self.driver, 20).until(
                lambda driver: driver.find_element(*ProductPageLocators.NUMBER_OF_PRODUCTS_IN_THE_CART).text.strip())
            return True
        except TimeoutException:
            return False

    def is_added_to_cart(self):
        try:
            self.driver.find_element(*ProductPageLocators.NUMBER_OF_PRODUCTS_IN_THE_CART)
            return True
        except NoSuchElementException:
            return False

    def click_cart_btn(self):
        try:
            cart_btn = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(ProductPageLocators.CART_BTN))
            cart_btn.click()
            return CartPage(self.driver)
        except TimeoutException:
            return None
