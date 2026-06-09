import allure
from config.settings import BASE_URL, API_DOCS_URL
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage
from api_clients.order_client import OrderClient
from locators.main_page_locators import MainPageLocators
import time
from pages.order_modal_page import OrderModalPage
from pages.personal_account_page import PersonalAccountPage


@allure.feature("Лента заказов")
@allure.link(BASE_URL, name='Ссылка на сайт')
@allure.link(API_DOCS_URL, name='Ссылка на документацию API')
class TestOrderFeed:

    @allure.title("Клик на заказ открывает всплывающее окно с деталями")
    @allure.description("Проверяем, что при клике на карточку заказа в ленте появляется модальное окно с деталями")
    def test_order_modal_opens_on_click(self, logged_in_browser, create_order_api):

        with allure.step("Создать заказ через API и получить номер созданного заказа"):
            order_number = create_order_api

        main_page = MainPage(logged_in_browser)
        main_page.click_order_feed()
        order_feed = OrderFeedPage(logged_in_browser)
        order_feed.wait_for_order_number(order_number)
        order_feed.click_first_order() 
        with allure.step("Проверить, что модальное окно заказа отображается"):
            assert order_feed.is_order_modal_displayed()

    @allure.title("Заказы пользователя из истории заказов отображаются в ленте заказов")
    @allure.description("Проверяем, что номер заказа, полученный из истории заказов, присутствует в ленте заказов")
    def test_user_orders_appear_in_feed(self, logged_in_browser, create_order_api):

        with allure.step("Создать заказ через API и получить номер созданного заказа"):
            create_order_api

        main_page = MainPage(logged_in_browser)
        main_page.click_personal_account()
        personal_page = PersonalAccountPage(logged_in_browser)
        personal_page.go_to_order_history()
        order_history_number = personal_page.get_first_order_number_from_history()
        main_page.click_order_feed()
        order_feed = OrderFeedPage(logged_in_browser)
        order_feed_number = order_feed.get_first_order_number_from_feed()
        with allure.step("Проверить, что в ленте заказов- номер заказа такой же, как и в истории заказов"):
            assert int(order_history_number) == int(order_feed_number), f"Номер заказа не совпадает: {int(order_history_number)} vs {int(order_feed_number)}"

    @allure.title("При создании нового заказа счётчик «Выполнено за всё время» увеличивается")
    @allure.description("Проверяем, что после создания заказа увеличивается общий счётчик")
    def test_all_time_counter_increments(self, logged_in_browser, create_user_and_login, real_ingredient_id):
        main_page = MainPage(logged_in_browser)
        main_page.click_order_feed()
        order_feed = OrderFeedPage(logged_in_browser)
        before = order_feed.get_all_time_counter()
        with allure.step("Создать заказ через API"):
            token = create_user_and_login["token"]
            order_client = OrderClient()
            order_client.create_order([real_ingredient_id], token=token)
        
        order_feed.open()
        after = order_feed.get_all_time_counter()
        with allure.step("Проверить, что счётчик «Выполнено за всё время» увеличился"):
            assert after > before, f"Счётчик не увеличился: было {before}, стало {after}"

    @allure.title("При создании нового заказа счётчик «Выполнено за сегодня» увеличивается")
    @allure.description("Проверяем, что после создания заказа увеличивается сегодняшний счётчик")
    def test_today_counter_increments(self, logged_in_browser, create_user_and_login, real_ingredient_id):
        order_feed = OrderFeedPage(logged_in_browser)
        order_feed.open()
        before = order_feed.get_today_counter()

        with allure.step("Создать заказ через API"):
            token = create_user_and_login["token"]
            order_client = OrderClient()
            order_client.create_order([real_ingredient_id], token=token)

        order_feed.open()
        after = order_feed.get_today_counter()
        with allure.step("Проверить, что счётчик «Выполнено за сегодня» увеличился"):
            assert after > before, f"Счётчик не увеличился: было {before}, стало {after}"

    @allure.title("После оформления заказа его номер появляется в разделе «В работе»")
    @allure.description("Проверяем, что номер созданного заказа отображается в блоке «В работе» на странице ленты")
    def test_order_number_appears_in_work(self, logged_in_browser):
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
        main_page.click_order_feed()
        order_feed = OrderFeedPage(logged_in_browser)

        with allure.step(f"Проверить, что номер заказа {order_number} появился в блоке «В работе»"):
            order_feed.wait_for_order_in_work(order_number)
            assert order_number in order_feed.get_order_numbers_in_work()