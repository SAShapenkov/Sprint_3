from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from constants import Constants
from locators import Locators

class TestExistingReg:
    def test_existing_user_registration(self, driver):

        driver.get("https://stellarburgers.nomoreparties.site/register")

# Заполнение полей регистрации

        driver.find_element(*Locators.NAME_REGISTRATION).send_keys(Constants.NAME)
        driver.find_element(*Locators.EMAIL_REGISTRATION).send_keys(Constants.EXIST_EMAIL)
        driver.find_element(*Locators.PASSWORD_REGISTRATION).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.REGISTRATION_BUTTON).click()

# ожидание появления ошибки
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "#root > div > main > div > p")))

# Проверка корректности текста ошибки
        expected_title =  f"Такой пользователь уже существует"
        fact_title = driver.find_element(*Locators.EXISTING_USER)
        assert fact_title.text == expected_title
        driver.quit()

