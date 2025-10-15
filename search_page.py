from selenium.webdriver.common.by import By
from .base_page import BasePage

class SearchPage(BasePage):
    # Locators
    SEARCH_INPUT = (By.NAME, "search")
    SEARCH_BUTTON = (By.XPATH, "//button[contains(@class, 'btn-default')]")
    PRODUCT_RESULTS = (By.CLASS_NAME, "product-thumb")
    NO_RESULTS_MESSAGE = (By.XPATH, "//p[contains(text(), 'Нет товаров')]")
    
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get("https://demo-opencart.ru/")
    
    def search_product(self, product_name):
        """Выполняет поиск товара"""
        self.send_keys(self.SEARCH_INPUT, product_name)
        self.click(self.SEARCH_BUTTON)
    
    def get_search_results_count(self):
        """Возвращает количество найденных товаров"""
        return len(self.driver.find_elements(*self.PRODUCT_RESULTS))
    
    def is_no_results_message_displayed(self):
        """Проверяет отображение сообщения об отсутствии результатов"""
        return self.is_visible(self.NO_RESULTS_MESSAGE)