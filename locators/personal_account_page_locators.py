from selenium.webdriver.common.by import By

class PersonalAccountPageLocators:
    ORDER_HISTORY_LINK = (By.XPATH, "//a[text()='История заказов']")
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")
    FIRST_ORDER_NUMBER_IN_HISTORY = (By.XPATH, "//div[contains(@class, 'OrderHistory')]//a[1]//p")