# -*- coding: utf-8 -*-
# =====================================================================
# EcoAudit CLI - Módulo Principal
# Autores: [Miguel Ángel Torres] & [Cristina Mateos] & [David Pavía]
# =====================================================================

def menu():
    while True:
        print("\n=========================================")
        print(" 🌿 ECOAUDIT CLI - MENÚ PRINCIPAL 🌿 ")
        print("=========================================")
        print("1. Realizar nueva auditoría")
        print("2. Consultar histórico")
        print("3. Salir")

        entrada = input("\nSeleccione una opción (1-3): ").strip()

        try:
            opcion = int(entrada)
        except ValueError:
            print("⚠️ Error: Debe introducir un número entero.")
            continue

        if opcion == 1:
            print("\n[OPCIÓN 1] Iniciando proceso de auditoría...")
            proceso = input("Nombre del proceso o dispositivo: ").strip()
            potencia = float(input("Potencia del dispositivo en W: ").strip())
            horas = float(input("Horas de uso estimadas: ").strip())
            iteraciones = int(input("Ingrese el número de iteraciones para la auditoría: ").strip())

            if iteraciones <= 0:
                print("Error: El número de iteraciones debe ser un entero positivo.")
                continue

            consumo = potencia * horas
            huella = (consumo / 1000) * 0.23

            with open("auditorias.csv", mode="a", encoding="utf-8") as archivo:
                archivo.write(f"{proceso},{potencia},{horas},{iteraciones},{consumo:.2f},{huella:.4f}\n")
                print("💾 Registro guardado con éxito en 'auditorias.csv'.")

        elif opcion == 2:
            print("\n[OPCIÓN 2] Consultando registros históricos...")
            try:
                with open("auditorias.csv", encoding="utf-8") as archivo:
                    print("\n================ HISTORIAL DE AUDITORÍAS ================")
                    print(archivo.read())
            except FileNotFoundError:
                print("ℹ️ Aún no existen registros. Realiza una auditoría primero.")

        elif opcion == 3:
            print("\nSaliendo de EcoAudit CLI. ¡Hasta pronto!")
            break

        else:
            print("⚠️ Opción no válida. Elija un número entre 1 y 3.")


if __name__ == "__main__":
    menu()