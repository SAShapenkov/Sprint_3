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

sleep(2)

# проверка перехода к Соусам
driver.find_element(By.XPATH, ".//div/main/section[1]/div[1]/div[2]").click()
# Ожидание прокрутки
WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "#root > div > main > section.BurgerIngredients_ingredients__1N8v2 > div.BurgerIngredients_ingredients__menuContainer__Xu3Mo > ul:nth-child(4) > a:nth-child(3) > p")))
# проверка на видимость нижнего соуса
assert driver.find_element(By.CSS_SELECTOR, "#root > div > main > section.BurgerIngredients_ingredients__1N8v2 > div.BurgerIngredients_ingredients__menuContainer__Xu3Mo > ul:nth-child(4) > a:nth-child(3) > p").text == 'Соус традиционный галактический'

# проверка перехода к Начинкам
driver.find_element(By.XPATH, ".//div/main/section[1]/div[1]/div[3]").click()
# Ожидание прокрутки
WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "#root > div > main > section.BurgerIngredients_ingredients__1N8v2 > div.BurgerIngredients_ingredients__menuContainer__Xu3Mo > ul:nth-child(6) > a:nth-child(3) > p")))
# проверка на видимость нижней котлеты
assert driver.find_element(By.CSS_SELECTOR, "#root > div > main > section.BurgerIngredients_ingredients__1N8v2 > div.BurgerIngredients_ingredients__menuContainer__Xu3Mo > ul:nth-child(6) > a:nth-child(3) > p").text == 'Биокотлета из марсианской Магнолии'

# проверка перехода к Булкам
driver.find_element(By.XPATH, ".//div/main/section[1]/div[1]/div[1]").click()
# Ожидание прокрутки
WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "#root > div > main > section.BurgerIngredients_ingredients__1N8v2 > div.BurgerIngredients_ingredients__menuContainer__Xu3Mo > ul:nth-child(2) > a:nth-child(1) > p")))
# проверка на видимость первой булки
assert driver.find_element(By.CSS_SELECTOR, "#root > div > main > section.BurgerIngredients_ingredients__1N8v2 > div.BurgerIngredients_ingredients__menuContainer__Xu3Mo > ul:nth-child(2) > a:nth-child(1) > p").text == 'Флюоресцентная булка R2-D3'
driver.quite()