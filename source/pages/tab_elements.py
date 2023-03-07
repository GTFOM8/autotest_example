import allure
from source.pages.locators import ElementsMenuLocators
from source.pages.locators import MainPageLocators


class TabElements:
    """ POM (Page Object Model) для вкладки 'Elements' """

    def __init__(self, driver):
        self._driver = driver

    @allure.step("Открыть вкладку 'Elements'")
    def open_tab_elements(self):
        """ Открыть вкладку 'Elements' """
        open_tab = self._driver.find_element(*MainPageLocators.ELEMENTS)
        open_tab.click()

    @allure.step("Нажать кнопку 'CheckBox'")
    def push_tab_check_box(self):
        """ Нажать кнопку 'CheckBox' """
        push_tab = self._driver.find_element(*ElementsMenuLocators.CHECKBOX)
        push_tab.click()

    @allure.step("Раскрыть директорию 'Home'")
    def open_directory_home(self):
        """ Раскрыть директорию 'Home' """
        open_home = self._driver.find_element(*ElementsMenuLocators.TOGGLE_HOME_FOLDER)
        open_home.click()

    @allure.step("Раскрыть директорию 'Downloads'")
    def open_directory_downloads(self):
        """ Раскрыть директорию 'Downloads' """
        open_downloads = self._driver.find_element(*ElementsMenuLocators.TOGGLE_DOWNLOADS_FOLDER)
        open_downloads.click()

    @allure.step("Выбрать файл 'WordFile'")
    def select_file(self):
        """ Выбрать файл 'WordFile' """
        select_file = self._driver.find_element(*ElementsMenuLocators.INPUT_WORD_FILE)
        select_file.click()

    @allure.step("Проверить, что файл выбран успешно")
    def should_be_file_selected(self):
        file = self._driver.find_element(*ElementsMenuLocators.RESULT)

        assert file.text == "You have selected :\nwordFile", "Файл не был выбран!"
