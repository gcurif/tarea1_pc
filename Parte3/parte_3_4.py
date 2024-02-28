def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def main():
    celsius = float(input("Ingresa la temperatura en grados Celsius: "))
    fahrenheit = celsius_a_fahrenheit(celsius)
    print(f"{celsius} grados Celsius son {fahrenheit} grados Fahrenheit.")

main()
