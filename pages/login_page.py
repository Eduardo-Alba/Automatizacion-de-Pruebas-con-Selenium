"""
Page Object para la página de login de SauceDemo.
"""
from selenium.webdriver.common.by import By
from .base_page import BasePage
import config


class LoginPage(BasePage):
    """Página de inicio de sesión."""

    # Locators
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")
    LOGIN_CONTAINER = (By.CLASS_NAME, "login-box")

    def __init__(self, driver):
        super().__init__(driver, config.BASE_URL)

    def open_login(self):
        """Abre la página de login."""
        self.open()

    def enter_username(self, username):
        """Introduce el nombre de usuario."""
        elem = self.wait_for_element(*self.USERNAME_INPUT)
        elem.clear()
        elem.send_keys(username)

    def enter_password(self, password):
        """Introduce la contraseña."""
        elem = self.wait_for_element(*self.PASSWORD_INPUT)
        elem.clear()
        elem.send_keys(password)

    def click_login(self):
        """Hace clic en el botón de login."""
        btn = self.wait_for_clickable(*self.LOGIN_BUTTON)
        btn.click()

    def login(self, username, password):
        """Realiza el login completo."""
        self.open_login()
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def get_error_message(self):
        """Obtiene el mensaje de error si existe."""
        try:
            elem = self.wait_for_element(*self.ERROR_MESSAGE)
            return elem.text
        except Exception:
            return None

    def is_login_visible(self):
        """Comprueba si el formulario de login está visible."""
        try:
            self.wait_for_element(*self.USERNAME_INPUT)
            return True
        except Exception:
            return False
