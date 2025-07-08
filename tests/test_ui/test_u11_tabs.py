import allure

from pages.page_factory import PageFactory


@allure.epic('Web UI Tests')
@allure.feature('Tabs Functionality')
class TestMainPage:

    @allure.story('Tabs')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title('Проверка перехода по вкладкам браузера')
    def test_drag_n_drop(self, pages: PageFactory):
        with allure.step('Открыть стартовую страницу'):
            frame_and_windows_page = pages.frame_and_windows_page.open_page()

        with allure.step('Перелючиться на iframe'):
            frame_and_windows_page.switch_to_iframe()

        with allure.step('Нажать кнопку "New Browser Tab"'):
            frame_and_windows_page.click_new_tab_link()

        with allure.step('Переключиться на вторую вкладку'):
            frame_and_windows_page.switch_to_tab(2)

        with allure.step('Нажать кнопку "New Browser Tab"'):
            frame_and_windows_page.click_new_tab_link()

        with allure.step('Переключиться на третью вкладку'):
            frame_and_windows_page.switch_to_tab(3)

        with allure.step('Проверить количество открытых вкладок'):
            frame_and_windows_page.check_number_of_tab()

        with allure.step('Проверить title третьей вкладки'):
            frame_and_windows_page.check_tab_title()
