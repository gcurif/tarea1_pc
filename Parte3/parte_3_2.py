# Solicita al usuario ingresar su edad
edad = int(input("Ingresa tu edad: "))

# Verifica el rango de edad y muestra un mensaje correspondiente
if edad < 18:
    print("Eris ilegal no podis tomar.")
elif 18 <= edad < 65: # esta wena no se puede hacer en java jaja, si no que hay qe hacer esta otra wea 18 <= edad && edad < 65
    print("Eris wrande.")
else:
    print("Eres un octogenario, te vay a desarmar.")
