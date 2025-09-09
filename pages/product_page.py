from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def go_to_add_basket(self):
        add_basket = self.browser.find_element(*ProductPageLocators.BTN_ADD_BASKET)
        add_basket.click()

    def should_be_add_basket(self):
        assert self.is_element_present(*ProductPageLocators.BTN_ADD_BASKET), \
            "Adding to the cart from the product page is not working"
