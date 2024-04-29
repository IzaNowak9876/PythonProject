from ddt import ddt, data, unpack
from data import registration_data
from tests.base_test import BaseTest

@ddt
class SearchTest(BaseTest):

    def setUp(self):
        super().setUp()

    @data(*registration_data.get_csv_data("C:\\Users\\izabe\\PycharmProjects\\pythonProject_Nowak\\data\\search_product.csv"))
    @unpack
    def test_search_product_by_name(self, product_name):
        """
        TC6 Testing product search by name
        :return:
        """
        # KROKI
        # Skroluj stronę w dół
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # Kliknij w okno "Szukaj"
        # Wpisz szukaną frazę
        self.home_page.enter_product_name(product_name)
        # Kliknij ikonę lupki
        self.search_page = self.home_page.click_search_btn()
        # Sprawdź wyniki wyszukiwania
        self.search_page.get_search_results_attributes()



