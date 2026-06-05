import pytest
from pytest_bdd import given, parsers, scenarios, then, when

from recargaya.calculadora import calcular_recarga


scenarios("../recargas.feature")


@pytest.fixture
def contexto():
    return {}


@given("un usuario no premium")
def usuario_no_premium(contexto):
    contexto["premium"] = False


@given("un usuario premium")
def usuario_premium(contexto):
    contexto["premium"] = True


@when(parsers.parse("realiza una recarga de {monto:d} pesos"))
def realizar_recarga(contexto, monto):
    try:
        contexto["resultado"] = calcular_recarga(monto, contexto["premium"])
        contexto["error"] = None
    except ValueError as error:
        contexto["resultado"] = None
        contexto["error"] = str(error)


@then("la recarga debe ser rechazada")
def recarga_rechazada(contexto):
    assert contexto["error"] == "El monto debe estar entre 1000 y 50000"


@then(parsers.parse("el valor final debe ser {valor_final:g} pesos"))
def validar_valor_final(contexto, valor_final):
    assert contexto["resultado"]["valor_final"] == valor_final


@then(parsers.parse("la bonificacion debe ser {bonificacion:g} pesos"))
def validar_bonificacion(contexto, bonificacion):
    assert contexto["resultado"]["bonificacion"] == bonificacion


@then(parsers.parse('el resultado debe ser "{resultado_esperado}"'))
def validar_resultado_limite(contexto, resultado_esperado):
    if resultado_esperado == "rechazado":
        assert contexto["error"] == "El monto debe estar entre 1000 y 50000"
    else:
        assert contexto["error"] is None
        assert contexto["resultado"] is not None