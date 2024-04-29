from tests.base_test import BaseTest

class CartTest(BaseTest):
    def setUp(self):
        super().setUp()

    def test_add_to_the_cart(self):
        """
        # TC4 Testing add a product to the cart
        """
        # KROKI
        # Kliknij "PROMOCJE" w menu głównym
        self.promotions_page = self.home_page.click_promotions_link()
        # Kliknij w losowo wybrany produkt
        self.product_page = self.promotions_page.choose_product(self)
        # Dodaj wybrany produkt do koszyka
        while not self.product_page.add_to_the_cart():
            # Jeśli wybrany produkt nie jest dostępny wróć do poprzedniej strony
            self.driver.back()
            # Wybierz ponownie produkt
            self.product_page = self.promotions_page.choose_product(self)
        # Sprawdź czy produkt został dodany do koszyka
        self.assertTrue(self.product_page.is_added_to_cart())

    def test_remove_from_the_cart(self):
        """
        TC5 Removing a product from the cart
        :return:
        """
        # KROKI
        # Kliknij "PROMOCJE" w menu głównym
        self.promotions_page = self.home_page.click_promotions_link()
        # Kliknij w losowo wybrany produkt
        self.product_page = self.promotions_page.choose_product(self)
        # Dodaj wybrany produkt do koszyka
        while not self.product_page.add_to_the_cart():
            # Jeśli wybrany produkt nie jest dostępny wróć do poprzedniej strony
            self.driver.back()
            # Wybierz ponownie produkt
            self.product_page = self.promotions_page.choose_product(self)
        # Przejdź do strony koszyka
        self.cart_page = self.product_page.click_cart_btn()
        # Kliknij ikonę kosza na śmieci
        self.cart_page.remove_product()
        # Odśwież stronę
        self.driver.refresh()
        # Sprawdź czy produkt został usunięty z koszyka zakupowego
        message_text = self.cart_page.verify_message()
        self.assertEqual("Twój koszyk jest pusty.", message_text)








