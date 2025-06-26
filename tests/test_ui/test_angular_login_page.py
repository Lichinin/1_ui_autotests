import allure

from constants.constants import Constants
from pages.angular_login_page import AngularPage
from helpers.data_helpers import DataHelper


@allure.epic('Web UI Tests')
@allure.feature('Angular Login Page Functionality')
class TestAngularLoginPage:

    @allure.story('Form Elements')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title('Проверка видимости поля "Username"')
    def test_username_is_visible(self, angular_page: AngularPage):
        with allure.step('Проверить что поле "Username" отображается'):
            assert angular_page.is_element_visible(angular_page.LOGIN_FIELD)
        with allure.step('Проверить что есть атрибут "text"'):
            text_attr_value = angular_page.get_element_attribute(angular_page.LOGIN_FIELD, 'value')
            assert text_attr_value is not None, "Атрибут 'text' отсутствует у элемента"

    @allure.story('Form Elements')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title('Проверка видимости поля "Password"')
    def test_password_is_visible(self, angular_page: AngularPage):
        with allure.step('Проверить что поле "Password" отображается'):
            assert angular_page.is_element_visible(angular_page.PASSWORD_FIELD)
        with allure.step('Проверить что есть атрибут "text"'):
            text_attr_value = angular_page.get_element_attribute(angular_page.PASSWORD_FIELD, 'value')
            assert text_attr_value is not None, "Атрибут 'text' отсутствует у элемента"

    @allure.story('Login Button')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title('Проверка, что кнопка "Login" изначально отключена')
    def test_login_button_is_disabled(self, angular_page: AngularPage):
        with allure.step('Проверить что кнопка "Login" не активна'):
            assert angular_page.get_element_attribute(AngularPage.LOGIN_BUTTON, 'disabled') == 'true'
        with allure.step('Проверить, что текстом кнопки является "Login"'):
            assert angular_page.get_element_text(AngularPage.LOGIN_BUTTON) == 'Login'


    @allure.story('Authorization')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('Успешная авторизация с валидными данными')
    def test_valid_autorization(self, angular_page: AngularPage):
        with allure.step('Заполнить поле "Username"'):
            angular_page.fill_field(angular_page.LOGIN_FIELD, Constants.ANGULAR_VALID_LOGIN)
        with allure.step('Заполнить поле Pass"word'):
            angular_page.fill_field(angular_page.PASSWORD_FIELD, Constants.ANGULAR_VALID_PASS)
        with allure.step('Заполнить описание пользователя'):
            angular_page.fill_field(angular_page.LOGIN_DESCRIPTION_FIELD, Constants.ANGULAR_VALID_DESC)
        with allure.step('Нажать на кнопку "Login"'):
            angular_page.click_button(angular_page.LOGIN_BUTTON)
        with allure.step('Проверить текст успешного входа'):
            text = angular_page.get_sucessful_login_text()
            assert text == Constants.ANGULAR_SUCCESS_LOGIN_TEXT

    @allure.story('Authorization')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title('Неудачная авторизация с неверным логином')
    def test_invalid_autorization(self, angular_page: AngularPage):
        with allure.step('Заполнить поле "Username" неверным значением'):
            angular_page.fill_field(angular_page.LOGIN_FIELD, DataHelper.random_login_data()['login'])
        with allure.step('Заполнить поле "Password"'):
            angular_page.fill_field(angular_page.PASSWORD_FIELD, DataHelper.random_login_data()['password'])
        with allure.step('Заполнить описание пользователя'):
            angular_page.fill_field(angular_page.LOGIN_DESCRIPTION_FIELD, DataHelper.random_login_data()['description'])
        with allure.step('Нажать на кнопку "Login"'):
            angular_page.click_button(angular_page.LOGIN_BUTTON)
        with allure.step('Проверить текст ошибки'):
            text = angular_page.get_unsucessful_login_text()
            assert text == Constants.ANGULAR_UNSUCCESS_LOGIN_TEXT

    @allure.story('Logout')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title('Выход из аккаунта (logout)')
    def test_logout(self, angular_page: AngularPage):
        with allure.step('Вход с валидными данными'):
            angular_page.fill_field(angular_page.LOGIN_FIELD, Constants.ANGULAR_VALID_LOGIN)
            angular_page.fill_field(angular_page.PASSWORD_FIELD, Constants.ANGULAR_VALID_PASS)
            angular_page.fill_field(angular_page.LOGIN_DESCRIPTION_FIELD, Constants.ANGULAR_VALID_DESC)
            angular_page.click_button(angular_page.LOGIN_BUTTON)
        with allure.step('Нажать на ссылку "Logout"'):
            angular_page.click_button(angular_page.LOGOUT_LINK)
        with allure.step('Проверить, что пользователь перенаправлён обратно на форму входа'):
            assert angular_page.get_element(angular_page.LOGIN_FIELD)
            assert angular_page.get_element(angular_page.PASSWORD_FIELD)
