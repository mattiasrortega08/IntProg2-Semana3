peso = float(input("Ingrese su peso en kilogramos: "))

altura = float(input("Ingrese su altura en metros: "))

imc = peso / (altura ** 2)

imc = round(imc, 2)

print(f"Peso ingresado: {peso} kg")
print(f"Altura ingresada: {altura} m")
print(f"Su índice de masa corporal (IMC) es: {imc}")

if imc < 18.5:
    clasificacion = "Bajo peso"
elif 18.5 <= imc < 24.9:
    clasificacion = "Peso normal"
elif 25 <= imc < 29.9:
    clasificacion = "Sobrepeso"
else:
    clasificacion = "Obesidad"

print(f"Clasificación del IMC: {clasificacion}")