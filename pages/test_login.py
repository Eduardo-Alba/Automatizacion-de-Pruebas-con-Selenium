import pytest
from pages.login_page import LoginPage
from pages.products_page import ProductsPage

def test_valid_login(driver):
    """Verifica que un usuario válido pueda iniciar sesión."""
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")
    
    products_page = ProductsPage(driver)
    assert products_page.is_products_page(), "No se redirigió a la página de inventario tras el login."
    assert products_page.get_page_title() == "Products", "El título de la página no es correcto."

def test_locked_out_user(driver):
    """Verifica el mensaje de error para un usuario bloqueado."""
    login_page = LoginPage(driver)
    login_page.login("locked_out_user", "secret_sauce")
    
    error_msg = login_page.get_error_message()
    assert error_msg is not None, "No apareció el mensaje de error."
    assert "locked out" in error_msg, f"Mensaje de error incorrecto: {error_msg}"

def test_logout(driver):
    """Verifica que se pueda cerrar sesión correctamente."""
    # 1. Login
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")
    
    # 2. Logout
    products_page = ProductsPage(driver)
    products_page.logout()
    
    # 3. Verificar vuelta al login
    assert login_page.is_login_visible(), "El formulario de login no es visible tras el logout."