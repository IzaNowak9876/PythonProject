from data import registration_data
from ddt import ddt, data, unpack
from tests.base_test import BaseTest

@ddt
class RegistrationTest(BaseTest):

    def setUp(self):
        super().setUp()

    def test_enter_wrong_email(self):
        """"
        TC1 User enter wrong email
        """
        # KROKI
        # Kliknij "Rejestracja"
        self.registration_page = self.home_page.click_registration_link()
        # Wpisz błędny email
        # Kliknij "Zarejestruj się"
        self.create_account_page = self.registration_page.enter_wrong_email_and_click_register()
        # Sprawdź poprawność komunikatu
        self.assertEqual("Nieprawidłowy adres e-mail", self.registration_page.verify_errors()[0])

    @data(*registration_data.get_csv_data(
        "C:\\Users\\izabe\\PycharmProjects\\pythonProject_Nowak\\data\\registration.csv"))
    @unpack
    def test_no_last_name_ddt(self, first_name, last_name, email, phone_number, password):
        """
        TC2 User does not enter last name
        """
        # KROKI
        # Kliknij "Rejestracja"
        self.registration_page = self.home_page.click_registration_link()
        # Wpisz poprawny adres email
        # Kliknij "Zarejestruj się"
        self.create_account_page = self.registration_page.enter_email_and_click_register(email)
        # Uzupełnij poprawnie pole "Imię"
        self.create_account_page.enter_first_name(first_name)
        # Sprawdź poprawność adresu email
        self.assertEqual(email, self.create_account_page.get_email())
        # Uzupełnij poprawnie pole "Telefon"
        self.create_account_page.enter_phone_number(phone_number)
        # Uzupełnij poprawnie pole "Hasło"
        self.create_account_page.enter_password(password)
        # Kliknij "Zarejestruj się"
        self.create_account_page.click_register_btn()
        # Sprawdź komunikat
        self.assertEqual("Nazwisko jest wymagane.", self.create_account_page.verify_errors()[0])

    @data(*registration_data.get_csv_data(
        "C:\\Users\\izabe\\PycharmProjects\\pythonProject_Nowak\\data\\registration.csv"))
    @unpack
    def test_wrong_password_ddt(self, first_name, last_name, email, phone_number, password):
        """
        TC3 User does not enter password
        :param first_name:
        :param last_name:
        :param email:
        :param phone_number:
        :param password:
        :return:
        """
        # KROKI
        # Kliknij "Rejestracja"
        self.registration_page = self.home_page.click_registration_link()
        # Wpisz poprawny adres email
        # Kliknij "Zarejestruj się"
        self.create_account_page = self.registration_page.enter_email_and_click_register(email)
        # Uzupełnij poprawnie pole "Imię"
        self.create_account_page.enter_first_name(first_name)
        # Uzupełnij poprawnie pole "Nazwisko"
        self.create_account_page.enter_last_name(last_name)
        # Sprawdź poprawność adresu email
        self.assertEqual(email, self.create_account_page.get_email())
        # Uzupełnij poprawnie pole "Telefon"
        self.create_account_page.enter_phone_number(phone_number)
        # Uzupełnij błędne hasło (mniej niż 5 znaków)
        self.create_account_page.enter_wrong_password(password)
        # Kliknij "Zarejestruj się"
        self.create_account_page.click_register_btn()
        # Sprawdź komunikat
        self.assertEqual("Hasło jest nieprawidłowe.", self.create_account_page.verify_password()[0])

    def test_no_first_name(self):
        pass

    def test_no_phone_number(self):
        pass












