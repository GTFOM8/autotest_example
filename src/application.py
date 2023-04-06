from src.pages.tab_homepage import TabHomePage
from src.pages.tab_authorization import TabAuth
from src.pages.tab_yandexDisk import TabYandexDisk


class Application:
    def __init__(self, driver):
        self.driver = driver

        self.tab_homepage = TabHomePage(self.driver)
        self.tab_auth = TabAuth(self.driver)
        self.tab_disk = TabYandexDisk(self.driver)
