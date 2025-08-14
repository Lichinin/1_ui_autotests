import allure

from helpers.data_helpers import DataHelper
from pages.page_factory import PageFactory


@allure.epic('Web UI Tests')
@allure.feature('Bank Manager Forms')
class TestBankManager:

    @allure.story('Customers Transactions')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('5.3.1 Проверка успешного пополнения счета')
    def test_success_deposit(self, pages: PageFactory, setup_processed_customer):
        first_name = setup_processed_customer['first_name']
        last_name = setup_processed_customer['last_name']
        amount = '100321'

        with allure.step('1. Открыть стартовую страницу'):
            banking_page = pages.banking_page.open_page()

        with allure.step('2. Выбрать созданного пользователя'):
            banking_page.click_customer_login_button()
            banking_page.select_customer(f'{first_name} {last_name}')
            banking_page.click_confirm_button()
            banking_page.check_welcome_text(f'{first_name} {last_name}')

        with allure.step('3. Кликнуть кнопку "Deposit"'):
            banking_page.click_deposit_button()

        with allure.step('4. Заполнить поле "Amount"'):
            banking_page.fill_amount_field(amount)

        with allure.step('5. Кликнуть кнопку подтверждения "Deposit"'):
            banking_page.click_confirm_button()

        with allure.step('6. Проверить сообщение о успешном пополненни Deposit'):
            banking_page.check_deposit_success_message()

        with allure.step('7. Перейти в раздел транзакций'):
            banking_page.click_transactions_button()

        with allure.step('8. Проверить сумму транзакции'):
            banking_page.check_transaction_present(amount)

    @allure.story('Customers Transactions')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('5.3.2 Проверка неуспешного пополнения счета')
    def test_unsuccess_deposit(self, pages: PageFactory, setup_processed_customer):
        first_name = setup_processed_customer['first_name']
        last_name = setup_processed_customer['last_name']
        amount = '0'

        with allure.step('1. Открыть стартовую страницу'):
            banking_page = pages.banking_page.open_page()

        with allure.step('2. Выбрать созданного пользователя'):
            banking_page.click_customer_login_button()
            banking_page.select_customer(f'{first_name} {last_name}')
            banking_page.click_confirm_button()
            banking_page.check_welcome_text(f'{first_name} {last_name}')

        with allure.step('3. Кликнуть кнопку "Deposit"'):
            banking_page.click_deposit_button()

        with allure.step('4. Заполнить поле "Amount"'):
            banking_page.fill_amount_field(amount)

        with allure.step('5. Кликнуть кнопку подтверждения "Deposit"'):
            banking_page.click_confirm_button()

        with allure.step('6. Проверить отсутствие сообщения о успешном пополненни Deposit'):
            banking_page.check_no_deposit_success_message()

        with allure.step('7. Перейти в раздел транзакций'):
            banking_page.click_transactions_button()

        with allure.step('8. Проверить отсутствие пополнения на 0'):
            banking_page.check_transaction_absent(amount)

    @allure.story('Customers Transactions')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('5.3.3 Проверка успешного снятия средств')
    def test_success_withdrawl(self, pages: PageFactory, setup_processed_customer):
        first_name = setup_processed_customer['first_name']
        last_name = setup_processed_customer['last_name']
        deposit = '1000'

        with allure.step('1. Открыть стартовую страницу'):
            banking_page = pages.banking_page.open_page()

        with allure.step('2. Выбрать созданного пользователя'):
            banking_page.click_customer_login_button()
            banking_page.select_customer(f'{first_name} {last_name}')
            banking_page.click_confirm_button()
            banking_page.check_welcome_text(f'{first_name} {last_name}')

        with allure.step('3. Пополнить депозит пользователя'):
            banking_page.click_deposit_button()
            banking_page.fill_amount_field(deposit)
            banking_page.click_confirm_button()

        with allure.step('4. Получить значение баланса'):
            balance = banking_page.get_balance()

        with allure.step('5. Кликнуть кнопку "withdrawl"'):
            banking_page.click_withdrawl_button()

        with allure.step('6. Ввести сумму "withdrawl"'):
            withdrawl = DataHelper.get_valid_withdrawl_value(balance)
            banking_page.fill_withdrawl_field(withdrawl)

        with allure.step('7. Нажать кнопку подтверждения операции'):
            banking_page.click_confirm_button()

        with allure.step('8. Проверить сообщение о успешном снятии средств'):
            banking_page.check_withdrawl_success_message()

        with allure.step('9. Перейти в раздел транзакций'):
            banking_page.click_transactions_button()

        with allure.step('10. Проверить сумму списания в транзакциях'):
            banking_page.check_withdrawl_transaction_present(withdrawl)

    @allure.story('Customers Transactions')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('5.3.4 Проверка не успешного снятия средств')
    def test_unsuccess_withdrawl(self, pages: PageFactory, setup_processed_customer):
        first_name = setup_processed_customer['first_name']
        last_name = setup_processed_customer['last_name']
        withdrawl = '1000000'

        with allure.step('1. Открыть стартовую страницу'):
            banking_page = pages.banking_page.open_page()

        with allure.step('2. Выбрать созданного пользователя'):
            banking_page.click_customer_login_button()
            banking_page.select_customer(f'{first_name} {last_name}')
            banking_page.click_confirm_button()
            banking_page.check_welcome_text(f'{first_name} {last_name}')

        with allure.step('3. Кликнуть кнопку "withdrawl"'):
            banking_page.click_withdrawl_button()

        with allure.step('4. Ввести сумму "withdrawl"'):
            banking_page.fill_withdrawl_field(withdrawl)

        with allure.step('5. Назать кнопку подтверждения операции'):
            banking_page.click_confirm_button()

        with allure.step('6. Проверить появления сообщения об ошибке'):
            banking_page.check_withdrawl_failed_message()

        with allure.step('7. Перейти в раздел транзакций'):
            banking_page.click_transactions_button()

        with allure.step('8. Проверить отсутствие списания в транзакциях'):
            banking_page.check_withdrawl_transaction_absent(withdrawl)

    @allure.story('Customers Transactions')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('5.3.5 Проверка отображаемого и рассчитанного баланса')
    def test_balance(self, pages: PageFactory, setup_processed_customer):
        first_name = setup_processed_customer['first_name']
        last_name = setup_processed_customer['last_name']
        deposit = '1000'
        withdrawl = '333'

        with allure.step('1. Открыть стартовую страницу'):
            banking_page = pages.banking_page.open_page()

        with allure.step('2. Выбрать созданного пользователя'):
            banking_page.click_customer_login_button()
            banking_page.select_customer(f'{first_name} {last_name}')
            banking_page.click_confirm_button()

        with allure.step('3. Пополнить депозит пользователя'):
            banking_page.click_deposit_button()
            banking_page.fill_amount_field(deposit)
            banking_page.click_confirm_button()

        with allure.step('4. Снять средства с баланса'):
            banking_page.click_withdrawl_button()
            banking_page.fill_withdrawl_field(withdrawl)
            banking_page.click_confirm_button()

        with allure.step('5. Перезайти под пользователем для обновления баланса на странице'):
            banking_page.open_page()
            banking_page.click_customer_login_button()
            banking_page.select_customer(f'{first_name} {last_name}')
            banking_page.click_confirm_button()

        with allure.step('6. Получить значение баланса со страницы'):
            displayed_balance = banking_page.get_balance()

        with allure.step('7. Перейти в раздел транзакций'):
            banking_page.click_transactions_button()

        with allure.step('8. Рассчитать баланс из раздела транзакций'):
            calculated_balance = banking_page.calculate_balance()

        with allure.step('9.Сравнить рассчитанный баланс с отображаемым'):
            banking_page.check_balance(displayed_balance, calculated_balance)

    @allure.story('Customers Transactions')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('5.3.6 Проверка снятия всех доступных средств с баланса')
    def test_withdrawl_all_balance(self, pages: PageFactory, setup_processed_customer):
        first_name = setup_processed_customer['first_name']
        last_name = setup_processed_customer['last_name']
        deposit = '1000'
        withdrawl = '333'

        with allure.step('1. Открыть стартовую страницу'):
            banking_page = pages.banking_page.open_page()

        with allure.step('2. Выбрать созданного пользователя'):
            banking_page.click_customer_login_button()
            banking_page.select_customer(f'{first_name} {last_name}')
            banking_page.click_confirm_button()

        with allure.step('3. Пополнить депозит пользователя'):
            banking_page.click_deposit_button()
            banking_page.fill_amount_field(deposit)
            banking_page.click_confirm_button()

        with allure.step('4. Снять средства с баланса'):
            banking_page.click_withdrawl_button()
            banking_page.fill_withdrawl_field(withdrawl)
            banking_page.click_confirm_button()

        with allure.step('5. Обновить значение баланса'):
            banking_page.refresh_balance(first_name, last_name)

        with allure.step('6. Получить значение баланса со страницы'):
            balance = banking_page.get_balance()

        with allure.step('7. Снять все доступные средства'):
            banking_page.click_withdrawl_button()
            banking_page.fill_withdrawl_field(balance)
            banking_page.click_confirm_button()

        with allure.step('8. Проверить сообщение о успешном снятии средств'):
            banking_page.check_withdrawl_success_message()

        with allure.step('5. Обновить значение баланса'):
            banking_page.refresh_balance(first_name, last_name)

        with allure.step('10. Получить значение баланса со страницы'):
            balance = banking_page.get_balance()

        with allure.step('11. Проверить что баланс равен нулю'):
            banking_page.check_balance_null(balance)

    @allure.story('Customers Transactions')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('5.3.7 Проверка сброса всех транзакций')
    def test_clear_transaction(self, pages: PageFactory, setup_processed_customer):
        first_name = setup_processed_customer['first_name']
        last_name = setup_processed_customer['last_name']
        deposit = '1000'
        withdrawl = '333'

        with allure.step('1. Открыть стартовую страницу'):
            banking_page = pages.banking_page.open_page()

        with allure.step('2. Выбрать созданного пользователя'):
            banking_page.click_customer_login_button()
            banking_page.select_customer(f'{first_name} {last_name}')
            banking_page.click_confirm_button()

        with allure.step('3. Пополнить депозит пользователя'):
            banking_page.click_deposit_button()
            banking_page.fill_amount_field(deposit)
            banking_page.click_confirm_button()

        with allure.step('4. Снять средства с баланса'):
            banking_page.click_withdrawl_button()
            banking_page.fill_withdrawl_field(withdrawl)
            banking_page.click_confirm_button()

        with allure.step('5. Перейти в раздел транзакций'):
            banking_page.click_transactions_button()

        with allure.step('6. Получить количество транзакций'):
            transactions_count = banking_page.count_transactions()

        with allure.step('7. Проверить что количество транзакций не нулевое'):
            banking_page.check_transaction_count_not_null(transactions_count)

        with allure.step('7. Нажать кнопку "Reset"'):
            banking_page.click_reset_button()

        with allure.step('8. Получить количество транзакций'):
            transactions_count = banking_page.count_transactions()

        with allure.step('9. Проверить что количество транзакций равно нулю'):
            banking_page.check_transaction_count_is_null(transactions_count)

        with allure.step('10. Проверить что баланс равен нулю'):
            banking_page.click_back_button()
            balance = banking_page.get_balance()
            banking_page.check_balance_null(balance)
