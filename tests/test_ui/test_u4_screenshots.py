import allure
import pytest

from helpers.data_helpers import DataHelper
from pages.angular_login_page import AngularPage


@allure.epic('Web UI Tests')
@allure.feature('Angular Login Page Functionality')
class TestParametrizedLogin:

    positive_cases = [
        pytest.param(
            'angular',
            'password',
            'angular',
            id='valid_user'
        ),
    ]

    neganive_cases = [
        pytest.param(
            DataHelper.random_login_data()['login'],
            DataHelper.random_login_data()['password'],
            DataHelper.random_login_data()['description'],
            id='invalid_user'
        ),
    ]

    @allure.story('Authorization')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('Неверный текст при авторизации (fail_screenshot)')
    @pytest.mark.parametrize(
        'username, password, description',
        positive_cases,
        )
    def test_valid_autorization_text(self, angular_page: AngularPage, username, password, description):
        with allure.step(
            f'Тестовые данные:Логин = {username}, Пароль = {password}, Описание = {description}'
        ):
            with allure.step('Заполнить поле "Username" валидным значением'):
                angular_page.fill_username_field(username)
            with allure.step('Заполнить поле "Password" валидным значением'):
                angular_page.fill_password_field(password)
            with allure.step('Заполнить поле "Description" валидным значением'):
                angular_page.fill_description_field(description)
            with allure.step('Нажать на кнопку "Login"'):
                angular_page.click_login_button()
            with allure.step('Проверить текст успешного входа'):
                angular_page.check_login_text_and_get_screenshot()()


    @allure.story('Authorization')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('Broken test (fail_screenshot)')
    @pytest.mark.parametrize(
        'username, password, description',
        neganive_cases,
        )
    def test_invalid_autorization(self, angular_page: AngularPage, username, password, description):
        with allure.step(
            f'Тестовые данные:Логин = {username}, Пароль = {password}, Описание = {description}'
        ):
            with allure.step('Заполнить поле "Username" валидным значением'):
                angular_page.fill_username_field(username)
            with allure.step('Заполнить поле "Password" валидным значением'):
                angular_page.fill_password_field(password)
            with allure.step('Заполнить поле "Description" валидным значением'):
                angular_page.fill_description_field(description)
            with allure.step('Нажать на кнопку "Login"'):
                angular_page.click_login_button()
            with allure.step('Проверить текст успешного входа'):
                angular_page.check_login_success_text()

    @allure.story('Form Elements')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title('Проверка видимости поля "Username" (fail_screenshot)')
    def test_username_is_visible(self, angular_page: AngularPage):
        with allure.step('Проверить что поле "Username" отображается'):
            angular_page.check_username_field_visible()
        with allure.step('Проверить что есть атрибут "text"'):
            angular_page.check_username_text_attr()
        with allure.step('Проверить "label" поля "Username"'):
            angular_page.check_username_label_invalid()
