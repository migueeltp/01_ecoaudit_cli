pareja_autora=input("Dime el nombre de la pareja: ").strip()
dispositivo=input("Dime el nombre del dispositivo: ").strip()
potencia=input("Dime la potencia del dispositivo en W: ").strip()
potencia_w=float(potencia)
uso_diario=potencia_w*24
print(f"El dispositivo {dispositivo} de la pareja {pareja_autora} consume {uso_diario} W al día.")