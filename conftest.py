import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from config.settings import BASE_URL, SUPPORTED_BROWSERS 
from api_clients.user_client import UserClient
from data.generator import generate_user_data
from pages.main_page import MainPage
from pages.login_page import LoginPage
from api_clients.order_client import OrderClient
from api_clients.ingredients_client import IngredientsClient

@pytest.fixture(params=SUPPORTED_BROWSERS)
def browser(request):
    if request.param == "chrome":
        options = ChromeOptions()
        options.add_argument("--window-size=1920,1080")
        driver = webdriver.Chrome(options=options)
    elif request.param == "firefox":
        options = FirefoxOptions()
        options.add_argument("--width=1920")
        options.add_argument("--height=1080")
        driver = webdriver.Firefox(options=options)
    else:
        raise ValueError(f"Неподдерживаемый браузер: {request.param}")
    driver.get(BASE_URL)
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def create_user_and_login():
    """Создать пользователя через API, возврнуть данные и токен. После теста пользователь удаляется."""
    user_client = UserClient()
    user_data = generate_user_data()
    reg_resp = user_client.register(user_data)
    token = reg_resp.json().get("accessToken")
    yield {
        "email": user_data["email"],
        "password": user_data["password"],
        "token": token,
        "name": user_data["name"]
    }
    if token:
        user_client.delete_user(token)

@pytest.fixture
def logged_in_browser(browser, create_user_and_login):
    """Возвращает браузер, уже авторизованный через UI."""
    main_page = MainPage(browser)
    main_page.click_personal_account()
    login_page = LoginPage(browser)
    login_page.login(create_user_and_login["email"], create_user_and_login["password"])
    main_page.wait_for_load()
    return browser

@pytest.fixture
def ingredients_client():
    return IngredientsClient()

@pytest.fixture
def real_ingredient_id(ingredients_client):
    response = ingredients_client.get_ingredients()
    ingredients = response.json()["data"]
    return ingredients[0]["_id"]

@pytest.fixture
def create_order_api(create_user_and_login, real_ingredient_id):
    """Создаёт заказ через API для авторизованного пользователя и возвращает номер заказа."""
    order_client = OrderClient()
    token = create_user_and_login["token"]
    ingredients = [real_ingredient_id]
    response = order_client.create_order(ingredients, token=token)
    order_number = response.json()["order"]["number"]
    return order_number
