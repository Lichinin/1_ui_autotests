import json
import os

import allure
from dotenv import load_dotenv
from selenium.webdriver.common.by import By

from pages.base_page import BasePage

load_dotenv()


class SqlExPage(BasePage):

    COOKIES_PATH = os.path.join("data/cookies/", "cookies")

    ENDPOINT_URL = ''

    LOGIN_BUTTON = (By.CSS_SELECTOR, 'input[name="subm1"]')
    LOGIN_FIELD = (By.CSS_SELECTOR, 'input[name="login"]')
    PASSWORD_FIELD = (By.CSS_SELECTOR, 'input[name="psw"]')
    AUTHORIZED_USER = (By.CSS_SELECTOR, 'td[align="right"][valign="middle"]')

    @allure.step('Заполнить поле "username"')
    def fill_login_field(self):
        self.fill_field(self.LOGIN_FIELD, os.getenv('SQL_EX_LOGIN'))

    @allure.step('Заполнить поле "password"')
    def fill_passsword_field(self):
        self.fill_field(self.PASSWORD_FIELD, os.getenv('SQL_EX_PASSWORD'))

    @allure.step('Нажать кнопку "Вход без регистрации"')
    def click_login_button(self):
        self.click_button(self.LOGIN_BUTTON)

    @allure.step('Получить имя авторизованного пользователя')
    def get_authorized_user_username(self):
        return self.get_element(self.AUTHORIZED_USER).text

    @allure.step('Проверить авторизацию под пользователем "test_lichinin"')
    def check_guest_authorization_name(self):
        actual_username = self.get_authorized_user_username()
        expected_username = 'test_lichinin'
        assert expected_username in actual_username, \
            f'Ожидалось {expected_username}, получено {actual_username}'

    @allure.step('Записать файл с данными cookie')
    def create_cookie_file(self):
        guest_cookies = self.browser.get_cookies()
        os.makedirs(os.path.dirname(self.COOKIES_PATH), exist_ok=True)

        with open(self.COOKIES_PATH, 'w', encoding='utf-8') as file:
            json.dump(guest_cookies, file, indent=4)

    @allure.step('Записать cookie в браузер')
    def add_cookies(self):
        with open(self.COOKIES_PATH, 'r', encoding='utf-8') as file:
            cookies = json.load(file)
        self.browser.delete_all_cookies()
        for cookie in cookies:
            self.browser.add_cookie(cookie)
        self.browser.refresh()
