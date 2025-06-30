import allure
from selenium.webdriver.common.by import By

from constants.constants import Constants
from pages.base_page import BasePage


class AngularPage(BasePage):

    ENDPOINT_URL = '/angularjs-protractor/registeration/#/login'

    LOGIN_FIELD = (By.ID, 'username')
    LOGIN_FIELD_LABEL = (By.XPATH, '//label[@for="username"]')
    LOGIN_DESCRIPTION_FIELD = (By.ID, 'formly_1_input_username_0')
    PASSWORD_FIELD = (By.ID, 'password')
    PASSWORD_FIELD_LABEL = (By.XPATH, '//label[@for="password"]')
    LOGIN_BUTTON = (By. CLASS_NAME, 'btn-danger')
    LOGIN_MESSAGE_SUCCESS = (By.XPATH, "//p[normalize-space()=\"You're logged in!!\"]")
    LOGOUT_LINK = (By.CSS_SELECTOR, 'a[href="#/login"]')
    DANGER_ALERT = (By.CLASS_NAME, 'alert-danger ')

    @allure.step('Нажать кнопку "Login"')
    def click_login_button(self):
        self.click_button(self.LOGIN_BUTTON)

    @allure.step('Нажать кнопку "Logout"')
    def click_logout_button(self):
        self.click_button(self.LOGOUT_LINK)

    @allure.step('Заполнить поле "username"')
    def fill_username_field(self, value):
        self.fill_field(self.LOGIN_FIELD, value)

    @allure.step('Заполнить поле "password"')
    def fill_password_field(self, value):
        self.fill_field(self.PASSWORD_FIELD, value)

    @allure.step('Заполнить поле "description"')
    def fill_description_field(self, value):
        self.fill_field(self.LOGIN_DESCRIPTION_FIELD, value)

    @allure.step('Проверить что поле "Username" отображается')
    def check_username_field_visible(self):
        assert self.is_element_visible(self.LOGIN_FIELD), 'Поле "Username" не отображается на странице'

    @allure.step('Проверить наличие атрибута "text" у поле "Username"')
    def check_username_text_attr(self):
        text_attr_value = self.get_element_attribute(self.LOGIN_FIELD, 'value')
        assert text_attr_value is not None, "Атрибут 'text' отсутствует у поля 'Username'"

    @allure.step('Проверить значение "label" поля "Username"')
    def check_username_label(self):
        label_text = self.get_element_text(self.LOGIN_FIELD_LABEL)
        expected_label = 'Username'
        assert label_text == expected_label, f'Ожидалось: "{expected_label}", получен: "{label_text}"'

    @allure.step('Проверить что поле "Password" отображается')
    def check_password_field_visible(self):
        assert self.is_element_visible(self.PASSWORD_FIELD), 'Поле "Password" не отображается на странице'

    @allure.step('Проверить наличие атрибута "text" у поле "Password"')
    def check_password_text_attr(self):
        text_attr_value = self.get_element_attribute(self.PASSWORD_FIELD, 'value')
        assert text_attr_value is not None, "Атрибут 'text' отсутствует у поля 'Password'"

    @allure.step('Проверить значение "label" поля "Passwowd"')
    def check_password_label(self):
        label_text = self.get_element_text(self.PASSWORD_FIELD_LABEL)
        expected_label = 'Password'
        assert label_text == expected_label, f'Ожидалось: "{expected_label}", получен: "{label_text}"'

    @allure.step('Проверить, что кнопка "Login" неактивна')
    def check_login_button_is_disabled(self):
        with allure.step('Проверить оступность кнопки'):
            assert self.get_element_attribute(AngularPage.LOGIN_BUTTON, 'disabled') == 'true', \
                'Кнопка "Login" должна быть disabled'

    @allure.step('Проверить текст кнопки "Login"')
    def check_login_button_text(self):
        button_text = self.get_element_text(AngularPage.LOGIN_BUTTON)
        expected_text = 'Login'
        assert button_text == expected_text, \
            f'Текст кнопки "Login" некорректный. Ожидалось: "{expected_text}", получено: "{button_text}"'

    @allure.step('Проверить текст успешного входа')
    def check_login_success_text(self):
        actual_text = self.get_element_text(self.LOGIN_MESSAGE_SUCCESS)
        expected_text = Constants.ANGULAR_SUCCESS_LOGIN_TEXT
        with allure.step('Сравнить текст сообщения'):
            assert actual_text == expected_text, \
                f'Текст успешного входа неверен. Ожидалось: "{expected_text}", получено: "{actual_text}"'

    @allure.step('Проверить текст неуспешного входа')
    def check_login_unsuccess_text(self):
        self.get_element(self.DANGER_ALERT)
        actual_text = self.get_element_text(self.DANGER_ALERT)
        expected_text = Constants.ANGULAR_UNSUCCESS_LOGIN_TEXT
        with allure.step('Сравнить текст сообщения'):
            assert actual_text == expected_text, \
                f'Текст ошибки авторизации неверен. Ожидалось: "{expected_text}", получено: "{actual_text}"'

    @allure.step('Проверить, что пользователь перенаправлён обратно на форму входа')
    def check_logout_redirect(self):
        self.check_username_field_visible()
        self.check_password_field_visible()
