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

   