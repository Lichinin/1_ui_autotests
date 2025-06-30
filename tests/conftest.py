import datetime
import logging
import logging.handlers
from logging.handlers import RotatingFileHandler

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.remote.webdriver import WebDriver

from config import Pathes, Urls
from pages.angular_login_page import AngularPage
from pages.main_page import MainPage
from pages.sql_ex_page import SqlExPage


def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default='chrome')
    parser.addoption('--url', action='store', default=Urls.BASE_URL)
    parser.addoption('--log_level', action='store', default="INFO")
    parser.addoption('--browser_version', action='store')


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
def browser(request, logger) -> WebDriver:
    browser_name = request.config.getoption('--browser')
    browser_version = request.config.getoption('--browser_version')
    url = request.config.getoption('--url')

    if browser_name == 'chrome':
        options = ChromeOptions()
        # options.add_argument('--headless')
        options.add_argument("--incognito")
        options.add_argument('--ignore-certificate-errors')
        options.add_argument("--start-maximized")
        options.page_load_strategy = 'eager'
        driver = webdriver.Chrome(options=options)
    elif browser_name == 'firefox':
        options = FirefoxOptions()
        options.add_argument('--ignore-certificate-errors')
        # options.add_argument('--headless')
        options.page_load_strategy = 'eager'
        driver = webdriver.Firefox(options=options)
    elif browser_name == 'edge':
        options = EdgeOptions()
        options.page_load_strategy = 'eager'
        driver = webdriver.Edge(options=options)
    else:
        raise ValueError(
            'Browser name must be "chrome", "firefox" or "edge"'
        )
    driver.url = url
    driver.logger = logger
    driver.test_name = request.node.name

    logger.info("Browser %s v. %s started" % (browser_name, browser_version))

    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def main_page(browser) -> MainPage:
    browser.get(MainPage.get_full_url())
    return MainPage(browser)


@pytest.fixture(scope='function')
def angular_page(browser) -> AngularPage:
    browser.get(AngularPage.get_full_url())
    return AngularPage(browser)

@pytest.fixture(scope='function')
def sql_ex_page(browser) -> SqlExPage:
    browser.get(Urls.SQL_EX_RU)
    return SqlExPage(browser)

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
