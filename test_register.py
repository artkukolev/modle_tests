import pytest
import random
import string

class TestRegistrationFunctionality:
    """Тестирование функциональности регистрации"""
    
    def generate_random_email(self):
        """Генерирует случайный email для тестирования"""
        random_string = ''.join(random.choices(string.ascii_lowercase, k=8))
        return f"test_{random_string}@example.com"
    
    @pytest.mark.register
    def test_successful_registration(self, register_page):
        """
        Тест: Успешная регистрация новой учетной записи
        Ожидаемый результат: Учетная запись успешно создана
        """
        test_email = self.generate_random_email()
        
        register_page.register(
            firstname="Иван",
            lastname="Петров",
            email=test_email,
            telephone="+79991234567",
            password="testpassword123"
        )
        
        assert register_page.is_registration_successful(), "Регистрация не выполнена успешно"
    
    @pytest.mark.register
    def test_registration_with_existing_email(self, register_page):
        """
        Тест: Регистрация с уже существующим email
        Ожидаемый результат: Отображается сообщение об ошибке
        """
        # Используем email, который уже существует в системе
        existing_email = "demo@example.com"
        
        register_page.register(
            firstname="Иван",
            lastname="Петров",
            email=existing_email,
            telephone="+79991234567",
            password="testpassword123"
        )
        
        error_message = register_page.get_error_message()
        assert "уже зарегистрирован" in error_message or "уже используется" in error_message, \
            "Сообщение об ошибке повторной регистрации не отображается"