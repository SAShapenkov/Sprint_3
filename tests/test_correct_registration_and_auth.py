from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from constants import Constants

driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/register")

# Заполнение полей регистрации
driver.find_element(By.XPATH, ".//div/main/div/form/fieldset[1]/div/div/input").send_keys(Constants.NAME)
driver.find_element(By.XPATH, ".//div/main/div/form/fieldset[2]/div/div/input").send_keys(Constants.TEST_EMAIL)
driver.find_element(By.XPATH, ".//div/main/div/form/fieldset[3]/div/div/input").send_keys(Constants.PASSWORD)
driver.find_element(By.CSS_SELECTOR, "#root > div > main > div > form > button").click()

# ожидание появления формы авторизации
WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "Auth_login__3hAey")))

# проверка что url авторизации верен
current_url = driver.current_url
assert current_url == 'https://stellarburgers.nomoreparties.site/login'

# Проверка корректной авторизации
driver.find_element(By.NAME, "name").send_keys(Constants.TEST_EMAIL)
driver.find_element(By.NAME, "Пароль").send_keys(Constants.PASSWORD)
driver.find_element(By.CSS_SELECTOR, "#root > div > main > div > form > button").click()

# проверка редиректа на главную страницу
current_url = driver.current_url
assert current_url == 'https://stellarburgers.nomoreparties.site/'
driver.quite()
