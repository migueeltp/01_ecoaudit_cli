# =====================================================================
# EcoAudit CLI - Módulo de Cálculo Matemático
# Autor: David Pavía Pérez
# =====================================================================


def estimar_consumo_wh(wh: float, horasuso: float) -> float:
    """Calcula el consumo total en Wh a partir de la potencia y el tiempo de uso."""
    consumo = wh * horasuso
    return consumo


def calcular_huella_co2(consumo: float, factor_emision: float = 0.23) -> float:
    """Calcula la huella de carbono en kg de CO2 a partir del consumo en Wh."""
    huellaco2 = (consumo / 1000) * factor_emision
    return huellaco2


def clasificar_etiqueta_energetica(consumo: float) -> str:
    """Devuelve una etiqueta de eficiencia según el consumo estimado."""
    if consumo < 500:
        return "El dispositivo es eficiente"
    elif 500 <= consumo < 2000:
        return "El dispositivo es moderadamente eficiente"
    else:
        return "El dispositivo no es eficiente, requiere de optimización"


def c(consumo: float) -> str:
    """Alias de compatibilidad para mantener el código antiguo funcionando."""
    return clasificar_etiqueta_energetica(consumo)


def main() -> None:
    wh = float(input("Deme la potencia del dispositivo en W: ").strip())
    horasuso = float(input("Deme el tiempo de uso del dispositivo en horas: ").strip())
    consumo = estimar_consumo_wh(wh, horasuso)
    print(f"El consumo total de este dispositivo es de {consumo} Wh")
    print(clasificar_etiqueta_energetica(consumo))
    print(f"La huella de carbono provocada es de {calcular_huella_co2(consumo):.4f} kg de CO2")


if __name__ == "__main__":
    main()