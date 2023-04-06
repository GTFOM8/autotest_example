from src.application import Application


def test_copy_file(app: Application, driver):

    # with allure.step('Открыть Яндекс.Диск'):
    app.tab_homepage.go_to_yandex_disk(driver)
    app.tab_auth.input_login()
    app.tab_auth.click_input_button()
    app.tab_auth.input_password()
    app.tab_auth.click_input_button()

    # with allure.step('Создать папку'):
    app.tab_disk.click_create_button()
    app.tab_disk.select_folder_to_create()
    app.tab_disk.name_the_folder()
    app.tab_disk.click_save_button()

    # with allure.step('Перейти в созданную папку'):
    app.tab_disk.move_to_created_folder()

    # with allure.step('Создать файл, внутри новой папки'):
    app.tab_disk.click_create_button()
    app.tab_disk.select_file_to_create()
    app.tab_disk.name_the_file()
    app.tab_disk.click_save_button()

    # with allure.step('Закрыть открывшуюся вкладку браузера'):
    app.tab_disk.close_tab()

    # with allure.step('Открыть файл'):
    app.tab_disk.open_created_file()
    app.tab_disk.should_be_file_opened()

    # with allure.step('Закрыть файл'):
    app.tab_disk.close_tab()
    app.tab_disk.should_be_file_closed()

    # with allure.step('Вернуться в корневую папку'):
    app.tab_disk.click_back_button()
