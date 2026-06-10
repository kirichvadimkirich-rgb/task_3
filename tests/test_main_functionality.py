import allure
from config.settings import BASE_URL, API_DOCS_URL
from pages.main_page import MainPage
from pages.ingredient_modal_page import IngredientModalPage
from pages.order_modal_page import OrderModalPage


@allure.feature("Основной функционал")
@allure.link(BASE_URL, name='Ссылка на сайт')
@allure.link(API_DOCS_URL, name='Ссылка на документацию API')
class TestMainFunctionality:

    @allure.title("Переход по клику на «Конструктор»")
    @allure.description("Проверяем, что клик по кнопке «Конструктор» возвращает на главную страницу")
    def test_go_to_constructor(self, browser):
        main_page = MainPage(browser)
        main_page.click_order_feed()
        main_page.click_constructor()

        with allure.step("Проверить, что URL не содержит '/feed' и URL соответствует главной странице"):
            assert "feed" not in browser.current_url
            assert browser.current_url.rstrip('/') == BASE_URL.rstrip('/')

    @allure.title("Переход по клику на «Лента заказов»")
    @allure.description("Проверяем, что клик по кнопке «Лента заказов» открывает страницу /feed")
    def test_go_to_order_feed(self, browser):
        main_page = MainPage(browser)
        main_page.click_order_feed()
        with allure.step("Проверить, что URL содержит '/feed'"):
            assert "feed" in browser.current_url

    @allure.title("Клик на ингредиент открывает всплывающее окно с деталями")
    @allure.description("Проверяем, что при клике на карточку ингредиента появляется модальное окно")
    def test_ingredient_modal_opens(self, browser):
        main_page = MainPage(browser)
        main_page.click_ingredient()
        ingredient_modal = IngredientModalPage(browser)
        with allure.step("Проверить, что модальное окно с заголовком 'Детали ингредиента' отображается"):
            assert ingredient_modal.is_modal_title_displayed(), "Модальное окно с деталями ингредиента не появилось"

    @allure.title("Всплывающее окно с деталями закрывается кликом по крестику")
    @allure.description("Проверяем, что модальное окно ингредиента закрывается по нажатию на крестик")
    def test_ingredient_modal_closes(self, browser):
        main_page = MainPage(browser)
        main_page.click_ingredient()
        ingredient_modal = IngredientModalPage(browser)
        ingredient_modal.close_modal()
        ingredient_modal.wait_for_invisibility()
        with allure.step("Проверить, что модальное окно закрылось"):
            assert not ingredient_modal.is_modal_displayed()

    @allure.title("При добавлении ингредиента в заказ увеличивается счётчик данного ингредиента")
    @allure.description("Проверяем, что после перетаскивания булки счётчик увеличивается на 1")
    def test_counter_increases_when_ingredient_added(self, browser):
        main_page = MainPage(browser)
        main_page.add_bun()
        new_count = main_page.get_bun_counter()
        with allure.step("Проверить, что счётчик булки = 2"):
            assert new_count == 2, f"Ожидалось 2, получено {new_count}"

    @allure.title("Залогиненный пользователь может оформить заказ")
    @allure.description("Проверяем, что авторизованный пользователь может успешно оформить заказ")
    def test_authorized_user_can_order(self, logged_in_browser):
        main_page = MainPage(logged_in_browser)
        main_page.add_bun()
        main_page.add_sauce()
        main_page.add_filling()
        main_page.click_order_button()
        order_modal = OrderModalPage(logged_in_browser)
        with allure.step("Проверить, что появилось модальное окно с подтверждением заказа"):
            assert order_modal.is_modal_displayed(), "Модальное окно заказа не появилось"
        
        with allure.step("Проверить наличие текста 'Ваш заказ начали готовить'"):
            assert order_modal.is_confirmation_text_displayed(), "Текст подтверждения не отображается"