from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from constants import Constants
from locators import Locators


class TestLK:
    def test_LK_link(self, driver):
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.LK_BUTTON))
        driver.find_element(*Locators.LK_BUTTON).click()
        # ожидание появления формы авторизации
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.AUTH_FORM))
        # авторизация
        driver.find_element(*Locators.LOGIN_FIELD).send_keys(Constants.TEST_EMAIL)
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.LOGIN_BUTTON).click()

        # ожидание появления кнопки
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.LK_BUTTON))

        # переход в личный кабинет по кнопке Личный кабинет
        driver.find_element(*Locators.LK_BUTTON).click()

        # ожидание появления списка пунктов в кабинете
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.LK_LIST))
# проверка редиректа в личный кабинет
        current_url = driver.current_url
        assert current_url == 'https://stellarburgers.nomoreparties.site/account/profile'