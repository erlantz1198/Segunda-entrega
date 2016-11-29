#modulo de opciones de menu
def opciones_disponibles():
	opciones = []
	opciones.append("\n----------------------------\n   OPCIONES DISPONIBLES: \n----------------------------")
	opciones.append("\t1. LEER FICHERO")
	opciones.append("\t2. MOSTRAR")
	opciones.append("\t3. AÑADIR UN NUEVO CUERPO")
	opciones.append("\t4. ELIMINAR UN CUERPO")
	opciones.append("\t5. MODIFICAR LOS DATOS DE UN CUERPO")
	opciones.append("\t6. GUARDAR")

	return opciones



def menu_opciones(lista_opciones):
	salir = False
	while not salir:
	
		for e in lista_opciones:
			print(e)

		print("\n\tQ - salir")
		print("--------------------------------------")
		respuesta = input(" Selecciona una tarea a realizar[1-%d]: " %(len(lista_opciones)-1))
		print("--------------------------------------")

		try:
			respuesta = int(respuesta)

			if respuesta>=1 and (respuesta<=(len(lista_opciones)-1)):
				salir = True
			else:
				print("\n### ERROR ### Seleccione una opción de la lista o introduzca \"Q\" para sarlir.\n")

		except ValueError:
			if respuesta == "q" or respuesta == "Q":
				salir = True

			else:
				print("\n### ERROR ### Seleccione una opción de la lista o introduzca \"Q\" para sarlir.\n")

	return respuesta