import allure
from selenium.webdriver.common.by import By

from constants.constants import Constants
from helpers.data_helpers import DataHelper
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

    @allure.step('Получить атрибут "text" поля "username"')
    def get_username_text_attr(self):
        return self.get_element_attribute(self.LOGIN_FIELD, 'value')

    @allure.step('Получить атрибут "text" поля "password"')
    def get_password_text_attr(self):
        return self.get_element_attribute(self.PASSWORD_FIELD, 'value')

    @allure.step('Заполнить поле "username" валидным значением')
    def fill_username_field_valid(self):
        self.fill_field(self.LOGIN_FIELD, Constants.ANGULAR_VALID_LOGIN)

    @allure.step('Заполнить поле "password" валидным значением')
    def fill_password_field_valid(self):
        self.fill_field(self.PASSWORD_FIELD, Constants.ANGULAR_VALID_PASS)

    @allure.step('Заполнить поле "description" валидным значением')
    def fill_description_field_valid(self):
        self.fill_field(self.LOGIN_DESCRIPTION_FIELD, Constants.ANGULAR_VALID_DESC)

    @allure.step('Нажать кнопку "Login"')
    def click_login_button(self):
        self.click_button(self.LOGIN_BUTTON)

    @allure.step('Нажать кнопку "Logout"')
    def click_logout_button(self):
        self.click_button(self.LOGOUT_LINK)

    @allure.step('Заполнить поле "username" невалидным значением')
    def fill_username_field_invalid(self):
        self.fill_field(self.LOGIN_FIELD, DataHelper.random_login_data()['login'])

    @allure.step('Заполнить поле "password" невалидным значением')
    def fill_password_field_invalid(self):
        self.fill_field(self.PASSWORD_FIELD, DataHelper.random_login_data()['password'])

    @allure.step('Заполнить поле "description" невалидным значением')
    def fill_description_field_invalid(self):
        self.fill_field(self.LOGIN_DESCRIPTION_FIELD, DataHelper.random_login_data()['description'])
