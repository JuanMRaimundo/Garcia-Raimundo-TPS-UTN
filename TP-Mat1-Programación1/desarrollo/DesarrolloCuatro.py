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
}
# Mostrar opciones
print("Operaciones disponibles:")
for op in operaciones:
    print(f"- {op}")

#Solicitar operación al usuario
#el .strip() elimina los espacios y otros caracteres como salto de linea en la respuesta
#el .upper() toma cualquier minuscula y lo convierte en mayuscula
opcion = input("Elige una operación lógica: ").strip().upper()

#Esto valida operación, si la opcion no esta en las operaciones imprira un mensaje
#sino, imprimira la primera fila de la tabla
if opcion not in operaciones:
    print("Operación no válida.")
else:
    print(f"\nTabla de verdad para: {opcion}")
    print("A\tB\tResultado")
    print("-" * 24)