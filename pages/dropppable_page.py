import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class DroppablePage(BasePage):

    def __init__(self, browser):
        super().__init__(browser)

    ENDPOINT_URL = '/way2auto_jquery/droppable.php#load_box'

    IFRAME = (By.CSS_SELECTOR, 'iframe[src="droppable/default.html"]')
    DROPPABLE_ELEMENT = (By.ID, 'droppable')
    DRAGABLE_ELEMENT = (By.ID, 'draggable')

    @allure.step('Открыть стартовую страницу')
    def open_page(self):
        url = self.get_full_url()
        self.browser.get(url)
        return self

    @allure.step('Перелючиться на iframe')
    def switch_to_iframe(self):
        iframe = self.get_element(self.IFRAME)
        self.browser.switch_to.frame(iframe)

    @allure.step('Получить текст droppable-элемента')
    def get_droppable_field_text(self):
        return self.get_element(self.DROPPABLE_ELEMENT).text

    @allure.step('Кликнуть draggable-элемент и перетащить его на droppable-элемент')
    def drag_n_drop_element(self):
        draggable = self.get_element(self.DRAGABLE_ELEMENT)
        droppable = self.get_element(self.DROPPABLE_ELEMENT)
        self.drag_n_drop(draggable, droppable)

    @allure.step('Проверить текст droppable-элемента')
    def check_droppable_field_text(self):
        expected_text = 'Dropped!'
        self.check_element_text(
            self.DROPPABLE_ELEMENT,
            expected_text
        )
