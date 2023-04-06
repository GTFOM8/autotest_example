from selenium.webdriver.common.by import By


class HomePageLocators:
    """ Локаторы веб-элементов, расположенных на главной странице Яндекса """
    INPUT_BUTTON = (By.XPATH, "/html/body/div[2]/div[2]/header/div/div[2]/div[3]/div")
    AUTH_YANDEX = (By.XPATH, '//*[@id="tooltip-0-1"]/div/div[2]')
    SEARCH_STRING = (By.XPATH, '/html/body/form')
    HEHE = (By.XPATH, '//*[@id="rso"]/div[1]/div/div/div/div/div/div/div[1]/a/div')
    SEARCH_BUTTON = (By.XPATH, '/html/body/form/button')


class AuthorizationPage:
    """ Локаторы веб-элементов, используемых для авторизации """
    LOGIN_FIELD = (By.ID, "passp-field-login")
    PASSWORD_FIELD = (By.ID, "passp-field-passwd")
    INPUT_BUTTON = (By.ID, "passp:sign-in")


class ServicesList:
    """ Локаторы веб-элементов, расположенных в Поисковой строке Яндекса """
    DISK = (By.XPATH, "/html/body/form/div[1]/div/div/div/ul/li[5]/a")


class YandexDistElements:
    """ Локаторы веб-элементов, расположенных в Яндекс. Диске """
    LIST_FILES = (By.XPATH, '/html/body/div[1]/div/div/div[3]/div[2]/div[1]/div/div/div[3]')
    BUTTON_CREATE = (By.XPATH, "/html/body/div[1]/div/div/div[3]/div[1]/div[1]/div/div/span[2]/button")
    BUTTON_SAVE = (By.XPATH, '/html/body/div[4]/div[2]/div/div/div/div/div/div[2]/button')
    BUTTON_BACK = (By.XPATH, '/html/body/div[1]/div/div/div[3]/div[2]/div[1]/div/div/div[2]/div[2]/button')
    SELECT_FOR_CREATE_FOLDER = (By.XPATH, '/html/body/div[3]/div/button[1]')
    SELECT_FOR_CREATE_FILE = (By.XPATH, '/html/body/div[3]/div/button[2]')
    SEARCH_STRING_NAME_FOLDER = (By.XPATH, '/html/body/div[4]/div[2]/div/div/div/div/div/div[1]/div/form/span/input')
    CREATED_FOLDER = (By.XPATH, '/html/body/div[1]/div/div/div[3]/div[2]/div[1]/div/div/div[3]/div/div[1]')
    CREATED_FILE = (By.XPATH, '/html/body/div[1]/div/div/div[3]/div[2]/div[1]/div/div/div[3]/div/div[1]')
