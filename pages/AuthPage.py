from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class AuthPage:
    def __init__(self, driver: WebDriver) -> None:
        self.__url = "https://trello.com/login"
        self.__driver = driver

    def go(self):
        self.__driver.get(self.__url)

    def login_as(self, email: str, password: str):
        # ожидаем появления поля логина
        (WebDriverWait(self.__driver, 10).until(
            EC.visibility_of_element_located((By.NAME, "username"))))
        (self.__driver.find_element(By.NAME, "username").send_keys(email))
        (self.__driver.find_element(By.CSS_SELECTOR, "button[id='login-submit']").click())

        # Ожидаем появления поля ввода пароля
        (WebDriverWait(self.__driver, 10).until(
            EC.visibility_of_element_located((By.ID, "password"))))
        (self.__driver.find_element(By.ID, "password").
         send_keys(password))
        (self.__driver.find_element(By.CSS_SELECTOR, "button[id='login-submit']").click())

        # Ожидаем появления логотипа
        # (убеждаемся что главная страница полностью загружена)
        (WebDriverWait(self.__driver, 10).until((EC.visibility_of_element_located((By.CLASS_NAME, "GiAR33CZIrXv1a")))))

