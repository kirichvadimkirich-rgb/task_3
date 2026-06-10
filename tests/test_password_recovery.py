import allure
from config.settings import BASE_URL, API_DOCS_URL
from data.generator import generate_user_data
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.password_recovery_page import PasswordRecoveryPage


@allure.feature("Восстановление пароля")
@allure.link(BASE_URL, name='Ссылка на сайт')
@allure.link(API_DOCS_URL, name='Ссылка на документацию API')
class TestPasswordRecovery:

    @allure.title("Переход на страницу восстановления пароля по кнопке 'Восстановить пароль'")
    @allure.description("Проверяем, что клик по ссылке 'Восстановить пароль' на странице логина ведёт на страницу /forgot-password" \
    " и отображается заголовок")
    def test_go_to_recovery_page(self, browser):
        main_page = MainPage(browser) 
        main_page.click_personal_account()
        login_page = LoginPage(browser)
        login_page.go_to_forgot_password()

        with allure.step("Проверить, что URL содержит 'forgot-password'"):
            assert "forgot-password" in browser.current_url

        recovery_page = PasswordRecoveryPage(browser)

        with allure.step("Проверить, что отображается заголовок 'Восстановление пароля'"):
            assert recovery_page.is_title_displayed(), "Заголовок 'Восстановление пароля' не отображается"
       

    @allure.title("Ввод почты и клик по кнопке 'Восстановить'")
    @allure.description("После ввода email и нажатия кнопки 'Восстановить' открывается страница сброса пароля (reset-password)")
    def test_recovery_send_email(self, browser):
        user_data = generate_user_data()
        main_page = MainPage(browser)
        main_page.click_personal_account()
        login_page = LoginPage(browser)
        login_page.go_to_forgot_password()
        recovery_page = PasswordRecoveryPage(browser)
        recovery_page.enter_email(user_data["email"])
        recovery_page.click_recover_button()
        recovery_page._wait_for_url("reset-password")

        with allure.step("Проверить, что URL содержит 'reset-password'"):
            assert "reset-password" in browser.current_url
        
        with allure.step("Проверить, что отображается заголовок 'Восстановление пароля'"):
            assert recovery_page.is_title_displayed(), "Заголовок 'Восстановление пароля' не отображается"


    @allure.title("Клик по кнопке показать/скрыть пароль делает поле активным (подсветка)")
    @allure.description("На странице восстановления пароля клик по кнопке показать/скрыть пароль должен подсветить поле ввода пароля (сверяем цвет и  класс active)")
    def test_click_password_toggle_and_verify_highlight(self, browser):
        user_data = generate_user_data()
        main_page = MainPage(browser)
        main_page.click_personal_account()
        login_page = LoginPage(browser)
        login_page.go_to_forgot_password()
        recovery_page = PasswordRecoveryPage(browser)
        recovery_page.enter_email(user_data["email"])
        recovery_page.click_recover_button()
        recovery_page.click_show_password()

        with allure.step("Проверить, что поле 'Пароль' активно по нажатию 'Отобразить пароль'"):
            assert recovery_page.is_password_field_active()
        recovery_page.wait_for_highlight_color()
        border_color = recovery_page.get_password_field_border_color()

        with allure.step("Проверить цвет рамки поля 'Пароль' по нажатию 'Отобразить пароль'"):
            assert "rgb(76, 76, 255)" in border_color or "rgba(76, 76, 255" in border_color
