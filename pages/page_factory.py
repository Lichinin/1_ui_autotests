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
