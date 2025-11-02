import csv


ruta_db="dataBase/paises.csv"


def leerArchivo():
    lista_paises=[]
    with open(ruta_db,"r",newline="",encoding="utf-8") as archivo:
        lector=csv.DictReader(archivo)
        for fila in lector:
            lista_paises.append({
                "nombre":fila["nombre"],
                "poblacion":int(fila["poblacion"]),
                "superficie":float(fila["superficie"]),
                "continente":fila["continente"]})
        return lista_paises    