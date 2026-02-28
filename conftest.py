"""
Configuración de pytest: fixtures para WebDriver, esperas y reportes.
"""
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import config


def pytest_configure(config):
    """Añade marcadores personalizados."""
    config.addinivalue_line(
        "markers", "smoke: pruebas críticas de humo (login, navegación)"
    )
    config.addinivalue_line(
        "markers", "checkout: pruebas del flujo de checkout"
    )


@pytest.fixture(scope="function")
def driver():
    """
    Crea y cierra el WebDriver para cada test.
    Usa webdriver-manager para gestionar ChromeDriver automáticamente.
    """
    options = Options()
    options.add_argument("--headless")  # Descomenta para ver el navegador
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--window-size=1920,1080")
    service = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=service, options=options)
    browser.implicitly_wait(config.IMPLICIT_WAIT)
    browser.maximize_window()
    yield browser
    browser.quit()


@pytest.fixture
def login_page(driver):
    """Proporciona la página de login ya instanciada."""
    from pages.login_page import LoginPage
    return LoginPage(driver)


@pytest.fixture
def products_page(driver):
    """Proporciona la página de productos (requiere estar logueado)."""
    from pages.products_page import ProductsPage
    return ProductsPage(driver)


@pytest.fixture
def cart_page(driver):
    """Proporciona la página del carrito."""
    from pages.cart_page import CartPage
    return CartPage(driver)


@pytest.fixture
def logged_in_driver(driver, login_page):
    """Driver con sesión ya iniciada como standard_user."""
    login_page.login(config.VALID_USER, config.VALID_PASSWORD)
    return driver
