duracion_pelicula = int(input("Ingrese la duración de la película en minutos: "))

duracion_comerciales_previos = int(input("Ingrese la duración de los comerciales previos (en minutos): "))

cantidad_pausas = int(input("Ingrese la cantidad de pausas comerciales durante la película: "))

duracion_pausa = int(input("Ingrese la duración de cada pausa comercial (en minutos): "))

total_comerciales_durante_pelicula = cantidad_pausas * duracion_pausa

tiempo_total = duracion_pelicula + duracion_comerciales_previos + total_comerciales_durante_pelicula

print(f"Duración de la película: {duracion_pelicula} minutos")
print(f"Duración de los comerciales previos: {duracion_comerciales_previos} minutos")
print(f"Total de comerciales durante la película: {total_comerciales_durante_pelicula} minutos")
print(f"Tiempo total de la película con comerciales: {tiempo_total} minutos")