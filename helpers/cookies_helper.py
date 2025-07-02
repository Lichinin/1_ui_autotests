import json
import os

import allure
from selenium.webdriver.remote.webdriver import WebDriver


class CookiesHelper:

    cookies_path = os.path.join("data/cookies/", "cookies")

    def __init__(self, page_object):
        self.page = page_object

    @property
    def browser(self):
        return self.page.browser

    @allure.step('Сохранить cookies в файле')
    def save_cookies_to_file(self):
        cookies = self.browser.get_cookies()
        os.makedirs(os.path.dirname(CookiesHelper.cookies_path), exist_ok=True)

        with open(CookiesHelper.cookies_path, 'w', encoding='utf-8') as file:
            json.dump(cookies, file, indent=4)

    @staticmethod
    @allure.step('Прочитать охранить cookies из файла')
    def load_cookies_from_file():
        with open(CookiesHelper.cookies_path, 'r', encoding='utf-8') as file:
            return json.load(file)

    @staticmethod
    @allure.step('Применить cookies к сессии')
    def add_cookies_to_browser_and_refresh(browser: WebDriver) -> None:
        cookies = CookiesHelper.load_cookies_from_file()
        browser.delete_all_cookies()

        for cookie in cookies:
            browser.add_cookie(cookie)

        browser.refresh()

    @staticmethod
    @allure.step('Удалить файл cookies')
    def delete_cookies_file():
        os.remove(CookiesHelper.cookies_path)
