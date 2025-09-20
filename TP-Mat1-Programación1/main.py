import os
import platform
CLEAR = "cls" if platform.system() == "Windows" else "clear"
os.system(CLEAR)
print("1- Simulador de Puertas Lógicas\n2- Conversor de Números\n3- Cuenta del 0 al 15 en diferentes sistemas numéricos")
decision=int(input("Que actividad deseas ver: "))
CLEAR = "cls" if platform.system() == "Windows" else "clear"
os.system(CLEAR)
if decision==1:
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
            valor=input("Usted ingresó a la compuerta NOT. Por favor, ingrese el valor binario (1 o 0): ")
            while valor not in ['0', '1']:
                print("Numero binario inválido. Debe ingresar un 1 o 0: ")
                valor = input("Ingrese un valor binario (0 o 1): ")   
            a=int(valor)
            resultado = 0 
            if a == 1:
                resultado=0
            else:
                resultado=1
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
elif decision==2:
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
            numero= int(input("Ingrese un número decimal entero: "))
        if numero == 0:
            resultado_binario = 0
        else:
            resultado_binario = ""
            print("resultado: ", resultado_binario)
            temp = numero
            while temp>0:
                resto=temp%2
                resultado_binario = str(resto) + resultado_binario
                temp = temp//2
        print(f"Ingresaste el número : {numero}. Su equivalente binario es el: {resultado_binario}")
elif decision==3:
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
elif desicion==4:

else:
    print("esa no es una opcion valida")