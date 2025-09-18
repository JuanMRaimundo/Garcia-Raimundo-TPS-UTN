import time  # Para usar sleep

# Cuenta del 0 al 15
for numero in range(16):
    # Representaciones en distintos sistemas
    binario = format(numero, '04b')   # Binario con 4 bits
    octal = format(numero, 'o')       # Octal
    hexadecimal = format(numero, 'X') # Hexadecimal en mayúsculas
    #Esto crea la ilusion de led encendidos y apagados, esto muestran de manera visual los encendidos y apagados del codigo 
    #🔴 para 1 y  ⚫ para 0
    leds = ''.join('🔴' if bit == '1' else '⚫' for bit in binario)
    #Muestra número y su representación binaria, octal y hexadecimal y con sus leds encendidos y apagados
    print(f"{numero:2} -> {binario}  {leds} | Oct: {octal:>2} | Hex: {hexadecimal:>2}")
    # se produce un retardo de 0.5 segundos para simular el conteo
    time.sleep(0.5)