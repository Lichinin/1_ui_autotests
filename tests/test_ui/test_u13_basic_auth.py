import allure

from helpers.data_helpers import DataHelper
from pages.page_factory import PageFactory


@allure.epic('Web UI Tests')
@allure.feature('Basic auth')
class TestMainPage:

    @allure.story('Basic auth')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title('Проверка авторизации (Basic Auth)')
    def test_basic_auth(self, pages: PageFactory):
        username = DataHelper.get_from_env('BASIC_AUTH_LOGIN')
        password = DataHelper.get_from_env('BASIC_AUTH_PASSWORD')

        with allure.step('Открыть стартовую страницу'):
            basic_auth = pages.basic_auth.open_page()

        with allure.step('Нажать кнопку "DISPLAY IMAGE"'):
            basic_auth.click_display_image_button()

        with allure.step('Передать данные авторизации'):
            basic_auth.fill_credentials_and_refresh(username, password)

        with allure.step('Повторно нажать кнопку "DISPLAY IMAGE"'):
            basic_auth.click_display_image_button()

        with allure.step('Проверить, что изображение отображается на странице'):
            basic_auth.check_image_is_visible()
