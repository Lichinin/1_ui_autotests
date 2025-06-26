import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException, NoSuchElementException
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

    @classmethod
    @allure.step('Сформировать полный URL')
    def get_full_url(cls):
        return f'{Urls.BASE_URL}{cls.ENDPOINT_URL}'

    @allure.step('Прокрутить страницу до элемента')
    def scroll_to(self, element):
        self.browser.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center' });", element)

    @allure.step('Заполнить поле "{field}" значением "{text}"')
    def fill_field(self, field, text):
        field = self.get_element(field)
        field.clear()
        field.send_keys(text)

    @allure.step('Кликнуть на кнопку "{button}"')
    def click_button(self, button):
        self.get_element(button).click()

    @allure.step('Кликнуть текст элемента')
    def get_element_text(self, locator):
        element = self.get_element(locator)
        return element.text

    @allure.step('Проверить видимость элемента')
    def is_element_visible(self, locator):
        try:
            WebDriverWait(self.browser, 10).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except (TimeoutException, NoSuchElementException):
            return False

    def get_element_attribute(self, locator, attribute_name):
        element = self.get_element(locator)
        return element.get_attribute(attribute_name)