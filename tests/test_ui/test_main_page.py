import allure

from constants.constants import Constants
from helpers.assertion_helpers import AssertionHelper
from helpers.data_helpers import DataHelper
from pages.main_page import MainPage


@allure.epic('Web UI Tests')
@allure.feature('Main Page Functionality')
class TestMainPage:

    @allure.story('Header Section')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title('Проверка видимости header страницы')
    def test_header_is_visible(self, main_page: MainPage):
        assert main_page.get_element(MainPage.HEADER)

    @allure.story('Navigation Bar')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title('Проверка видимости навигационной панели')
    def test_navbar_is_visible(self, main_page: MainPage):
        assert main_page.get_element(MainPage.NAV_BAR)

    @allure.story('Register Button')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title('Проверка видимости кнопки регистрации')
    def test_register_button_is_visible(self, main_page: MainPage):
        assert main_page.get_element(MainPage.REGISTER_BUTTON)

    @allure.story('Courses Section')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title('Проверка видимости блока курсов')
    def test_courses_list_is_visible(self, main_page: MainPage):
        assert main_page.get_element(MainPage.COURSES_LIST)

    @allure.story('Footer Section')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title('Проверка видимости футера')
    def test_footer_is_visible(self, main_page: MainPage):
        assert main_page.get_element(MainPage.FOOTER)

    @allure.story('Contacts Validation')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('Проверка контактов в хедере')
    def test_header_contacts(self, main_page: MainPage):
        contacts = DataHelper.get_contacts_values(main_page)
        assert contacts == Constants.HEADER_CONTACTS

    @allure.story('Contacts Validation')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('Проверка контактов в футере')
    def test_footer_contacts(self, main_page: MainPage):
        contacts = DataHelper.get_footer_contacts_values(main_page)
        AssertionHelper.assert_footer_contact(contacts)

    @allure.story('Slider Interaction')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title('Проверка работы слайдера популярных курсов')
    def test_popular_courses_slider(self, main_page: MainPage):
        with allure.step('Прокрутить до слайдера "Most Popular"'):
            main_page.scroll_to(main_page.get_element(MainPage.SLIDER_MOST_POPULAR))
        main_page.close_popup()
        first_index = main_page.get_active_slide_index()

        with allure.step('Переключиться на следующий слайд'):
            main_page.click_next_slide()
        second_index = main_page.get_active_slide_index()

        with allure.step('Вернуться к предыдущему слайду)'):
            main_page.click_prev_slide()

        third_index = main_page.get_active_slide_index()

        with allure.step('Проверить переключения слайдера'):
            assert first_index == third_index and int(second_index) == int(first_index) + 1

    @allure.story('Navigation Menu')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title('Проверка меню после прокрутки вниз')
    def test_nav_menu_after_scroll(self, main_page: MainPage):
        with allure.step('Прокрутить до футера страницы'):
            main_page.scroll_to(main_page.get_element(MainPage.FOOTER))
        with allure.step('Проверить, что навигационная панель остаётся видимой'):
            assert main_page.get_element(MainPage.NAV_BAR)

    @allure.story('Navigation to Other Page')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title('Переход на страницу Lifetime Membership')
    def test_navigation_to_other_page(self, main_page: MainPage):
        with allure.step('Нажать на кнопку "All Courses"'):
            main_page.click_button(main_page.ALL_COURSES_BUTTON)

        with allure.step('Нажать на кнопку "Lifetime Membership"'):
            main_page.click_button(main_page.LIFETIME_MEMBERSHIP_BUTTON)
        with allure.step('Проверить URL страницы'):
            assert main_page.get_current_url() == Constants.LIFETIME_MEMEDERSHIP_URL
        with allure.step('Проверить заголовок страницы'):
            assert Constants.LIFETIME_MEMEDERSHIP_PAGE_TITLE in main_page.get_page_title()
