from selenium.webdriver.common.by import By

class LoginPageLocators:
    
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")
    EMAIL_FIELD = (By.XPATH, "//input[@name='name' and @type='text']")
    PASSWORD_FIELD = (By.XPATH, "//input[@name='Пароль' and @type='password']")
    FORGOT_PASSWORD_LINK = (By.XPATH, "//a[text()='Восстановить пароль']")
    PAGE_TITLE = (By.XPATH, "//h2[text()='Вход']")