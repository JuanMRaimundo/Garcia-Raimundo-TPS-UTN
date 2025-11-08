
def buscarPais(lista_paises):

    ##  Le damos al usuario dos opciones para búsqueda
        while True:

            print("\n##  ¿Búsqueda parcial o exacta?  ##\n")
            print("\n1. Parcial\n2. Exacta")
            sub_opcion = input("Opción (1-2): ").strip()
            
            #Validación si no ingresa una opción correcta

            if sub_opcion == "1" or sub_opcion == "2":
                break
            else:
                print("\nError: Opción incorrecta. Por favor, ingrese 1 o 2.\n")
    
        busqueda = input("Ingrese el nombre del país: ")

        ## Acá normalizamos la intrada del usuario para evitar errores en las comparaciones
        busqueda_normalizada = busqueda.strip().lower()
        
        encontrados = []
        
        for pais in lista_paises:
            nombre_pais = pais["nombre"].lower()
            
            if sub_opcion == "1":  
                ## Acá comparamos con un "in", donde se incluyen todos los que tengas los caracteres ingresados
                if busqueda_normalizada in nombre_pais:
                    encontrados.append(pais)

            elif sub_opcion == "2":  
                ## Acá lo comparamos con un "==" para la búsqueda exacta    
                if nombre_pais == busqueda_normalizada:
                    encontrados.append(pais)
        
        ## Acá definimos la salida según la opción ingresada
        if encontrados:
            print(f"\nSe encontraron {len(encontrados)} país(es):")
            for pais in encontrados:
                ## Volvemos a capitalizar el nombre para que aparezca en Mayúsculas
                print(f"- {pais['nombre']}")
        else:
            print("No se encontraron países")





