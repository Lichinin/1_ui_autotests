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
                message=f'Не удалось найти {locator} за {timeout} секунд'
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
                message=f'Не удалось найти {locator} за {timeout} секунд'
            )

    @allure.step('Получить текст allert')
    def get_alert_message(self):
        alert = self.browser.switch_to.alert
        return alert.text if alert.text else ''

    @classmethod
    def get_full_url(cls):
        return f'{Urls.BASE_URL}{cls.ENDPOINT_URL}'

    def scroll_to(self, element):
        self.browser.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center' });", element)

    def fill_field(self, field, text):
        field = self.get_element(field)
        field.clear()
        field.send_keys(text)

    def click_button(self, button):
        self.get_element(button).click()
