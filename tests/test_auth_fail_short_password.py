from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from constants import Constants
from locators import Locators


class TestShortPassAuth:
    def test_auth_short_pass(self, driver):
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.LK_BUTTON))
        driver.find_element(*Locators.LK_BUTTON).click()

        # Вход с неправильным (коротким) паролем
        driver.find_element(*Locators.LOGIN_FIELD).send_keys(Constants.TEST_EMAIL)
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(Constants.SHORT_PASSWORD)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.INCORRECT_PASSWORD))

        # Проверка корректности текста ошибки
        expected_title = f"Некорректный пароль"
        fact_title = driver.find_element(*Locators.INCORRECT_PASSWORD)
        assert fact_title.text == expected_title
