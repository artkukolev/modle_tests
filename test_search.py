import pytest

class TestSearchFunctionality:
    """Тестирование функциональности поиска"""
    
    @pytest.mark.search
    def test_search_with_valid_keyword(self, search_page):
        """
        Тест: Поиск по существующему ключевому слову
        Ожидаемый результат: Возвращаются соответствующие результаты
        """
        search_page.search_product("iPhone")
        
        results_count = search_page.get_search_results_count()
        assert results_count > 0, "Поиск не вернул результаты"
    
    @pytest.mark.search
    def test_search_with_invalid_keyword(self, search_page):
        """
        Тест: Поиск по несуществующему ключевому слову
        Ожидаемый результат: Отображается сообщение об отсутствии результатов
        """
        search_page.search_product("nonexistentproduct12345")
        
        assert search_page.is_no_results_message_displayed(), \
            "Сообщение об отсутствии результатов не отображается"
    
    @pytest.mark.search
    def test_search_with_empty_query(self, search_page):
        """
        Тест: Поиск с пустым запросом
        Ожидаемый результат: Отображается сообщение об ошибке или пустой результат
        """
        search_page.search_product("")
        
        # Проверяем поведение при пустом поиске
        results_count = search_page.get_search_results_count()
        no_results = search_page.is_no_results_message_displayed()
        
        assert results_count == 0 or no_results, \
            "Пустой поиск должен возвращать 0 результатов или сообщение об ошибке"