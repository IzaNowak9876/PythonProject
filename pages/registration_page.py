from selenium.webdriver.support.expected_conditions import text_to_be_present_in_element
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import BasePage
from pages.create_account_page import CreateAccountPage
from selenium.webdriver.common.by import By

class RegistrationPageLocators:
    EMAIL_TEXTBOX = (By.ID, "email_create")
    SUBMIT_CREATE_BTN = (By.ID, "SubmitCreate")
    USER_ERROR_MESSAGES = (By.XPATH, "//div[@class='error']//li[1]")

class RegistrationPage(BasePage):
    def enter_wrong_email_and_click_register(self):
        self.driver.find_element(*RegistrationPageLocators.EMAIL_TEXTBOX).send_keys("iza_janas.op.pl")
        self.driver.find_element(*RegistrationPageLocators.SUBMIT_CREATE_BTN).click()
        error = self.driver.find_element(*RegistrationPageLocators.USER_ERROR_MESSAGES)
        return error

    def enter_email_and_click_register(self, email):
        self.driver.find_element(*RegistrationPageLocators.EMAIL_TEXTBOX).send_keys(email)
        self.driver.find_element(*RegistrationPageLocators.SUBMIT_CREATE_BTN).click()
        return CreateAccountPage(self.driver)

    def verify_errors(self):
        errors = self.driver.find_elements(*RegistrationPageLocators.USER_ERROR_MESSAGES)
        WebDriverWait(self.driver, 30).until(
            text_to_be_present_in_element((By.XPATH, "//div[@class='error']//li[1]"),
                                          "Nieprawidłowy adres e-mail"))
        errors_texts = [e.text for e in errors]
        return errors_texts
