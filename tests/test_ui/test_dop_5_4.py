import allure

from pages.page_factory import PageFactory


@allure.epic('Web UI Tests')
@allure.feature('Bank Manager Forms')
class TestBankManager:

    @allure.story('Customers Transactions')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('5.4 Проверка удаления customer')
    def test_customer_delete(self, pages: PageFactory, setup_processed_customer):
        first_name = setup_processed_customer['first_name']
        last_name = setup_processed_customer['last_name']

        with allure.step('1. Открыть стартовую страницу'):
            banking_page = pages.banking_page.open_page()

        with allure.step('2. Перейти на страницу "Bank Manager login"'):
            banking_page.click_bank_manager_login_button()

        with allure.step('3. Нажать вкладку "Customers"'):
            banking_page.click_customers_tab()

        with allure.step('4. В строке поиска ввести имя созданного customer'):
            banking_page.searh_customer(first_name)

        with allure.step('5. Проверить что customer отображается в результатах поиска'):
            banking_page.check_customer_in_table(first_name, last_name)

        with allure.step('6. Нажать кнопку "Delete" у найденного customer'):
            banking_page.delete_customer(first_name, last_name)

        with allure.step('7. Очистить поле поиска'):
            banking_page.clear_search_field()

        with allure.step('8. Проверить что в списке customers нет удаленного customer'):
            banking_page.check_customer_not_in_table(first_name, last_name)
