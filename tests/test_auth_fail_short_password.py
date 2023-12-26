from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from constants import Constants

driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/login")

# Вход с неправильным (коротким) паролем
driver.find_element(By.NAME, "name").send_keys(Constants.TEST_EMAIL)
driver.find_element(By.NAME, "Пароль").send_keys(Constants.SHORT_PASSWORD)
driver.find_element(By.CSS_SELECTOR, "#root > div > main > div > form > button").click()
WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "#root > div > main > div > form > fieldset:nth-child(2) > div > p")))

# Проверка корректности текста ошибки
expected_title =  f"Некорректный пароль"
fact_title = driver.find_element(By.CSS_SELECTOR, "#root > div > main > div > form > fieldset:nth-child(2) > div > p")
assert fact_title.text == expected_title