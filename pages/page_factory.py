from pages.alert_page import AlertPage
from pages.angular_login_page import AngularPage
from pages.dropppable_page import DroppablePage
from pages.frames_and_windows_page import FramesAndWindowsPage
from pages.httpwatch_auth_page import HttpWatchAuthPage
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

    @property
    def droppable_page(self) -> DroppablePage:
        if 'droppable_page' not in self._cache:
            self._cache['droppable_page'] = DroppablePage(self.driver)
        return self._cache['droppable_page']

    @property
    def frame_and_windows_page(self) -> FramesAndWindowsPage:
        if 'frame_and_windows_page' not in self._cache:
            self._cache['frame_and_windows_page'] = FramesAndWindowsPage(self.driver)
        return self._cache['frame_and_windows_page']

    @property
    def alert_page(self) -> AlertPage:
        if 'alert_page' not in self._cache:
            self._cache['alert_page'] = AlertPage(self.driver)
        return self._cache['alert_page']

    @property
    def basic_auth(self) -> HttpWatchAuthPage:
        if 'basic_auth' not in self._cache:
            self._cache['basic_auth'] = HttpWatchAuthPage(self.driver)
        return self._cache['basic_auth']
