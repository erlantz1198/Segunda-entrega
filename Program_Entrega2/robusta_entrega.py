#entradas robustisimas

def entrada_cuerpos():
	salir = False
	while not salir:
		try:

			respuesta = int(input("¿Cuántos cuerpos quieres añadir?: "))
			salir = True

		except ValueError:

			print("Se esperaba un numero de cuerpos a añadir.")

	return respuesta


