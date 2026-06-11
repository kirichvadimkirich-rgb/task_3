from selenium.webdriver.common.by import By

class MainPageLocators:

    BUN_INGREDIENT = (By.XPATH, "//img[@alt='Краторная булка N-200i']/ancestor::a[contains(@class, 'BurgerIngredient_ingredient')]")
    SAUCE_INGREDIENT = (By.XPATH, "//img[@alt='Соус с шипами Антарианского плоскоходца']/ancestor::a[contains(@class, 'BurgerIngredient_ingredient')]")
    FILLING_INGREDIENT = (By.XPATH, "//img[@alt='Плоды Фалленианского дерева']/ancestor::a[contains(@class, 'BurgerIngredient_ingredient')]")
    COUNTER_BUN = (By.XPATH, "//img[@alt='Краторная булка N-200i']/parent::a//div[contains(@class, 'counter_counter')]//p")
    BASKET_CONTAINER = (By.XPATH, "//section[contains(@class, 'BurgerConstructor')]/ul")
    ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
   

