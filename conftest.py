import pytest
from selenium import webdriver
from src.application import Application
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope='function')
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    driver.get('https://disk.yandex.ru/client/disk')

    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def app(driver):
    return Application(driver)
