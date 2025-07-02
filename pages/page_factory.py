from pages.angular_login_page import AngularPage
from pages.main_page import MainPage
from pages.sql_ex_page import SqlExPage


class PageFactory:
    def __init__(self, driver):
        self.driver = driver
        self._cache = {}

    @property
    def sqlex(self) -> SqlExPage:
        if 'sqlex' not in self._cache:
            self._cache['sqlex'] = SqlExPage(self.driver)
        return self._cache['sqlex']

    @property
    def angular_page(self) -> AngularPage:
        if 'angular_page' not in self._cache:
            self._cache['angular_page'] = AngularPage(self.driver)
        return self._cache['angular_page']

    @property
    def main_page(self) -> AngularPage:
        if 'main_page' not in self._cache:
            self._cache['main_page'] = MainPage(self.driver)
        return self._cache['main_page']
