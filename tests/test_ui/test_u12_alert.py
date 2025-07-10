import allure

from helpers.data_helpers import DataHelper
from pages.page_factory import PageFactory


@allure.epic('Web UI Tests')
@allure.feature('Alert Functionality')
class TestMainPage:

    @allure.story('Alert')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title('Проверка ввода текста в alert')
    def test_input_text_to_alert(self, pages: PageFactory):

        username = DataHelper.random_username()

        with allure.step('Открыть стартовую страницу'):
            alert_page = pages.alert_page.open_page()

        with allure.step('Нажать кнопку "INPUT ALERT"'):
            alert_page.click_input_alert_button()

        with allure.step('Перелючиться на iframe'):
            alert_page.switch_to_iframe()

        with allure.step('Нажать кнопку "click the button to demonstrate the input box"'):
            alert_page.click_button_to_demonstrate()

        with allure.step('Ввести текст в alert'):
            alert_page.intut_text_to_alert(username)

        with allure.step('Проверить результат ввода в alert'):
            alert_page.check_intut_alert_text(username)
