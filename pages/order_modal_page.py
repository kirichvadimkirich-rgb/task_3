import allure
from pages.base_page import BasePage
from locators.order_modal_locators import OrderModalLocators

class OrderModalPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = OrderModalLocators()

    @allure.step("Закрыть модальное окно заказа")
    def close(self):
        self._click_by_js(self.locators.CLOSE_BUTTON)

    @allure.step("Получить текст окна заказа")
    def get_modal_text(self):
        return self._get_text(self.locators.ORDER_TEXT)
   
    @allure.step("Проверить, что модальное окно отображается")
    def is_modal_displayed(self):
        return self._is_displayed(self.locators.MODAL_WINDOW) 
    
    @allure.step("Получить номер заказа в окне заказа")
    def get_modal_order_number(self):
        return self._get_text(self.locators.ORDER_NUMBER)
    
    @allure.step("Ожидать появления реального номера заказа (замена заглушки 9999)")
    def wait_for_real_order_number(self):
        self.wait.until(lambda d: "9999" not in d.find_element(*self.locators.ORDER_NUMBER).text, message="Номер заказа не перестал быть 9999 за отведённое время")
