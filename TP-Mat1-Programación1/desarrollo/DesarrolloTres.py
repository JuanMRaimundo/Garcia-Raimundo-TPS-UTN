import time  # Para usar sleep

# Cuenta del 0 al 15
for numero in range(16):
    # Convertierte a binario con formato de 4 bits
    binario = format(numero, '04b')
    #Esto crea la ilusion de led encendidos y apagados, esto muestran de manera visual los encendidos y apagados del codigo 
    #🔴 para 1 y  ⚫ para 0
    leds = ''.join('🔴' if bit == '1' else '⚫' for bit in binario)
    #Muestra número y su representación binaria y con sus leds encendidos y apagados
    print(f"{numero:2} -> {binario}  {leds}")
    # se produce un retardo de 0.5 segundos para simular el conteo
    time.sleep(0.5)