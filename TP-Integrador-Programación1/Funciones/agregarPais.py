

from Validaciones.validaciones import pedir_numero, pedir_texto


def agregarPais(lista_paises):

    print("\n ## A continuación podrá agregar países: ##\n")

    cantidad_paises=pedir_numero("Ingrese la cantidad de países que desea agregar: ")


    ## Primera iteración para agregar la cantidad de países que indique el usuario
    for i in range(cantidad_paises):
        print(f"\n--- País {i+1} ---")
        while True:
            nombre=pedir_texto("\nIngrese un país: ").capitalize()
            
            print("pais ingresado", nombre)
            
            ## Validación por si el país ingresado ya está en el listado
            for p in lista_paises:
                if p["nombre"]==nombre:
                    print("Error: El país ya se encuentra registrado. ")
                    break
            else:
                break    
        ## Si no existe, lo agrega        
        print(f"Datos para '{nombre}':")    
        ## Inputs con Validaciones 
        poblacion=pedir_numero("\n Ingrese la población: ",0)
        superficie=pedir_numero("\n ingrese la superficie: ",0)
        continente=pedir_texto("\n Ingrese el continente(Recuerde ingresar acentos si es necesario): ").capitalize()                            
        lista_paises.append({"nombre":nombre,
                            "poblacion":poblacion,
                            "superficie":superficie,
                            "continente":continente})
            

        print("El/los país/es ha/han sido agregados correctamente")    
