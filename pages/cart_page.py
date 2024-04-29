from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC

class CartPageLocators:
    CART_PRODUCT_ITEMS = (By.XPATH, "(//tbody)[2]//tr")  # Lokator dla wszystkich produktów w koszyku
    MESSAGE_AT_THE_CART = (By.XPATH, "//p[@class='warning']")

class CartPage(BasePage):
    def remove_product(self):
        # Znajdź wszystkie elementy produktów w koszyku
        product_elements = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_all_elements_located(CartPageLocators.CART_PRODUCT_ITEMS))
        # Kliknij w przycisk usunięcia pierwszego produktu z listy
        if product_elements:
            first_product_delete_button = product_elements[0].find_element(
                By.CSS_SELECTOR,"body > div:nth-child(4) > div:nth-child(2) > div:nth-child(1) > div:nth-child(5) > "
                                "table:nth-child(1) > tbody:nth-child(4) > tr:nth-child(1) > td:nth-child(6) > "
                                "div:nth-child(1) > a:nth-child(1)")
            first_product_delete_button.click()
        return product_elements

    def verify_message(self):
        message_element = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(CartPageLocators.MESSAGE_AT_THE_CART))
        message_text = message_element.text
        return message_text