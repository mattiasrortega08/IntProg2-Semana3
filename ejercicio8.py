cantidad_dolares = float(input("Ingrese la cantidad en dólares: "))

tasa_euros = 0.93  
tasa_libras = 0.76  
tasa_yenes = 146.20

cantidad_euros = cantidad_dolares * tasa_euros
cantidad_libras = cantidad_dolares * tasa_libras
cantidad_yenes = cantidad_dolares * tasa_yenes

print(f"Cantidad en dólares: {cantidad_dolares}")
print(f"Equivalente en euros: {cantidad_euros}")
print(f"Equivalente en libras: {cantidad_libras}")
print(f"Equivalente en yenes: {cantidad_yenes}")