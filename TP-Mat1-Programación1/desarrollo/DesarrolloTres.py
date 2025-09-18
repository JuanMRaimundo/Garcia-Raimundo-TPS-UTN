#Programa:Cuenta del 0 al 15 en diferentes sistemas numericos
import time  # Para usar sleep

# Función para convertir a números romanos (hasta 3999)
def a_romano(numero):
    #Lista con los valores de numeros en romano
    valores = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]
    #variable para la conversion de numero a simbolo romano
    resultado = ""
    n = numero
    for valor, simbolo in valores:
        #Mientras que n sea igual o mayor que valor a el resultado se le suma un sinbolo y a n se le resta el valor
        while n >= valor:
            resultado += simbolo
            n -= valor
    #el cero no cambia por que no existe el cero en los numeros romanos
    return resultado if resultado else "0"  # Para el caso de 0
# Cuenta del 0 al 15
for numero in range(16):
    # Representaciones en distintos sistemas
    binario = format(numero, '04b')   # Binario con 4 bits
    octal = format(numero, 'o')       # Octal
    hexadecimal = format(numero, 'X') # Hexadecimal en mayúsculas
    romano = a_romano(numero)              # Romano
    #Esto crea la ilusion de led encendidos y apagados, esto muestran de manera visual los encendidos y apagados del codigo 
    #🔴 para 1 y  ⚫ para 0
    leds = ''.join('🔴' if bit == '1' else '⚫' for bit in binario)
    #Muestra número y su representación binaria, octal, hexadecimal y romano con sus leds encendidos y apagados
    print(f"{numero:2} -> {binario}  {leds} | Oct: {octal:>2} | Hex: {hexadecimal:>2} | Rom: {romano}")
    # se produce un retardo de 0.5 segundos para simular el conteo
    time.sleep(0.5)