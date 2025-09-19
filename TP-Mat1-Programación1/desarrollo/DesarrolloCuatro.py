# Programa: Tabla de verdad interactiva
from colorama import Fore, Style, init
from tabulate import tabulate

# Inicializar colorama
init(autoreset=True)
# Lista de operaciones disponibles
operaciones = {
    "AND": lambda a, b: a and b,
    "OR": lambda a, b: a or b,
    "XOR": lambda a, b: a ^ b,
    "NAND": lambda a, b: not (a and b),
    "NOR": lambda a, b: not (a or b),
    "XNOR": lambda a, b: not (a ^ b),
    "NOT A": lambda a, b: not a,
    "NOT B": lambda a, b: not b
}#Cada valor es una función lambda que recibe A y B y devuelve el resultado lógico.
# Muestra las opciones en color amarillo y el titulo en cyan
print(Fore.CYAN + "Operaciones disponibles:")
for op in operaciones:
    print(Fore.YELLOW + f"- {op}")

#Solicitar operación al usuario em color cyan 
#el .strip() elimina los espacios y otros caracteres como salto de linea en la respuesta
#el .upper() toma cualquier minuscula y lo convierte en mayuscula
opcion = input(Fore.CYAN + "Elige una operación lógica: ").strip().upper()

#Esto valida operación, si la opcion no esta en las operaciones imprira un mensaje en rojo
#sino, imprimira la tabla de verdad  
if opcion not in operaciones:
    print(Fore.RED + "Operación no válida.")
else:
    print(Fore.GREEN + f"\nTabla de verdad para: {opcion}\n")
    #Construye los datos para la tabla
    tabla = []
    for A in [False, True]:
        for B in [False, True]:
            resultado = operaciones[opcion](A, B)
            # Convertir a 0 y 1 con colores
            val_A = Fore.RED + "0" if not A else Fore.GREEN + "1"
            val_B = Fore.RED + "0" if not B else Fore.GREEN + "1"
            val_R = Fore.RED + "0" if not resultado else Fore.GREEN + "1"
            tabla.append([val_A, val_B, val_R])
    # Muestra la tabla con formato
    print(tabulate(tabla, headers=[Fore.CYAN + "A", Fore.CYAN + "B", Fore.CYAN + "Resultado"], tablefmt="fancy_grid"))