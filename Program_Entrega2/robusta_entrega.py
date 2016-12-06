# -*- coding: utf-8 -*-
#Modulo de entradas robustas.

def entrada_cuerpos():
	salir = False
	
	while not salir:
		try:

			respuesta = int(input("¿Cuántos cuerpos quieres añadir?: "))
			salir = True

		except ValueError:

			print("Se esperaba un numero de cuerpos a añadir.")

	return respuesta



def entrada_enteros(unidad):
	salir = False
	while not salir:
		try:

			respuesta = int(input("Introduce la %s: "%unidad))
			salir = True

		except ValueError:

			print("Se esperaba un numero válido.")

	return respuesta

def entrada_sino():

	salir = False
	while not salir:
		
		respuesta = input("¿El cuerpo es fijo?: ")	
		respuesta = respuesta.lower()
		if respuesta == "si" or respuesta == "no":
			salir = True

		else:
			print("Se esperaba un 'sí' o un 'no'.")

	return respuesta

def robusta_fichero():

	dato_valido = False
	
	while not dato_valido:
		
		try:
			direccion = input("Introduce la dirección del fichero:\n")
			fichero = open(direccion) 
			dato_valido = True

		except FileNotFoundError:
			print("### ERROR ### La dirección introducida no es correcta.")
		
		except PermissionError:
			print("### ERROR ### No tienes permiso para abrir este fichero.")

	return fichero




def fichero_w():

	dato_valido = False
	
	while not dato_valido:
		
		try:
			direccion = input("Introduce la dirección o el destino del fichero:\n")
			fichero = open(direccion, "w") 
			dato_valido = True

		except FileNotFoundError:
			print("### ERROR ### La dirección introducida no es correcta.")
		
		except PermissionError:
			print("### ERROR ### No tienes permiso para abrir este fichero.")

	return fichero





