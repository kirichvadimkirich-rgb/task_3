import allure
from pages.base_page import BasePage
from locators.personal_account_page_locators import PersonalAccountPageLocators


class PersonalAccountPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = PersonalAccountPageLocators()

    @allure.step("Перейти в 'Историю заказов'")
    def go_to_order_history(self):
        self._click(self.locators.ORDER_HISTORY_LINK)

    @allure.step("Выйти из аккаунта")
    def logout(self):
        self._click(self.locators.LOGOUT_BUTTON)
        self._wait_for_url("login")
        
    @allure.step("Получить номер первого заказа из истории")
    def get_first_order_number_from_history(self):
        number = self._get_number_from_text(self.locators.FIRST_ORDER_NUMBER_IN_HISTORY)
        if number is None:
            raise ValueError("Не удалось извлечь номер заказа из ленты")
        return number
        