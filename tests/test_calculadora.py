import pytest

from recargaya.calculadora import calcular_recarga


def test_rechaza_monto_menor_al_minimo():
    with pytest.raises(ValueError, match="El monto debe estar entre 1000 y 50000"):
        calcular_recarga(999, False)