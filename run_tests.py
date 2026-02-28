"""
Script para ejecutar las pruebas y generar reporte HTML.
Uso: python run_tests.py
      python run_tests.py --report   (genera reporte en reportes/)
"""
import subprocess
import sys
import os
from datetime import datetime

def main():
    base = os.path.dirname(os.path.abspath(__file__))
    report_dir = os.path.join(base, "reportes")
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    report_file = os.path.join(report_dir, f"reporte_{timestamp}.html")
    os.makedirs(report_dir, exist_ok=True)
    args = [
        sys.executable, "-m", "pytest",
        "tests/",
        "-v",
        "--tb=short",
        f"--html={report_file}",
        "--self-contained-html",
    ]
    print("Ejecutando pruebas...")
    result = subprocess.run(args, cwd=base)
    if result.returncode == 0:
        print(f"Reporte HTML: {report_file}")
    return result.returncode

if __name__ == "__main__":
    sys.exit(main())
