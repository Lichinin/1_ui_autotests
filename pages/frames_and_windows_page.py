import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class FramesAndWindowsPage(BasePage):

    def __init__(self, browser):
        super().__init__(browser)

    ENDPOINT_URL = '/way2auto_jquery/frames-and-windows.php#load_box'

    IFRAME = (By.CSS_SELECTOR, 'iframe[src="frames-windows/defult1.html"]')
    NEW_TAB_LINK = (By.LINK_TEXT, "New Browser Tab")

    @allure.step('Открыть стартовую страницу')
    def open_page(self):
        url = self.get_full_url()
        self.browser.get(url)
        return self

    @allure.step('Перелючиться на iframe')
    def switch_to_iframe(self):
        iframe = self.get_element(self.IFRAME)
        self.browser.switch_to.frame(iframe)

    @allure.step('Нажать ссылку " New browser tab"')
    def click_new_tab_link(self):
        self.click_button(self.NEW_TAB_LINK)

    @allure.step('Проверить, что открыто 3 вкладки')
    def check_number_of_tab(self):
        tabs = self.browser.window_handles
        excpected_number_of_tabs = 3
        self.check_element_list_lenght(tabs, excpected_number_of_tabs)

    @allure.step('Проверить title открытой вкладки')
    def check_tab_title(self):
        actual_title = self.get_page_title()
        expected_title = 'JQUERY UI DATEPICKER - DEFAULT FUNCTIONALITY'
        assert actual_title == expected_title, \
            f'Ожидался title страницы "{expected_title}", получен "{actual_title}"'
