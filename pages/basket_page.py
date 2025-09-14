from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_basket_page(self):
        self.should_be_text_basket_empty()
        self.should_be_no_items_basket()

    def should_be_text_basket_empty(self):
        assert self.is_element_present(*BasketPageLocators.TEXT_BASKET), \
            "There is no text stating that the basket is empty"

    def should_be_no_items_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.ITEMS_BASKET), \
            "There are items in the basket"
