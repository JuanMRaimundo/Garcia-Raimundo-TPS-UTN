import time  # Para usar sleep

# Cuenta del 0 al 15
for numero in range(16):
    # Convertierte a binario con formato de 4 bits
    binario = format(numero, '04b')
    # Muestra número y su representación binaria
    print(f"{numero} -> {binario}")
    # SE produce un retardo de 0.5 segundos para simular el conteo
    time.sleep(0.5)