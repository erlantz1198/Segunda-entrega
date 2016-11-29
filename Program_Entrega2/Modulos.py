#Modulos para la segunda parte del proyecto de programación


class Cuerpo:
	def __init__(self, nom, mas, x , y, img, fijo, vx, vy):
		self. nombre = nom
		self.masa = mas
		self.Px = x
		self.Py = y
		self.imagen = img
		self.fijo = fijo
		self.velocidad_X = vx
		self.velocidad_Y = vy


def Leer(Cuerpo):
	dato_valido = False
	while not dato_valido:
		
		try:
			direccion = input("Introduce la dirección del fichero:\n")
			
			dato_valido = True

		except FileNotFoundError:
			print("### ERROR ### La dirección introducida no es correcta.")
		
		except PermissionError:
			print("### ERROR ### No tienes permiso para abrir este fichero.")

	fichero = open(direccion)
	Lista_cuerpos = []
	palabra_actual = ""
	for c in fichero:
		if c != "\n":
			if c == ",":
				valor = palabra_actual
				palabra_actual = ""
				if etiqueta == "nombre" or etiqueta == "Nombre":
					nombre = valor
				if etiqueta == "masa" or etiqueta == "Masa":
					masa = valor
				if etiqueta == "Px":
					Px = valor
				if etiqueta == "Py":
					Py = valor
				if etiqueta == "imagen" or etiqueta == "Imagen":
					imagen = valor
				if etiqueta == "fijo" or etiqueta == "Fijo":
					fijo = valor
				if etiqueta == "Vx":
					velocidad_X = valor
				if etiqueta == "Vy":
					velocidad_Y = valor

			elif c ==":":
				etiqueta = palabra_actual
				palabra_actual = ""

			elif c == " ":
				pass

			else:
				palabra_actual += c
			

		else:
			cuerpo_actual =Cuerpo(nombre, masa, Px, Py, imagen, fijo, velocidad_X, velocidad_Y)
			Lista_cuerpos.append(cuerpo_actual)
			
	return Lista_cuerpos	


