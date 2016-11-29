import Modulos
import Opciones_Menu

def main():

	print("WELCOME")

	lista_opciones = Opciones_Menu.Opciones_Disponibles()

	opcion_elegida = Opciones_Menu.Menu_Opciones(lista_opciones)

	if opcion_elegida == 1:
		dato = Modulos.Leer(Modulos.Cuerpo())





if __name__ == '__main__':
	main()