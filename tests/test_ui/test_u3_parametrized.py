import allure
import pytest

from helpers.data_helpers import DataHelper
from pages.page_factory import PageFactory


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
    @allure.title('Авторизация валидного пользователя')
    @pytest.mark.parametrize(
        'username, password, description',
        positive_cases,
        )
    def test_valid_autorization(self, pages: PageFactory, username, password, description):
        with allure.step(
            f'Тестовые данные:Логин = {username}, Пароль = {password}, Описание = {description}'
        ):
            with allure.step('Открыть стартовую страницу'):
                angular_page = pages.angular_page.open_page()

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

    @allure.story('Authorization')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('Авторизация невалидного пользователя')
    @pytest.mark.parametrize(
        'username, password, description',
        neganive_cases,
        )
    def test_invalid_autorization(self, pages: PageFactory, username, password, description):
        with allure.step(
            f'Тестовые данные:Логин = {username}, Пароль = {password}, Описание = {description}'
        ):
            with allure.step('Открыть стартовую страницу'):
                angular_page = pages.angular_page.open_page()

            with allure.step('Заполнить поле "Username" невалидным значением'):
                angular_page.fill_username_field(username)

            with allure.step('Заполнить поле "Password" невалидным значением'):
                angular_page.fill_password_field(password)

            with allure.step('Заполнить поле "Description" невалидным значением'):
                angular_page.fill_description_field(description)

            with allure.step('Нажать на кнопку "Login"'):
                angular_page.click_login_button()

            with allure.step('Проверить текст ошибки'):
                angular_page.check_login_unsuccess_text()
