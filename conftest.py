import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from constants import Constants
from locators import Locators


@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get(Constants.URL)
    yield driver
    driver.quit()


@pytest.fixture
def login(driver):
    driver.find_element(*Locators.LOGIN_FIELD).send_keys(Constants.TEST_EMAIL)
    driver.find_element(*Locators.PASSWORD_FIELD).send_keys(Constants.PASSWORD)
    driver.find_element(*Locators.LOGIN_BUTTON).click()
    return driver
