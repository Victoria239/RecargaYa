# RecargaYa S.A.S. - Módulo de cálculo de recargas

Este proyecto implementa un módulo para calcular el valor final de recargas de celular, aplicando validación de monto, bonificaciones por rango y bonificación adicional para usuarios premium.

## Reglas de negocio

- El monto de recarga debe estar entre $1.000 y $50.000.
- Recargas menores a $1.000 o mayores a $50.000 deben ser rechazadas.
- Recargas desde $10.000 reciben 10% de bonificación.
- Recargas desde $30.000 reciben 25% de bonificación.
- Usuarios premium reciben 5% adicional sobre la bonificación obtenida.
- Si no existe bonificación base, el usuario premium no recibe adicional.

## Tecnologías utilizadas

- Python
- FastAPI
- Pytest
- Pytest-Cov
- Pytest-BDD
- Locust
- GitHub Actions

## Estructura del proyecto

```text
RecargaYa/
├── src/
│   └── recargaya/
│       ├── __init__.py
│       ├── api.py
│       └── calculadora.py
├── tests/
│   ├── test_api.py
│   └── test_calculadora.py
├── features/
│   ├── recargas.feature
│   └── steps/
│       └── test_recargas_steps.py
├── locustfile.py
├── pytest.ini
├── requirements.txt
├── README.md
└── .github/
    └── workflows/
        └── ci.yml