import allure
from pages.base_page import BasePage
from locators.password_recovery_page_locators import PasswordRecoveryPageLocators


class PasswordRecoveryPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = PasswordRecoveryPageLocators()

    @allure.step("Получить заголовок страницы")
    def get_title(self):
        return self._get_text(self.locators.PAGE_TITLE)    

    @allure.step("Ввести email")
    def enter_email(self, email):
        self._send_keys(self.locators.EMAIL_FIELD, email)

    @allure.step("Нажать 'Восстановить'")
    def click_recover_button(self):
        self._click_by_js(self.locators.RECOVER_BUTTON)

    @allure.step("Кликнуть на кнопку показа пароля")
    def click_show_password(self):
        self._click_by_js(self.locators.SHOW_PASSWORD_BUTTON)

    @allure.step("Проверить, что поле пароля активно")
    def is_password_field_active(self):
        return self._is_clickable(self.locators.ACTIVE_INPUT)
    
    def get_password_field_border_color(self):
        """Возвращает цвет рамки поля ввода пароля в формате rgba."""
        return self._get_css_property(self.locators.ACTIVE_INPUT, "border-color")
    

    def wait_for_highlight_color(self):
        """Ожидает, пока поле пароля получит подсветку (цвет рамки #4c4cff)."""
        self._wait_for_rgb_color(self.locators.ACTIVE_INPUT,"border-top-color",(76, 76, 255))    
    