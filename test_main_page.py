from .pages.main_page import MainPage
from .pages.login_page import LoginPage
import time

link = "http://selenium1py.pythonanywhere.com/"

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
