from faker import Faker
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from constants import Constants
from locators import Locators

faker = Faker()
email = faker.email()
class TestCorrectReg:
    def test_correct_registration(self, driver):
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.LK_BUTTON))
        driver.find_element(*Locators.LK_BUTTON).click()
        driver.find_element(*Locators.REGISTRATION_BUTTON).click()

# Заполнение полей регистрации

        driver.find_element(*Locators.NAME_REGISTRATION).send_keys(Constants.NAME)
        driver.find_element(*Locators.EMAIL_REGISTRATION).send_keys(email)
        driver.find_element(*Locators.PASSWORD_REGISTRATION).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.REGISTRATION_BUTTON).click()

# ожидание появления формы авторизации
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.AUTH_FORM))

# Проверка корректной авторизации новым пользователем
    def test_auth_new_user(self, driver):
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.LK_BUTTON))
        driver.find_element(*Locators.LK_BUTTON).click()
        driver.find_element(*Locators.LOGIN_FIELD).send_keys(email)
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.LOGIN_BUTTON).click()

# проверка редиректа на главную страницу
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.PLACE_ORDER))
        current_url = driver.current_url
        assert current_url == 'https://stellarburgers.nomoreparties.site/'