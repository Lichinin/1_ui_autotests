from pages.angular_login_page import AngularPage
from constants.constants import Constants


class TestAngularLoginPage:

    def test_username_is_visible(self, angular_page: AngularPage):
        assert angular_page.LOGIN_FIELD

    def test_password_is_visible(self, angular_page: AngularPage):
        assert angular_page.PASSWORD_FIELD

    def test_login_button_is_disabled(self, angular_page: AngularPage):
        login_button = angular_page.get_element(AngularPage.LOGIN_BUTTON)
        assert login_button.get_attribute('disabled') == 'true'

    def test_valid_autorization(self, angular_page: AngularPage):
        angular_page.fill_field(angular_page.LOGIN_FIELD, Constants.ANGULAR_VALID_LOGIN)
        angular_page.fill_field(angular_page.PASSWORD_FIELD, Constants.ANGULAR_VALID_PASS)
        angular_page.fill_field(angular_page.LOGIN_DESCRIPTION_FIELD, Constants.ANGULAR_VALID_DESC)
        angular_page.get_element(angular_page.LOGIN_BUTTON).click()
        text = angular_page.get_sucessful_login_text()
        assert text == Constants.ANGULAR_SUCCESS_LOGIN_TEXT

    def test_invalid_autorization(self, angular_page: AngularPage):
        angular_page.fill_field(angular_page.LOGIN_FIELD, Constants.ANGULAR_INVALID_LOGIN)
        angular_page.fill_field(angular_page.PASSWORD_FIELD, Constants.ANGULAR_VALID_PASS)
        angular_page.fill_field(angular_page.LOGIN_DESCRIPTION_FIELD, Constants.ANGULAR_VALID_DESC)
        angular_page.get_element(angular_page.LOGIN_BUTTON).click()
        text = angular_page.get_unsucessful_login_text()
        assert text == Constants.ANGULAR_UNSUCCESS_LOGIN_TEXT

    def test_logout(self, angular_page: AngularPage):
        angular_page.fill_field(angular_page.LOGIN_FIELD, Constants.ANGULAR_VALID_LOGIN)
        angular_page.fill_field(angular_page.PASSWORD_FIELD, Constants.ANGULAR_VALID_PASS)
        angular_page.fill_field(angular_page.LOGIN_DESCRIPTION_FIELD, Constants.ANGULAR_VALID_DESC)
        angular_page.get_element(angular_page.LOGIN_BUTTON).click()
        angular_page.get_element(angular_page.LOGOUT_LINK).click()
        assert angular_page.get_element(angular_page.LOGIN_FIELD)
        assert angular_page.get_element(angular_page.PASSWORD_FIELD)
