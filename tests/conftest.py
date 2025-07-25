import datetime
import logging
from logging.handlers import RotatingFileHandler
from typing import Generator

import allure
import pytest
from selenium.webdriver.remote.webdriver import WebDriver

from config import Pathes, Urls
from drivers.driver_factory import DriverFactory
from helpers.cookies_helper import CookiesHelper
from pages.page_factory import PageFactory


def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default='chrome')
    parser.addoption('--url', action='store', default=Urls.BASE_URL)
    parser.addoption('--log_level', action='store', default="INFO")
    parser.addoption('--browser_version', action='store')
    parser.addoption('--executor', action='store', default=None)


@pytest.fixture(scope='function')
def logger(request):
    log_dir = Pathes.LOG_DIR
    log_dir.mkdir(exist_ok=True)
    log_level = request.config.getoption('--log_level')
    browser_name = request.config.getoption('--browser')
    logger = logging.getLogger(request.node.name)
    file_handler = RotatingFileHandler(
        str(log_dir / f'{request.node.name}({browser_name}).log'),
        maxBytes=30000000,
        backupCount=3)
    file_handler.setFormatter(logging.Formatter('%(levelname)s %(message)s'))
    logger.addHandler(file_handler)
    logger.setLevel(level=log_level)

    logger.info('===> Test %s started at %s' % (request.node.name, datetime.datetime.now()))

    yield logger

    logger.info('===> Test %s finished at %s' % (request.node.name, datetime.datetime.now()))

    for handler in logger.handlers:
        handler.close()
    logger.handlers.clear()


@pytest.fixture(scope="function")
def browser(request, logger) -> Generator[WebDriver, None, None]:
    browser_name = request.config.getoption('--browser')
    browser_version = request.config.getoption('--browser_version')
    url = request.config.getoption('--url')
    executor = request.config.getoption('--executor')

    driver = DriverFactory.create_driver(
        browser_name=browser_name,
        executor=executor
    )

    driver.url = url
    driver.logger = logger
    driver.test_name = request.node.name

    logger.info("Browser %s v. %s started" % (browser_name, browser_version))

    yield driver
    driver.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        browser = item.funcargs.get('browser')
        if browser:
            allure.attach(
                browser.get_screenshot_as_png(),
                name="screenshot_on_failure",
                attachment_type=allure.attachment_type.PNG
            )


@pytest.fixture(scope='function')
def prepare_cookies(pages: PageFactory):
    sql_ex_page = pages.sqlex.open_page()
    cookies_helper = CookiesHelper(sql_ex_page)
    sql_ex_page.fill_login_field()
    sql_ex_page.fill_passsword_field()
    sql_ex_page.click_login_button()
    cookies_helper.save_cookies_to_file()

    yield

    CookiesHelper.delete_cookies_file()


@pytest.fixture(scope='function')
def pages(browser) -> PageFactory:
    return PageFactory(browser)
