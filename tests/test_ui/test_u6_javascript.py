import allure

from pages.page_factory import PageFactory


@allure.epic('Web UI Tests')
@allure.feature('Test javascript on sql-ex.ru')
class TestSqlExPage:

    @allure.story('JavaScript')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title('Проверка очистки фокуса через JavaScript')
    def test_clean_focus_by_javascript(self, pages: PageFactory):
        with allure.step('Открыть страницу SqlEx'):
            sql_ex_page = pages.sqlex.open_page()

        with allure.step('Установить фокус на поле "Password"'):
            sql_ex_page.click_password_field()

        with allure.step('Получить текущий активный элемент'):
            active_element = sql_ex_page.get_active_element()

        with allure.step('Очистить фокус с активного элемента'):
            sql_ex_page.clear_focus_from_element()

        with allure.step('Проверить, что фокус убрался с активного элемента'):
            sql_ex_page.check_clean_focus_from_element(active_element)

    @allure.story('JavaScript')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title('Проверка наличия скролла на странице через JavaScript')
    def test_scroll_by_javascript(self, pages: PageFactory):
        with allure.step('Открыть страницу SqlEx'):
            sql_ex_page = pages.sqlex.open_page()

        with allure.step('Проверить, что страница имеет скролл'):
            sql_ex_page.check_page_has_scroll()
