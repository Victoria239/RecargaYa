def calcular_recarga(monto: int, premium: bool = False) -> dict:
    if monto < 1000 or monto > 50000:
        raise ValueError("El monto debe estar entre 1000 y 50000")

    porcentaje_bonificacion = 0

    if monto >= 30000:
        porcentaje_bonificacion = 25
    elif monto >= 10000:
        porcentaje_bonificacion = 10

    bonificacion = monto * (porcentaje_bonificacion / 100)

    if premium and bonificacion > 0:
        bonificacion = bonificacion + (bonificacion * 0.05)

    valor_final = monto + bonificacion

    return {
        "monto": monto,
        "premium": premium,
        "porcentaje_bonificacion": porcentaje_bonificacion,
        "bonificacion": round(bonificacion, 2),
        "valor_final": round(valor_final, 2),
    }