#Modulos para la segunda parte del proyecto de programación


def Opciones_Disponibles():
	opciones = []
	opciones.append("\n----------------------------\n   OPCIONES DISPONIBLES: \n----------------------------")
	opciones.append("\t1. LEER FICHERO")
	opciones.append("\t2. MOSTRAR")
	opciones.append("\t3. AÑADIR UN NUEVO CUERPO")
	opciones.append("\t4. ELIMINAR UN CUERPO")
	opciones.append("\t5. MODIFICAR LOS DATOS DE UN CUERPO")
	opciones.append("\t6. GUARDAR")

	return opciones



def Menu_Opciones(lista_opciones):
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

		except:
			if respuesta == "q" or respuesta == "Q":
				salir = True

			else:
				print("\n### ERROR ### Seleccione una opción de la lista o introduzca \"Q\" para sarlir.\n")

	return respuesta


def Leer():
	dato_valido = False
	while not dato_valido:
		try:
			direccion = input("Introduce la dirección del fichero:\n")
			fichero = open(direccion)
			dato_valido = True

		except ValueError:
			print("### ERROR ### La dirección introducida no es correcta.")
			
	Lista_cuerpos = []
	palabra_actual = ""
	for c in fichero:
		if c != "\n":
			if c == ",":
				valor = palabra_actual
				palabra_actual = ""
				if etiqueta == "nombre" or etiqueta == "Nombre":
					nombre = valor
				if etiqueta== "masa" or etiqueta == "Masa":
					masa = valor
				if etiqueta== "Px":
					Px = valor
				if etiqueta== "Py":
					Py = valor
				if etiqueta== "imagen" or etiqueta == "Imagen":
					imagen = valor
				if etiqueta== "fjo" or etiqueta == "Fijo":
					fijo = valor
				if etiqueta== "Vx":
					velocidad_X = valor
				if etiqueta== "Vy":
					velocidad_Y = valor

			elif c ==":":
				etiqueta = palabra_actual
				palabra_actual = ""s

			elif c == " ":
				pass

			else:
				palabra_actual += c
			

		else:
			cuerpo_actual = cuerpo(nombre, masa, Px, Py, imagen, fijo, velocidad_X, velocidad_Y)
			Lista_cuerpos.append(cuerpo_actual)

			

class Cuerpo:
	def __init__(self, nom, mas, x , y, img, fijo, vx, vy):
		self. nombre = nom
		self.masa = masa
		self.Px = x
		self.Py = y
		self.imagen = img
		self.fijo = fijo
		self.velocidad_X = vx
		self.velocidad_Y = vy
