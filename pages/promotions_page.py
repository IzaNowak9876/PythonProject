from random import random
from time import sleep
import random
import time
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.product_page import ProductPage

class PromotionsPageLocators:
    PRODUCTS = (By.XPATH, "//ul[@id='product_list']/li")

class PromotionsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def choose_product(self):
        products = self.driver.find_elements(*PromotionsPageLocators.PRODUCTS)

        if products:
            # Wybierz losowy produkt
            random.seed(time.time())
            random_product = random.choice(products)
            # Kliknij w wybrany produkt
            random_product.click()
            # Poczekaj na załadowanie strony produktu
            sleep(2)
            # Zwróć stronę produktu
            return ProductPage(self.driver)
        else:
            print("Nie znaleziono produktów na stronie promocji.")
            return None
