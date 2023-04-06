from src.pages.locators import AuthorizationPage


class TabAuth:
    """ POM(Page Object Model) для страницы авторизации """
    def __init__(self, driver):
        self.driver = driver

    # @allure.step('Ввести логин')
    def input_login(self):
        """ Заполнить поле 'Логин' """
        login = self.driver.find_element(*AuthorizationPage.LOGIN_FIELD)
        login.click()
        login.send_keys('s.samss')

    # @allure.step('Ввести пароль')
    def input_password(self):
        """ Заполнить поле 'Пароль' """
        pwd = self.driver.find_element(*AuthorizationPage.PASSWORD_FIELD)
        pwd.click()
        pwd.send_keys('Qwerty123_.')

    # @allure.step('Нажать кнопку "Войти"')
    def click_input_button(self):
        """ Нажать кнопку 'Войти' """
        button = self.driver.find_element(*AuthorizationPage.INPUT_BUTTON)
        button.click()
