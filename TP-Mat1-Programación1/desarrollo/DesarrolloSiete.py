# Tabla de verdad del sumador de 1 bit
print("=== Tabla de verdad del sumador de 1 bit ===")
print(" A | B | Suma | Carry")
print("---+---+------+------")

for A in [0, 1]:
    for B in [0, 1]:
        suma  = A ^ B   # XOR para el bit de suma
        carry = A & B   # AND para el acarreo
        print(f" {A} | {B} |  {suma}   |   {carry}")
#Esto valida que el numero es 0 o 1
while True:
    #el usuario ingresa el valor de A
    A_str=input("\nIngresa A (0 o 1): ").strip()
    #si A_str no es 0 o 1 imprime mensaje de error y vuelve a pedir el numero
    if A_str not in ("0", "1"):
        print("  Entrada inválida. Debes ingresar 0 o 1.")
        continue
    #si la entreda es valida convierte A_str a entero y lo asigna a A
    A = int(A_str)
    #el usuario ingresa el valor de B
    B_str = input("Ingresa B (0 o 1): ").strip()
    #si B_str no es 0 o 1 imprime mensaje de error y vuelve a pedir el numero
    if B_str not in ("0", "1"):
        print("  Entrada inválida. Debes ingresar 0 o 1.")
        continue
    #si la entreda es valida convierte B_str a entero y lo asigna a B
    B = int(B_str)

