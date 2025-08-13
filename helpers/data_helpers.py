import os

import allure
from dotenv import load_dotenv
from faker import Faker

from pages.main_page import MainPage

load_dotenv()

fake = Faker(['en_US'])


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

    @staticmethod
    @allure.step('Сгенерировать случайные данные для авторизации')
    def random_login_data():
        login = fake.user_name()
        description = fake.sentence(nb_words=6)
        password = fake.password(length=8)
        return {
            'login': login,
            'description': description,
            'password': password
        }

    @staticmethod
    @allure.step('Сгенерировать username')
    def random_username():
        username = fake.name()
        return username

    @staticmethod
    @allure.step('Получить данные из .ENV')
    def get_from_env(value):
        return os.getenv(value)

    @staticmethod
    @allure.step('Сгенерировать данные для авторизации BankingPage')
    def random_login_banking_page_data():
        first_name = fake.first_name()
        last_name = fake.last_name()
        email = fake.email()
        password = fake.password(length=8)
        postcode = fake.postcode()
        return {
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            'password': password,
            'postcode': postcode
        }

    @staticmethod
    @allure.step('Получить самое длинное значение хобби')
    def get_longest_hobbie(list):
        list_values = [hobby.get_attribute('value') for hobby in list]
        return max(list_values)
