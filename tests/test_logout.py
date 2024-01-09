from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from constants import Constants
from locators import Locators

class TestLogOut:
    def test_logout(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/login")
# ожидание появления формы авторизации
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "Auth_login__3hAey")))
# авторизация
        driver.find_element(*Locators.LOGIN_FIELD).send_keys(Constants.TEST_EMAIL)
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.LOGIN_BUTTON).click()

# ожидание появления кнопки
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, ".//p[contains(text(),'Личный Кабинет')]")))

# переход в личный кабинет по кнопке Личный кабинет
        driver.find_element(*Locators.LK_BUTTON).click()

# ожидание появления списка пунктов в кабинете
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "Account_listItem__35dAP")))

# нажатие на кнопку Выход
        driver.find_element(*Locators.LOGOUT_PERSONAL_ACCOUNT).click()

# ожидание появления формы авторизации
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "Auth_login__3hAey")))

# проверка редиректа на страницу авторизации
        current_url = driver.current_url
        assert current_url == 'https://stellarburgers.nomoreparties.site/login'
        driver.quit()