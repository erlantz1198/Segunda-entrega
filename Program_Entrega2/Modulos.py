#Modulos para la segunda parte del proyecto de programación
import opciones_menu

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

	def imprimir(self):

		print("Nombre : %s , Masa: %s , Posición X: %s , Posición Y: %s , Imagen: %s , Cuerpo Fijo: %s , Velocidad X: %s , Velocidad Y: %s " %(self.nombre, self.masa, self.px, self.py, self.imagen, self.fijo, self.velocidad_x, self.velocidad_y))				

def leer(Cuerpo):
	
	fichero = robusta_fichero()
	lista_cuerpos = cargar_cuerpos(fichero, Cuerpo)
	return lista_cuerpos


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

def cargar_cuerpos(fichero,Cuerpo):

	lista_cuerpos = []
	palabra_actual = ""
	
	for linea in fichero:
		
		for c in linea:
			
			if c == ",":
				valor = palabra_actual
				palabra_actual = ""

				if etiqueta == "nombre" or etiqueta == "Nombre":
					nombre = valor
				if etiqueta == "masa" or etiqueta == "Masa":
					masa = valor
				if etiqueta == "x":
					px = valor
				if etiqueta == "y":
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
			
			
		cuerpo_actual = Cuerpo(nombre, masa, px, py, imagen, fijo, velocidad_x, velocidad_y)
		lista_cuerpos.append(cuerpo_actual)
		palabra_actual = ""
			
	return lista_cuerpos	

		