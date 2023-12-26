from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from constants import Constants
from time import sleep

driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/login")

# ожидание появления формы авторизации
WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "Auth_login__3hAey")))

# Авторизация
driver.find_element(By.NAME, "name").send_keys(Constants.TEST_EMAIL)
driver.find_element(By.NAME, "Пароль").send_keys(Constants.PASSWORD)
driver.find_element(By.CSS_SELECTOR, "#root > div > main > div > form > button").click()

# ожидание появления кнопки
WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "#root > div > header > nav > a > p")))
# переход в личный кабинет по кнопке Личный кабинет
driver.find_element(By.CSS_SELECTOR, "#root > div > header > nav > a > p").click()

# ожидание появления списка пунктов в кабинете
WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "Account_listItem__35dAP")))

# нажатие на кнопку Выход
driver.find_element(By.CSS_SELECTOR, "#root > div > main > div > nav > ul > li:nth-child(3) > button").click()

# ожидание появления формы авторизации
WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "Auth_login__3hAey")))

# проверка редиректа на страницу авторизации
current_url = driver.current_url
assert current_url == 'https://stellarburgers.nomoreparties.site/login'
driver.quite()