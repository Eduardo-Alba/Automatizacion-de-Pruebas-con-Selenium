import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
import config

@pytest.fixture(scope="function")
def driver():
    """
    Fixture de Pytest para inicializar el WebDriver antes de cada prueba
    y cerrarlo al finalizar.
    """
    if config.BROWSER.lower() == "chrome":
        driver = webdriver.Chrome()
    elif config.BROWSER.lower() == "firefox":
        driver = webdriver.Firefox()
    elif config.BROWSER.lower() == "edge":
        driver = webdriver.Edge()
    else:
        driver = webdriver.Chrome()

    driver.maximize_window()
    
    if hasattr(config, 'IMPLICIT_WAIT'):
        driver.implicitly_wait(config.IMPLICIT_WAIT)

    yield driver

    driver.quit()

@pytest.fixture
def login_page(driver):
    """Fixture para instanciar la página de login."""
    return LoginPage(driver)

@pytest.fixture
def products_page(driver):
    """Fixture para instanciar la página de productos."""
    return ProductsPage(driver)