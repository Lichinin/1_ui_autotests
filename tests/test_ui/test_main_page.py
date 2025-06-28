import allure

from pages.main_page import MainPage


@allure.epic('Web UI Tests')
@allure.feature('Main Page Functionality')
class TestMainPage:

    @allure.story('Page elements')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title('Проверка основных элементов страницы')
    def test_page_elements_is_visible(self, main_page: MainPage):
        with allure.step('Проверить видимость header'):
            main_page.check_header_visible()

        with allure.step('Проверить видимость навигационной панели'):
            main_page.check_navbar_visible()

        with allure.step('Проверить видимость блока курсов'):
            main_page.check_best_courses_visible()

        with allure.step('Проверить видимость футера'):
            main_page.check_footer_visible()

    @allure.story('Register Button')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title('Проверка кнопки регистрации')
    def test_register_button_is_visible(self, main_page: MainPage):
        with allure.step('Проверить видимость кнопки регистрации'):
            main_page.check_register_button_visible()
        with allure.step('Проверить текст кнопки регистрации'):
            main_page.check_register_button_text()
        with allure.step('Проверить цвет фона кнопки регистрации'):
            main_page.check_register_button_background()

    @allure.story('Contacts Validation')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('Проверка контактов в хедере')
    def test_header_contacts(self, main_page: MainPage):
        with allure.step('Проверить количество контактов в header'):
            main_page.check_header_contacts_lenght()
        with allure.step('Проверить данные контактов в header'):
            main_page.check_header_contacts_data()

    @allure.story('Contacts Validation')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('Проверка контактов в футере')
    def test_footer_contacts(self, main_page: MainPage):
        with allure.step('Проверить количество контактов в footer'):
            main_page.check_footer_contacts_lenght()
        with allure.step('Проверить данные контактов в footer'):
            main_page.check_footer_contacts_data()

    # @allure.story('Slider Interaction')
    # @allure.severity(allure.severity_level.NORMAL)
    # @allure.title('Проверка работы слайдера популярных курсов')
    # def test_popular_courses_slider(self, main_page: MainPage):
    #     with allure.step('Прокрутить до слайдера "Most Popular"'):
    #         main_page.scroll_to_most_popular()
    #     main_page.close_popup()
    #     first_index = main_page.get_active_slide_index()

    #     with allure.step('Переключиться на следующий слайд'):
    #         main_page.click_next_slide()
    #     second_index = main_page.get_active_slide_index()

    #     with allure.step('Вернуться к предыдущему слайду)'):
    #         main_page.click_prev_slide()

    #     third_index = main_page.get_active_slide_index()

    #     with allure.step('Проверить переключения слайдера'):
    #         assert first_index == third_index and int(second_index) == int(first_index) + 1

    @allure.story('Best Courses')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title('Проверка блока "Best Selenium Certification Course Online"')
    def test_best_courses_menu(self, main_page: MainPage):
        with allure.step('Проверить видимость блока курсов'):
            main_page.check_best_courses_visible()

        with allure.step('Проверить количество курсов в блоке'):
            main_page.check_best_courses_lenght()

        with allure.step('Проверить данные карточек курсов'):
            main_page.check_best_courses_data()

    @allure.story('Navigation Menu')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title('Проверка меню после прокрутки вниз')
    def test_nav_menu_after_scroll(self, main_page: MainPage):
        with allure.step('Прокрутить до футера страницы'):
            main_page.scroll_to_footer()
        with allure.step('Проверить, что навигационная панель остаётся видимой'):
            main_page.check_navbar_visible()

    @allure.story('Navigation to Other Page')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title('Переход на страницу Lifetime Membership')
    def test_navigation_to_other_page(self, main_page: MainPage):
        with allure.step('Нажать на кнопку "All Courses"'):
            main_page.click_all_courses_button()
        with allure.step('Нажать на кнопку "Lifetime Membership"'):
            main_page.click_lifetime_membership_button()
        with allure.step('Проверить URL страницы'):
            main_page.check_url_lifetime_membership_page()
        with allure.step('Проверить заголовок страницы'):
            main_page.check_title_lifetime_membership_page()
