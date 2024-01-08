from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from constants import Constants
from locators import Locators
class TestAuthMain:
    def test_auth_main_page_button(self, driver):
        # переход в авторизацию через кнопку Войти в аккаунт
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, ".//p[contains(text(),'Личный Кабинет')]")))
        driver.find_element(*Locators.BUTTON_ENTER_ACCOUNT).click()


# ожидание появления формы авторизации
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "Auth_login__3hAey")))

# Проверка корректной авторизации
        driver.find_element(*Locators.LOGIN_FIELD).send_keys(Constants.TEST_EMAIL)
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.LOGIN_BUTTON).click()


# проверка редиректа на главную страницу
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//h1[text()='Соберите бургер']")))
        current_url = driver.current_url
        assert current_url == 'https://stellarburgers.nomoreparties.site/'
        driver.quit()
