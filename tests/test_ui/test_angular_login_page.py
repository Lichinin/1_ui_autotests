from pages.angular_login_page import AngularPage


class TestAngularLoginPage:

    def test_username_is_visible(self, angular_page: AngularPage):
        assert angular_page.LOGIN_FIELD

    def test_password_is_visible(self, angular_page: AngularPage):
        assert angular_page.PASSWORD_FIELD

    def test_login_button_is_disabled(self, angular_page: AngularPage):
        login_button = angular_page.get_element(AngularPage.LOGIN_BUTTON)
        assert login_button.get_attribute('disabled') == 'true'

    def test_valid_autorization(self, angular_page: AngularPage):
        angular_page.fill_field(angular_page.LOGIN_FIELD, 'angular')
        angular_page.fill_field(angular_page.PASSWORD_FIELD, 'password')
        angular_page.fill_field(angular_page.LOGIN_DESCRIPTION_FIELD, 'angular')
        angular_page.get_element(angular_page.LOGIN_BUTTON).click()
        text = angular_page.get_sucessful_login_text()
        assert text == "You're logged in!!"

    def test_invalid_autorization(self, angular_page: AngularPage):
        angular_page.fill_field(angular_page.LOGIN_FIELD, 'angudlar')
        angular_page.fill_field(angular_page.PASSWORD_FIELD, 'password')
        angular_page.fill_field(angular_page.LOGIN_DESCRIPTION_FIELD, 'angular')
        angular_page.get_element(angular_page.LOGIN_BUTTON).click()
        text = angular_page.get_unsucessful_login_text()
        assert text == "Username or password is incorrect"

    def test_logout(self, angular_page: AngularPage):
        angular_page.fill_field(angular_page.LOGIN_FIELD, 'angular')
        angular_page.fill_field(angular_page.PASSWORD_FIELD, 'password')
        angular_page.fill_field(angular_page.LOGIN_DESCRIPTION_FIELD, 'angular')
        angular_page.get_element(angular_page.LOGIN_BUTTON).click()
        angular_page.get_element(angular_page.LOGOUT_LINK).click()
        assert angular_page.get_element(angular_page.LOGIN_FIELD)
        assert angular_page.get_element(angular_page.PASSWORD_FIELD)
