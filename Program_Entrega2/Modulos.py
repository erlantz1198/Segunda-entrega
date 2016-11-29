#Modulos para la segunda parte del proyecto de programación

class Cuerpo:
	def __init__(self, nom, mas, x , y, img, fijo, vx, vy):
		self.nombre = nom
		self.masa = mas
		self.px = x
		self.py = y
		self.imagen = img
		self.fijo = fijo
		self.velocidad_x = vx
		self.velocidad_y = vy


def leer(Cuerpo):
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

	lista_cuerpos = []
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
				if etiqueta == "vx":
					px = valor
				if etiqueta == "vy":
					py = valor
				if etiqueta == "imagen" or etiqueta == "Imagen":
					imagen = valor
				if etiqueta == "fijo" or etiqueta == "Fijo":
					fijo = valor
				if etiqueta == "vx":
					velocidad_x = valor
				if etiqueta == "vy":
					velocidad_y = valor

			elif c ==":":
				etiqueta = palabra_actual
				palabra_actual = ""

			elif c == " ":
				pass

			else:
				palabra_actual += c
			

		else:
			cuerpo_actual =Cuerpo(nombre, masa, px, py, imagen, fijo, velocidad_x, velocidad_y)
			lista_cuerpos.append(cuerpo_actual)
			
	return lista_cuerpos	