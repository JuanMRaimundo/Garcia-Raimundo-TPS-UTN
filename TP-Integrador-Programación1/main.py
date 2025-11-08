# main.py
# Archivo principal que utiliza las funciones del TP Integrador de Programación 1

#librerías y módulos importados
# funciones propias
from Funciones.agregarPais import agregarPais
from Funciones.buscarPais import buscarPais
from Funciones.estadisticas import estadisticas
from Funciones.guardarArchivo import guardar_archivo
from Funciones.leerArchivo import leerArchivo
import Funciones.estadisticas as Estadisticas
import Funciones.filtrado as filtrado
import Funciones.ordenamiento as ordenamiento
import Funciones.actualizarDatos as actualizarDatos
# otras librerías estándar
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
    print("2. Actualizar un país")
    print("3. Buscar un país")
    print("4. Filtrar países por:")
    print("5. ordenar países por:")
    print("6. Mostrar estadísticas")
    print("7. Salir")
    # Solicita al usuario que seleccione una opcion
    opcion =input("Seleccione una opcion (1-7): ")
    # Procesa la opcion seleccionada usando match-case
    os.system(clear)
    match opcion:
        # si la opcion es "1"
        case "1":
            agregarPais(lista_paises)
            guardar_archivo(lista_paises)
        # si la opcion es "2"
        case "2":
            actualizarDatos.menu_actualizar_pais(lista_paises)
            guardar_archivo(lista_paises)
        #si la opcion es "3"
        case "3":
            buscarPais(lista_paises)
        #si la opcion es "4"
        case "4":
            filtrado.menu_filtrar_interactivo(lista_paises)
        # si la opcion es "5"
        case "5":
            ordenamiento.menu_ordenar_interactivo(lista_paises)
        # si la opcion es "6"
        case "6":
            Estadisticas.estadisticas(lista_paises)
        # si la opcion es "7"
        case "7":
            # Imprime un mensaje indicando que se está saliendo del programa
            print("Saliendo del programa...")
            # Sale del bucle y termina el programa
            sys.exit()
        # si la opcion no es valida
        case _:
            # Imprime un mensaje indicando que la opción seleccionada no es válida
            print("Opcion invalida. Por favor seleccione una opcion valida.")   
