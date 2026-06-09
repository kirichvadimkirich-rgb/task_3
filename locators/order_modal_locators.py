
from selenium.webdriver.common.by import By

class OrderModalLocators:
    
    MODAL_WINDOW = (By.XPATH, "//section[contains(@class, 'Modal_modal_opened__')]/div[1]")
    CLOSE_BUTTON = (By.XPATH, "//button[contains(@class, 'Modal_modal__close')]")
    ORDER_NUMBER = (By.XPATH, "//section[contains(@class, 'Modal_modal_opened__')]//h2")
    ORDER_TEXT = (By.XPATH, "//div[contains(@class, 'Modal_modal__textContainer')]//p[contains(text(), 'Ваш заказ начали готовить')]")