import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help="Choose language: ru or en")

@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    language_browser = None
    options = Options()
    if language == "ru":
        print("\nstart chrome browser for test..")
        link = "http://selenium1py.pythonanywhere.com/ru/"
        browser.get(link)
    elif language == "en":
        print("\nstart chrome browser for test..")
        link = "http://selenium1py.pythonanywhere.com/en-gb/"
        browser.get(link)
    else:
        raise pytest.UsageError("--browser_name should en or ru")
    yield browser
    print("\nquit browser..")
    browser.quit()


