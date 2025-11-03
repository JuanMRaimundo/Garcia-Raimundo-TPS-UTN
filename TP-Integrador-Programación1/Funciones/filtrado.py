# menu_filtrado_con_datos.py
import sys

# Utilidades de validación y conversión
def es_entero(s):
    s = s.strip()
    if s == "":
        return False
    # admitir negativos si fuera necesario
    if s.lstrip("-").isdigit():
        return True
    return False

def convertir_int_opcional(s):
    s = s.strip()
    if s == "":
        return None
    return int(s) if s.lstrip("-").isdigit() else None

def mostrar_lista(paises):
    if not paises:
        print("No se encontraron países.")
        return
    for p in paises:
        nombre = p["nombre"]
        cont = p["continente"].title()
        pobl = f"{p['poblacion']:,}"
        sup = f"{p['superficie']:,}"
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
    resultado = []
    criterio_norm = criterio.strip().lower()

    if criterio_norm == "continente":
        if valor is None:
            return []
        v = valor.strip().lower()
        for p in paises:
            if p.get("continente", "").lower() == v:
                resultado.append(p)
        return resultado

    if criterio_norm in ("poblacion", "superficie"):
        campo = "poblacion" if criterio_norm == "poblacion" else "superficie"
        for p in paises:
            val = p.get(campo)
            if val is None:
                continue
            if (min_val is not None) and (val < min_val):
                continue
            if (max_val is not None) and (val > max_val):
                continue
            resultado.append(p)
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

