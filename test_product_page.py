from .pages.product_page import ProductPage
from .pages.base_page import BasePage
import time


link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"

def test_guest_can_add_product_to_basket(browser):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.go_to_add_basket()
    code = BasePage.solve_quiz_and_get_code(product_page)
    print(code)
    time.sleep(5)
