from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import Locators
from constants import Constants


class TestAuthLk:
    def test_auth_lk(self, driver):
        # переход в авторизацию через кнопку Личный кабинет
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.LK_BUTTON))
        driver.find_element(*Locators.LK_BUTTON).click()

        # ожидание появления формы авторизации
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.AUTH_FORM))

        # Проверка корректной авторизации
        driver.find_element(*Locators.LOGIN_FIELD).send_keys(Constants.TEST_EMAIL)
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        # проверка редиректа на главную страницу
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.PLACE_ORDER))
        current_url = driver.current_url
        assert current_url == 'https://stellarburgers.nomoreparties.site/'
