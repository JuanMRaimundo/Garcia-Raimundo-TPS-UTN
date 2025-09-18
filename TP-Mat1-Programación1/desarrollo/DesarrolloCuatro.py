# Programa: Tabla de verdad interactiva

# Lista de operaciones disponibles
operaciones = {
    "AND": lambda a, b: a and b,
    "OR": lambda a, b: a or b,
    "XOR": lambda a, b: a ^ b,
    "NAND": lambda a, b: not (a and b),
    "NOR": lambda a, b: not (a or b),
    "XNOR": lambda a, b: not (a ^ b),
    "NOT A": lambda a, b: not a,
    "NOT B": lambda a, b: not b
}#Cada valor es una función lambda que recibe A y B y devuelve el resultado lógico.
# Mostrar opciones
print("Operaciones disponibles:")
for op in operaciones:
    print(f"- {op}")

#Solicitar operación al usuario
#el .strip() elimina los espacios y otros caracteres como salto de linea en la respuesta
#el .upper() toma cualquier minuscula y lo convierte en mayuscula
opcion = input("Elige una operación lógica: ").strip().upper()

#Esto valida operación, si la opcion no esta en las operaciones imprira un mensaje
#sino, imprimira la tabla de verdad
if opcion not in operaciones:
    print("Operación no válida.")
else:
    print(f"\nTabla de verdad para: {opcion}")
    print("A\tB\tResultado")
    print("-" * 24)
    #Se recorren todas las combinaciones posibles de A y B (False/True).
    for A in [False, True]:
        for B in [False, True]:
            resultado = operaciones[opcion](A, B)
            #se imprimen los resultados
            print(f"{int(A)}\t{int(B)}\t{int(resultado)}")