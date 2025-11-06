

def buscarPais(lista_paises):

    print("\n##  ¿Búsqueda parcial o exacta?  ##\n")
    print("\n1. Parcial\n2. Exacta")
    sub_opcion = input("Opción (1-2): ")
    
    if sub_opcion != "1" and sub_opcion != "2":
        print("Error: ha ingresado una opción incorrecta")
        
    else:
    
        busqueda = input("Ingrese el nombre del país: ")
        busqueda_normalizada = busqueda.strip().capitalize()
        
        encontrados = []
        
        for pais in lista_paises:
            nombre_pais = pais["nombre"].capitalize()
            
            if sub_opcion == "1":  
                if busqueda_normalizada in nombre_pais:
                    encontrados.append(pais)
            elif sub_opcion == "2":  
                if nombre_pais == busqueda_normalizada:
                    encontrados.append(pais)
        
        
        if encontrados:
            print(f"\nSe encontraron {len(encontrados)} país(es):")
            for pais in encontrados:
                print(f"- {pais['nombre']}")
        else:
            print("No se encontraron países")





