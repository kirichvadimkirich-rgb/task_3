import allure
from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = LoginPageLocators()

    @allure.step("Войти с email")
    def login(self, email, password):
        self._send_keys(self.locators.EMAIL_FIELD, email)
        self._send_keys(self.locators.PASSWORD_FIELD, password)
        self._click(self.locators.LOGIN_BUTTON)

    @allure.step("Перейти на страницу восстановления пароля.")
    def go_to_forgot_password(self):
        self._click(self.locators.FORGOT_PASSWORD_LINK)

    @allure.step("Возвращает текст заголовка страницы входа.")
    def get_title(self):
        return self._get_text(self.locators.PAGE_TITLE)    