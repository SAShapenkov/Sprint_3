from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import Locators

class TestConstructor:
    def test_constructor_to_buns(self, driver):
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.MAKE_A_BURGER))

        driver.find_element(*Locators.FILLINGS_BUTTON).click()

        driver.find_element(*Locators.BUNS_BUTTON).click()
        assert driver.find_element(*Locators.HEADER_BUNS).is_displayed()

    def test_constructor_to_sauces(self, driver):
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.MAKE_A_BURGER))

        driver.find_element(*Locators.SAUCES_BUTTON).click()
        assert driver.find_element(*Locators.HEADER_SAUCES).is_displayed()

    def test_constructor_to_fillings(self, driver):
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.MAKE_A_BURGER))

        driver.find_element(*Locators.FILLINGS_BUTTON).click()
        assert driver.find_element(*Locators.HEADER_FILLINGS).is_displayed()