import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from utilities.config import Config

@pytest.fixture(scope="function")
def driver():
    # Настройка драйвера
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Для запуска в headless режиме
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )
    driver.implicitly_wait(Config.IMPLICIT_WAIT)
    driver.maximize_window()
    
    yield driver
    
    driver.quit()

@pytest.fixture
def login_page(driver):
    from pages.login_page import LoginPage
    return LoginPage(driver)

@pytest.fixture
def register_page(driver):
    from pages.register_page import RegisterPage
    return RegisterPage(driver)

@pytest.fixture
def search_page(driver):
    from pages.search_page import SearchPage
    return SearchPage(driver)