from selenium.webdriver.common.by import By
from selenium import webdriver
from constants import Constants

driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/login")

# Вход незарегистрированным пользователем
driver.find_element(By.NAME, "name").send_keys(Constants.UNREG_EMAIL)
driver.find_element(By.NAME, "Пароль").send_keys(Constants.PASSWORD)
driver.find_element(By.CSS_SELECTOR, "#root > div > main > div > form > button").click()

# проверка на отсутствие редиректа на главную страницу
current_url = driver.current_url
assert current_url == 'https://stellarburgers.nomoreparties.site/login'
