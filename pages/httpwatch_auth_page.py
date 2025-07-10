import base64

import allure
from dotenv import load_dotenv
from selenium.webdriver.common.by import By

from config import Urls
from pages.base_page import BasePage

load_dotenv()


class HttpWatchAuthPage(BasePage):

    def __init__(self, browser):
        super().__init__(browser)

    ENDPOINT_URL = '/httpgallery/authentication/#showExample10'

    DISPLAY_IMAGE_BUTTON = (By.ID, 'displayImage')
    IMAGE = (By.ID, 'downloadImg')

    def open_page(self):
        url = Urls.HTTPWATCH + self.ENDPOINT_URL
        return self.open_url(url)

    @allure.step('Нажать кнопку "Display Image"')
    def click_display_image_button(self):
        self.click_button(self.DISPLAY_IMAGE_BUTTON)

    @allure.step('Ввести значения логина и пароля, обновить страницу')
    def fill_credentials_and_refresh(self, username, password):
        credentials = f'{username}:{password}'
        encoded_credentials = base64.b64encode(credentials.encode()).decode('ascii')

        self.browser.execute_cdp_cmd('Network.enable', {})
        self.browser.execute_cdp_cmd('Network.setExtraHTTPHeaders', {
            'headers': {'Authorization': f'Basic {encoded_credentials}'}
        })
        self.browser.refresh()

    def check_image_is_visible(self):
        assert self.is_element_visible(self.IMAGE), 'Изображение не отображается'
