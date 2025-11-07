# Para que no ingrese un texto vacío. 
def pedir_texto(mensaje):
    while True:
        texto = input(mensaje).strip().capitalize()
        if not texto:
            print("Error: El texto no puede estar vacío")
            continue
        if texto.isdigit():
            print("Error: No puede ingresar sólo números.")
            continue

        return texto
            


#Para pedír número

def pedir_numero(mensaje, minimo=None, maximo=None):
    
    while True:
        entrada = input(mensaje)
        if not entrada.isdigit():
            print("Error: Debe ingresar un número válido")
            continue
        
        numero = int(entrada)
        
        if minimo is not None and numero < minimo:
            print(f"Error: El número debe ser mayor o igual a {minimo}")
            continue
        
        if maximo is not None and numero > maximo:
            print(f"Error: El número debe ser menor o igual a {maximo}")
            continue
        
        return numero
    

