def calcular_impuesto(salario, tasa):
    return salario * (tasa / 100)

def main():
    salario = float(input("Ingresa tu salario anual: "))
    tasa_impuesto = float(input("Ingresa la tasa de impuesto (%): "))
    impuesto = calcular_impuesto(salario, tasa_impuesto)
    print(f"Debes pagar ${impuesto} en impuestos.")

main()
