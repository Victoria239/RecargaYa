def calcular_recarga(monto: int, premium: bool = False) -> dict:
    if monto < 1000 or monto > 50000:
        raise ValueError("El monto debe estar entre 1000 y 50000")

    return {
        "monto": monto,
        "premium": premium,
        "porcentaje_bonificacion": 0,
        "bonificacion": 0,
        "valor_final": monto,
    }
