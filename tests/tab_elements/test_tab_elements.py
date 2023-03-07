import allure
from source.application import Application


def test_tab_elements(app: Application, driver):
    """ Проверка работы """
    with allure.step("Открыть вкладку 'Elements'"):
        app.tab_elements.open_tab_elements()

    with allure.step("Перейти в раздел 'CheckBox'"):
        app.tab_elements.push_tab_check_box()

    with allure.step("Раскрыть директорию 'Home'"):
        app.tab_elements.open_directory_home()

    with allure.step("Раскрыть директорию 'Downloads'"):
        app.tab_elements.open_directory_downloads()

    with allure.step("Выбрать файл 'WordFile'"):
        app.tab_elements.select_file()
        app.tab_elements.should_be_file_selected()

