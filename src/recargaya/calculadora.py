MONTO_MINIMO = 1000
MONTO_MAXIMO = 50000
BONIFICACION_MEDIA = 10
BONIFICACION_ALTA = 25
ADICIONAL_PREMIUM = 0.05


def calcular_recarga(monto: int, premium: bool = False) -> dict:
    validar_monto(monto)

    porcentaje_bonificacion = obtener_porcentaje_bonificacion(monto)
    bonificacion_base = monto * (porcentaje_bonificacion / 100)

    bonificacion_total = aplicar_adicional_premium(
        bonificacion_base=bonificacion_base,
        premium=premium,
    )

    valor_final = monto + bonificacion_total

    return {
        "monto": monto,
        "premium": premium,
        "porcentaje_bonificacion": porcentaje_bonificacion,
        "bonificacion": round(bonificacion_total, 2),
        "valor_final": round(valor_final, 2),
    }


def validar_monto(monto: int) -> None:
    if monto < MONTO_MINIMO or monto > MONTO_MAXIMO:
        raise ValueError("El monto debe estar entre 1000 y 50000")


def obtener_porcentaje_bonificacion(monto: int) -> int:
    if monto >= 30000:
        return BONIFICACION_ALTA

    if monto >= 10000:
        return BONIFICACION_MEDIA

    return 0


def aplicar_adicional_premium(bonificacion_base: float, premium: bool) -> float:
    if premium and bonificacion_base > 0:
        return bonificacion_base + (bonificacion_base * ADICIONAL_PREMIUM)

    return bonificacion_base