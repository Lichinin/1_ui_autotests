import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class AngularPage(BasePage):

    ENDPOINT_URL = '/angularjs-protractor/registeration/#/login'

    LOGIN_FIELD = (By.ID, 'username')
    LOGIN_DESCRIPTION_FIELD = (By.ID, 'formly_1_input_username_0')
    PASSWORD_FIELD = (By.ID, 'password')
    LOGIN_BUTTON = (By. CLASS_NAME, 'btn-danger')
    LOGIN_MESSAGE_SUCCESS = (By.XPATH, "//p[normalize-space()=\"You're logged in!!\"]")
    LOGOUT_LINK = (By.CSS_SELECTOR, 'a[href="#/login"]')
    DANGER_ALERT = (By.CLASS_NAME, 'alert-danger ')

    @allure.step('Получить текст успешного входа')
    def get_sucessful_login_text(self):
        text = self.get_element_text(self.LOGIN_MESSAGE_SUCCESS)
        return text

    @allure.step('Получить текст ошибки входа')
    def get_unsucessful_login_text(self):
        self.get_element(self.DANGER_ALERT)
        text = self.get_element(self.DANGER_ALERT).text
        return text
