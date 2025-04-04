precio_original = float(input("Ingrese el precio original del producto: "))

porcentaje_descuento = float(input("Ingrese el porcentaje de descuento aplicado: "))

descuento = (precio_original * porcentaje_descuento) / 100

precio_con_descuento = precio_original - descuento

porcentaje_iva = float(input("Ingrese el porcentaje de IVA: "))

iva = (precio_con_descuento * porcentaje_iva) / 100

precio_final = precio_con_descuento + iva

print(f"Precio original: {precio_original}")
print(f"Descuento aplicado: {descuento}")
print(f"Precio con descuento: {precio_con_descuento}")
print(f"IVA calculado: {iva}")
print(f"Precio final: {precio_final}")