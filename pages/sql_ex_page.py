import os

import allure
from dotenv import load_dotenv
from selenium.webdriver.common.by import By

from config import Urls
from helpers.cookies_helper import CookiesHelper
from pages.base_page import BasePage

load_dotenv()


class SqlExPage(BasePage):

    def __init__(self, browser):
        super().__init__(browser)

    ENDPOINT_URL = ''

    LOGIN_BUTTON = (By.CSS_SELECTOR, 'input[name="subm1"]')
    LOGIN_FIELD = (By.CSS_SELECTOR, 'input[name="login"]')
    PASSWORD_FIELD = (By.CSS_SELECTOR, 'input[name="psw"]')
    AUTHORIZED_USER = (By.CSS_SELECTOR, 'td[align="right"][valign="middle"]')

    def open_page(self):
        self.browser.get(Urls.SQL_EX_RU)
        return self

    @allure.step('Заполнить поле "username"')
    def fill_login_field(self):
        self.fill_field(self.LOGIN_FIELD, os.getenv('SQL_EX_LOGIN'))

    @allure.step('Заполнить поле "password"')
    def fill_passsword_field(self):
        self.fill_field(self.PASSWORD_FIELD, os.getenv('SQL_EX_PASSWORD'))

    @allure.step('Нажать кнопку "Вход"')
    def click_login_button(self):
        self.click_button(self.LOGIN_BUTTON)

    @allure.step('Получить имя авторизованного пользователя')
    def get_authorized_user_username(self):
        return self.get_element(self.AUTHORIZED_USER).text

    @allure.step('Проверить авторизацию под пользователем "test_lichinin"')
    def check_authorization_name(self):
        actual_username = self.get_authorized_user_username()
        expected_username = os.getenv('SQL_EX_USERNAME')
        assert expected_username in actual_username, \
            f'Ожидалось {expected_username}, получено {actual_username}'

    @allure.step('Записать cookie в браузер')
    def add_cookies_and_refresh(self):
        CookiesHelper.add_cookies_to_browser_and_refresh(self.browser)
