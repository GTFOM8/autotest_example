import time
from selenium.webdriver import ActionChains
from src.pages.locators import YandexDistElements


class TabYandexDisk:
    """ POM(Page Object Model) для домашней страницы Яндекс.Диска """
    def __init__(self, driver):
        self.driver = driver

    # @allure.step('Нажать кнопку "Создать"')
    def click_create_button(self):
        """ Нажать кнопку 'Создать' """
        button = self.driver.find_element(*YandexDistElements.BUTTON_CREATE)
        button.click()
        time.sleep(2)

    # @allure.step('Нажать кнопку "Сохранить"')
    def click_save_button(self):
        """ Нажать кнопку 'Сохранить' """
        button = self.driver.find_element(*YandexDistElements.BUTTON_SAVE)
        button.click()
        time.sleep(2)

    # @allure.step('Нажать кнопку назад')
    def click_back_button(self):
        """ Нажать кнопку назад """
        button = self.driver.find_element(*YandexDistElements.BUTTON_BACK)
        button.click()

    # @allure.step('Создать папку')
    def select_folder_to_create(self):
        """ Создать папку  """
        folder = self.driver.find_element(*YandexDistElements.SELECT_FOR_CREATE_FOLDER)
        folder.click()

    # @allure.step('Создать файл')
    def select_file_to_create(self):
        """ Создать файл """
        file = self.driver.find_element(*YandexDistElements.SELECT_FOR_CREATE_FILE)
        file.click()
        time.sleep(2)

    # @allure.step('Дать папке имя')
    def name_the_folder(self):
        """ Дать папке имя """
        folder = self.driver.find_element(*YandexDistElements.SEARCH_STRING_NAME_FOLDER)
        folder.send_keys('Тестовая папка')

    # @allure.step('Дать файлу имя')
    def name_the_file(self):
        """ Дать файлу имя """
        file = self.driver.find_element(*YandexDistElements.SEARCH_STRING_NAME_FOLDER)
        file.send_keys('Тестовый файл')
        time.sleep(2)

    # @allure.step('Перейти в папку')
    def move_to_created_folder(self):
        """ Перейти в папку  """
        folder = self.driver.find_element(*YandexDistElements.CREATED_FOLDER)

        actions = ActionChains(self.driver)
        actions.double_click(folder).perform()

        time.sleep(2)

    # @allure.step('Закрыть вкладку в браузере')
    def close_tab(self):
        """ Закрыть вкладку в браузере """
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

    # @allure.step('Открыть созданный файл')
    def open_created_file(self):
        """ Открыть созданный файл """
        file = self.driver.find_element(*YandexDistElements.CREATED_FILE)

        actions = ActionChains(self.driver)
        actions.double_click(file).perform()

    # @allure.step('Проверить, что файл открылся')
    def should_be_file_opened(self):
        """ Проверить, что файл открылся """
        assert len(self.driver.window_handles) == 2, 'Файл не был открыт'

    # @allure.step('Проверить, что файл закрылся')
    def should_be_file_closed(self):
        """ Проверить, что файл закрылся """
        assert len(self.driver.window_handles) == 1, 'Файл не был закрыт'
