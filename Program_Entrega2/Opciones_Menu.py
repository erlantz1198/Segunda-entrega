# -*- coding: utf-8 -*-
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


def opcion_final(opcion_elegida, lista_cuerpos):

	salir_menu = False

	while not salir_menu:

		
		if opcion_elegida == 1:
			
<<<<<<< HEAD
			lista_cuerpos = modulos.leer(modulos.Cuerpo)
=======

			lista_cuerpos = modulos.leer(modulos.Cuerpo, lista_cuerpos)
>>>>>>> origin/master
			print("\n\t# Fichero cargado con éxito #")
			salir_menu = True
			return lista_cuerpos
			
			
		elif opcion_elegida == 2:
			error = False
			for a in lista_cuerpos:
				try:
					a.imprimir()
					error = True

				except:
					pass

			if not error:
				print("# Es necesario seleccionar un fichero o añadir un cuerpo antes. Selecciona la opción 1 para cargar un fichero o la opción 3 para añadir un cuerpo. #")
			salir_menu = True

			return lista_cuerpos

		elif opcion_elegida == 3:
			lista_cuerpos = modulos.agregar_cuerpos(lista_cuerpos, modulos.Cuerpo)
			salir_menu = True
			return lista_cuerpos

		elif opcion_elegida == 4:
			modulos.eliminar_cuerpo(lista_cuerpos, modulos.Cuerpo)
			salir_menu = True
			return lista_cuerpos

		elif opcion_elegida == 5:
			modulos.seleccionar_modificacion(lista_cuerpos, modulos.Cuerpo)
			salir_menu = True
			return lista_cuerpos

		elif opcion_elegida == 6:
			
			modulos.guardar(lista_cuerpos)
			salir_menu = True
			return lista_cuerpos

		elif opcion_elegida == "q" or opcion_elegida == "Q":
			print("\n\t# Hasta pronto #\n ")
			salir_menu = True
			return True
