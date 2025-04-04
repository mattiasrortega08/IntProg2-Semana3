salario_bruto = float(input("Ingrese el salario bruto del empleado: "))

impuesto_renta = salario_bruto * 0.10  # 10% como impuesto sobre la renta
seguro_social = salario_bruto * 0.05  # 5% como seguro social
fondo_pensiones = salario_bruto * 0.03  # 3% como fondo de pensiones

descuentos_totales = impuesto_renta + seguro_social + fondo_pensiones

salario_neto = salario_bruto - descuentos_totales

print(f"El salario bruto es: {salario_bruto}")
print(f"Los descuentos totales son: {descuentos_totales}")
print(f"El salario neto es: {salario_neto}")