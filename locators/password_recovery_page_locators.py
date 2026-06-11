from selenium.webdriver.common.by import By

class PasswordRecoveryPageLocators:
    PAGE_TITLE = (By.XPATH, "//h2[text()='Восстановление пароля']")
    EMAIL_FIELD = (By.XPATH, "//input[@name='name']")
    RECOVER_BUTTON = (By.XPATH, "//button[text()='Восстановить']")
    SHOW_PASSWORD_BUTTON = (By.XPATH, "//div[contains(@class, 'input__icon')]")
    ACTIVE_INPUT = (By.CSS_SELECTOR, "div.input.input_type_text.input_status_active")
    