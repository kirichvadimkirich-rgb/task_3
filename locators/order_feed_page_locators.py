from selenium.webdriver.common.by import By

class OrderFeedPageLocators:

    FIRST_ORDER = (By.XPATH, "//ul[contains(@class, 'OrderFeed_list')]/li[1]/a")
    ORDER_MODAL = (By.XPATH, "//div[contains(@class, 'Modal_order')]")
    COUNTER_ALL_TIME = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p")
    COUNTER_TODAY = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p")
    ORDER_NUMBER_IN_WORK = (By.XPATH, "//ul[contains(@class, 'OrderFeed_orderListReady')]//li[contains(@class, 'text_type_digits-default')]")
    FIRST_ORDER_NUMBER = (By.XPATH, "//ul[contains(@class, 'OrderFeed_list')]/li[1]//p[(@class= 'text text_type_digits-default')]")