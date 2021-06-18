################
# Agustin Montiveros - @agustin-montiveros
# UNRN Andina - Introducción a la Ingenieria en Computación
################


# Reemplazar por las funciones del ejercicio


def busqueda_de_palabra(texto, palabra):
    valor_a = -1
    valor_b = len(palabra) -1
    for n in range(len(texto)):
        valor_a = valor_a+1
        valor_b = valor_b+1
        if palabra[:] == texto[valor_a:valor_b]:
            print("La palabra se encuentra primero en el caracter n°: ", len(texto[valor_a:valor_b]))
        elif n == range(len(texto)):
            raise Exception("La palabra no se encuentra en el texto")
    


def prueba():
    texto_a = input("Ingresar el texto: ")
    palabra_a = input("Ingresar la palabra a buscar: ")
    texto= list(texto_a)
    palabra = list(palabra_a)
    busqueda_de_palabra(texto, palabra)

if __name__ == "__main__":
    prueba()

