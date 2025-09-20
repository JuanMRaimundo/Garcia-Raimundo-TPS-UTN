# --- Bloque de tabla ---
print("=== Tabla de verdad de la suma, resta, division y multiplicacion de 1 bit ===")
print(" A | B | Suma | Carry | Resta | Borrow | Mult | DivQ | DivR")
print("---+---+------+------+-------+--------+------+------+------")
# Recorre todas las combinaciones posibles de A y B (0 y 1)
for A in [0, 1]:
    for B in [0, 1]:
        suma   = A ^ B
        carry  = A & B
        resta  = A ^ B
        borrow = int((not A) and B)
        mult   = A * B
        if B == 0:
            divq = "NaN"
            divr = "NaN"
        else:
            divq = A // B
            divr = A % B
        print(f" {A} | {B} |  {suma}   |   {carry}   |   {resta}   |   {borrow}    |  {mult}   |  {divq}   |  {divr}")
print("\n=== Modo interactivo ===")
print("Ingresa solo 0 o 1 para A y B.")
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
    #se le presentan al usuario las opciones de operaciones que puede realizar,
    #eliminamos espacios y convertimos mayusculas a minusculas por si acaso
    op = input("Elige operación: suma (s), resta (r), mult (m) o div (d): ").strip().lower()
    #si la operacion no es valida imprime mensaje de error y vuelve a pedir la operacion
    if op not in ("s", "r", "m", "d"):
        print("  Operación inválida. Usa 's', 'r', 'm' o 'd'.")
        continue
    #Calcula todas las operaciones
    suma   = A ^ B
    carry  = A & B
    resta  = A ^ B
    borrow = int((not A) and B)
    mult   = A * B
    #Maneja división por cero
    if B == 0:
        divq = "NaN"
        divr = "NaN"
    #si B no es 0 realiza la division
    else:
        divq = A // B
        divr = A % B
    #Muestra el resultado de la operacion seleccionada
    #si la operacion es suma, muestra el resultado de la suma y el carry
    if op == "s":
        print(f"  Suma   → bit: {suma}, carry: {carry}")
    #si la operacion es resta, muestra el resultado de la resta y el borrow
    elif op == "r":
        print(f"  Resta  → bit: {resta}, borrow: {borrow}")
    #si la operacion es multiplicacion, muestra el resultado de la multiplicacion
    elif op == "m":
        print(f"  Mult   → resultado: {mult}")
    #si la operacion es division, muestra el cociente y el resto
    else:
        if divq is None:
            print("  División indefinida (división por cero)")
        else:
            print(f"  DivQ   → cociente: {divq}")
            print(f"  DivR   → resto:     {divr}")
    otra = input("  ¿Otra operación? (s/n): ").strip().lower()
    if otra != "s":
        print("  Fin del simulador.")
        break