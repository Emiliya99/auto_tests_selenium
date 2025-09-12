from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def go_to_add_basket(self):
        self.should_be_add_basket()
        btn_add_basket = self.browser.find_element(*ProductPageLocators.BTN_ADD_BASKET)
        btn_add_basket.click()
        # self.solve_quiz_and_get_code()
        self.should_be_product_main()

    def should_be_add_basket(self):
        assert self.is_element_present(*ProductPageLocators.BTN_ADD_BASKET), \
            "Adding to the cart from the product page is not working"

    def should_be_product_main(self):
        assert self.is_element_present(*ProductPageLocators.NAME_PRODUCT), "Name product not found"
        assert self.is_element_present(*ProductPageLocators.MSG_NAME_PRODUCT), "The message with the product name was not found"
        name_product = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT).text
        msg_name_product = self.browser.find_element(*ProductPageLocators.MSG_NAME_PRODUCT).text
        assert name_product == msg_name_product, "The product names don't match"

        assert self.is_element_present(*ProductPageLocators.PRICE_PRODUCT), "Price product not found"
        assert self.is_element_present(*ProductPageLocators.MSG_PRICE_PRODUCT), "The message with the product price was not found"
        price_product = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT).text
        msg_price_product = self.browser.find_element(*ProductPageLocators.MSG_NAME_PRODUCT).text
        assert price_product == msg_price_product, "The product price don't match"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.MSG_NAME_PRODUCT), \
            "Success message is presented, but should not be"

    def should_be_message_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.MSG_NAME_PRODUCT), \
            "Success message is presented, but should be disappeared"