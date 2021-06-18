################
# Agustin Montiveros - @agustin-montiveros
# UNRN Andina - Introducción a la Ingenieria en Computación
################


# Reemplazar por las funciones del ejercicio


def busqueda_de_palabra(texto, palabra):
    return texto.find(palabra)
    


def prueba():
    texto = input("Ingresar el texto: ")
    palabra = input("Ingresar la palabra a buscar: ")
    resultado = busqueda_de_palabra(texto,palabra)
    if resultado != -1:
        print(f"La palabra '{palabra}' se encuentra en la posicion: ", resultado)
    else:
        raise Exception("La palabra no se encuentra en el texto")
        
if __name__ == "__main__":
    prueba()

