import modulos
import opciones_menu

def main():

	print("WELCOME")

	finish = False
	while not finish:

		lista_opciones = opciones_menu.opciones_disponibles()

		opcion_elegida = opciones_menu.menu_opciones(lista_opciones)
		
		finish = modulos.opcion_final(opcion_elegida)
		



if __name__ == '__main__':
	main()