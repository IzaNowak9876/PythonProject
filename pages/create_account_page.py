from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import text_to_be_present_in_element
from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class CreateAccountPageLocators:
    FIRST_NAME_TEXTBOX = (By.ID, "customer_firstname")
    LAST_NAME_TEXTBOX = (By.ID, "customer_lastname")
    PHONE_TEXTBOX = (By.ID, "phone")
    EMAIL_TEXTBOX = (By.XPATH, "/html/body/div[2]/div[2]/div[2]/div/form/fieldset/p[3]/input")
    PASSWORD_TEXTBOX = (By.XPATH, "/html/body/div[2]/div[2]/div[2]/div/form/fieldset/p[5]/input")
    REGISTER_BTN = (By.ID, "submitAccount")
    USER_ERROR_MESSAGES = (By.XPATH, "//div[@class='error']//li[1]")
    PASSWORD_MESSAGE = (By. XPATH, '//*[@id="center_column"]/div/ol/li')

class CreateAccountPage(BasePage):
    def enter_first_name(self, first_name):
        el = self.driver.find_element(*CreateAccountPageLocators.FIRST_NAME_TEXTBOX)
        el.send_keys(first_name)

    def enter_last_name(self, last_name):
        el = self.driver.find_element(*CreateAccountPageLocators.LAST_NAME_TEXTBOX)
        el.send_keys(last_name)

    def get_email(self):
        (WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(CreateAccountPageLocators.EMAIL_TEXTBOX)))
        el = self.driver.find_element(*CreateAccountPageLocators.EMAIL_TEXTBOX)
        return el.get_attribute("value")

    def enter_phone_number(self, phone_number):
        el = self.driver.find_element(*CreateAccountPageLocators.PHONE_TEXTBOX)
        el.send_keys(phone_number)

    def enter_password(self, password):
        el = self.driver.find_element(*CreateAccountPageLocators.PASSWORD_TEXTBOX)
        el.send_keys(password)

    def enter_wrong_password(self, wrong_password):
        el = self.driver.find_element(*CreateAccountPageLocators.PASSWORD_TEXTBOX)
        el.send_keys("1234")

    def click_register_btn(self):
        self.driver.find_element(*CreateAccountPageLocators.REGISTER_BTN).click()

    def verify_errors(self):
        errors = self.driver.find_elements(*CreateAccountPageLocators.USER_ERROR_MESSAGES)
        WebDriverWait(self.driver, 20).until(
            text_to_be_present_in_element((By.XPATH, "//div[@class='error']//li[1]"),
                                          "Nazwisko jest wymagane."))
        errors_texts = [e.text for e in errors]
        return errors_texts

    def verify_password(self):
        errors = self.driver.find_elements(*CreateAccountPageLocators.PASSWORD_MESSAGE)
        WebDriverWait(self.driver, 20).until(
            text_to_be_present_in_element((By.XPATH, '//*[@id="center_column"]/div/ol/li'),
                                          "Hasło jest nieprawidłowe."))
        errors_texts = [e.text for e in errors]
        return errors_texts



