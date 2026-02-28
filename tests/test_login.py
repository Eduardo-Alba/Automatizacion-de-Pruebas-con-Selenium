"""
Casos de prueba: Inicio de sesión en SauceDemo.
Escenarios: login exitoso, credenciales inválidas, usuario bloqueado.
"""
import pytest
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
import config


@pytest.mark.smoke
class TestLogin:
    """Pruebas del flujo de login."""

    def test_login_exitoso(self, driver, login_page, products_page):
        """
        Caso de prueba: Login con credenciales válidas.
        Precondición: Página de login cargada.
        Pasos: Introducir user y password correctos, pulsar Login.
        Resultado esperado: Redirección a /inventory.html y título "Products".
        """
        login_page.login(config.VALID_USER, config.VALID_PASSWORD)
        assert products_page.is_products_page(), "Debería estar en la página de productos"
        assert products_page.get_page_title() == "Products", "El título debe ser 'Products'"

    def test_login_credenciales_vacias(self, driver, login_page):
        """
        Caso de prueba: Login sin introducir datos.
        Resultado esperado: Mensaje de error y permanencia en login.
        """
        login_page.open_login()
        login_page.click_login()
        error = login_page.get_error_message()
        assert error is not None, "Debe mostrarse un mensaje de error"
        assert "Username is required" in error or "required" in error.lower()

    def test_login_password_incorrecta(self, driver, login_page):
        """
        Caso de prueba: Usuario válido, contraseña incorrecta.
        Resultado esperado: Mensaje de error, no redirección.
        """
        login_page.login(config.VALID_USER, "wrong_password")
        assert login_page.is_login_visible(), "Debe permanecer en la página de login"
        error = login_page.get_error_message()
        assert error is not None
        assert "Username and password do not match" in error or "do not match" in error.lower()

    def test_login_usuario_bloqueado(self, driver, login_page):
        """
        Caso de prueba: Usuario locked_out_user.
        Resultado esperado: Mensaje indicando que el usuario está bloqueado.
        """
        login_page.login(config.LOCKED_USER, config.VALID_PASSWORD)
        assert login_page.is_login_visible()
        error = login_page.get_error_message()
        assert error is not None
        assert "locked out" in error.lower() or "locked" in error.lower()
