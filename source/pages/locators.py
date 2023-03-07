from selenium.webdriver.common.by import By

""" XPATH взял из-за отсутствия уникальности локаторов """


class MainPageLocators:
    """ Локаторы веб-элементов, расположенных на главной странице сайта """
    ELEMENTS = (By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div[1]/div/div[2]")


class ElementsMenuLocators:
    """ Локаторы веб-элементов, расположенных в боковом меню раздела 'Elements' """
    CHECKBOX = (By.XPATH, "/html/body/div[2]/div/div/div[2]/div[1]/div/div/div[1]/div/ul/li[2]")
    TOGGLE_HOME_FOLDER = (By.XPATH, "/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div/ol/li/span/button")
    TOGGLE_DOWNLOADS_FOLDER = (By.XPATH, "/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div/ol/li/"
                                         "ol/li[3]/span/button")
    INPUT_WORD_FILE = (By.XPATH, '/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[1]/ol/'
                                 'li/ol/li[3]/ol/li[1]/span/label/span[1]')
    RESULT = (By.ID, "result")
