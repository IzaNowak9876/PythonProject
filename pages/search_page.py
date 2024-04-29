from selenium.webdriver.support.expected_conditions import text_to_be_present_in_element
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class SearchPageLocators:
    SEARCH_RESULTS = (By.XPATH, "//ul[@id='product_list']")

class SearchPage(BasePage):
    def get_search_results_attributes(self):
        WebDriverWait(self.driver, 20).until(
            text_to_be_present_in_element((By.XPATH, "//h1[normalize-space()='Wyniki wyszukiwania']"),
                                          "WYNIKI WYSZUKIWANIA"))

        results = self.driver.find_elements(*SearchPageLocators.SEARCH_RESULTS)
        image_attributes = []

        for result in results:
            image_src = result.get_attribute('src')
            image_alt = result.get_attribute('alt')
            image_attributes.append({'src': image_src, 'alt': image_alt})
        return image_attributes

