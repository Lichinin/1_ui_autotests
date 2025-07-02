from pathlib import Path


class Timeouts:
    ELEMENT_VISIBILITY = 3


class Urls:
    BASE_URL = 'https://www.way2automation.com'
    SQL_EX_RU = 'https://sql-ex.ru/'
    AUTH_URS = 'https://authenticationtest.com/simpleFormAuth/'


class Pathes:
    LOG_DIR = Path(__file__).parent / 'log'
