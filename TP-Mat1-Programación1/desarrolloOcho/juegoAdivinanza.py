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