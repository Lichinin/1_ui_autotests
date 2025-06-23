import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from config import Timeouts, Urls


class BasePage:

    def __init__(self, browser):
        self.browser = browser
        self.logger = browser.logger

    @allure.step('Найти элемент на странице')
    def get_element(
        self,
        locator: tuple,
        timeout=Timeouts.ELEMENT_VISIBILITY
    ):
        with allure.step(f'Найти элемент "{locator}"'):
            self.browser.logger.info(f'* Get element "{repr(locator)}"')
            return WebDriverWait(self.browser, timeout).until(
                EC.visibility_of_element_located(locator),
                message='Не удалось найти {locator} за {timeout} секунд'
            )

    @allure.step('Найти несколько элементов на странице')
    def get_elements(
        self,
        locator: tuple,
        timeout=Timeouts.ELEMENT_VISIBILITY
    ):
        with allure.step(f'Найти элемент "{locator}"'):
            self.browser.logger.info(f'* Get elements {repr(locator)}')
            return WebDriverWait(self.browser, timeout).until(
                EC.visibility_of_all_elements_located(locator),
                message='Не удалось найти {locator} за {timeout} секунд'
            )

    @allure.step('Получить текст allert')
    def get_alert_message(self):
        alert = self.browser.switch_to.alert
        return alert.text if alert.text else ''

    @classmethod
    def get_full_url(cls):
        return f'{Urls.BASE_URL}{cls.ENDPOINT_URL}'
