
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import allure
import re

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def _is_displayed(self, locator, timeout=3):
        try:
            self._wait_until_visible(locator, timeout)
            return True
        except TimeoutException:
            return False  

    def _wait_until_visible(self, locator, timeout=3):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))   
    
    def _is_clickable(self, locator, timeout=3):
        try:
            self._wait_until_clickable(locator, timeout)
            return True
        except TimeoutException:
            return False

    def _wait_until_clickable(self, locator, timeout=3):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator)) 

    def _click(self, locator):
        self._wait_until_clickable(locator).click()

    def _click_by_js(self, locator, timeout=3):
        element = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
        self.driver.execute_script("arguments[0].click();", element)    

    def _get_text(self, locator):
        element = self._wait_until_visible(locator)
        return element.text
    
    def _send_keys(self, locator, text):
        element = self._wait_until_visible(locator)
        element.clear()
        element.send_keys(text)

    @allure.step("Ожидаем url")
    def _wait_for_url(self, expected_part, timeout=5):
        WebDriverWait(self.driver, timeout).until(lambda d: expected_part in d.current_url)   

    @allure.step("Получение цвета поля/рамки")
    def _get_css_property(self, locator, property_name):
        # property_name: имя CSS-свойства (например, 'border-color', 'color')
        element = self._wait_until_visible(locator)
        return element.value_of_css_property(property_name)  

    def _wait_for_rgb_color(self, locator, property_name, expected_rgb, timeout=5):
        #Ожидает, пока CSS-свойство элемента не станет равно ожидаемому RGB.
        def check(driver):
            element = driver.find_element(*locator)
            color = element.value_of_css_property(property_name)
        # Извлекаем числа из формата rgb(...) или rgba(...)
            import re
            match = re.search(r'rgba?\((\d+),\s*(\d+),\s*(\d+)', color)
            if match:
                actual_rgb = tuple(map(int, match.groups()[:3]))
                return actual_rgb == expected_rgb
            return False
        WebDriverWait(self.driver, timeout).until(check)

    def _wait_for_overlay(self,locator, timeout=10):
        #Ожидает исчезновения стандартного слоя затемнения.
        try:
            WebDriverWait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))
        except TimeoutException:
            pass  # Если оверлея нет, просто продолжаем    

    def _drag_and_drop_js(self, source_locator, target_locator):
        source = self._wait_until_visible(source_locator)
        target = self._wait_until_visible(target_locator)
        js = """
        function simulateDragDrop(src, dst) {
            var dataTransfer = new DataTransfer();
            var dragStartEvent = new DragEvent('dragstart', { bubbles: true, cancelable: true, dataTransfer: dataTransfer });
            src.dispatchEvent(dragStartEvent);
        
            var dragEnterEvent = new DragEvent('dragenter', { bubbles: true, cancelable: true, dataTransfer: dataTransfer });
            dst.dispatchEvent(dragEnterEvent);
        
            var dragOverEvent = new DragEvent('dragover', { bubbles: true, cancelable: true, dataTransfer: dataTransfer });
            dst.dispatchEvent(dragOverEvent);
        
            var dropEvent = new DragEvent('drop', { bubbles: true, cancelable: true, dataTransfer: dataTransfer });
            dst.dispatchEvent(dropEvent);
        
            var dragEndEvent = new DragEvent('dragend', { bubbles: true, cancelable: true, dataTransfer: dataTransfer });
            src.dispatchEvent(dragEndEvent);
        }
        simulateDragDrop(arguments[0], arguments[1]);
        """
        self.driver.execute_script(js, source, target)  

    def _wait_for_invisibility(self, locator, timeout=5):
    #Ожидает, пока элемент станет невидимым или исчезнет из DOM.
        WebDriverWait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))

    def _get_number_from_text(self, locator):
        element = self._wait_until_visible(locator)
        text = element.text
        # Извлекаем цифры из текста (номер заказа)
        match = re.search(r'\d+', text)
        assert match, f"Не удалось извлечь номер заказа из текста: {text}"
        return match.group()

