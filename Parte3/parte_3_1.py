"""
El siguiene código contiene un ejemplo de todo lo pasado
en la ultima capacitación

* comentarios (como este texto)
* print (mostrar datos por pantalla)
* lectura de input (teclado)
* declaración de variables
* tipos de datos
* operaciones aritmeticas entre variables
* if/else
* for

"""

""" asomao 3=> """

# otro asomao 3=> 

# declaración de variables
nombre = "wenseslao"
apellido = "weas pal lao"
edad = 23

# print 1
print("hola culiaos")

#print 2
saludo = "hola culiaos desde variable"
print(saludo)

# suma de strings
espacio = " "
nombreCompleto = nombre + espacio + apellido
print("el nombre completo es: " + nombreCompleto)

# solicitar datos por pantalla
nombre2 = input("ingresa tu nombre")
print("soy adivino, creo que tu nombre es: " + nombre2)

# solicitar NUMEROS por pantalla
peso = int(input("ingresa tu peso"))

# bloque de decision if
if peso > 65:
    print("wena waton tetos kulia jaja")
else:
    print("wena esperpento kuliao jaja")


for i in range(100):
    print("iwiwiwiwiwiwiwiwi")


# ciclo for
cantidad =  int(input("selecciona el numero de veces que quieres ser insultado"))

for contador in range(cantidad):
    print("xuapalo .l. " + nombre2)

# ciclo for con contador
print("ahora seras insultado contando del 0 al numero que pusiste")

for contador in range(cantidad):
    print( str(contador) + " xuapalo .l. " + nombre2)




