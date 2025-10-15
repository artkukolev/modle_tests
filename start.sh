# Запуск всех тестов
pytest

# Запуск тестов определенной категории
pytest -m login
pytest -m register
pytest -m search

# Запуск с генерацией Allure отчетов
pytest --alluredir=allure-results
allure serve allure-results