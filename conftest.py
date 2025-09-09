import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose language")

@pytest.fixture(scope="function")
def browser(request):
    language_name = request.config.getoption("language")
    browser = webdriver.Chrome()
    browser.get(f"http://selenium1py.pythonanywhere.com/{language_name}/catalogue/coders-at-work_207/")
    yield browser
    print("\nquit browser..")
    browser.quit()