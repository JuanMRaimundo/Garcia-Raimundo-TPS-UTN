import os
import platform
import sys
from rich import box
from rich.console import Console
from rich.table import Table

console = Console()
clear_cmd = "cls" if platform.system() == "Windows" else "clear"

while True:
    # Limpia pantalla y muestra menú
    os.system(clear_cmd)
    opciones = {
        "1": "Simulador de Puertas Lógicas",
        "2": "Conversor de Números",
        "3": "cuenta del 0 al 15 en diferentes sistemas numéricos",
        "4": "Tabla de Verdad Interactiva",
        "5": "Tabla de Verdad 1-bit (sum/rest/mul/div)"
    }
    menu = Table(
        title="MENÚ PRINCIPAL",
        title_style="bold cyan",
        box=box.SQUARE,
        border_style="cyan"
    )
    menu.add_column("Opción", style="yellow", justify="center", no_wrap=True)
    menu.add_column("Descripción", style="green")
    for clave, desc in opciones.items():
        menu.add_row(clave, desc)
    menu.add_row("0", "Salir", style="red")
    console.print(menu)

    eleccion = console.input("[cyan]¿Qué actividad deseas ver?[/cyan] [yellow]> [/yellow]").strip()

    # Salir
    if eleccion == "0":
        os.system(clear_cmd)
        console.print("[bold green]👋 ¡Hasta luego![/]\n")
        sys.exit()

    # Opción 1: simulador de puertas lógicas (código original íntegro)
    elif eleccion == "1":
        os.system(clear_cmd)
        #Hola! Este es un simulador de Puertas Lógicas
        print("SIMULADOR DE PUERTAS LÓGICAS")
        while True:  
            print("\nOpciones disponibles:")
            print("1. AND    2. OR    3. NOT")
            print("4. SALIR") 
            opcion = input("Seleccione una opción (1-4): ")
            #Salimos del while y se corta el programa
            if opcion == "4":
                print("Nos vemos pronto, hasta luego!")
                break
            if opcion == "3":
                valor = input("Usted ingresó a la compuerta NOT. Por favor, ingrese el valor binario (1 o 0): ")
                while valor not in ['0', '1']:
                    print("Numero binario inválido. Debe ingresar un 1 o 0: ")
                    valor = input("Ingrese un valor binario (0 o 1): ")
                a = int(valor)
                resultado = 0 
                if a == 1:
                    resultado = 0
                else:
                    resultado = 1
                print(f"COMPUERTA NOT({a}) = {resultado}")    
            elif opcion in ["1","2"]:
                valor1 = input("Ingrese el primer valor binario (0 o 1): ")
                while valor1 not in ['0', '1']:
                    print("Error: Debe ingresar 0 o 1.")
                    valor1 = input("Ingrese el primer valor binario (0 o 1): ")
                valor2 = input("Ingrese el segundo valor binario (0 o 1): ")
                while valor2 not in ['0', '1']:
                    print("Error: Debe ingresar 0 o 1.")
                    valor2 = input("Ingrese el segundo valor binario (0 o 1): ")
                a = int(valor1)
                b = int(valor2)          
                if opcion == "1":  # COMPUERTA AND
                    if a == 1 and b == 1:
                        resultado = 1
                    else:
                        resultado = 0
                    print(f"COMPUERTA AND: ({a}), ({b}) = {resultado}")  
                if opcion == "2":  # COMPUERTA OR
                    if a == 0 and b == 0:
                        resultado = 0
                    else:
                        resultado = 1
                    print(f"COMPUERTA OR: ({a}), ({b}) = {resultado}")
        console.input("\n[cyan]Presiona Enter para volver al menú…[/cyan]")

    # Opción 2: conversor de números
    elif eleccion == "2":
        os.system(clear_cmd)
        #Hola! Este es un conversor de números decimales
        print("CONVERSOR DE NÚMEROS")
        while True:
            print("\nOpciones disponibles:")
            print("1. Decimal a Binario")
            print("2. Binario a Decimal")
            print("3. Salir")
            opcion = input("Seleccione una opción (1-3): ")
            if opcion == "3":
                print("¡Hasta luego!")
                break
            if opcion == "1":
                numero = int(input("Ingrese un número decimal entero: "))
            if numero == 0:
                resultado_binario = 0
            else:
                resultado_binario = ""
                print("resultado: ", resultado_binario)
                temp = numero
                while temp > 0:
                    resto = temp % 2
                    resultado_binario = str(resto) + resultado_binario
                    temp = temp // 2
            print(f"Ingresaste el número : {numero}. Su equivalente binario es el: {resultado_binario}")
        console.input("\n[cyan]Presiona Enter para volver al menú…[/cyan]")

    # Opción 3: cuenta del 0 al 15 en diferentes sistemas numéricos
    elif eleccion == "3":
        os.system(clear_cmd)
        #Programa:Cuenta del 0 al 15 en diferentes sistemas numericos
        import time  # Para usar sleep
        # Función para convertir a números romanos (hasta 3999)
        def a_romano(numero):
            #Lista con los valores de numeros en romano
            valores = [
                (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
                (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
                (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
            ]
            #variable para la conversion de numero a simbolo romano
            resultado = ""
            n = numero
            for valor, simbolo in valores:
                #Mientras que n sea igual o mayor que valor a el resultado se le suma un sinbolo y a n se le resta el valor
                while n >= valor:
                    resultado += simbolo
                    n -= valor
            #el cero no cambia por que no existe el cero en los numeros romanos
            return resultado if resultado else "0"  # Para el caso de 0
        # Cuenta del 0 al 15
        for numero in range(16):
            # Representaciones en distintos sistemas
            binario = format(numero, '04b')   # Binario con 4 bits
            octal = format(numero, 'o')       # Octal
            hexadecimal = format(numero, 'X') # Hexadecimal en mayúsculas
            romano = a_romano(numero)              # Romano
            #Esto crea la ilusion de led encendidos y apagados, esto muestran de manera visual los encendidos y apagados del codigo 
            #🔴 para 1 y  ⚫ para 0
            leds = ''.join('🔴' if bit == '1' else '⚫' for bit in binario)
            #Muestra número y su representación binaria, octal, hexadecimal y romano con sus leds encendidos y apagados
            print(f"{numero:2} -> {binario}  {leds} | Oct: {octal:>2} | Hex: {hexadecimal:>2} | Rom: {romano}")
            # se produce un retardo de 0.5 segundos para simular el conteo
            time.sleep(0.5)
        console.input("\n[cyan]Presiona Enter para volver al menú…[/cyan]")

    # Opción 4: Tabla de verdad interactiva

    elif eleccion == "4":
        # Programa: Tabla de verdad interactiva
        from colorama import Fore, init
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
        } #Cada valor es una función lambda que recibe A y B y devuelve el resultado lógico.
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
        console.input("\n[cyan]Presiona Enter para volver al menú…[/cyan]")

    # Opción 5: tabla de verdad 1-bit operaciones
    elif eleccion == "5":
        os.system(clear_cmd)
        #--- Bloque de tabla ---
        print("=== Tabla de verdad de la suma, resta, division y multiplicacion de 1 bit ===")
        print(" A | B | Suma | Carry | Resta | Borrow | Mult | DivQ | DivR")
        print("---+---+------+------+-------+--------+------+------+------")
        # Recorre todas las combinaciones posibles de A y B (0 y 1)
        for A in [0, 1]:
            for B in [0, 1]:
                suma   = A ^ B
                carry  = A & B
                resta  = A ^ B
                borrow = int((not A) and B)
                mult   = A * B
                if B == 0:
                    divq = "NaN"
                    divr = "NaN"
                else:
                    divq = A // B
                    divr = A % B
                print(f" {A} | {B} |  {suma}   |   {carry}   |   {resta}   |   {borrow}    |  {mult}   |  {divq}   |  {divr}")
        print("\n=== Modo interactivo ===")
        print("Ingresa solo 0 o 1 para A y B.")
        while True:
            #el usuario ingresa el valor de A
            A_str=input("\nIngresa A (0 o 1): ").strip()
            #si A_str no es 0 o 1 imprime mensaje de error y vuelve a pedir el numero
            if A_str not in ("0", "1"):
                print("  Entrada inválida. Debes ingresar 0 o 1.")
                continue
            #si la entreda es valida convierte A_str a entero y lo asigna a A
            A = int(A_str)
            #el usuario ingresa el valor de B
            B_str = input("Ingresa B (0 o 1): ").strip()
            #si B_str no es 0 o 1 imprime mensaje de error y vuelve a pedir el numero
            if B_str not in ("0", "1"):
                print("  Entrada inválida. Debes ingresar 0 o 1.")
                continue
            #si la entreda es valida convierte B_str a entero y lo asigna a B
            B = int(B_str)
            #se le presentan al usuario las opciones de operaciones que puede realizar,
            #eliminamos espacios y convertimos mayusculas a minusculas por si acaso
            op = input("Elige operación: suma (s), resta (r), mult (m) o div (d): ").strip().lower()
            #si la operacion no es valida imprime mensaje de error y vuelve a pedir la operacion
            if op not in ("s", "r", "m", "d"):
                print("  Operación inválida. Usa 's', 'r', 'm' o 'd'.")
                continue
            #Calcula todas las operaciones
            suma   = A ^ B
            carry  = A & B
            resta  = A ^ B
            borrow = int((not A) and B)
            mult   = A * B
            #Maneja división por cero
            if B == 0:
                divq = "NaN"
                divr = "NaN"
            #si B no es 0 realiza la division
            else:
                divq = A // B
                divr = A % B
            #Muestra el resultado de la operacion seleccionada
            #si la operacion es suma, muestra el resultado de la suma y el carry
            if op == "s":
                print(f"  Suma   → bit: {suma}, carry: {carry}")
            #si la operacion es resta, muestra el resultado de la resta y el borrow
            elif op == "r":
                print(f"  Resta  → bit: {resta}, borrow: {borrow}")
            #si la operacion es multiplicacion, muestra el resultado de la multiplicacion
            elif op == "m":
                print(f"  Mult   → resultado: {mult}")
            #si la operacion es division, muestra el cociente y el resto
            else:
                if divq is None:
                    print("  División indefinida (división por cero)")
                else:
                    print(f"  DivQ   → cociente: {divq}")
                    print(f"  DivR   → resto:     {divr}")
            otra = input("  ¿Otra operación? (s/n): ").strip().lower()
            if otra != "s":
                print("  Fin del simulador.")
                break
        console.input("\n[cyan]Presiona Enter para volver al menú…[/cyan]")
    else:
        console.print("[red]Esa no es una opción válida.[/]\n")
        console.input("\n[cyan]Presiona Enter para volver al menú…[/cyan]")
