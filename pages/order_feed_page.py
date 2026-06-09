import allure
from pages.base_page import BasePage
from locators.order_feed_page_locators import OrderFeedPageLocators
from config.settings import BASE_URL
from config.endpoints import ORDER_FEED_URL

class OrderFeedPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = OrderFeedPageLocators()

    @allure.step("Открыть страницу ленты заказов")
    def open(self):
        self.driver.get(f"{BASE_URL}{ORDER_FEED_URL}")

    @allure.step("Кликнуть на первый заказ в ленте")
    def click_first_order(self):
        self._click(self.locators.FIRST_ORDER)

    @allure.step("Проверить, что модальное окно заказа отображается")
    def is_order_modal_displayed(self):
        return self._is_displayed(self.locators.ORDER_MODAL)

    @allure.step("Получить счётчик «Выполнено за всё время»")
    def get_all_time_counter(self):
        text = self._get_text(self.locators.COUNTER_ALL_TIME)
        return int(text) if text.isdigit() else 0

    @allure.step("Получить счётчик «Выполнено за сегодня»")
    def get_today_counter(self):
        text = self._get_text(self.locators.COUNTER_TODAY)
        return int(text) if text.isdigit() else 0

    @allure.step("Получить текст блока «В работе» (номера заказов)")
    def get_order_numbers_in_work(self):
        return self._get_text(self.locators.ORDER_NUMBER_IN_WORK)

    @allure.step("Ожидание появления номера заказа на странице ленты")
    def wait_for_order_number(self, order_number):
        self.wait.until(lambda d: str(order_number) in d.page_source, message=f"Заказ {order_number} не появился")   

    @allure.step("Получить номер первого заказа из ленты")
    def get_first_order_number_from_feed(self):
        return self._get_number_from_text(self.locators.FIRST_ORDER_NUMBER)  
    
    @allure.step("Ожидать появления номера заказа в блоке «В работе»")
    def wait_for_order_in_work(self, order_number):
        self.wait.until(lambda d: str(order_number) in d.find_element(*self.locators.ORDER_NUMBER_IN_WORK).text)