from typing import List, Dict

# funciones auxiliares para validación y conversión
# funcion para validar enteros
def es_entero_valido(s: str) -> bool:
    # eliminar comas y espacios
    s2 = s.strip().replace(",", "")
    # retornar si es dígito o negativo válido
    return s2.isdigit() or (s2.startswith("-") and s2[1:].isdigit())

#funcion para validar flotantes
def es_flotante_valido(s: str) -> bool:
    # eliminar comas y espacios y almacenar en s2
    s2 = s.strip().replace(",", "")
    #si s2 está vacío
    if s2 == "":
        #retorna false
        return False
    # si tiene un solo punto decimal
    if s2.count(".") == 1:
        #variable que almacena las partes separadas por el punto
        parts = s2.split(".")
        #retorna si ambas partes son dígitos (la parte entera puede ser negativa)
        return parts[0].lstrip("-").isdigit() and parts[1].isdigit()
    #si no tiene punto decimal, verificar si es entero válido
    return s2.lstrip("-").isdigit()


#funciones para conversiones opcionales
#funcion para convertir a int o None
def to_int_opcional(v):
    #"""
    #Acepta str, int, float o None.
    #Devuelve int si es posible, o None si no se puede convertir.
    #"""
    # Si ya es int, devolver tal cual
    if isinstance(v, int) and not isinstance(v, bool):
        return v
    # Si es float convertible a int, convertir truncando decimal
    if isinstance(v, float):
        return int(v)
    # Si es None o booleano no es válido
    if v is None:
        return None
    # Si es string, sanear y comprobar
    if isinstance(v, str):
        #variable para limpiar comas y espacios
        s = v.strip().replace(",", "")
        #si el string está vacío
        if s == "":
            #retornar None
            return None
        # si es un entero válido
        if s.lstrip("-").isdigit():
            #retornar el entero
            return int(s)
        # si es un float válido
        if s.replace(".", "", 1).lstrip("-").isdigit() and s.count(".") <= 1:
            #retornar el entero truncado
            return int(float(s))
    # cualquier otro tipo no convertible
    return None

#funcion para convertir a float o None
def to_float_opcional(v):
    #"""
    #Acepta str, int, float o None.
    #Devuelve float si es posible, o None si no se puede convertir.
    #"""
    if isinstance(v, float):
        return v
    if isinstance(v, int) and not isinstance(v, bool):
        return float(v)
    if v is None:
        return None
    if isinstance(v, str):
        s = v.strip().replace(",", "")
        if s == "":
            return None
        # permitir enteros o floats con un único punto decimal
        if s.lstrip("-").isdigit():
            return float(int(s))
        if s.replace(".", "", 1).lstrip("-").isdigit() and s.count(".") <= 1:
            return float(s)
    return None

# funcion para normalizar lista de países
def normalizar_paises(paises_raw):
    #"""
    #Convierte y normaliza una lista de diccionarios de entrada.
    #- nombre: strip -> string (vacío si no existe)
    #- continente: strip + lower -> string (vacío si no existe)
    #- poblacion: int (0 si no disponible)
    #- superficie: float (0.0 si no disponible)
    #"""
    # variable para la lista normalizada
    lista = []
    # para cada país en la lista de entrada
    for p in paises_raw:
        # Obtener bruto (si la clave no existe, usar None)
        # variable para el nombre bruto
        raw_nombre = p.get("nombre") if isinstance(p, dict) else None
        # variable para el continente bruto
        raw_continente = p.get("continente") if isinstance(p, dict) else None
        # variable para la población bruto
        raw_pobl = p.get("poblacion") if isinstance(p, dict) else None
        # variable para la superficie bruto
        raw_sup = p.get("superficie") if isinstance(p, dict) else None
        # variables normalizadas
        nombre = (raw_nombre.strip() if isinstance(raw_nombre, str) else (str(raw_nombre) if raw_nombre is not None else "")).strip()
        continente = (raw_continente.strip().lower() if isinstance(raw_continente, str) else (str(raw_continente).lower() if raw_continente is not None else "")).strip()
        # convertir población y superficie a tipos adecuados
        pobl = to_int_opcional(raw_pobl)
        sup = to_float_opcional(raw_sup)
        # asegurar valores por defecto si la conversión falla 
        poblacion = pobl if isinstance(pobl, int) else 0
        superficie = sup if isinstance(sup, (int, float)) else 0.0
        # añadir país normalizado a la lista
        lista.append({
            "nombre": nombre,
            "continente": continente,
            "poblacion": poblacion,
            "superficie": superficie
        })
    return lista

# funcion para ordenar países
def ordenar_paises(paises: List[Dict], criterio: str, descendente: bool = False) -> List[Dict]:
    #"""
    #Ordena por 'nombre', 'poblacion' o 'superficie'.
    #- criterio: case-insensitive
    #- descendente: True => mayor->menor or Z->A
    #Devuelve nueva lista sin modificar la original.
    #"""
    #variable para normalizar el criterio
    crit = (criterio or "").strip().lower()
    #si el criterio es nombre
    if crit == "nombre":
        #sorted(paises, ...): llama al ordenador incorporado para generar una nueva lista ordenada a partir de la lista original paises.
        #key=lambda x: (x.get("nombre") or "").lower(): define la clave de ordenación; para cada elemento x (un dict de país):
        #x.get("nombre") obtiene el valor asociado a la clave "nombre" o devuelve None si no existe;
        #(x.get("nombre") or "") sustituye None o cadenas vacías por la cadena vacía "" para evitar errores;
        #.lower() convierte el texto a minúsculas para que la comparación sea case-insensitive y consistente.
        #reverse=descendente: si descendente es True invierte el orden (Z→A), si es False mantiene ascendente (A→Z).
        #La expresión retorna la lista ordenada sin modificar la original.
        return sorted(paises, key=lambda x: (x.get("nombre") or "").lower(), reverse=descendente)
    #si el criterio es población
    if crit == "poblacion":
        #sorted(paises, ...): devuelve una nueva lista ordenada por el valor numérico de población.
        #key=lambda x: x.get("poblacion") if isinstance(x.get("poblacion"), (int, float)) else 0: para cada país x:
        #x.get("poblacion") obtiene el valor asociado;
        #isinstance(..., (int, float)) verifica que el valor sea numérico (int o float);
        #si es numérico se usa ese valor como clave de ordenación; si no, se usa 0 como valor por defecto para que faltas o datos inválidos no rompan el ordenamiento.
        #reverse=descendente controla si el orden es ascendente (False) o descendente (True).
        return sorted(paises, key=lambda x: x.get("poblacion") if isinstance(x.get("poblacion"), (int, float)) else 0, reverse=descendente)
    if crit == "superficie":
        return sorted(paises, key=lambda x: x.get("superficie") if isinstance(x.get("superficie"), (int, float)) else 0.0, reverse=descendente)
    # criterio no reconocido: devolver copia sin ordenar
    return list(paises)

# funcion para mostrar lista de países
def mostrar_lista(paises: List[Dict]) -> None:
    #si la lista está vacía
    if not paises:
        #imprimir mensaje y retornar
        print("No hay países para mostrar.")
        return
    #para cada país en la lista
    for p in paises:
        #extraer y formatear datos
        nombre = p.get("nombre", "")
        cont = p.get("continente", "").title()
        pobl = f"{p.get('poblacion',0):,}"
        sup = f"{p.get('superficie',0):,}"
        #imprimir datos formateados
        print(f"- {nombre} | Continente: {cont} | Población: {pobl} | Superficie km²: {sup}")

#funcion para menú interactivo de ordenamiento
def menu_ordenar_interactivo(paises_raw: List[Dict]) -> None:
    #normalizar datos de países
    paises = normalizar_paises(paises_raw)
    #bucle infinito para el menú
    while True:
        #mostrar opciones del menú
        print("\n--- Menú de Ordenamiento ---")
        print("1. Ordenar por Nombre (A-Z)")
        print("2. Ordenar por Nombre (Z-A)")
        print("3. Ordenar por Población (ascendente)")
        print("4. Ordenar por Población (descendente)")
        print("5. Ordenar por Superficie (ascendente)")
        print("6. Ordenar por Superficie (descendente)")
        print("7. Ver lista original normalizada")
        print("8. Salir")
        # solicitar opción al usuario
        opt = input("Seleccione una opción (1-8): ").strip()      
        match opt:
            case "1":
                res = ordenar_paises(paises, "nombre", descendente=False)
                mostrar_lista(res)
            case "2":
                res = ordenar_paises(paises, "nombre", descendente=True)
                mostrar_lista(res)
            case "3":
                res = ordenar_paises(paises, "poblacion", descendente=False)
                mostrar_lista(res)
            case "4":
                res = ordenar_paises(paises, "poblacion", descendente=True)
                mostrar_lista(res)
            case "5":
                res = ordenar_paises(paises, "superficie", descendente=False)
                mostrar_lista(res)
            case "6":
                res = ordenar_paises(paises, "superficie", descendente=True)
                mostrar_lista(res)
            case "7":
                mostrar_lista(paises)
            case "8":
                print("Saliendo...")
                break
            case _:
                print("Opción inválida. Intente nuevamente.")
                    
