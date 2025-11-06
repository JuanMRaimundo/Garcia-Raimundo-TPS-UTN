
from Funciones.agregarPais import agregarPais
from Funciones.buscarPais import buscarPais
from Funciones.estadisticas import estadisticas
from Funciones.guardarArchivo import guardar_archivo
from Funciones.leerArchivo import leerArchivo
import Funciones.filtrado as filtrado
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
        case "2":
            buscarPais(lista_paises)
        case "3":
            filtrado.menu_filtrar_interactivo(lista_paises)
        # si la opcion es "3"
        case "4":
            #imprime un mensaje de confirmación
            print("haz seleccionado ordenar países")
            #• Ordenar países por: Nombre, Población, Superficie (Ascendente y Descendente).
            print("¿Cómo desea ordenar los países?")
            # Muestra las opciones de ordenamiento
            print("1. Nombre\n2. Población\n3. Superficie Ascendente\n4. Superficie Descendente")
            # Solicita al usuario que seleccione una opcion de ordenamiento
            filtro_opcion = input("Seleccione una opcion (1-4): ")
            # Procesa la opcion de ordenamiento seleccionada
            match filtro_opcion:
                case "1":
                    print("Ordenando países por Nombre...")
                    # Aquí iría la lógica para ordenar países por nombre
                case "2":
                    print("Ordenando países por Población...")
                    # Aquí iría la lógica para ordenar países por población
                case "3":
                    print("Ordenando países por Superficie Ascendente...")
                    # Aquí iría la lógica para ordenar países por superficie ascendente
                case "4":
                    print("Ordenando países por Superficie Descendente...")
                    # Aquí iría la lógica para ordenar países por superficie descendente
                case _:
                    print("Opcion invalida. Por favor seleccione una opcion valida.")
        # si la opcion es "4"
        case "5":
           estadisticas(lista_paises)
        case "6":
            # Imprime un mensaje indicando que se está saliendo del programa
            print("Saliendo del programa...")
            # Sale del bucle y termina el programa
            sys.exit()
        # si la opcion no es valida
        case _:
            # Imprime un mensaje indicando que la opción seleccionada no es válida
            print("Opcion invalida. Por favor seleccione una opcion valida.")   
