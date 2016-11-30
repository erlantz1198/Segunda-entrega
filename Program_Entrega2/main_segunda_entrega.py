import modulos
import opciones_menu

def main():

	print("\n\t##WELCOME##")
	finish = False
	accion = []
	while not finish:

		lista_opciones = opciones_menu.opciones_disponibles()

		opcion_elegida = opciones_menu.menu_opciones(lista_opciones)
		
		accion = opciones_menu.opcion_final(opcion_elegida, accion)
				
		if accion == True:

			finish = accion


if __name__ == '__main__':
	main()