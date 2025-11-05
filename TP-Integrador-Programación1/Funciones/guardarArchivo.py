import csv
from pathlib import Path

# Ruta del archivo actual (Funciones → ../dataBase/paises.csv)
RUTA_CSV = Path(__file__).resolve().parent.parent / "dataBase" / "paises.csv"


def guardar_archivo(lista_paises):
    #"""
    #Guarda la lista de países en el archivo CSV ubicado en ../dataBase/paises.csv.
    #Cada país debe tener las claves: nombre, poblacion, superficie, continente.
    #"""
    if not lista_paises:
        print("ERROR: Falta la lista de países para guardar.")
        return

    with RUTA_CSV.open("w", newline="", encoding="utf-8") as archivo:
        campos = ["nombre", "poblacion", "superficie", "continente"]
        escritor = csv.DictWriter(archivo, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(lista_paises)

    print(f"archivo guardado correctamente en: {RUTA_CSV}")
