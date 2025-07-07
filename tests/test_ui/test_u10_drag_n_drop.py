import allure

from pages.page_factory import PageFactory


@allure.epic('Web UI Tests')
@allure.feature('Drag-N-Drop Functionality')
class TestMainPage:

    @allure.story('drag-n-drop')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title('Проверка состояния элемента после выполнения drag-ndrop')
    def test_drag_n_drop(self, pages: PageFactory):
        with allure.step('Открыть стартовую страницу'):
            droppable_page = pages.droppable_page.open_page()

        with allure.step('Перелючиться на iframe'):
            droppable_page.switch_to_iframe()

        with allure.step('Выполнить drag_n_drop элементов'):
            droppable_page.drag_n_drop_element()

        with allure.step('Проверить текст droppable-элемента'):
            droppable_page.check_droppable_field_text()
