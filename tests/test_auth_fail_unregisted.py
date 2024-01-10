from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from constants import Constants
from locators import Locators

class TestUnreg:
    def test_unreg_user_auth(self, driver):
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.LK_BUTTON))
        driver.find_element(*Locators.LK_BUTTON).click()

# Вход незарегистрированным пользователем
        driver.find_element(*Locators.LOGIN_FIELD).send_keys(Constants.UNREG_EMAIL)
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.LOGIN_BUTTON).click()

# проверка на отсутствие редиректа на главную страницу
        current_url = driver.current_url
        assert current_url == 'https://stellarburgers.nomoreparties.site/login'