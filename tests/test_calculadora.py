import pytest

from recargaya.calculadora import calcular_recarga


def test_rechaza_monto_menor_al_minimo():
    with pytest.raises(ValueError, match="El monto debe estar entre 1000 y 50000"):
        calcular_recarga(999, False)


def test_rechaza_monto_mayor_al_maximo():
    with pytest.raises(ValueError, match="El monto debe estar entre 1000 y 50000"):
        calcular_recarga(50001, False)


def test_acepta_monto_minimo_sin_bonificacion():
    resultado = calcular_recarga(1000, False)

    assert resultado["monto"] == 1000
    assert resultado["bonificacion"] == 0
    assert resultado["valor_final"] == 1000


def test_recarga_menor_a_10000_no_tiene_bonificacion():
    resultado = calcular_recarga(9999, False)

    assert resultado["porcentaje_bonificacion"] == 0
    assert resultado["bonificacion"] == 0
    assert resultado["valor_final"] == 9999


def test_recarga_de_10000_recibe_10_por_ciento():
    resultado = calcular_recarga(10000, False)

    assert resultado["porcentaje_bonificacion"] == 10
    assert resultado["bonificacion"] == 1000
    assert resultado["valor_final"] == 11000


def test_recarga_de_29999_recibe_10_por_ciento():
    resultado = calcular_recarga(29999, False)

    assert resultado["porcentaje_bonificacion"] == 10
    assert resultado["bonificacion"] == 2999.9
    assert resultado["valor_final"] == 32998.9


def test_recarga_de_30000_recibe_25_por_ciento():
    resultado = calcular_recarga(30000, False)

    assert resultado["porcentaje_bonificacion"] == 25
    assert resultado["bonificacion"] == 7500
    assert resultado["valor_final"] == 37500


def test_recarga_de_50000_es_valida():
    resultado = calcular_recarga(50000, False)

    assert resultado["porcentaje_bonificacion"] == 25
    assert resultado["bonificacion"] == 12500
    assert resultado["valor_final"] == 62500


def test_usuario_premium_recibe_5_por_ciento_adicional_sobre_bonificacion_10():
    resultado = calcular_recarga(10000, True)

    assert resultado["porcentaje_bonificacion"] == 10
    assert resultado["bonificacion"] == 1050
    assert resultado["valor_final"] == 11050


def test_usuario_premium_recibe_5_por_ciento_adicional_sobre_bonificacion_25():
    resultado = calcular_recarga(30000, True)

    assert resultado["porcentaje_bonificacion"] == 25
    assert resultado["bonificacion"] == 7875
    assert resultado["valor_final"] == 37875


def test_usuario_premium_sin_bonificacion_base_no_recibe_adicional():
    resultado = calcular_recarga(5000, True)

    assert resultado["porcentaje_bonificacion"] == 0
    assert resultado["bonificacion"] == 0
    assert resultado["valor_final"] == 5000