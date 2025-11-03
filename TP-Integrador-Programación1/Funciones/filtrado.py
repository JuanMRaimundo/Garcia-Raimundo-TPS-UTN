# menu_filtrado_con_datos.py
import sys

#función para validar si un string es un entero
def es_entero(s):
    #variable para limpiar espacios
    s = s.strip()
    #si el string está vacío
    if s == "":
        #devolver False
        return False
    # admitir negativos si fuera necesario
    if s.lstrip("-").isdigit():
        #devolver True
        return True
    #devolver False
    return False

#función para convertir string a int o None
def convertir_int_opcional(s):
    #variable para limpiar espacios
    s = s.strip()
    #si el string está vacío
    if s == "":
        #devolver None
        return None
    #devolver el entero o None si no es válido
    return int(s) if s.lstrip("-").isdigit() else None

# funcion para mostrar una lista de países
def mostrar_lista(paises):
    #si la lista está vacía
    if not paises:
        print("No se encontraron países.")
        return
    #para cada país en la lista 
    for p in paises:
        #extraer datos
        nombre = p["nombre"]
        cont = p["continente"].title()
        pobl = f"{p['poblacion']:,}"
        sup = f"{p['superficie']:,}"
        #imprimir datos formateados
        print(f"- {nombre} | Continente: {cont} | Población: {pobl} | Superficie km²: {sup}")

# Función de filtrado reutilizable
def filtrar_paises(paises, criterio, valor=None, min_val=None, max_val=None):
    #"""
    #Filtra 'paises' según:
    #- criterio == "continente": usar 'valor' (string, comparado en minúsculas)
    #- criterio == "poblacion": usar min_val y/o max_val (enteros o None)
    #- criterio == "superficie": usar min_val y/o max_val (enteros o None)
    #Devuelve la lista filtrada (posible lista vacía).
    #"""
    # variable para almacenar los resultados
    resultado = []
    #variable para normalizar el criterio
    criterio_norm = criterio.strip().lower()
    #si el criterio es continente
    if criterio_norm == "continente":
        #si el valor es None
        if valor is None:
            #devolver lista vacía
            return []
        #variable para limpiar y normalizar el valor
        v = valor.strip().lower()
        #para cada país en la lista
        for p in paises:
            #si el continente del país coincide con el valor
            if p.get("continente", "").lower() == v:
                #añadir país a resultados
                resultado.append(p)
        #devolver resultados
        return resultado
    #si el criterio es población o superficie
    if criterio_norm in ("poblacion", "superficie"):
        #variable para determinar si es población o superficie
        campo = "poblacion" if criterio_norm == "poblacion" else "superficie"
        #para cada país en la lista
        for p in paises:
            # obtener el valor del campo
            val = p.get(campo)
            #si el valor es None, o no cumple los límites
            if val is None:
                #continua
                continue
            #si min_val está definido y el valor es menor que min_val
            if (min_val is not None) and (val < min_val):
                #continuar
                continue
            #si max_val está definido y el valor es mayor que max_val
            if (max_val is not None) and (val > max_val):
                #continuar
                continue
            #añadir país a resultados
            resultado.append(p)
        #devolver resultados
        return resultado

    # criterio no reconocido -> devolver vacío
    return []

# Menú interactivo que usa la función filtrar_paises
def menu_filtrar_interactivo(paises):
    print("Haz seleccionado: Filtrar países")
    print("Opciones de filtrado:")
    print("1. Por Continente")
    print("2. Por Rango de Población")
    print("3. Por Rango de Superficie")
    opcion = input("Seleccione una opción (1-3, Enter para cancelar): ").strip()

    if opcion == "1":
        continente = input("Considere poner acentos y mayusculas correctamente\nIngrese el continente (ej. Europa, América, Asia, África, Oceanía):").strip()
        if continente == "":
            print("Continente vacío. Cancelado.")
            return
        resultados = filtrar_paises(paises, "continente", valor=continente)
        print(f"\nResultados para continente '{continente}':")
        mostrar_lista(resultados)

    elif opcion == "2":
        min_p = input("Población mínima (Enter para omitir): ").strip()
        max_p = input("Población máxima (Enter para omitir): ").strip()
        min_val = convertir_int_opcional(min_p)
        max_val = convertir_int_opcional(max_p)
        if min_p != "" and min_val is None:
            print("Población mínima inválida; se omitirá ese límite.")
        if max_p != "" and max_val is None:
            print("Población máxima inválida; se omitirá ese límite.")
        resultados = filtrar_paises(paises, "poblacion", min_val=min_val, max_val=max_val)
        print(f"\nResultados para población entre {min_val if min_val is not None else '-inf'} y {max_val if max_val is not None else 'inf'}:")
        mostrar_lista(resultados)

    elif opcion == "3":
        min_s = input("Superficie mínima km² (Enter para omitir): ").strip()
        max_s = input("Superficie máxima km² (Enter para omitir): ").strip()
        min_val = convertir_int_opcional(min_s)
        max_val = convertir_int_opcional(max_s)
        if min_s != "" and min_val is None:
            print("Superficie mínima inválida; se omitirá ese límite.")
        if max_s != "" and max_val is None:
            print("Superficie máxima inválida; se omitirá ese límite.")
        resultados = filtrar_paises(paises, "superficie", min_val=min_val, max_val=max_val)
        print(f"\nResultados para superficie entre {min_val if min_val is not None else '-inf'} y {max_val if max_val is not None else 'inf'}:")
        mostrar_lista(resultados)

    else:
        print("Operación cancelada o opción inválida.")

# Pequeño menú principal para probar
def main():
    while True:
        print("\n--- Menú Principal ---")
        print("1. Filtrar países")
        print("2. Listar todos los países")
        print("3. Salir")
        opc = input("Seleccione (1-3): ").strip()
        if opc == "1":
            menu_filtrar_interactivo(PAISES)
        elif opc == "2":
            mostrar_lista(PAISES)
        elif opc == "3":
            print("Saliendo...")
            sys.exit(0)
        else:
            print("Opción inválida. Intente nuevamente.")

