from constants.constants import Constants
from helpers.assertion_helpers import AssertionHelper
from helpers.data_helpers import DataHelper
from pages.main_page import MainPage


class TestMainPage:

    def test_header_is_visible(self, main_page: MainPage):
        assert main_page.get_element(MainPage.HEADER)

    def test_navbar_is_visible(self, main_page: MainPage):
        assert main_page.get_element(MainPage.NAV_BAR)

    def test_register_button_is_visible(self, main_page: MainPage):
        assert main_page.get_element(MainPage.REGISTER_BUTTON)

    def test_courses_list_is_visible(self, main_page: MainPage):
        assert main_page.get_element(MainPage.COURSES_LIST)

    def test_footer_is_visible(self, main_page: MainPage):
        assert main_page.get_element(MainPage.FOOTER)

    def test_header_contacts(self, main_page: MainPage):
        contacts = DataHelper.get_contacts_values(main_page)
        assert contacts == Constants.HEADER_CONTACTS

    def test_footer_contacts(self, main_page: MainPage):
        contacts = DataHelper.get_footer_contacts_values(main_page)
        AssertionHelper.assert_footer_contact(contacts)

    def test_popular_courser_slider(self, main_page: MainPage):
        main_page.scroll_to(main_page.get_element(MainPage.SLIDER_MOST_POPULAR))
        main_page.close_popup()
        first_index = main_page.get_active_slide_index()

        main_page.click_next_slide()

        second_index = main_page.get_active_slide_index()
        main_page.click_prev_slide()

        third_index = main_page.get_active_slide_index()

        assert first_index == third_index and int(second_index) == int(first_index) + 1

    def test_nav_menu_after_scroll(self, main_page: MainPage):
        main_page.scroll_to(main_page.get_element(MainPage.FOOTER))
        assert main_page.get_element(MainPage.NAV_BAR)

    def test_navigation_to_other_page(self, main_page: MainPage):
        main_page.click_button(main_page.ALL_COURSES_BUTTON)
        main_page.click_button(main_page.LIFETIME_MEMBERSHIP_BUTTON)
        assert main_page.browser.current_url == Constants.LIFETIME_MEMEDERSHIP_URL
        assert Constants.LIFETIME_MEMEDERSHIP_PAGE_TITLE in main_page.browser.title.upper()
