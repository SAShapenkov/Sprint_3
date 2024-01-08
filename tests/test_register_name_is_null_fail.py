from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from constants import Constants
from locators import Locators



class TestNullName:
    def test_null_name_registration(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/register")

        # Заполнение полей регистрации
        driver.find_element(*Locators.EMAIL_REGISTRATION).send_keys(Constants.TEST_EMAIL)
        driver.find_element(*Locators.PASSWORD_REGISTRATION).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.REGISTRATION_BUTTON).click()

# Проверка на отсутствие перевода с страницы регистрации (можно было бы по аналогии с паролем сделать ошибку)
        current_url = driver.current_url
        assert current_url == 'https://stellarburgers.nomoreparties.site/register'

