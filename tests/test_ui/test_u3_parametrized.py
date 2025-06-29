import allure
import pytest

from pages.angular_login_page import AngularPage


@allure.epic('Web UI Tests')
@allure.feature('Angular Login Page Functionality')
class TestParametrizedLogin:

    testcases = [
        pytest.param('angular', 'password', 'angular', 'success', id='valid_user'),
        pytest.param('moderator_login', 'moderator_password', 'moderator_desription', 'fault', id='moderator'),
        pytest.param('admin_login', 'admin_password', 'admin_desription', 'fault', id='administrator'),
        pytest.param('invalid_username', 'invalid_password', 'invalid_description', 'fault', id='invalid_user'),
        pytest.param('', 'password', 'desription', 'no_logging', id='without_login'),
        pytest.param('login', '', 'desription', 'no_logging', id='without_password')
    ]

    @allure.story('Authorization')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('Авторизация пользователя')
    @pytest.mark.parametrize(
        'username, password, description, result',
        testcases,
        )
    def test_autorization(self, angular_page: AngularPage, username, password, description, result):
        with allure.step(
            f'Тестовые данные:Логин = {username}, Пароль = {password}, Описание = {description}, Авторизация = {result}'
        ):
            with allure.step('Заполнить поле "Username"'):
                angular_page.fill_username_field(username)
            with allure.step('Заполнить поле "Password"'):
                angular_page.fill_password_field(password)
            with allure.step('Заполнить поле "Description"'):
                angular_page.fill_description_field(description)
            with allure.step('Нажать на кнопку "Login"'):
                angular_page.click_login_button()
            with allure.step('Проверить текст успешного входа'):
                angular_page.check_login(result)
