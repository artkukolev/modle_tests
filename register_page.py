from selenium.webdriver.common.by import By
from .base_page import BasePage

class RegisterPage(BasePage):
    # Locators
    FIRSTNAME_INPUT = (By.ID, "input-firstname")
    LASTNAME_INPUT = (By.ID, "input-lastname")
    EMAIL_INPUT = (By.ID, "input-email")
    TELEPHONE_INPUT = (By.ID, "input-telephone")
    PASSWORD_INPUT = (By.ID, "input-password")
    CONFIRM_PASSWORD_INPUT = (By.ID, "input-confirm")
    AGREE_CHECKBOX = (By.NAME, "agree")
    CONTINUE_BUTTON = (By.XPATH, "//input[@value='Продолжить']")
    SUCCESS_MESSAGE = (By.XPATH, "//h1[contains(text(), 'Ваша учетная запись создана!')]")
    ERROR_MESSAGE = (By.CLASS_NAME, "alert-danger")
    
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get("https://demo-opencart.ru/index.php?route=account/register")
    
    def register(self, firstname, lastname, email, telephone, password):
        """Регистрирует нового пользователя"""
        self.send_keys(self.FIRSTNAME_INPUT, firstname)
        self.send_keys(self.LASTNAME_INPUT, lastname)
        self.send_keys(self.EMAIL_INPUT, email)
        self.send_keys(self.TELEPHONE_INPUT, telephone)
        self.send_keys(self.PASSWORD_INPUT, password)
        self.send_keys(self.CONFIRM_PASSWORD_INPUT, password)
        self.click(self.AGREE_CHECKBOX)
        self.click(self.CONTINUE_BUTTON)
    
    def is_registration_successful(self):
        """Проверяет успешность регистрации"""
        return self.is_visible(self.SUCCESS_MESSAGE)
    
    def get_error_message(self):
        """Возвращает текст сообщения об ошибке"""
        return self.get_text(self.ERROR_MESSAGE) if self.is_visible(self.ERROR_MESSAGE) else ""