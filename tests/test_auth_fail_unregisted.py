from selenium import webdriver
from constants import Constants
from locators import Locators

class TestUnreg:
    def test_unreg_user_auth(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/login")

# Вход незарегистрированным пользователем
        driver.find_element(*Locators.LOGIN_FIELD).send_keys(Constants.UNREG_EMAIL)
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.LOGIN_BUTTON).click()

# проверка на отсутствие редиректа на главную страницу
        current_url = driver.current_url
        assert current_url == 'https://stellarburgers.nomoreparties.site/login'
        driver.quit()
