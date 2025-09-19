# Tabla de verdad del sumador de 1 bit
print("=== Tabla de verdad del sumador de 1 bit ===")
print(" A | B | Suma | Carry")
print("---+---+------+------")

for A in [0, 1]:
    for B in [0, 1]:
        suma  = A ^ B   # XOR para el bit de suma
        carry = A & B   # AND para el acarreo
        print(f" {A} | {B} |  {suma}   |   {carry}")