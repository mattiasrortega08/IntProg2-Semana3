total_segundos = int(input("Ingrese la cantidad total de segundos: "))

horas = total_segundos // 3600

segundos_restantes = total_segundos % 3600
minutos = segundos_restantes // 60

segundos = segundos_restantes % 60

print(f"{total_segundos} segundos equivalen a:")
print(f"{horas} horas, {minutos} minutos y {segundos} segundos.")