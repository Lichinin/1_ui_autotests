from typing import Dict, List

import allure

from helpers.data_helpers import DataHelper
from pages.page_factory import PageFactory


@allure.epic('Web UI Tests')
@allure.feature('Bank Manager Forms')
class TestBankManager:

    @allure.story('Add new Bank Manager Customes')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('Проверка добавления Customer')
    def test_customer_add(self, customer_cleaner: List, pages: PageFactory):

        user_data = DataHelper.random_login_banking_page_data()
        first_name = user_data['first_name']
        last_name = user_data['last_name']
        postcode = user_data['postcode']
        customer_cleaner.append(user_data)

        with allure.step('1. Открыть стартовую страницу'):
            banking_page = pages.banking_page.open_page()

        with allure.step('2. Кликнуть кнопку "Bank Manager Login"'):
            banking_page.click_bank_manager_login_button()

        with allure.step('3. Кликнуть по вкладке "Add Customer"'):
            banking_page.click_add_customer_tab()

        with allure.step('4. Заполнить поле "First Name'):
            banking_page.fill_customer_first_name_field(first_name)

        with allure.step('5. Заполнить поле "Last Name'):
            banking_page.fill_customer_last_name_field(last_name)

        with allure.step('6. Заполнить поле "Post Code'):
            banking_page.fill_customer_postcode_field(postcode)

        with allure.step('7. Кликнуть кнопку "Add Customer"'):
            banking_page.click_confirm_button()

        with allure.step('8. Проверить сообщение всплывающего окна после нажатия "Add Customer"'):
            banking_page.check_registration_alert_text()

    @allure.story('Process new Bank Manager Customes')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('Проверка process созданного Customer')
    def test_customer_process(self, setup_not_processed_customer: Dict, pages: PageFactory):

        first_name = setup_not_processed_customer['first_name']
        last_name = setup_not_processed_customer['last_name']

        with allure.step('1. Открыть стартовую страницу'):
            banking_page = pages.banking_page.open_page()

        with allure.step('2. Кликнуть кнопку "Bank Manager Login"'):
            banking_page.click_bank_manager_login_button()

        with allure.step('9. Кликнуть по вкладке "Open Account"'):
            banking_page.click_open_account_tab()

        with allure.step('10. Выбрать созданного ранее пользователя в списке Customer'):
            banking_page.select_customer(f'{first_name} {last_name}')

        with allure.step('11. Выбрать валюту в поле "Currency"'):
            banking_page.select_random_currency()

        with allure.step('12. Нажать кнопку "Process"'):
            banking_page.click_confirm_button()

        with allure.step('13. Проверить сообщение всплывающего окна после нажатия "Process"'):
            banking_page.check_process_alert_text()
