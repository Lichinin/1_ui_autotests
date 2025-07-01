import allure

from pages.sql_ex_page import SqlExPage


@allure.epic('Web UI Tests')
@allure.feature('Test cookies on sql-ex.ru')
class TestSqlExPage:

    @allure.story('Cookies')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title('Проверка авторизации через UI')
    def test_login(self, sql_ex_page: SqlExPage):
        sql_ex_page.fill_login_field()
        sql_ex_page.fill_passsword_field()
        sql_ex_page.click_login_button()
        sql_ex_page.check_guest_authorization_name()

    @allure.story('Cookies')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title('Проверка авторизации с помощью cookies')
    def test_with_cookies(self, sql_ex_page: SqlExPage, prepare_cookies):
        sql_ex_page.add_cookies()
        sql_ex_page.check_guest_authorization_name()
