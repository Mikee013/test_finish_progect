import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='ru',
                     help="Choose language: ru or en")

@pytest.fixture(scope="function")
def language(request):
    browser_language = request.config.getoption("language")
    language = None
    if browser_language == 'ru':
        browser = webdriver.Chrome()
        link = "http://selenium1py.pythonanywhere.com/ru/"
      
    elif language == 'en':
        browser = webdriver.Chrome()
        link = "http://selenium1py.pythonanywhere.com/en-gb/"
    else:
        raise pytest.UsageError("--language should be ru or en")
    yield browser
    print("\nquit browser..")
    browser.quit()
