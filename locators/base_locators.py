from selenium.webdriver.common.by import By

class BaseLocators:
  
   PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//a[@href='/account']")
   CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")
   ORDER_FEED_BUTTON = (By.XPATH, "//p[text()='Лента Заказов']")
   OVERLAY = (By.CLASS_NAME, "Modal_modal_overlay__x2ZCr")