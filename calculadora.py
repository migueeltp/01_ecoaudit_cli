# =====================================================================
# EcoAudit CLI - Módulo de Cálculo Matemático
# Autor: David Pavía Pérez
# =====================================================================


def estimar_consumo_wh(wh: float, horasuso: float) -> float:
    """Calcula el consumo total en Wh."""
    consumo = wh * horasuso
    print(f"El consumo total de este dispositivo es de {consumo} Wh")
    return consumo


def calcular_huella_co2(consumo: float, factor_emision: float = 0.23) -> float:
    """Calcula la huella de carbono en kg de CO2 a partir del consumo en Wh."""
    huellaco2 = (consumo / 1000) * factor_emision
    print(f"La huella de carbono provocada es de {huellaco2} kg de CO2")
    return huellaco2


def main() -> None:
    wh = float(input("Deme el consumo del dispositivo en W: ").strip())
    horasuso = float(input("Deme el tiempo de uso del dispositivo en horas: ").strip())
    consumo = estimar_consumo_wh(wh, horasuso)
    calcular_huella_co2(consumo)


if __name__ == "__main__":
    main()