from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import BasePage
from pages.promotions_page import PromotionsPage
from pages.registration_page import RegistrationPage
from selenium.webdriver.common.by import By
from pages.search_page import SearchPage

class HomePageLocators:
    REGISTRATION_LINK = (By.CLASS_NAME, "top2")
    SEARCH_INPUT = (By.ID, "search_query_block")
    SEARCH_BTN = (By.ID, "search_button")
    PROMOTIONS_LINK = (By.XPATH, "//a[@title='Promocje']")
    NEWSLETTER_INPUT = (By.XPATH, "//input[@value='Wpisz swój adres e-mail...']")
    NEWSLETTER_BTN = (By.XPATH, "//input[@name='submitNewsletter']")
    MESSAGE_TXT = (By. XPATH, "//span[@class='newsletter_inline warning_inline']")

class HomePage(BasePage):
    def click_registration_link(self):
        el = self.driver.find_element(*HomePageLocators.REGISTRATION_LINK)
        registration_link_locator = HomePageLocators.REGISTRATION_LINK
        WebDriverWait(self.driver, 20).until(
            expected_conditions.element_to_be_clickable(registration_link_locator))
        el.click()
        return RegistrationPage(self.driver)

    def enter_product_name(self, product_name):
        search_field = WebDriverWait(self.driver,20).until(
            EC.presence_of_element_located((By.ID, "search_query_block")))
        search_field.send_keys(product_name)

    def click_search_btn(self):
        search_btn_locator = HomePageLocators.SEARCH_BTN
        search_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(search_btn_locator))
        search_button.click()
        return SearchPage(self.driver)

    def click_promotions_link(self):
        el = self.driver.find_element(*HomePageLocators.PROMOTIONS_LINK)
        el.click()
        return PromotionsPage

    def enter_email(self, email):
        el = self.driver.find_element(*HomePageLocators.NEWSLETTER_INPUT)
        el.send_keys(email)

    def click_newsletter_btn(self):
        el = self.driver.find_element(*HomePageLocators.NEWSLETTER_BTN)
        el.click()

    def verify_message(self):
        message = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(HomePageLocators.MESSAGE_TXT))
        return message.text

