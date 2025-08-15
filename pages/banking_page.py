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
    CUSTOMER_LOGIN_BUTTON = (By.CSS_SELECTOR, 'button[ng-click="customer()"]')
    WELCOME_TEXT = (By.XPATH, '//strong[contains(., "Welcome")]')
    TRANSACTIONS_BUTTON = (By.CSS_SELECTOR, 'button[ng-click="transactions()"]')
    DEPOSIT_BUTTON = (By.CSS_SELECTOR, 'button[ng-click="deposit()"]')
    WITHDRAWL_BUTTON = (By.CSS_SELECTOR, 'button[ng-click="withdrawl()"]')
    AMOUNT_FIELD = (By.CSS_SELECTOR, 'input[ng-model="amount"]')
    DEPOSIT_MESSAGE = (By.CSS_SELECTOR, 'span.error')
    TRANSACTIONS_AMOUNT = (By.CSS_SELECTOR, 'tbody tr td:nth-of-type(2)')
    TABLE = (By.CSS_SELECTOR, 'table.table')
    ACCOUNT_INFO = (By.CSS_SELECTOR, 'div[ng-hide="noAccount"]')
    DEBIT_COLUMN = (By.XPATH, './/tr[td[3][contains(text(), "Debit")]]/td[2]')
    CREDIT_COLUMN = (By.XPATH, './/tr[td[3][contains(text(), "Credit")]]/td[2]')
    ANY_COLUMN = (By.XPATH, './/tbody//tr/td[2]')
    RESET_BUTTON = (By.CSS_SELECTOR, 'button[ng-click="reset()"]')
    BACK_BUTTON = (By.CSS_SELECTOR, 'button[ng-click="back()"]')

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
        customer_table = self.get_element(self.TABLE)
        customer_row = customer_table.find_element(
            By.XPATH,
            f'//tr[contains(td[1], "{first_name}") and contains(td[2], "{last_name}")]'
        )
        button = customer_row.find_element(*self.CUSTOMER_ROW_DELETE_BUTTON)
        button.click()

    @allure.step('Нажать кнопку "Customer Login"')
    def click_customer_login_button(self):
        self.click_button(self.CUSTOMER_LOGIN_BUTTON)

    @allure.step('Проверить, что сообщение приветствия соответствует выбранному пользователю')
    def check_welcome_text(self, username):
        expected_text = f'Welcome {username} !!'
        self.check_element_text(self.WELCOME_TEXT, expected_text)

    @allure.step('Нажать кнопку "Transactions"')
    def click_transactions_button(self):
        self.browser.refresh()
        self.click_button(self.TRANSACTIONS_BUTTON)

    @allure.step('Нажать кнопку "Deposit"')
    def click_deposit_button(self):
        self.click_button(self.DEPOSIT_BUTTON)

    @allure.step('Нажать кнопку "Withdrawl"')
    def click_withdrawl_button(self):
        self.browser.refresh()
        self.click_button(self.WITHDRAWL_BUTTON)

    @allure.step('Заполнить поле "amount" значением "{value}"')
    def fill_amount_field(self, value):
        self.fill_field(self.AMOUNT_FIELD, value)

    @allure.step('Проверить что вернулось сообщение "Deposit Successful"')
    def check_deposit_success_message(self):
        expected_message = 'Deposit Successful'
        self.check_element_text(self.DEPOSIT_MESSAGE, expected_message)

    @allure.step('Проверить что сообщение "Deposit Successful" нет')
    def check_no_deposit_success_message(self):
        assert not self.is_element_visible(self.DEPOSIT_MESSAGE), \
            'Сообщение о успешном пополнении депопиза отображается'

    @allure.step('Проверить что транзакция со значением"{amount}" присутствует в списке')
    def check_transaction_present(self, amount):
        transaction_table = self.get_element(self.TABLE)
        transactions_credit_raw = transaction_table.find_elements(*self.CREDIT_COLUMN)
        transactions_credit = [amount.text for amount in transactions_credit_raw]
        assert amount in transactions_credit, \
            f'Транзакция на сумму {amount}, отсутствует в списке транзакций: {transactions_credit}'

    @allure.step('Проверить что транзакция со значением"{amount}" отсутствует в списке')
    def check_transaction_absent(self, amount):
        transaction_table = self.get_element(self.TABLE)
        transactions_credit_raw = transaction_table.find_elements(*self.CREDIT_COLUMN)
        transactions_credit = [amount.text for amount in transactions_credit_raw]
        assert amount not in transactions_credit, \
            f'Транзакция на сумму {amount}, присутствует в списке транзакций: {transactions_credit}'

    @allure.step('Получить значение баланса Customer')
    def get_balance(self):
        account_info = self.get_element_text(self.ACCOUNT_INFO)
        account_balance = account_info.split()[7]
        return account_balance

    @allure.step('Заполнить значение withdrawl рандобной суммой, не больше баланса')
    def fill_withdrawl_field(self, value):
        self.fill_field(self.AMOUNT_FIELD, value)

    @allure.step('Проверить что вернулось сообщение "Transaction successful"')
    def check_withdrawl_success_message(self):
        expected_message = 'Transaction successful'

        self.check_element_text(self.DEPOSIT_MESSAGE, expected_message)

    @allure.step('Проверить что транзакция со значением"{withdrawl}" присутствует в списке')
    def check_withdrawl_transaction_present(self, withdrawl):
        transaction_table = self.get_element(self.TABLE)
        transactions_debit_raw = transaction_table.find_elements(*self.DEBIT_COLUMN)
        transactions_debit = [amount.text for amount in transactions_debit_raw]
        assert withdrawl in transactions_debit, \
            f'Транзакция на сумму {withdrawl}, отсутствует в списке транзакций: {transactions_debit}'

    @allure.step('Проверить что транзакция со значением"{withdrawl}" отсутствует в списке')
    def check_withdrawl_transaction_absent(self, withdrawl):
        transaction_table = self.get_element(self.TABLE)
        transactions_debit_raw = transaction_table.find_elements(*self.DEBIT_COLUMN)
        transactions_debit = [amount.text for amount in transactions_debit_raw]
        assert withdrawl not in transactions_debit, \
            f'Транзакция на сумму {withdrawl}, отсутствует в списке транзакций: {transactions_debit}'

    @allure.step('Проверить что вернулось сообщение о ошибке снятия средств')
    def check_withdrawl_failed_message(self):
        expected_message = 'Transaction Failed. You can not withdraw amount more than the balance.'
        self.check_element_text(self.DEPOSIT_MESSAGE, expected_message)

    @allure.step('Получить все операции из транзакций и рассчитать баланс')
    def calculate_balance(self):
        transaction_table = self.get_element(self.TABLE)

        transactions_debit_raw = transaction_table.find_elements(*self.DEBIT_COLUMN)
        transactions_debit = [int(amount.text) for amount in transactions_debit_raw]

        transactions_credit_raw = transaction_table.find_elements(*self.CREDIT_COLUMN)
        transactions_credit = [int(amount.text) for amount in transactions_credit_raw]

        calculated_balance = sum(transactions_credit) - sum(transactions_debit)
        return calculated_balance

    @allure.step('Сравнить отображаемое значение баланса с рассчетным')
    def check_balance(self, displayed_balance, calculated_balance):
        assert int(displayed_balance) == int(calculated_balance), \
            f'Отображаемый баланс ({displayed_balance}) не соответствует рассчитанному ({calculated_balance})'

    @allure.step('Проверить, чо значение баланса равно нулю')
    def check_balance_null(self, balance):
        assert balance == '0', \
            f'Ожидалось значение баланса равное "0", получено "{balance}"'

    @allure.step('Подсчитать количество транзакций')
    def count_transactions(self):
        transaction_table = self.get_element(self.TABLE)
        transactions_raw = transaction_table.find_elements(*self.ANY_COLUMN)
        return len(transactions_raw)

    @allure.step('Проверить, что количество транзакций не равно нулю')
    def check_transaction_count_not_null(self, transaction_count):
        assert transaction_count != 0, \
            'Ожидается количество транзакций не равное нулю, получено "0"'

    @allure.step('Нажать кнопку "Reset"')
    def click_reset_button(self):
        self.click_button(self.RESET_BUTTON)

    @allure.step('Нажать кнопку "Back"')
    def click_back_button(self):
        self.click_button(self.BACK_BUTTON)

    @allure.step('Проверить, что количество транзакций равно нулю')
    def check_transaction_count_is_null(self, transaction_count):
        assert transaction_count == 0, \
            f'Ожидается количество транзакций равное нулю, получено "{transaction_count}"'

    @allure.step('Перезайти под выбранным бользователем для обновления баланса')
    def refresh_user_balance(self, first_name, last_name):
        self.open_page()
        self.click_customer_login_button()
        self.select_customer(f'{first_name} {last_name}')
        self.click_confirm_button()
