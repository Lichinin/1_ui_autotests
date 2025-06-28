import allure

from pages.angular_login_page import AngularPage


@allure.epic('Web UI Tests')
@allure.feature('Angular Login Page Functionality')
class TestAngularLoginPage:

    @allure.story('Form Elements')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title('Проверка видимости поля "Username"')
    def test_username_is_visible(self, angular_page: AngularPage):
        with allure.step('Проверить что поле "Username" отображается'):
            angular_page.check_username_field_visible()
        with allure.step('Проверить что есть атрибут "text"'):
            angular_page.check_username_text_attr()
        with allure.step('Проверить "label" поля "Username"'):
            angular_page.check_username_label()

    @allure.story('Form Elements')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title('Проверка видимости поля "Password"')
    def test_password_is_visible(self, angular_page: AngularPage):
        with allure.step('Проверить что поле "Password" отображается'):
            angular_page.check_password_field_visible()
        with allure.step('Проверить что есть атрибут "text"'):
            angular_page.check_password_text_attr()
        with allure.step('Проверить "label" поля "Password"'):
            angular_page.check_password_label()

    @allure.story('Login Button')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title('Проверка, что кнопка "Login" изначально отключена')
    def test_login_button_is_disabled(self, angular_page: AngularPage):
        with allure.step('Проверить что кнопка "Login" не активна'):
            angular_page.check_login_button_is_disabled()
        with allure.step('Проверить, что текстом кнопки является "Login"'):
            angular_page.check_login_button_text()

    @allure.story('Authorization')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('Успешная авторизация с валидными данными')
    def test_valid_autorization(self, angular_page: AngularPage):
        with allure.step('Заполнить поле "Username"'):
            angular_page.fill_username_field_valid()
        with allure.step('Заполнить поле Pass"word'):
            angular_page.fill_password_field_valid()
        with allure.step('Заполнить описание пользователя'):
            angular_page.fill_description_field_valid()
        with allure.step('Нажать на кнопку "Login"'):
            angular_page.click_login_button()
        with allure.step('Проверить текст успешного входа'):
            angular_page.check_login_success_text()

    @allure.story('Authorization')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title('Неудачная авторизация с невалидными данными')
    def test_invalid_autorization(self, angular_page: AngularPage):
        with allure.step('Заполнить поле "Username" неверным значением'):
            angular_page.fill_username_field_invalid()
        with allure.step('Заполнить поле "Password"'):
            angular_page.fill_password_field_invalid()
        with allure.step('Заполнить описание пользователя'):
            angular_page.fill_description_field_invalid()
        with allure.step('Нажать на кнопку "Login"'):
            angular_page.click_login_button()
        with allure.step('Проверить текст ошибки'):
            angular_page.check_login_unsuccess_text()

    @allure.story('Logout')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title('Выход из аккаунта (logout)')
    def test_logout(self, angular_page: AngularPage):
        with allure.step('Вход с валидными данными'):
            angular_page.fill_username_field_valid()
            angular_page.fill_password_field_valid()
            angular_page.fill_description_field_valid()
            angular_page.click_login_button()
        with allure.step('Нажать на ссылку "Logout"'):
            angular_page.click_logout_button()
        with allure.step('Проверить, что пользователь перенаправлён обратно на форму входа'):
            angular_page.check_logout_redirect()
