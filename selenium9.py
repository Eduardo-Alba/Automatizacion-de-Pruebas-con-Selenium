"""
Práctica: Automatización de Pruebas en Selenium para SauceDemo.
Ejecuta la suite de pruebas y genera el reporte HTML.

Uso:
    python selenium9.py          # Ejecuta todas las pruebas con reporte
    python selenium9.py --no-html # Solo ejecuta las pruebas (sin reporte)
"""
import subprocess
import sys
import os

if __name__ == "__main__":
    base = os.path.dirname(os.path.abspath(__file__))
    args = [sys.executable, "-m", "pytest", "tests/", "-v", "--tb=short"]
    if "--no-html" not in sys.argv:
        from datetime import datetime
        report_dir = os.path.join(base, "reportes")
        os.makedirs(report_dir, exist_ok=True)
        report_file = os.path.join(report_dir, f"reporte_{datetime.now().strftime('%Y%m%d_%H%M%S')}.html")
        args.extend([f"--html={report_file}", "--self-contained-html"])
        print("Generando reporte HTML en reportes/")
    result = subprocess.run(args, cwd=base)
    sys.exit(result.returncode)
