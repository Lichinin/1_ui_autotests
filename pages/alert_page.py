import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class AlertPage(BasePage):

    def __init__(self, browser):
        super().__init__(browser)

    ENDPOINT_URL = '/way2auto_jquery/alert.php#load_box'

    IFRAME = (By.CSS_SELECTOR, 'iframe[src="alert/input-alert.html"]')
    INPUT_ALERT_BUTTON = (By.CSS_SELECTOR, 'a[href="#example-1-tab-2"]')
    CLICK_TO_DEMONSTRATE_BUTTON = (By.CSS_SELECTOR, 'button[onclick="myFunction()"]')
    ALERT_EDITED_TEXT = (By. ID, 'demo')

    @allure.step('Открыть стартовую страницу')
    def open_page(self):
        url = self.get_full_url()
        return self.open_url(url)

    @allure.step('Перелючиться на iframe')
    def switch_to_iframe(self):
        iframe = self.get_element(self.IFRAME)
        self.browser.switch_to.frame(iframe)

    @allure.step('Нажать кнопку "INPUT ALERT"')
    def click_input_alert_button(self):
        self.click_button(self.INPUT_ALERT_BUTTON)

    @allure.step('Нажать кнопку "click the button to demonstrate the input box"')
    def click_button_to_demonstrate(self):
        self.click_button(self.CLICK_TO_DEMONSTRATE_BUTTON)

    @allure.step('Проверить результат отправки текста')
    def check_intut_alert_text(self, username):
        actual_text = self.get_element_text(self.ALERT_EDITED_TEXT)
        expected_text = f'Hello {username}! How are you today?'
        assert expected_text == actual_text, \
            f'Ожидался текст "{expected_text}", получен "{actual_text}'
