from selenium.webdriver.common.by import By

class IngredientModalLocators:

    MODAL_TITLE = (By.XPATH, "//h2[text()='Детали ингредиента']")
    MODAL_CLOSE_BUTTON = (By.XPATH, "//section[contains(@class, 'Modal_modal_opened__')]//button")
   