from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, \
            "URL is not presented"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), \
            "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), \
            "Register form is not presented"

    def register_new_user(self, email, password):
        email_reg = self.browser.find_element(*LoginPageLocators.EMAIL_REG)
        email_reg.send_keys(email)
        pass1_reg = self.browser.find_element(*LoginPageLocators.PASSWORD1_REG)
        pass1_reg.send_keys(password)
        pass2_reg = self.browser.find_element(*LoginPageLocators.PASSWORD2_REG)
        pass2_reg.send_keys(password)
        btn_reg = self.browser.find_element(*LoginPageLocators.BTN_REG)
        btn_reg.click()
