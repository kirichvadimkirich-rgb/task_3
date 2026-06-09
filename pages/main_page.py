
import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from locators.base_locators import BaseLocators
from config.settings import BASE_URL


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = MainPageLocators()

    @allure.step("Кликнуть на ингредиент")
    def click_ingredient(self):
        self._click_by_js(MainPageLocators.BUN_INGREDIENT)

    @allure.step("Нажать 'Оформить заказ'")
    def click_order_button(self):
        self._click(self.locators.ORDER_BUTTON)

    @allure.step("Кликнуть на 'Личный кабинет'")
    def click_personal_account(self):
        self._wait_for_overlay(BaseLocators.OVERLAY)
        self._click_by_js(BaseLocators.PERSONAL_ACCOUNT_BUTTON)
    
    @allure.step(f"Ожидание загрузки главной страницы (URL равен {BASE_URL})")
    def wait_for_load(self):
        self.wait.until(lambda d: d.current_url.rstrip('/') == BASE_URL.rstrip('/'))

    @allure.step("Добавить булку 'вверх' в заказ")
    def add_bun(self):
        self._drag_and_drop_js(self.locators.BUN_INGREDIENT, self.locators.BASKET_CONTAINER)

    @allure.step("Добавить соус в заказ")
    def add_sauce(self):
        self._drag_and_drop_js(self.locators.SAUCE_INGREDIENT, self.locators.BASKET_CONTAINER)

    @allure.step("Добавить начинку в заказ")
    def add_filling(self):
        self._drag_and_drop_js(self.locators.FILLING_INGREDIENT, self.locators.BASKET_CONTAINER)

    @allure.step("Кликнуть на 'Конструктор'")
    def click_constructor(self):
        self._click_by_js(BaseLocators.CONSTRUCTOR_BUTTON)
    
    @allure.step("Кликнуть на 'Лента заказов'")
    def click_order_feed(self):
        self._click_by_js(BaseLocators.ORDER_FEED_BUTTON)

    @allure.step("Получить счетчик булочки")
    def get_bun_counter(self):
        text = self._get_text(self.locators.COUNTER_BUN)
        return int(text) if text.isdigit() else 0


