import random

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from constants.constants import Constants
from helpers.data_helpers import DataHelper
from pages.base_page import BasePage


class BankingPage(BasePage):

    def __init__(self, browser):
        super().__init__(browser)

    ENDPOINT_URL = '/angularjs-protractor/banking/#/login'

    SAMPLE_FORM_BUTTON = (By.LINK_TEXT, 'Sample Form')
    BANK_MANAGER_LOGIN_BUTTON = (By.CSS_SELECTOR, 'button[ng-click="manager()"]')
    FIRST_NAME_FIELD = (By.ID, 'firstName')
    LAST_NAME_FIELD = (By.ID, 'lastName')
    EMAIL_FIELD = (By.ID, 'email')
    PASSWORD_FIELD = (By.ID, 'password')
    CHECKBOX_SPORT = (By.CSS_SELECTOR, 'input[value="Sports"]')
    GENDER_DROPDOWN = (By.ID, 'gender')
    HOBBIES_VALUES = (By.CSS_SELECTOR, 'input[name="hobbies"]')
    ABOUT_YOURSELF_AREA = (By.ID, 'about')
    CONFIRM_BUTTON = (By.CSS_SELECTOR, 'button[type="submit"]')
    SUCCESS_REGISTER_MESSAGE = (By.ID, 'successMessage')
    ADD_CUSTOMER_TAB = (By.CSS_SELECTOR, 'button[ng-click="addCust()"]')
    CUSTOMERS_TAB = (By.CSS_SELECTOR, 'button[ng-click="showCust()"]')
    OPEN_ACCOUNT_TAB = (By.CSS_SELECTOR, 'button[ng-click="openAccount()"]')
    CUSTOMER_FIRST_NAME_FIELD = (By.CSS_SELECTOR, 'input[ng-model="fName"]')
    CUSTOMER_LAST_NAME_FIELD = (By.CSS_SELECTOR, 'input[ng-model="lName"]')
    CUSTOMER_POSTCODE_FIELD = (By.CSS_SELECTOR, 'input[ng-model="postCd"]')
    CUSTOMER_DROPDOWN = (By.ID, 'userSelect')
    CURRENCY_DROPDOWN = (By.ID, 'currency')
    CUSTOMER_ROW_DELETE_BUTTON = (By.XPATH, './/button[contains(text(), "Delete")]')

    @allure.step('Открыть стартовую страницу')
    def open_page(self):
        url = self.get_full_url()
        self.browser.get(url)
        return self

    @allure.step('Нажать кнопку "SAMPLE BUTTON"')
    def click_sample_form_button(self):
        self.click_button(self.SAMPLE_FORM_BUTTON)

    @allure.step('Нажать кнопку "Bank Manager Login"')
    def click_bank_manager_login_button(self):
        self.click_button(self.BANK_MANAGER_LOGIN_BUTTON)

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

    @allure.step('Нажать кнопку подтверждения регистрации')
    def click_confirm_button(self):
        self.click_button(self.CONFIRM_BUTTON)

    @allure.step('Проверить появление сообщения "User registered successfully!"')
    def check_success_register_message(self):
        assert self.is_element_visible(self.SUCCESS_REGISTER_MESSAGE), \
            'Сообщение о успешной регистрации не отображается на странице'

    @allure.step('Нажать на вкладку "ADD CUSTOMER"')
    def click_add_customer_tab(self):
        self.click_button(self.ADD_CUSTOMER_TAB)

    @allure.step('Заполнить поле Customer "First Name"')
    def fill_customer_first_name_field(self, value):
        self.fill_field(self.CUSTOMER_FIRST_NAME_FIELD, value)

    @allure.step('Заполнить поле Customer "Last Name"')
    def fill_customer_last_name_field(self, value):
        self.fill_field(self.CUSTOMER_LAST_NAME_FIELD, value)

    @allure.step('Заполнить поле Customer "Postcode"')
    def fill_customer_postcode_field(self, value):
        self.fill_field(self.CUSTOMER_POSTCODE_FIELD, value)

    @allure.step('Проверить сообщение о успешной решистрации')
    def check_registration_alert_text(self):
        expected_text = Constants.CUSTOMER_REGISTRATION_TEXT
        self.check_alert_text(expected_text)

    @allure.step('Нажать на вкладку "Open Account"')
    def click_open_account_tab(self):
        self.click_button(self.OPEN_ACCOUNT_TAB)

    @allure.step('Выбрать созданного пользователя в списке "Customer"')
    def select_customer(self, customer):
        customer_dropdown = self.get_element(self.CUSTOMER_DROPDOWN)
        select_customer = Select(customer_dropdown)
        select_customer.select_by_visible_text(customer)

    @allure.step('Выбрать случайную валюту в поле "Currency"')
    def select_random_currency(self):
        currency_dropdown = self.get_element(self.CURRENCY_DROPDOWN)
        select_currency = Select(currency_dropdown)
        select_options = select_currency.options[1:]
        random_currency = (random.choice(select_options)).text
        select_currency.select_by_visible_text(random_currency)

    @allure.step('Проверить сообщение о успешного "Process"')
    def check_process_alert_text(self):
        expected_text = Constants.CUSTOMER_PROCESS_TEXT
        self.check_alert_text(expected_text)

    @allure.step('Нажать на вкладку "Customers"')
    def click_customers_tab(self):
        self.click_button(self.CUSTOMERS_TAB)

    @allure.step('Нажать на кнопку "Delete" У пользователя "{first_name} {last_name}"')
    def delete_customer(self, first_name, last_name):
        customer_row = self.browser.find_element(
            By.XPATH,
            f'//tr[contains(td[1], "{first_name}") and contains(td[2], "{last_name}")]'
        )
        button = customer_row.find_element(*self.CUSTOMER_ROW_DELETE_BUTTON)
        button.click()
