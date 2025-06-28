import allure

from constants.constants import Constants


class AssertionHelper:

    @staticmethod
    @allure.step('Проверить значения контактов в header')
    def assert_header_contact(contacts):
        errors = []
        try:
            assert contacts[0] == Constants.FIRST_HEADER_CONTACT_DATA
        except AssertionError as e:
            errors.append(f'Контакт 1: {e}')
        try:
            assert contacts[1] == Constants.SECOND_HEADER_CONTACT_DATA
        except AssertionError as e:
            errors.append(f'Контакт 2: {e}')
        try:
            assert contacts[2] == Constants.THIRD_HEADER_CONTACT_DATA
        except AssertionError as e:
            errors.append(f'Контакт 3: {e}')
        try:
            assert contacts[3] == Constants.FOURTH_HEADER_CONTACT_DATA
        except AssertionError as e:
            errors.append(f'Контакт 4: {e}')
        try:
            assert contacts[4] == Constants.FIFTH_HEADER_CONTACT_DATA
        except AssertionError as e:
            errors.append(f'Контакт 5: {e}')

        if errors:
            raise AssertionError(f'Найдены ошибки в контактах: {errors}')
