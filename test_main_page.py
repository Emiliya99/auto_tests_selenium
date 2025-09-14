import pytest
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import time

link = "http://selenium1py.pythonanywhere.com/"

@pytest.mark.skip
def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    page.should_be_login_link()
    time.sleep(2)

    page_login = LoginPage(browser, link)
    page_login.should_be_login_url()
    page_login.should_be_login_form()
    page_login.should_be_register_form()
    time.sleep(2)

def test_guest_cant_see_product_in_basket_opened_from_basket_page(browser):
    page = BasketPage(browser, link)
    page.open()
    time.sleep(2)
    page.go_to_basket_page()
    page.should_be_basket_page()
    time.sleep(6)
