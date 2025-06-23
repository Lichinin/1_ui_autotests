from selenium.webdriver.common.by import By

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
    FOOTER_CONTACT_ELEMENT = (By.CSS_SELECTOR, 'div[data-id="695441a0"] .elementor-icon-list-items > li.elementor-icon-list-item a')

    POPULAR_COURSES_SLIDER = (By.CLASS_NAME, 'swiper-container-c50f9f0')
    ACTIVE_SLIDE = (By.CSS_SELECTOR, 'div[data-id="c50f9f0"] .swiper-slide-active')
    NEXT_SLIDE_BUTTON = (By.CLASS_NAME, 'swiper-button-next-c50f9f0')
    PREVIOUS_SLIDE_BUTTON = (By.CLASS_NAME, 'swiper-button-prev-c50f9f0')
