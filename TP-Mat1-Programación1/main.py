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
    opciones ={
        "1": "Simulador de Puertas Lógicas",
        "2": "Conversor de Números",
        "3": "cuenta del 0 al 15 en diferentes sistemas numéricos",
        "4": "Tabla de Verdad Interactiva",
        "5": "Tabla de Verdad 1-bit (sum/rest/mul/div)",
        "6": "Juego de Adivinanza Binaria"
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
                numero_usuario= int(input("Ingrese un número decimal entero: "))
                resultado_binario = ""
                # Creamos la variable temp para poder hacer la conversión, sin perder el valor ingresado por el usuario
                temp = numero_usuario       
                #Dividimos secuencialmente por 2 hasta que no haya número para dividir.
                while temp>0:  
                    resto=temp%2
                    resultado_binario = str(resto) + resultado_binario
                    temp = temp//2
            print(f"Ingresaste el número : {numero_usuario}. Su equivalente binario es el: {resultado_binario}")            
                
            if opcion == "2":
                numero_usuario= input("Ingrese un número binario con 0s y 1s: ")
                es_binario=True
                #En este IF validamos si el usuario no ingresó nada, o ingresó un número no binario
                if numero_usuario == "":
                    es_binario = False
                else:
                    i = 0
                    while i < len(numero_usuario) and es_binario:
                        if numero_usuario[i] != '0' and numero_usuario[i] != '1':
                            es_binario = False
                        i += 1
                if not es_binario:
                    print("Error: Debes ingresar solo 0s y 1s.")
                    continue
                resultado_decimal=0
                longitud = len(numero_usuario)          
                #Acá vamos a convertir el binario a decimal, sabiendo la cantidad de digitos, y calculando las potencias para cada uno
                for i in range(longitud):
                    digito= int(numero_usuario[i])
                    potencia = longitud - 1 - i #Acá le restamos primero 1 y luego el índice , para q exista la potencia 0
                    resultado_decimal += digito * (2**potencia)
                print(f"Ingresaste el número : {numero_usuario}. Su equivalente decimal es el: {resultado_decimal}")
            console.input("\n[cyan]Presiona Enter para volver al menú…[/cyan]")

    # Opción 3: cuenta del 0 al 15 en diferentes sistemas numéricos
    elif eleccion == "3":
        os.system(clear_cmd)
        #Programa:Cuenta del 0 al 15 en diferentes sistemas numericos
        import time
        # Lista con los valores y símbolos del sistema romano
        valores_romanos = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
            (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
        ]
        for numero in range(16):
            # Representaciones en otros sistemas
            binario     = format(numero, '04b')
            octal       = format(numero, 'o')
            hexadecimal = format(numero, 'X')
            # Conversión a romano 
            n = numero
            resultado_romano = ""
            for valor, simbolo in valores_romanos:
                while n >= valor:
                    resultado_romano += simbolo
                    n -= valor
            if resultado_romano == "":
                resultado_romano = "0"  # No existe cero en números romanos
            # Simulación de LEDs: 🔴 para 1 y ⚫ para 0
            leds = ''.join('🔴' if bit == '1' else '⚫' for bit in binario)
            # Salida formateada
            print(f"{numero:2} -> {binario}  {leds} | Oct: {octal:>2} | Hex: {hexadecimal:>2} | Rom: {resultado_romano}")
            # Retardo para simular conteo
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
    elif eleccion == "6":
        os.system(clear_cmd)
        # Hola! Soy un juego de adivinanza binaria
        import random

        print("JUEGO DE ADIVINANZA")

        while True:
            print("\nOpciones disponibles:")
            print("1. Adivinanza Decimal (Te mostramos un número decimal y debes adivinar el binario)")
            print("2. Adivinanza Binaria (Te mostramos un número binario y debes adivinar el decimal)")
            print("3. Salir")
    

            opcion = input("Seleccione una opción (1-3): ")
    
            if opcion == "3":
                print("¡Hasta luego!")
                break
            if opcion == "1":
                num_decimal = random.randint(0, 15)    # Generamos un número decimal entre 0 y 15
        
                print(f"\n¿Cuál es la representación binaria del número decimal: {num_decimal}?")
                print("(Ingresa solo 0s y 1s, sin espacios)")
        
                respuesta = input("Tu respuesta: ")
                respuesta_valida = True
        
                                #En este IF validamos si el usuario no ingresó nada, o ingresó un número no binario
                if respuesta == "":
                    respuesta_valida = False
                else:
                    i = 0
                    while i < len(respuesta) and respuesta_valida:
                        if respuesta[i] != '0' and respuesta[i] != '1':
                            respuesta_valida = False
                        i += 1
        
                if not respuesta_valida:
                    print("Error: Debes ingresar solo 0s y 1s.")
                    continue
                respuesta_decimal = 0
                longitud = len(respuesta)   
                # Convertimos la respuesta del usuario a decimal para comparar con el decimal random
                for i in range(longitud):
                    digito = int(respuesta[i])
                    potencia = longitud - 1 - i
                    respuesta_decimal += digito * (2 ** potencia)
    
                temp = num_decimal
                binario_correcto = ""
        
                if temp == 0:                      # Convertimos el decimal correcto a binario para mostrar la respuesta
                    binario_correcto = "0"
                else:
                    while temp > 0:
                        resto = temp % 2
                        binario_correcto = str(resto) + binario_correcto
                        temp = temp // 2
        
                if respuesta_decimal == num_decimal:
                    print("¡Correcto!")
                else:
                    print(f"Incorrecto. La respuesta correcta era: {binario_correcto}")
    
            if opcion == "2":
        
                decimal_correcto = random.randint(0, 15) #Número decimal random entre 0 y 15
        
                # Convertimos el decimal random a binario 
                temp = decimal_correcto
                binario_str = ""
        
                if temp == 0:
                    binario_str = "0"
                else:
                    while temp > 0:
                        resto = temp % 2
                        binario_str = str(resto) + binario_str
                        temp = temp // 2
        
                print(f"\n¿Cuál es el valor decimal del número binario: {binario_str}?")
        
                # Obtenemos la respuesta del usuario y validamos el valor
                respuesta = input("Tu respuesta: ")
        
                if not respuesta.isdigit():
                    print("Error: Debes ingresar un número entero.")
                    continue
            
                respuesta_int = int(respuesta)
        
                if respuesta_int == decimal_correcto:
                    print("¡Correcto! ")
                else:
                    print(f"Incorrecto. La respuesta correcta era: {decimal_correcto}")
    
            else:
                continue
            console.input("\n[cyan]Presiona Enter para volver al menú…[/cyan]")
    else:
        console.print("[red]Esa no es una opción válida.[/]\n")
        console.input("\n[cyan]Presiona Enter para volver al menú…[/cyan]")
