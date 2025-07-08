from selenium import webdriver
from selenium import webdriver as remote_webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.remote.webdriver import WebDriver


class DriverFactory:

    @staticmethod
    def create_driver(
        browser_name,
        executor
    ) -> WebDriver:

        options_map = {
            'chrome': ChromeOptions(),
            'firefox': FirefoxOptions(),
            'edge': EdgeOptions()
        }

        options = options_map.get(browser_name.lower())

        if options is None:
            raise ValueError('Browser name must be "chrome", "firefox", "edge"')

        options.add_argument('--ignore-certificate-errors')
        # options.add_argument('--headless')
        options.add_argument("--start-maximized")
        options.add_argument("--incognito")
        options.page_load_strategy = 'eager'

        if executor:
            return remote_webdriver.Remote(
                command_executor=executor,
                options=options
            )
        else:
            return DriverFactory._create_local_driver(browser_name, options)

    @staticmethod
    def _create_local_driver(browser_name, options):
        if browser_name == 'chrome':
            return webdriver.Chrome(options=options)
        elif browser_name == 'firefox':
            return webdriver.Firefox(options=options)
        elif browser_name == 'edge':
            return webdriver.Edge(options=options)
