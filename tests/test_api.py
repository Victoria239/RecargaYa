from fastapi.testclient import TestClient

from recargaya.api import app


client = TestClient(app)


def test_api_calcula_recarga_sin_bonificacion():
    response = client.post(
        "/recargas/calcular",
        json={"monto": 5000, "premium": False},
    )

    assert response.status_code == 200
    assert response.json()["valor_final"] == 5000


def test_api_calcula_recarga_con_bonificacion_10():
    response = client.post(
        "/recargas/calcular",
        json={"monto": 10000, "premium": False},
    )

    assert response.status_code == 200
    assert response.json()["bonificacion"] == 1000
    assert response.json()["valor_final"] == 11000


def test_api_calcula_recarga_con_bonificacion_25():
    response = client.post(
        "/recargas/calcular",
        json={"monto": 30000, "premium": False},
    )

    assert response.status_code == 200
    assert response.json()["bonificacion"] == 7500
    assert response.json()["valor_final"] == 37500


def test_api_calcula_recarga_premium():
    response = client.post(
        "/recargas/calcular",
        json={"monto": 10000, "premium": True},
    )

    assert response.status_code == 200
    assert response.json()["bonificacion"] == 1050
    assert response.json()["valor_final"] == 11050


def test_api_rechaza_monto_invalido():
    response = client.post(
        "/recargas/calcular",
        json={"monto": 999, "premium": False},
    )

    assert response.status_code == 400
    assert response.json()["detail"] == "El monto debe estar entre 1000 y 50000"