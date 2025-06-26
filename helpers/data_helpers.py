import allure
from pages.main_page import MainPage


class DataHelper:
    @staticmethod
    @allure.step('Получить контакты из хедера')
    def get_contacts_values(page: MainPage):
        contacts = page.get_elements(MainPage.HEADER_CONTACT_ELEMENT)
        return [contact.text for contact in contacts]

    @staticmethod
    @allure.step('Получить контакты из футера')
    def get_footer_contacts_values(page: MainPage):
        contacts = page.get_elements(MainPage.FOOTER_CONTACT_ELEMENT)
        return [contact.text for contact in contacts]
