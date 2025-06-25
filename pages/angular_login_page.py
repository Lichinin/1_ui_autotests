from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class AngularPage(BasePage):

    ENDPOINT_URL = '/angularjs-protractor/registeration/#/login'
    
    LOGIN_FIELD = (By.ID, 'username')
    LOGIN_DESCRIPTION_FIELD = (By.ID, 'formly_1_input_username_0')
    PASSWORD_FIELD = (By.ID, 'password')
    LOGIN_BUTTON = (By. CLASS_NAME, 'btn-danger')
    LOGIN_MESSAGE_SUCCESS = (By.CSS_SELECTOR, 'p.ng-scope')
    LOGOUT_LINK = (By.CSS_SELECTOR, 'a[href="#/login"]')
    DANGER_ALERT = (By.CLASS_NAME, 'alert-danger ')

    def get_sucessful_login_text(self):
        self.get_element(self.LOGOUT_LINK)
        text = self.get_element(self.LOGIN_MESSAGE_SUCCESS).text
        return text

    def get_unsucessful_login_text(self):
        self.get_element(self.DANGER_ALERT)
        text = self.get_element(self.DANGER_ALERT).text
        return text
