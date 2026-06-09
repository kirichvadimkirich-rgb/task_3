import allure
from config.settings import BASE_URL, API_DOCS_URL
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.personal_account_page import PersonalAccountPage
from pages.order_modal_page import OrderModalPage


@allure.feature("Личный кабинет")
@allure.link(BASE_URL, name='Ссылка на сайт')
@allure.link(API_DOCS_URL, name='Ссылка на документацию API')
class TestPersonalAccount:

    @allure.title("Переход по клику на «Личный кабинет»")
    @allure.description("Проверяем, что клик по кнопке «Личный кабинет» после авторизации открывает страницу аккаунта")
    def test_go_to_personal_account_unauthorized(self, browser):
        main_page = MainPage(browser)
        main_page.click_personal_account()
        login_page = LoginPage(browser)

        with allure.step("Проверить, что открылась страница 'Вход'(url, Заголовок 'Вход')"):
            assert "login" in browser.current_url
            assert login_page.get_title() == "Вход", "Заголовок страницы входа не соответствует"

    @allure.title("Переход в раздел «История заказов» и отображение созданного заказа")
    @allure.description("Проверяем, что после создания заказа, он отображается в истории заказов, сверяем номер заказа")
    def test_go_to_order_history(self, logged_in_browser):
        main_page = MainPage(logged_in_browser)

        with allure.step("Создать заказ через UI"):
            main_page.add_bun()
            main_page.add_sauce()
            main_page.add_filling()
            main_page.click_order_button()

        order_modal = OrderModalPage(logged_in_browser)
        order_modal.wait_for_real_order_number()
        order_number = order_modal.get_modal_order_number()
        order_modal.close()    
        
        with allure.step("Перейти в историю заказов"):
            main_page.click_personal_account()
            personal_page = PersonalAccountPage(logged_in_browser)
            personal_page.go_to_order_history()
        order_number_from_history = personal_page.get_first_order_number_from_history()
        
        with allure.step("Проверить, что в истории номер заказа такой же как и при создании"):
            assert int(order_number) == int(order_number_from_history), f"Номер заказа не совпадает: {int(order_number)} vs {int(order_number_from_history)}"

    @allure.title("Выход из аккаунта")
    @allure.description("Проверяем, что нажатие на кнопку «Выход» разлогинивает пользователя и переводит на страницу входа")
    def test_logout(self, logged_in_browser):
        main_page = MainPage(logged_in_browser)
        main_page.click_personal_account()
        personal_page = PersonalAccountPage(logged_in_browser)
        personal_page.logout()
        login_page = LoginPage(logged_in_browser)

        with allure.step("Проверить, что открылась страница 'Вход'(url, Заголовок 'Вход')"):
            assert "login" in personal_page.driver.current_url
            assert login_page.get_title() == "Вход", "Заголовок страницы входа не соответствует"