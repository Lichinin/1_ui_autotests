

from constants.constants import Constants


class AssertionHelper:
    @staticmethod
    def assert_footer_contact(contacts):
        for contact in contacts:
            assert contact in Constants.FOOTER_CONTACTS