#Modulos para la segunda parte del proyecto de programación
import opciones_menu
import robusta_entrega
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
			
			if c == "," or c == ".":
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

def agregar_cuerpos(lista_cuerpos, Cuerpo):
	mas_cuerpos = True
	while mas_cuerpos:
		num_cuerpos = robusta_entrega.entrada_cuerpos()
		print("")
		
		for n in range(num_cuerpos):
			nombre = input("Introduce el nombre del cuerpo: ")
			masa = robusta_entrega.entrada_enteros("masa")
			px = robusta_entrega.entrada_enteros("posición x")
			py = robusta_entrega.entrada_enteros("posición y")
			imagen = input("Introduce la ruta de la imagen: ")
			fijo = robusta_entrega.entrada_sino()
			vx = robusta_entrega.entrada_enteros("velocidad x")
			vy = robusta_entrega.entrada_enteros("velocidad y")

			cuerpo_nuevo = Cuerpo(nombre, masa, px, py, imagen, fijo, vx, vy)
			lista_cuerpos.append(cuerpo_nuevo)
		
		respuesta = input("\n\n¿Deseas añadir más cuerpos? (si/no): ")

		respuesta= respuesta.lower()

		if respuesta == "no":
			mas_cuerpos = False

	return lista_cuerpos











