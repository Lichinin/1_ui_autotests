import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from helpers.data_helpers import DataHelper
from pages.base_page import BasePage


class BankingPage(BasePage):

    def __init__(self, browser):
        super().__init__(browser)

    ENDPOINT_URL = '/angularjs-protractor/banking/#/login'

    SAMPLE_FORM_BUTTON = (By.LINK_TEXT, 'Sample Form')
    FIRST_NAME_FIELD = (By.ID, 'firstName')
    LAST_NAME_FIELD = (By.ID, 'lastName')
    EMAIL_FIELD = (By.ID, 'email')
    PASSWORD_FIELD = (By.ID, 'password')
    CHECKBOX_SPORT = (By.CSS_SELECTOR, 'input[value="Sports"]')
    GENDER_DROPDOWN = (By.ID, 'gender')
    HOBBIES_VALUES = (By.CSS_SELECTOR, 'input[name="hobbies"]')
    ABOUT_YOURSELF_AREA = (By.ID, 'about')
    REGISTER_BUTTON = (By.CSS_SELECTOR, 'button[type="submit"]')
    SUCCESS_REGISTER_MESSAGE = (By.ID, 'successMessage')

    @allure.step('Открыть стартовую страницу')
    def open_page(self):
        url = self.get_full_url()
        self.browser.get(url)
        return self

    @allure.step('Нажать кнопку "SAMPLE BUTTON"')
    def click_sample_form_button(self):
        self.click_button(self.SAMPLE_FORM_BUTTON)

    @allure.step('Заполнить поле "First Name"')
    def fill_first_name_field(self, value):
        self.fill_field(self.FIRST_NAME_FIELD, value)

    @allure.step('Заполнить поле "Last Name"')
    def fill_last_name_field(self, value):
        self.fill_field(self.LAST_NAME_FIELD, value)

    @allure.step('Заполнить поле "Email"')
    def fill_email_field(self, value):
        self.fill_field(self.EMAIL_FIELD, value)

    @allure.step('Заполнить поле "Password"')
    def fill_password_field(self, value):
        self.fill_field(self.PASSWORD_FIELD, value)

    @allure.step('Кликнуть чекбокс "Sports"')
    def check_sports(self):
        self.click_button(self.CHECKBOX_SPORT)

    @allure.step('Выбрать значение в списке "Gender"')
    def select_gender(self, gender):
        gender_dropdown = self.get_element(self.GENDER_DROPDOWN)
        select_gender = Select(gender_dropdown)
        select_gender.select_by_value(gender.lower())

    @allure.step('Заполнить поле "About Yourself"')
    def fill_about_yourself(self):
        hobbies = self.get_elements(self.HOBBIES_VALUES)
        longest_hobbie = DataHelper.get_longest_hobbie(hobbies)
        self.fill_field(self.ABOUT_YOURSELF_AREA, longest_hobbie)

    @allure.step('Нажать кнопку "Register"')
    def click_register_button(self):
        self.click_button(self.REGISTER_BUTTON)

    @allure.step('Проверить появление сообщения "User registered successfully!"')
    def check_success_register_message(self):
        assert self.is_element_visible(self.SUCCESS_REGISTER_MESSAGE), \
            'Сообщение о успешной регистрации не отображается на странице'
