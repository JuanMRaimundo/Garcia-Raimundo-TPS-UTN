# Tabla de verdad del sumador de 1 bit
print("=== Tabla de verdad del sumador de 1 bit ===")
print(" A | B | Suma | Carry | Resta | Borrow | Mult | DivQ | DivR")
print("---+---+------+------+-------+--------+------+------+------")

for A in [0, 1]:
    for B in [0, 1]:
        # Suma (half-adder)
        suma   = A ^ B
        carry  = A & B

        # Resta (half-subtractor)
        resta  = A ^ B
        borrow = int((not A) and B)

        # Multiplicación
        mult = A * B

        # División entera: cociente (DivQ) y resto (DivR), manejando B=0
        if B == 0:
            divq = "NaN"  # no definido
            divr = "NaN"
        else:
            divq = A // B
            divr = A % B

        print(f" {A} | {B} |  {suma}   |   {carry}   |   {resta}   |   {borrow}    |  {mult}   |  {divq}   |  {divr}")
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
    #Calcula la suma y el carry
    suma  = A ^ B
    carry = A & B
    #Muestra el resultado de la suma y el carry
    print(f"  Resultado → Suma: {suma}, Carry: {carry}")
    #Pregunta si desea realizar otra suma
    otra = input("  ¿Otra suma? (s/n): ").strip().lower()
    #si la respuesta no es 's' termina el programa
    if otra != "s":
        print("  Fin del simulador.")
        break