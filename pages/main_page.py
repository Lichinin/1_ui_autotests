import allure
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from constants.constants import Constants
from pages.base_page import BasePage


class MainPage(BasePage):

    def __init__(self, browser):
        super().__init__(browser)

    ENDPOINT_URL = ''

    HEADER = (By.ID, 'ast-desktop-header')
    NAV_BAR = (By.ID, 'site-navigation')
    REGISTER_BUTTON = (By.LINK_TEXT, 'Register Now')
    BEST_COURSES = (By.CSS_SELECTOR, 'section[data-id="5b4952c1"]')
    FOOTER = (By.CSS_SELECTOR, 'div[data-elementor-type="footer"]')
    HEADER_CONTACT_ELEMENT = (
        By.CSS_SELECTOR, '.elementor-icon-list-items > .elementor-inline-item'
    )
    HEADER_CONTACT_ICON = (By.CSS_SELECTOR, '.elementor-icon-list-icon')
    HEADER_CONTACT_TEXT = (By.CSS_SELECTOR, '.elementor-icon-list-text')
    HEADER_CONTACT_LINK = (By.CSS_SELECTOR, 'a')

    FOOTER_CONTACT_ELEMENT = (
        By.CSS_SELECTOR,
        '.elementor-element-695441a0 .elementor-icon-list-item'
    )
    FOOTER_CONTACT_ICON = (
        By.CSS_SELECTOR,
        '.elementor-icon-list-icon i'
    )
    FOOTER_CONTACT_TEXT = (
        By.CSS_SELECTOR,
        '.elementor-icon-list-text'
    )
    FOOTER_CONTACT_LINK = (By.CSS_SELECTOR, 'a')

    POPULAR_COURSES_SLIDER = (By.CLASS_NAME, 'swiper-container-c50f9f0')
    ACTIVE_SLIDE = (By.CSS_SELECTOR, 'div[data-id="c50f9f0"] .swiper-slide-active')
    SLIDE_TITLE = (By.CSS_SELECTOR, ".pp-info-box-title")
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

    @allure.step('Открыть страницу')
    def open_page(self):
        url = self.get_full_url()
        self.browser.get(url)
        return self

    @allure.step('Получить индекс активного слайда')
    def get_active_slide_index(self):
        active_slide = self.get_element(MainPage.ACTIVE_SLIDE)
        return active_slide.get_attribute("data-swiper-slide-index")

    @allure.step('Получить title активного слайда')
    def get_active_slide_title(self):
        active_slide = self.get_element(MainPage.ACTIVE_SLIDE)
        title = active_slide.find_element(*MainPage.SLIDE_TITLE).text.strip()
        return title

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
    def get_popular_courses_data(self):
        courses = self.get_elements(MainPage.POPULAR_COURSE_CARD)
        course_data_list = []
        for course in courses:
            title = course.find_element(*MainPage.COURSE_TITLE).text.strip()
            description = course.find_element(*MainPage.COURSE_DESCRIPTION).text.strip()
            logo_icon = bool(course.find_element(*MainPage.COURSE_LOGO_ICON))
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

    @allure.step('Получить контактов в header')
    def get_header_contacts_data(self):
        header_contacts = self.get_elements(MainPage.HEADER_CONTACT_ELEMENT)
        header_contacts_list = []
        for contact in header_contacts:
            link = contact.find_element(*self.HEADER_CONTACT_LINK).get_attribute("href").strip()
            text = contact.find_element(*self.HEADER_CONTACT_TEXT).text.strip()
            icon = bool(contact.find_elements(*self.HEADER_CONTACT_ICON))
            header_contacts_list.append({
                'link': link,
                'text': text,
                'icon': icon,
            })
        return header_contacts_list

    @allure.step('Получить контактов в footer')
    def get_footer_contacts_data(self):
        footer_contacts = self.get_elements(MainPage.FOOTER_CONTACT_ELEMENT)
        footer_contacts_list = []
        for contact in footer_contacts:
            link = (
                contact.find_element(*self.FOOTER_CONTACT_LINK).get_attribute("href").strip()
                if contact.find_elements(*self.FOOTER_CONTACT_LINK)
                else None
            )
            text = contact.find_element(*self.FOOTER_CONTACT_TEXT).text.strip()
            icon = bool(contact.find_elements(*self.FOOTER_CONTACT_ICON))
            footer_contacts_list.append({
                'link': link,
                'text': text,
                'icon': icon,
            })
        return footer_contacts_list

    @allure.step('Прокрутить до блока "Most Popular"')
    def scroll_to_most_popular(self):
        self.scroll_to(self.get_element(MainPage.SLIDER_MOST_POPULAR))

    @allure.step('Прокрутить до футера')
    def scroll_to_footer(self):
        self.scroll_to(self.get_element(MainPage.FOOTER))

    @allure.step('Нажать кнопку "All Courses"')
    def click_all_courses_button(self):
        self.click_button(self.ALL_COURSES_BUTTON)

    @allure.step('Нажать кнопку "Lifetime Membership"')
    def click_lifetime_membership_button(self):
        self.click_button(self.LIFETIME_MEMBERSHIP_BUTTON)

    @allure.step('Проверить видимость header')
    def check_header_visible(self):
        assert self.is_element_visible(self.HEADER), 'Header не отображается на странице'

    @allure.step('Проверить видимость навигационной панели')
    def check_navbar_visible(self):
        assert self.is_element_visible(self.NAV_BAR), 'Навигационная панель не отображается'

    @allure.step('Проверить видимость блока лучших курсов')
    def check_best_courses_visible(self):
        assert self.is_element_visible(self.BEST_COURSES), 'Блок лучших курсов не отображается'

    @allure.step('Проверить видимость footer')
    def check_footer_visible(self):
        assert self.is_element_visible(self.FOOTER), 'Footer не отображается на странице'

    @allure.step('Проверить видимость кнопки регистрации')
    def check_register_button_visible(self):
        assert self.is_element_visible(self.REGISTER_BUTTON), 'Кнопка "Register Now" не отображается'

    @allure.step('Проверить фон кнопки регистрации')
    def check_register_button_background(self):
        self.check_element_background_colour(self.REGISTER_BUTTON, Constants.REGISTER_BUTTON_COLOUR)

    @allure.step('Проверить текст кнопки регистрации')
    def check_register_button_text(self):
        self.check_element_text(self.REGISTER_BUTTON, Constants.REGISTER_BUTTON_TEXT)

    @allure.step('Проверить количество контактов в footer')
    def check_footer_contacts_lenght(self):
        contacts = self.get_footer_contacts_data()
        self.check_element_list_lenght(contacts, 5)

    @allure.step('Проверить значения контактов в footer')
    def check_footer_contacts_data(self):
        contacts = self.get_footer_contacts_data()
        self.verify_list_items(contacts, Constants.FOOTER_CONTACTS_LIST, 'Footer крнтакт')

    @allure.step('Проверить количество контактов в header')
    def check_header_contacts_lenght(self):
        contacts = self.get_header_contacts_data()
        self.check_element_list_lenght(contacts, 5)

    @allure.step('Проверить значения контактов в header')
    def check_header_contacts_data(self):
        contacts = self.get_header_contacts_data()
        self.verify_list_items(contacts, Constants.HEADER_CONTACT_LIST, 'Header контакт')

    @allure.step('Проверить количество курсов в блоке лучших курсов')
    def check_best_courses_lenght(self):
        courses_data_list = self.get_popular_courses_data()
        self.check_element_list_lenght(courses_data_list, 4)

    @allure.step('Проверить данные курсов в блоке лучших курсов')
    def check_best_courses_data(self):
        course_data = self.get_popular_courses_data()
        self.verify_list_items(course_data, Constants.BEST_COURSES_DATA_LIST, 'Курс')

    @allure.step('Проверить URL страницы Lifetime Membership')
    def check_url_lifetime_membership_page(self):
        current_url = self.get_current_url()
        expected_url = Constants.LIFETIME_MEMEDERSHIP_URL
        assert current_url == expected_url, \
            f'URL не совпадает. Ожидалось: "{expected_url}", получено: "{current_url}"'

    @allure.step('Проверить title страницы Lifetime Membership')
    def check_title_lifetime_membership_page(self):
        page_title = self.get_page_title()
        expected_title = Constants.LIFETIME_MEMEDERSHIP_PAGE_TITLE
        assert expected_title in page_title, \
            f'Title страницы некорректный. Ожидалось: "{expected_title}", получено: "{page_title}"'
