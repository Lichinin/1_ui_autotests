import base64

import allure
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
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

    @allure.step('Найти кликабельный элемент на странице')
    def get_clickable_element(
        self,
        locator: tuple,
        timeout=Timeouts.ELEMENT_VISIBILITY
    ):
        with allure.step(f'Найти элемент "{locator}"'):
            self.browser.logger.info(f'* Get element "{repr(locator)}"')
            return WebDriverWait(self.browser, timeout).until(
                EC.element_to_be_clickable(locator),
                message=f'Элемент {locator} не кликабельный'
            )

    @classmethod
    @allure.step('Сформировать полный URL')
    def get_full_url(cls):
        return f'{Urls.BASE_URL}{cls.ENDPOINT_URL}'

    @allure.step('Открыть страницу по URL')
    def open_url(self, url):
        self.browser.get(url)
        return self

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

    @allure.step('Получить текст элемента')
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

    @allure.step('Получить значение атрибута "{attribute_name}" у элемента "{locator}"')
    def get_element_attribute(self, locator, attribute_name):
        element = self.get_element(locator)
        return element.get_attribute(attribute_name)

    @allure.step('Получить текущий URL страницы')
    def get_current_url(self):
        return self.browser.current_url

    @allure.step('Получить title текущей  страницы')
    def get_page_title(self):
        return self.browser.title.upper()

    @allure.step('Получить цвет фона элемента "{element}"')
    def get_element_background_colour(self, element):
        element = self.get_element(element)
        return element.value_of_css_property('background-color')

    @allure.step('Проверить цвет фона элемента "{locator}"')
    def check_element_background_colour(self, locator, expected_colour):
        element = self.get_element(locator)
        element_colour = element.value_of_css_property('background-color')
        assert element_colour == expected_colour, \
            f'Цвет фона не совпадает. Ожидалось: {expected_colour}, получено: {element_colour}'

    @allure.step('Проверить текст элемента "{locator}"')
    def check_element_text(self, locator, expected_text):
        element_text = self.get_element_text(locator)
        assert element_text == expected_text, \
            f'Текст элемента не совпадает. Ожидалось: "{expected_text}", получено: "{element_text}"'

    @allure.step('Проверить количество элементов в "{elements_list}"')
    def check_element_list_lenght(self, elements_list, expected_len):
        assert len(elements_list) == expected_len, \
            f'Количество элементов не совпадает. Ожидалось: {expected_len}, найдено: {len(elements_list)}'

    @allure.step('Сравнить элементы списков')
    def verify_list_items(self, actual_list, expected_list, msg_prefix=""):
        for i, (actual, expected) in enumerate(zip(actual_list, expected_list)):
            assert actual == expected, f'{msg_prefix} [{i}] не совпадает: {actual} != {expected}'

    @allure.step('Убрать фокус с элемента')
    def clear_focus_from_element(self):
        self.browser.execute_script('document.activeElement.blur();')

    @allure.step('Получить активный элемент')
    def get_active_element(self):
        return self.browser.switch_to.active_element

    @allure.step('Проверить наличие скролла на странице')
    def check_page_has_scroll(self):
        assert self.browser.execute_script('return document.body.scrollHeight > window.innerHeight;'), \
            'Скролл на странице не обнаружен'

    @allure.step('Drag-n-drop элемента "{draggable}" на элемент "{droppable}"')
    def drag_n_drop(self, draggable, droppable):
        actions = ActionChains(self.browser)
        actions.drag_and_drop(draggable, droppable).perform()

    @allure.step('Переключиться на вкладку номер {tab_number}')
    def switch_to_tab(self, tab_number):
        tabs = self.browser.window_handles
        self.browser.switch_to.window(tabs[tab_number-1])

    @allure.step('Ввести текст "{text}" в alert')
    def intut_text_to_alert(self, text):
        alert = self.browser.switch_to.alert
        alert.send_keys(text)
        alert.accept()

    @allure.step('Ввести значения логина и пароля, обновить страницу')
    def fill_credentials_and_refresh(self, username, password):
        credentials = f'{username}:{password}'
        encoded_credentials = base64.b64encode(credentials.encode()).decode('ascii')

        self.browser.execute_cdp_cmd('Network.enable', {})
        self.browser.execute_cdp_cmd('Network.setExtraHTTPHeaders', {
            'headers': {'Authorization': f'Basic {encoded_credentials}'}
        })
        self.browser.refresh()
