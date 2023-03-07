from source.pages.tab_elements import TabElements


class Application:
    def __init__(self, driver):
        self._driver = driver

        self.tab_elements = TabElements(self._driver)

