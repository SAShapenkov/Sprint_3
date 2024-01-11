from selenium.webdriver.common.by import By

class Locators:
 # поля страницы
 LOGIN_FIELD = (By.XPATH, ".//*[@name='name']") # поле ввода логина
 PASSWORD_FIELD = (By.XPATH, ".//*[@name='Пароль']") # поле ввода пароля
 NAME_REGISTRATION = (By.XPATH, "//label[text()='Имя']/following-sibling::*") # имя при регистрации
 EMAIL_REGISTRATION = (By.XPATH, "//label[text()='Email']/following-sibling::*") # email при регистрации
 PASSWORD_REGISTRATION = (By.XPATH, ".//*[@name='Пароль']") # пароль при регистрации
 AUTH_FORM = (By.XPATH, "//*[@class='Auth_login__3hAey']") # форма авторизации
 LK_LIST = (By.XPATH, "//*[@class='Account_listItem__35dAP']") # список меню в ЛК

 # кнопки страницы
 LOGIN_BUTTON = (By.XPATH, './/form/button') # войти после ввода данных
 PLACE_ORDER = (By.XPATH, ".//button[text()='Оформить заказ']") # оформить заказ
 LK_BUTTON = (By.XPATH, ".//p[contains(text(),'Личный Кабинет')]") # личный кабинет
 REGISTRATION_BUTTON = (By.XPATH, ".//*[text()='Зарегистрироваться']") # зарегистрироваться
 LOGIN_VIA_REGISTRATION = (By.XPATH, "//a[text()='Войти']") # войти в меню регистрации
 BUTTON_ENTER_ACCOUNT = (By.XPATH, "//button[text()='Войти в аккаунт']")  # Кнопка Войти в аккаунт на гл. странице
 BUTTON_ENTER_ACCOUNT_FROM_RESTORE_FORM = (By.XPATH, "//a[text()='Войти']")  # Кнопка входа в аккаунт на форме восстановления пароля
 RECOVER_PASSWORD = (By.XPATH, ".//a[text()='Восстановить пароль']") # восстановить пароль
 LOGOUT_PERSONAL_ACCOUNT = (By.XPATH, "//button[text()='Выход']") # выход из личного кабинета
 CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']") # кнопка "Конструктор"
 LOGO = (By.XPATH, "//*[@class='AppHeader_header__logo__2D0X2']") # кнопка "Логотип"
 SAUCES_BUTTON = (By.XPATH, ".//span[@class='text text_type_main-default' and text()='Соусы']") # кнопка "Соусы"
 HEADER_SAUCES = (By.XPATH, ".//h2[text()='Соусы']") # Заголовок таба Соусы
 BUNS_BUTTON = (By.XPATH, ".//span[@class='text text_type_main-default' and text()='Булки']") # кнопка "Булки"
 HEADER_BUNS = (By.XPATH, ".//h2[text()='Булки']")  # Заголовок таба Булки
 FILLINGS_BUTTON = (By.XPATH, ".//span[@class='text text_type_main-default' and text()='Начинки']") # кнопка "Начинки"
 HEADER_FILLINGS = (By.XPATH, ".//h2[text()='Начинки']") # Заголовок таба Начинки
 MAKE_A_BURGER = (By.XPATH, ".//h1[text()='Соберите бургер']")  # Заголовок на главной странице


 # ошибки
 INCORRECT_PASSWORD = (By.XPATH, ".//p[contains(text(),'Некорректный пароль')]") # ошибка при вводе пароля
 EXISTING_USER = (By.XPATH, ".//p[contains(text(), 'Такой пользователь уже существует')]")