"""
Página base con métodos comunes para todos los Page Objects.
"""
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import config


class BasePage:
    """Clase base con esperas explícitas y métodos reutilizables."""

    def __init__(self, driver, url=None):
        self.driver = driver
        self.url = url or config.BASE_URL
        self.wait = WebDriverWait(driver, config.EXPLICIT_WAIT)

    def open(self):
        """Abre la URL de la página."""
        self.driver.get(self.url)

    def wait_for_element(self, by, value):
        """Espera explícita hasta que el elemento esté presente y visible."""
        return self.wait.until(EC.visibility_of_element_located((by, value)))

    def wait_for_clickable(self, by, value):
        """Espera hasta que el elemento sea clickeable."""
        return self.wait.until(EC.element_to_be_clickable((by, value)))

    def get_current_url(self):
        """Devuelve la URL actual."""
        return self.driver.current_url
