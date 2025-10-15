from selenium.webdriver.common.by import By
from .base_page import BasePage

class LoginPage(BasePage):
    # Locators
    EMAIL_INPUT = (By.ID, "input-email")
    PASSWORD_INPUT = (By.ID, "input-password")
    LOGIN_BUTTON = (By.XPATH, "//input[@value='Войти']")
    ERROR_MESSAGE = (By.CLASS_NAME, "alert-danger")
    SUCCESS_MESSAGE = (By.XPATH, "//h2[contains(text(), 'Мой Аккаунт')]")
    
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get("https://demo-opencart.ru/index.php?route=account/login")
    
    def login(self, email, password):
        """Выполняет вход в систему"""
        self.send_keys(self.EMAIL_INPUT, email)
        self.send_keys(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)
    
    def get_error_message(self):
        """Возвращает текст сообщения об ошибке"""
        return self.get_text(self.ERROR_MESSAGE) if self.is_visible(self.ERROR_MESSAGE) else ""
    
    def is_login_successful(self):
        """Проверяет успешность входа"""
        return self.is_visible(self.SUCCESS_MESSAGE)