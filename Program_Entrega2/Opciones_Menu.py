#modulo de opciones de menu
import modulos

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

		print("\n\tQ/q - salir")
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


def opcion_final(opcion_elegida, fichero_cargado):

	salir_menu = False

	
	while not salir_menu:

		if not fichero_cargado:
			
			if opcion_elegida == 1:
				
				lista_cuerpos = modulos.leer(modulos.Cuerpo)
				
				for a in lista_cuerpos:
					a.imprimir()

				salir_menu = True

		else:

			if opcion_elegida == 2:
				
				for a in lista_cuerpos:
				
					if fichero_cargado:
						a.imprimir()
				else:
					print("Selecciona antes un fichero")
				salir_menu = True

			elif opcion_elegida == 3:
				salir_menu = True
			elif opcion_elegida == 4:
				salir_menu = True
			elif opcion_elegida == 5:
				salir_menu = True
			elif opcion_elegida == 6:
				
				salir_menu = True
				
			elif opcion_elegida == "q" or opcion_elegida == "Q":

				salir_menu = True
				return True
