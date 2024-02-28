acumulador = 1

print("Hola, soy un acumulador :D y mi valor actual es:" + str(acumulador) + "\n")
print("Me puedo sumar a mi mismo una y otra vez, mira pesiona enter para ver \n")

input()

print("ahora me voy a sumar a mi mismo + 10, mira")

acumulador = acumulador + 10

print("mi nuevo valor es: " + str(acumulador) + "\n")

print("Probemos de nuevo, ahora me sumare a mi mismo + un numero que tu me des :D")
numUsuario = int(input("Ingresa un numero"))

acumulador = acumulador + numUsuario

print("Se entiende la idea? ahora voy a sumarme en un for que se repite 3 veces el numero 2")


for i in range(3):
    acumulador = acumulador + 2

print("Y mi nuevo valor es " + str(acumulador))


