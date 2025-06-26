import allure
from constants.constants import Constants


class AssertionHelper:
    @staticmethod
    @allure.step('Проверить, что все футер-контакты присутствуют в списке ожидаемых')
    def assert_footer_contact(contacts):
        for contact in contacts:
            assert contact in Constants.FOOTER_CONTACTS