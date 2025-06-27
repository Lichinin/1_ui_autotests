import allure
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage


class MainPage(BasePage):

    ENDPOINT_URL = ''

    HEADER = (By.ID, 'ast-desktop-header')
    NAV_BAR = (By.ID, 'site-navigation')
    REGISTER_BUTTON = (By.LINK_TEXT, 'Register Now')
    COURSES_LIST = (By.CSS_SELECTOR, 'section[data-id="5b4952c1"]')
    FOOTER = (By.CSS_SELECTOR, 'div[data-elementor-type="footer"]')
    HEADER_CONTACT_ELEMENT = (
        By.CSS_SELECTOR, '.elementor-icon-list-item.elementor-inline-item'
    )
    FOOTER_CONTACT_ELEMENT = (
        By.CSS_SELECTOR,
        'div[data-id="695441a0"] .elementor-icon-list-items > li.elementor-icon-list-item a'
    )

    POPULAR_COURSES_SLIDER = (By.CLASS_NAME, 'swiper-container-c50f9f0')
    ACTIVE_SLIDE = (By.CSS_SELECTOR, 'div[data-id="c50f9f0"] .swiper-slide-active')
    NEXT_SLIDE_BUTTON = (By.CLASS_NAME, 'swiper-button-next-c50f9f0')
    PREVIOUS_SLIDE_BUTTON = (By.CLASS_NAME, 'swiper-button-prev-c50f9f0')
    SLIDER_MOST_POPULAR = (By.CLASS_NAME, 'elementor-element-166618a')

    POPUP_CLOSE_BUTTON = (By.CSS_SELECTOR, ".dialog-close-button .eicon-close")

    ALL_COURSES_BUTTON = (By.ID, 'menu-item-27580')
    LIFETIME_MEMBERSHIP_BUTTON = (By.ID, 'menu-item-27581')

    POPULAR_COURSE_CARD = (By.CSS_SELECTOR, '.elementor-element-5b4952c1 > .elementor-container > .elementor-column')
    COURSE_TITLE = (By.CSS_SELECTOR, '.elementor-icon-box-title span')
    COURSE_DESCRIPTION = (By.CSS_SELECTOR, '.elementor-icon-box-description')
    POPULAR_COURSES_DATA = (By.CLASS_NAME, 'elementor-icon-box-wrapper')
    COURSE_LOGO_ICON = (By.CSS_SELECTOR, '.elementor-icon i')
    COURSE_BUTTON = (By.CSS_SELECTOR, '.elementor-button-text')
    COURSE_BUTTON_LINK = (By.CSS_SELECTOR, '.elementor-button-link')

    @allure.step('Получить индекс активного слайда')
    def get_active_slide_index(self):
        active_slide = self.get_element(MainPage.ACTIVE_SLIDE)
        return active_slide.get_attribute("data-swiper-slide-index")

    @allure.step('Переключиться на следующий слайд')
    def click_next_slide(self):
        next_button = self.get_clickable_element(MainPage.NEXT_SLIDE_BUTTON)
        ActionChains(self.browser).move_to_element(next_button).pause(0.5).click().perform()

    @allure.step('Переключиться на предыдущий слайд')
    def click_prev_slide(self):
        prev_button = self.get_clickable_element(MainPage.PREVIOUS_SLIDE_BUTTON)
        ActionChains(self.browser).move_to_element(prev_button).pause(0.5).click().perform()

    @allure.step('Закрыть всплывающее окно')
    def close_popup(self):
        self.click_next_slide()
        WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located((By.ID, 'elementor-popup-modal-26600'))
        )
        close_button = self.get_element(self.POPUP_CLOSE_BUTTON)
        close_button.click()

    @allure.step('Прокрутить страницу вниз')
    def scroll_to_bottom(self):
        actions = ActionChains(self.browser)
        actions.send_keys(Keys.PAGE_DOWN).perform()

    @allure.step('Получить данные карточек популярных курсов')
    def get_popular_couses_data(self):
        courses = self.get_elements(MainPage.POPULAR_COURSE_CARD)
        course_data_list = []
        for course in courses:
            title = course.find_element(*MainPage.COURSE_TITLE).text.strip()
            description = course.find_element(*MainPage.COURSE_DESCRIPTION).text.strip()
            logo_icon = True if course.find_element(*MainPage.COURSE_LOGO_ICON) else False
            button = course.find_element(*MainPage.COURSE_BUTTON)
            button_text = button.text.strip()
            button_parent = course.find_element(*MainPage.COURSE_BUTTON_LINK)
            button_link = button_parent.get_attribute('href')
            button_bg = button_parent.value_of_css_property('background-color')
            course_data_list.append({
                'title': title,
                'description': description,
                'logo_icon': logo_icon,
                'button_text': button_text,
                'button_background': button_bg,
                'button_link': button_link
            })
        return course_data_list
