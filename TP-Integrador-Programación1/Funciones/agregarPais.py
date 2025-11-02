

def agregarPais(lista_paises):
    print("\n ## A continuación podrá agregar países: ##\n")
    cantidad_paises=int(input("Ingrese la cantidad de países que desea agregar: "))
    for i in range(cantidad_paises):
        print(f"\n--- País {i+1} ---")
        nombre=input("Ingrese el nombre: ").upper()
        ##AGREGAR VALIDACIÓN SI EXISTE O NO
        poblacion=int(input("Ingrese la población: "))
        superficie=float((input("Ingrese la superficie: ")))
        continente=input("Ingrese el continente: ").upper()
        lista_paises.append({"nombre":nombre,
                       "poblacion":poblacion,
                       "superficie":superficie,
                       "continente":continente})
    print("Los países han sido agregados correctamente")    
