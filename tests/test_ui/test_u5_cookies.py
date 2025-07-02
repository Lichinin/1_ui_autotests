import allure

from pages.page_factory import PageFactory


@allure.epic('Web UI Tests')
@allure.feature('Test cookies on sql-ex.ru')
class TestSqlExPage:

    @allure.story('Cookies')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title('Проверка авторизации через UI')
    def test_login(self, pages: PageFactory):
        with allure.step('Открыть страницу SqlEx'):
            sql_ex_page = pages.sqlex.open_page()

        with allure.step('Заполнить поле "Login"'):
            sql_ex_page.fill_login_field()

        with allure.step('Заполнить поле "Password"'):
            sql_ex_page.fill_passsword_field()

        with allure.step('Нажать кнопку "Login"'):
            sql_ex_page.click_login_button()

        with allure.step('Проверить имя авторизованного пользователя'):
            sql_ex_page.check_authorization_name()

    @allure.story('Cookies')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title('Проверка авторизации с помощью cookies')
    def test_with_cookies(self, pages: PageFactory, prepare_cookies):
        with allure.step('Открыть страницу SqlEx'):
            sql_ex_page = pages.sqlex.open_page()

        with allure.step('Добавить cookies и обновить страницу'):
            sql_ex_page.add_cookies_and_refresh()

        with allure.step('Проверить имя авторизованного пользователя'):
            sql_ex_page.check_authorization_name()
