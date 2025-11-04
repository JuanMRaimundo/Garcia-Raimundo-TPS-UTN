# Para que no ingrese un texto vacío. 
def pedir_texto(mensaje):
   
    while True:
        texto = input(mensaje).strip()
        if texto:
            return texto
        print("Error: El texto no puede estar vacío")