def estadisticas(lista_paises):
    while True:
        print("\n=== ESTADÍSTICAS ===")
        print("1. País con mayor y menor población")
        print("2. Promedio de población")
        print("3. Promedio de superficie")
        print("4. Cantidad de países por continente")
        print("5. Volver al menú principal")
        
        opcion = input("Seleccione una opción (1-5): ")
        
        match opcion:
            case "1":
                pais_mayor_menor_poblacion(lista_paises)
            case "2":
                promedio_poblacion(lista_paises)
            case "3":
                promedio_superficie(lista_paises)
            case "4":
                paises_por_continente(lista_paises)
            case "5":
                #Este caso es para volver al menú principal.
                break  
            case _:
                print("Opción inválida! Por favor ingrese una opción dentro del menú indicado. ")



#Función para pasarle a la "key" del min y max, interno de python. 
def obtener_poblacion(pais):
    return pais["poblacion"]


def pais_mayor_menor_poblacion(lista_paises):

    if not lista_paises:
        print("No hay países en la lista")
        return
    pais_mayor = max(lista_paises,key=obtener_poblacion)
    pais_menor = min(lista_paises,key=obtener_poblacion)

    print(f"\nEl país con mayor población es: \n{pais_mayor["nombre"]}, con una población de {pais_mayor["poblacion"]} habitantes.")
    print(f"\nEl país con menor población es: \n{pais_menor["nombre"]}, con una población de {pais_menor["poblacion"]} habitantes.")
    



def promedio_poblacion(lista_paises):
    if not lista_paises:
        print("No hay países en la lista")
        return
    total=0
    
    for pais in lista_paises:
        total+=pais["poblacion"]
    promedio=total/len(lista_paises)

    print(f"\nEl promedio de población dentro de la lista de paises es de : {promedio} habitantes.")


def promedio_superficie(lista_paises):
    if not lista_paises:
        print("No hay países en la lista")
        return
    total=0
    
    for pais in lista_paises:
        total+=pais["superficie"]
    promedio=total/len(lista_paises)

    print(f"\nEl promedio de superficie dentro de la lista de paises es de : {promedio}mts cuadrados.")

    

def paises_por_continente(lista_paises):
    america=[]
    oceania=[]
    europa=[]
    asia=[]
    africa=[]

    if not lista_paises:
        print("No hay países en la lista")
        return
    
    for pais in lista_paises:
        continente = pais["continente"]

        if continente == "América":
            america.append(pais)
        if continente == "Oceanía":
            oceania.append(pais)
        if continente == "Europa":
            europa.append(pais)
        if continente == "Asia":
            asia.append(pais)        
        if continente == "África":
            africa.append(pais)   

    print(f"\n En la lista hay {len(america)} países de America. ")          
    print(f"\n En la lista hay {len(oceania)} países de Oceanía. ")          
    print(f"\n En la lista hay {len(europa)} países de Europa. ")          
    print(f"\n En la lista hay {len(asia)} países de Asia. ")          
    print(f"\n En la lista hay {len(africa)} países de Aáfrica. ")          

