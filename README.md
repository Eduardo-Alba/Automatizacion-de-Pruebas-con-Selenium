# Automatización de Pruebas con Selenium – SauceDemo

Proyecto de pruebas automatizadas para el sitio [SauceDemo](https://www.saucedemo.com) (Swag Labs), utilizando **Selenium WebDriver** y **pytest** en **Python**.

---

## 1. Sitio web bajo prueba

- **URL:** https://www.saucedemo.com  
- **Descripción:** Tienda demo para prácticas de automatización (login, catálogo, carrito y checkout).

---

## 2. Configuración del entorno

### Requisitos

- Python 3.8 o superior  
- Navegador Chrome (recomendado) o Chromium  

### Instalación

```bash
cd "tarea 9"
pip install -r requirements.txt
```

Dependencias principales:

- `selenium` – WebDriver  
- `webdriver-manager` – Gestión automática del ChromeDriver  
- `pytest` – Marco de pruebas  
- `pytest-html` – Reportes HTML  

---

## 3. Escenarios de prueba

| # | Escenario              | Descripción                                      |
|---|------------------------|--------------------------------------------------|
| 1 | Inicio de sesión       | Login con credenciales válidas e inválidas       |
| 2 | Navegación             | Ir al carrito, volver a productos, cerrar sesión |
| 3 | Carrito                | Añadir productos y comprobar badge/cantidad      |
| 4 | Checkout               | Flujo completo: datos, resumen y confirmación    |

---

## 4. Casos de prueba (resumen)

### Login (`tests/test_login.py`)

| Caso                    | Pasos                         | Resultado esperado                          |
|-------------------------|-------------------------------|---------------------------------------------|
| Login exitoso           | user/password válidos, Login  | Redirección a productos, título "Products"  |
| Credenciales vacías     | Login sin datos               | Mensaje de error "Username is required"     |
| Password incorrecta     | user válido, password errónea | Mensaje "do not match", permanece en login  |
| Usuario bloqueado       | locked_out_user               | Mensaje "locked out"                        |

### Navegación (`tests/test_navigation.py`)

| Caso                          | Resultado esperado                    |
|-------------------------------|----------------------------------------|
| Ir al carrito desde productos | URL con "cart", página carrito visible |
| Continuar comprando           | Volver a /inventory                    |
| Cerrar sesión                 | Volver a página de login               |

### Carrito (`tests/test_cart.py`)

| Caso                    | Resultado esperado              |
|-------------------------|----------------------------------|
| Añadir un producto      | Badge del carrito = 1            |
| Añadir varios           | Badge refleja la cantidad        |
| Ver productos en carrito| Al menos 1 ítem en la lista       |

### Checkout (`tests/test_checkout.py`)

| Caso              | Datos (ejemplo)     | Resultado esperado              |
|-------------------|---------------------|----------------------------------|
| Checkout completo | Nombre, apellido, CP| Página "Thank you for your order!" |

---

## 5. Estructura del proyecto

```
tarea 9/
├── config.py           # URL base, credenciales, timeouts
├── conftest.py         # Fixtures pytest (driver, páginas)
├── pytest.ini          # Configuración pytest y marcadores
├── requirements.txt    # Dependencias
├── run_tests.py        # Script para ejecutar pruebas y reporte
├── README.md           # Esta documentación
├── pages/              # Page Object Model
│   ├── base_page.py
│   ├── login_page.py
│   ├── products_page.py
│   ├── cart_page.py
│   └── checkout_page.py
├── tests/
│   ├── test_login.py
│   ├── test_navigation.py
│   ├── test_cart.py
│   └── test_checkout.py
└── reportes/           # Reportes HTML (generados al ejecutar)
```

---

## 6. Credenciales de prueba (SauceDemo)

| Usuario               | Contraseña   | Uso                    |
|-----------------------|-------------|------------------------|
| standard_user         | secret_sauce| Flujo normal           |
| locked_out_user       | secret_sauce| Usuario bloqueado      |
| problem_user          | secret_sauce| Comportamiento errático|
| performance_glitch_user | secret_sauce | Lentitud              |

---

## 7. Ejecución de pruebas

### Todas las pruebas (con reporte HTML)

```bash
python run_tests.py
```

### Solo con pytest (sin reporte HTML)

```bash
python run_tests.py --no-report
```

### Línea de comandos directa

```bash
# Todas las pruebas
pytest tests/ -v

# Con reporte HTML
pytest tests/ -v --html=reportes/reporte.html --self-contained-html

# Solo pruebas de login
pytest tests/test_login.py -v

# Solo pruebas marcadas como smoke
pytest tests/ -v -m smoke

# Solo checkout
pytest tests/ -v -m checkout
```

---

## 8. Comportamiento técnico

- **WebDriver:** Chrome, gestionado con `webdriver-manager`.  
- **Esperas:** Implícitas (10 s) en el driver; explícitas (15 s) en los Page Objects.  
- **Modo headless:** Por defecto en `conftest.py`. Para ver el navegador, comenta la línea `options.add_argument("--headless")` en `conftest.py`.  
- **Reportes:** `pytest-html` genera un HTML en `reportes/reporte_YYYYMMDD_HHMMSS.html`.

---

## 9. Replicar las pruebas

1. Clonar o copiar el proyecto en tu máquina.  
2. Crear un entorno virtual (opcional): `python -m venv venv` y activarlo.  
3. Instalar dependencias: `pip install -r requirements.txt`.  
4. Ejecutar: `python run_tests.py`.  
5. Revisar el reporte en la carpeta `reportes/`.

---

## 10. Notas

- Las pruebas son independientes: cada una obtiene un driver nuevo y cierra el navegador al final.  
- Los selectores usan `id` y `data-test` cuando está disponible para mayor estabilidad.  
- Para el video de entrega: ejecuta `python run_tests.py` con `--headless` comentado en `conftest.py` para grabar la ejecución en pantalla.
