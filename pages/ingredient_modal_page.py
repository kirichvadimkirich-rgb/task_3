import allure
from pages.base_page import BasePage
from locators.ingredient_modal_locators import IngredientModalLocators


class IngredientModalPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = IngredientModalLocators()

    @allure.step("Получить заголовок модального окна")
    def get_modal_title(self):
        return self._get_text(self.locators.MODAL_TITLE)

    @allure.step("Закрыть модальное окно заказа")
    def close_modal(self):
        self._click_by_js(self.locators.MODAL_CLOSE_BUTTON)

    @allure.step("Проверить, что модальное окно отображается")
    def is_modal_displayed(self):
        return self._is_displayed(self.locators.MODAL_TITLE) 


    @allure.step("Ожидание закрытия модального окна")
    def wait_for_invisibility(self):
          self._wait_for_invisibility(self.locators.MODAL_TITLE)   
