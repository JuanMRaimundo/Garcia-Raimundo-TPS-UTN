import csv


ruta_db="dataBase/paises.csv"

def guardar_archivo(lista_paises):
    if not lista_paises:
        print("ERROR: Falta la lista de paises para poder guardarlas")
    else:    
        with open(ruta_db,"w", newline="", encoding="utf-8") as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=["nombre","poblacion","superficie","continente"])
            escritor.writeheader()
            escritor.writerows(lista_paises)