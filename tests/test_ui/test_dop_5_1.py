import allure

from helpers.data_helpers import DataHelper
from pages.page_factory import PageFactory


@allure.epic('Web UI Tests')
@allure.feature('Forms')
class TestBankingPage:

    @allure.story('Registration')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('Проверка регистрации Sample Form')
    def test_registration(self, pages: PageFactory):
        user_data = DataHelper.random_login_banking_page_data()
        first_name = user_data['first_name']
        last_name = user_data['last_name']
        email = user_data['email']
        password = user_data['password']

        with allure.step('1. Открыть стартовую страницу'):
            banking_page = pages.banking_page.open_page()

        with allure.step('2. Кликнуть кнопку "SAMPLE FORM"'):
            banking_page.click_sample_form_button()

        with allure.step('3. Заполнить поле "First Name"'):
            banking_page.fill_first_name_field(first_name)

        with allure.step('4. Заполнить поле "Last Name"'):
            banking_page.fill_last_name_field(last_name)

        with allure.step('5. Заполнить поле "Email"'):
            banking_page.fill_email_field(email)

        with allure.step('6. Заполнить поле "Password"'):
            banking_page.fill_password_field(password)

        with allure.step('7. Выбрать в "Hobbies" значение "Sports"'):
            banking_page.check_sports()

        with allure.step('8. Выбрать в "Gender" значение "Male"'):
            banking_page.select_gender('Male')

        with allure.step('9. Заполнить "About Yourself"'):
            banking_page.fill_about_yourself()

        with allure.step('10. Кликнуть кнопку "Register"'):
            banking_page.click_confirm_button()

        with allure.step('11. Проверить появление сообщения о успешной регистрации'):
            banking_page.check_success_register_message()
