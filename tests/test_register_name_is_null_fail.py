from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep
from constants import Constants

driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/register")

# Заполнение полей регистрации
driver.find_element(By.XPATH, ".//div/main/div/form/fieldset[2]/div/div/input").send_keys(Constants.TEST_EMAIL)
driver.find_element(By.XPATH, ".//div/main/div/form/fieldset[3]/div/div/input").send_keys(Constants.SHORT_PASSWORD)
driver.find_element(By.CSS_SELECTOR, "#root > div > main > div > form > button").click()

# ожидание возможных загрузок
sleep(3)
# Проверка на отсутствие перевода с страницы регистрации (можно было бы по аналогии с паролем сделать ошибку)
current_url = driver.current_url
assert current_url == 'https://stellarburgers.nomoreparties.site/register'

