import modulos
import opciones_menu

def main():

	print("WELCOME")

	lista_opciones = opciones_menu.opciones_disponibles()

	opcion_elegida = opciones_menu.menu_opciones(lista_opciones)

	if opcion_elegida == 1:
		dato = modulos.leer(modulos.Cuerpo)





if __name__ == '__main__':
	main()