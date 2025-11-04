from Funciones.agregarPais import agregarPais
from Funciones.buscarPais import buscarPais
from Funciones.guardarArchivo import guardar_archivo
from Funciones.leerArchivo import leerArchivo
import Funciones.filtrado as filtrado
import Funciones.ordenamiento as ordenamiento
#Desarrollo de Menu con Python
import os
import platform
import sys


# Limpiar la consola
clear= "cls" if platform.system() == "Windows" else "clear"
os.system(clear)

# Imprime una bienvenida al usuario
print("Bienvenido al Menu de Opciones")
# Espera a que el usuario presione Enter para continuar
input("Presione Enter para continuar...")
# Limpia la consola nuevamente
os.system(clear)
lista_paises=leerArchivo()

while True:
    # Muestra el menu de opciones
    print("Menu de Opciones")
    print("1. Agregar países")
    print("2. Buscar un país")
    print("3. Filtrar países por:")
    print("4. ordenar países por:")
    print("5. Mostrar estadísticas")
    print("6. Salir")
    # Solicita al usuario que seleccione una opcion
    opcion =input("Seleccione una opcion (1-6): ")
    # Procesa la opcion seleccionada usando match-case
    os.system(clear)
    match opcion:
        # si la opcion es "1"
        case "1":
            agregarPais(lista_paises)
            guardar_archivo(lista_paises)
        # si la opcion es "2"
        case "2":
            buscarPais(lista_paises)
        #si la opcion es "3"
        case "3":
            filtrado.menu_filtrar_interactivo(lista_paises)
        # si la opcion es "4"
        case "4":
            ordenamiento.menu_ordenar_interactivo(lista_paises)
        # si la opcion es "5"
        case "5":
            # Imprime un mensaje indicando que se ha seleccionado la opción de mostrar estadísticas
            print("haz seleccionado mostrar estadísticas")
            # Solicita al usuario que elija el tipo de estadística a mostrar
            print("¿como desea ver las estadísticas?")
            # Muestra las opciones de estadísticas
            print("1. País con mayor y menor población\n2. Promedio de población\n3. Promedio de superficie\n4. Cantidad de países por continente")
            # Solicita al usuario que seleccione una opcion de estadística
            estadistica_opcion = input("Seleccione una opcion (1-4): ")
            # Procesa la opcion de estadística seleccionada
            match estadistica_opcion:
                case "1":
                    print("Mostrando país con mayor y menor población...")
                    # Aquí iría la lógica para mostrar el país con mayor y menor población
                case "2":
                    print("Calculando promedio de población...")
                    # Aquí iría la lógica para calcular el promedio de población
                case "3":
                    print("Calculando promedio de superficie...")
                    # Aquí iría la lógica para calcular el promedio de superficie
                case "4":
                    print("Contando cantidad de países por continente...")
                    # Aquí iría la lógica para contar la cantidad de países por continente
                case _:
                    print("Opcion invalida. Por favor seleccione una opcion valida.")
        # si la opcion es "6"
        case "6":
            # Imprime un mensaje indicando que se está saliendo del programa
            print("Saliendo del programa...")
            # Sale del bucle y termina el programa
            sys.exit()
        # si la opcion no es valida
        case _:
            # Imprime un mensaje indicando que la opción seleccionada no es válida
            print("Opcion invalida. Por favor seleccione una opcion valida.")   
