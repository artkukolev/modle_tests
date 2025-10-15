import pytest
import time

class TestLoginFunctionality:
    """Тестирование функциональности входа в систему"""
    
    @pytest.mark.login
    def test_successful_login(self, login_page):
        """
        Тест: Успешный вход с корректными учетными данными
        Ожидаемый результат: Пользователь успешно входит в систему
        """
        # Используем тестовые данные (в реальном проекте нужно использовать тестового пользователя)
        login_page.login("demo@example.com", "demo")
        
        assert login_page.is_login_successful(), "Вход не выполнен успешно"
    
    @pytest.mark.login
    def test_login_with_invalid_credentials(self, login_page):
        """
        Тест: Вход с некорректными учетными данными
        Ожидаемый результат: Отображается сообщение об ошибке
        """
        login_page.login("invalid@example.com", "wrongpassword")
        
        error_message = login_page.get_error_message()
        assert "не совпадает" in error_message or "не найден" in error_message, \
            "Сообщение об ошибке не отображается"