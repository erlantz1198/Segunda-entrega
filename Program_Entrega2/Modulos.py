# -*- coding: utf-8 -*-
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

	def imprimir_nombre(self):
		print(str(self.nombre))


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

			nombre = robusta_entrega.norepetirnombre(lista_cuerpos)

			masa = robusta_entrega.entrada_enteros("masa")
			px = robusta_entrega.entrada_enteros("posición x")
			py = robusta_entrega.entrada_enteros("posición y")
			imagen = input("Introduce la ruta de la imagen: ")
			fijo = robusta_entrega.entrada_sino()
			vx = robusta_entrega.entrada_enteros("velocidad x")
			vy = robusta_entrega.entrada_enteros("velocidad y")

			cuerpo_nuevo = Cuerpo(nombre, masa, px, py, imagen, fijo, vx, vy)
			lista_cuerpos.append(cuerpo_nuevo)

		entrada_valida = False

		while not entrada_valida:

			respuesta = input("\n\n¿Deseas añadir más cuerpos? (si/no): ")
			print("\n")
			respuesta= respuesta.lower()

			if respuesta == "no" or respuesta  == "si":

				if respuesta == "no":
					mas_cuerpos = False

			
				entrada_valida = True

			else:
				print("La respuesta introducida no es valida.")


	return lista_cuerpos


def eliminar_cuerpo(lista_cuerpos, Cuerpo):


	salir = False
	contador = 1

	print("\n")
	while not salir:

		for c in lista_cuerpos:

			try:
				print("\t", end="")
				print(contador, end="")
				print(". ", end="")

				c.imprimir_nombre()
				contador += 1

			except:
				pass
	
			
		print("\n\tQ/q - salir")
		print("--------------------------------------")
		respuesta = input(" Selecciona el cuerpo a eliminar[1-%d]: " %(len(lista_cuerpos)))
		print("--------------------------------------")


		try:
			respuesta = int(respuesta)

			if respuesta>=1 and respuesta<=len(lista_cuerpos):
				salir = True
				del lista_cuerpos[(respuesta-1)]
				print("\n\t# Cuerpo eliminado con exito. #")

			else:
				print("\n### ERROR ### Seleccione un cuerpo de la lista o introduzca \"Q\" para salir.\n")
				contador=1

		except ValueError:
			if respuesta == "q" or respuesta == "Q":
				salir = True

			else:
				print("\n### ERROR ### Seleccione un cuerpo de la lista o introduzca \"Q\" para salir.\n")
				contador=1



def seleccionar_modificacion(lista_cuerpos, Cuerpo):

	if lista_cuerpos == []:
		print("\n# ERROR # No hay ningun cuerpo cargado.")

	else:
		fin = False

		while not fin:
			salir = False
			contador = 1

			print("\n")
			while not salir:

				for c in lista_cuerpos:

					try:
						print("\t", end="")
						print(contador, end="")
						print(". ", end="")

						c.imprimir_nombre()
						contador += 1

					except:
						pass
			
					
				print("\n\tQ/q - salir")
				print("--------------------------------------")
				respuesta = input(" Selecciona el cuerpo a modificar[1-%d]: " %(len(lista_cuerpos)))
				print("--------------------------------------")


				try:
					respuesta = int(respuesta)

					if respuesta>=1 and respuesta<=len(lista_cuerpos):
						salir = True
						c = lista_cuerpos[(respuesta-1)]
						c = modificar(c)





						print("\n\t# Cuerpo modificado con exito #")
						print("--------------------------------------")


					else:
						print("\n### ERROR ### Seleccione un cuerpo de la lista o introduzca \"Q\" para salir.\n")
						contador=1

				except ValueError:
					if respuesta == "q" or respuesta == "Q":
						salir = True
						fin = True

					else:
						print("\n### ERROR ### Seleccione un cuerpo de la lista o introduzca \"Q\" para salir.\n")
						contador=1




def modificar(c):

	dato_valido = False
	while not dato_valido:

		c.imprimir()
		dato_viejo = input("Selecione el parametroa modificar:  ")
		dato_viejo = dato_viejo.lower()

		if dato_viejo == "nombre":
			dato_nuevo = input("Introduce el nuevo nombre:  ")
			c.nombre = dato_nuevo
			dato_valido = True

		elif dato_viejo == "masa":
			while not dato_valido:
				dato_nuevo = input("Introduce la nueva masa:  ")
				dato_valido = robusta_entrega.robusta_modificaciones_int(dato_nuevo)
				c.masa = dato_nuevo	

		elif dato_viejo == "posicion x" or dato_viejo == "posicionx":
			while not dato_valido:
				dato_nuevo = input("Introduce la nueva posicion en el eje x:  ")
				dato_valido = robusta_entrega.robusta_modificaciones_int(dato_nuevo)
				c.px = dato_nuevo

		elif dato_viejo == "posicion y" or dato_viejo == "posiciony":
			while not dato_valido:
				dato_nuevo = input("Introduce la nueva posicion en el eje y:  ")		
				dato_valido = robusta_entrega.robusta_modificaciones_int(dato_nuevo)
				c.py = dato_nuevo

		elif dato_viejo == "imagen":
				dato_nuevo = input("Introduce la ruta de nueva imagen:  ")
				c.imagen = dato_nuevo	
				dato_valido = True

		elif dato_viejo == "cuerpo fijo":
				dato_nuevo = input("Introduce el nuevo estado[si/no]:  ")
				c.nombre = dato_nuevo	
				dato_valido = True

		elif dato_viejo == "velocidad x" or dato_viejo == "velocidadx":
			while not dato_valido:
				dato_nuevo = input("Introduce la nueva velocidad en el eje x:  ")
				dato_valido = robusta_entrega.robusta_modificaciones_int(dato_nuevo)
				c.velocidad_x = dato_nuevo	


		elif dato_viejo == "velocida y" or dato_viejo == "velociday":
			while not dato_valido:
				dato_nuevo = input("Introduce la nueva velocidad en el eje y:  ")
				dato_valido = robusta_entrega.robusta_modificaciones_int(dato_nuevo)
				c.velocidad_y = dato_nuevo	

		else: 
			print("\n# ERROR # El parametro introducido no es correcto.\n ")


	return c


def guardar(lista_cuerpos):


	if lista_cuerpos == []:
		print("\n# ERROR # No hay ningun cuerpo cargado.")

	else:

		fichero = robusta_entrega.fichero_w()

		datos_salida = ""
		n = 0

		for e in lista_cuerpos:
		
			datos_salida = datos_salida + "Nombre: " + e.nombre +", Masa: " + str(e.masa) + ", x: " + str(e.px) + ", y: " + str(e.py) + ", imagen: " + str(e.imagen) + ", fijo: " + str(e.fijo) + ", vx: " + str(e.velocidad_x) + ", vy: " + str(e.velocidad_y) + ".\n"

		fichero.write(datos_salida)
		print("\n\t# Fichero guardado con exito #")
		fichero.close()









