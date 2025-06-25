from pages.main_page import MainPage
from helpers.data_helpers import DataHelper
from helpers.assertion_helpers import AssertionHelper
from constants.constants import Constants


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
        main_page.scroll_to(main_page.get_element(MainPage.ACTIVE_SLIDE))
        first_active_slide = main_page.get_element(MainPage.ACTIVE_SLIDE)
        main_page.get_element(MainPage.NEXT_SLIDE_BUTTON).click()
        second_active_slide = main_page.get_element(MainPage.ACTIVE_SLIDE)
        main_page.get_element(MainPage.PREVIOUS_SLIDE_BUTTON).click()
        third_active_slide = main_page.get_element(MainPage.ACTIVE_SLIDE)
        assert first_active_slide == third_active_slide
