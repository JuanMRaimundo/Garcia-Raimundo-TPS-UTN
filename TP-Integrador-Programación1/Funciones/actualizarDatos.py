def actualizar_datos_pais(paises: list, nombre_pais: str, nueva_poblacion: int, nueva_superficie: float) -> bool:
    #"""
    #Actualiza la población y superficie de un país en la lista. 
    # Parámetros:
    #- paises: lista de diccionarios con claves 'nombre', 'poblacion', 'superficie', 'continente'
    #- nombre_pais: nombre del país a actualizar (insensible a mayúsculas)
    #- nueva_poblacion: nuevo valor de población (entero positivo)
    #- nueva_superficie: nuevo valor de superficie (float positivo)
    #Retorna:
    #- True si se actualizó correctamente, False si el país no se encontró.
    #"""
    # variable para el nombre normalizado
    nombre_normalizado = nombre_pais.strip().lower()
    # para cada país en la lista
    for pais in paises:
        #si pais coincide con el nombre dado (insensible a mayúsculas)
        if pais.get("nombre", "").strip().lower() == nombre_normalizado:
            # si los nuevos valores son válidos, actualizar la población del país
            if isinstance(nueva_poblacion, int) and nueva_poblacion > 0:
                pais["poblacion"] = nueva_poblacion
            # si los nuevos valores son válidos, actualizar la superficie del país
            if isinstance(nueva_superficie, (int, float)) and nueva_superficie > 0:
                pais["superficie"] = float(nueva_superficie)
            return True  # Actualización exitosa
    return False  # País no encontrado

# funciones auxiliares para validación de entradas
# función para verificar si un string es un entero válido
def es_entero_valido(s):
    return s.strip().isdigit()

# función para verificar si un string es un float válido
def es_flotante_valido(s):
    s = s.strip().replace(",", "")
    if s.count(".") > 1:
        return False
    return s.replace(".", "", 1).isdigit()

# función de menú para actualizar datos de un país
def menu_actualizar_pais(paises: list):
    #"""
    #Menú interactivo para actualizar población y superficie de un país.
    #"""
    print("\nActualizar datos de un país")
    nombre = input("Ingrese el nombre del país a actualizar: ").strip()
    #si el nombre está vacío
    if not nombre:
        #imprimir mensaje de error y salir
        print(" Nombre vacío. Cancelando operación.")
        return
    # Pedir nueva población y superficie con validación
    nueva_poblacion = input("Ingrese la nueva población (entero positivo): ").strip()
    #si la población no es válida
    if not es_entero_valido(nueva_poblacion):
        #imprimir mensaje de error y salir
        print("Población inválida. Debe ser un número entero positivo.")
        return
    # Pedir nueva superficie
    nueva_superficie = input("Ingrese la nueva superficie en km² (número positivo): ").strip()
    #si la superficie no es válida
    if not es_flotante_valido(nueva_superficie):
        #imprimir mensaje de error y salir
        print("Superficie inválida. Debe ser un número decimal positivo.")
        return

    # Convertir valores a tipos adecuados
    poblacion = int(nueva_poblacion)
    superficie = float(nueva_superficie.replace(",", ""))

    # Llamar a la función de actualización
    actualizado = actualizar_datos_pais(paises, nombre, poblacion, superficie)
    # si se actualizó correctamente
    if actualizado:
        #imprimir mensaje de confirmación
        print(f"País '{nombre.title()}' actualizado correctamente.")
    #si no se encontró el país
    else:
        #imprimir mensaje de error
        print(f"País '{nombre.title()}' no encontrado en la base de datos.")