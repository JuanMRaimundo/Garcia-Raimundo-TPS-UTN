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

   