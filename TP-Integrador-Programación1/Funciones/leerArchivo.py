# leerArchivo.py
from pathlib import Path
import csv

# Ruta por defecto al archivo CSV
DEFAULT_CSV = Path(__file__).resolve().parent.parent / "dataBase" / "paises.csv"
# Función para leer el archivo CSV y devolver la lista de países
def leerArchivo(ruta_csv: Path | str = DEFAULT_CSV):
    #"""
    #Lee el CSV de países y devuelve una lista de dicts con
    #claves: nombre (str), poblacion (int), superficie (float), continente (str).
    #Se puede pasar una ruta alternativa como string o Path.
    # Devuelve lista vacía si no se encuentra el archivo.
    #"""
    ruta = Path(ruta_csv)
    lista_paises = []

    if not ruta.exists():
        # Manejo de error si el archivo no existe
        print(f"Archivo no encontrado: {ruta}")
        return lista_paises

    with ruta.open("r", newline="", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            # Extraer y limpiar datos
            nombre = fila.get("nombre", "").strip()
            continente = fila.get("continente", "").strip()
            
            pobl_str = fila.get("poblacion", "").strip().replace(",", "")
            sup_str = fila.get("superficie", "").strip().replace(",", "")
            # convertir a tipos adecuados, manejar errores
            poblacion = int(pobl_str) if pobl_str.isdigit() else 0
            # permitir decimales en superficie (ej: "1234.56")
            if sup_str.replace(".", "", 1).isdigit():
                superficie = float(sup_str)
            else:
                # si viene vacío o no es numérico, asignar 0.0
                superficie = 0.0

            lista_paises.append({
                "nombre": nombre,
                "poblacion": poblacion,
                "superficie": superficie,
                "continente": continente
            })

    return lista_paises
