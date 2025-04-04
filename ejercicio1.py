temperatura_fahrenheit = float(input("Ingrese la temperatura en grados Fahrenheit: "))

temperatura_celsius = (temperatura_fahrenheit - 32) * 5 / 9

temperatura_kelvin = temperatura_celsius + 273.15

print(f"La temperatura en Celsius es: {temperatura_celsius:.2f} °C")
print(f"La temperatura en Kelvin es: {temperatura_kelvin:.2f} K")