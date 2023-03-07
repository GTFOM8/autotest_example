import pytest
from selenium import webdriver
from source.application import Application
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://demoqa.com/")
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def app(driver):
    return Application(driver)
