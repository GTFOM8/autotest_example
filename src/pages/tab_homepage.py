from src.pages.locators import HomePageLocators


class TabHomePage:
    """ POM(Page Object Model) для главной страницы """
    def __init__(self, driver):
        self.driver = driver

    # @allure.step('')
    def click_input_button(self):
        """ Нажать кнопку 'Войти' на главной странице """
        auth = self.driver.find_element(*HomePageLocators.INPUT_BUTTON)
        auth.click()

    # @allure.step('')
    def click_search_string(self):
        """ Выбрать поисковую строку """
        search = self.driver.find_element(*HomePageLocators.SEARCH_STRING)
        search.send_keys('Яндекс диск')

    # @allure.step('')
    def auth_by_yandex(self):
        """ Авторизоваться с помощью Яндекс ID """
        auth = self.driver.find_element(*HomePageLocators.AUTH_YANDEX)
        auth.click()
