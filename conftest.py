import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def pytest_addoption(parser):
    parser.addoption(
        "--language", 
        action="store", 
        default="en", 
        help="Choose language: en or ru"
    )

@pytest.fixture
def browser():
    driver = webdriver.Chrome()  
    yield driver
    driver.quit()
 
def test_language_selection(browser, language):
        
    if language == "ru":
        url == "http://selenium1py.pythonanywhere.com/ru/"
        time.slip(10)
        pass
    elif language == "en":
        url == "http://selenium1py.pythonanywhere.com/en-gb/"
        time.slip(10)
        pass

    # Проверка, что язык выбран правильно
    assert browser.current_url == f"http://selenium1py.pythonanywhere.com/?lang={language}"


