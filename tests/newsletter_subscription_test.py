from data.newsletter_data import NewsletterData
from tests.base_test import BaseTest

class NewsletterSubscriptionTest(BaseTest):
    def setUp(self):
        super().setUp()
        self.data = NewsletterData()

    def test_newsletter_subscription(self):
        """
        TC7 User signs up for the newsletter
        :return:
        """
        # KROKI
        # Skroluj stronę w dół
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # Wpisz adres email w polu newsletter
        self.home_page.enter_email(self.data.newsletter_email)
        # Kliknij wyślij
        self.home_page.click_newsletter_btn()
        # Odśwież stronę
        self.driver.refresh()
        # Skroluj stronę w dół
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # Sprawdź komunikat
        message = self.home_page.verify_message()
        # Sprawdź czy wiadomość jest jedną z oczekiwanych
        self.assertIn(message, ["Zarejestrowano do subskrypcji", "Ten email już jest w bazie"])

