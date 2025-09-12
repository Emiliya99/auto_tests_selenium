from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    BTN_ADD_BASKET = (By.CLASS_NAME, "btn.btn-lg.btn-primary.btn-add-to-basket")

    NAME_PRODUCT = (By.CSS_SELECTOR, ".col-sm-6.product_main:nth-child(2) h1")
    PRICE_PRODUCT = (By.CSS_SELECTOR, ".col-sm-6.product_main:nth-child(2) > p.price_color")

    MSG_NAME_PRODUCT = (By.CSS_SELECTOR, "div.alertinner strong")
    MSG_PRICE_PRODUCT = (By.CSS_SELECTOR, ".alert-info .alertinner strong")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")