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