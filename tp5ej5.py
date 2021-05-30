################
# Agustin Montiveros - @agustin-montiveros
# UNRN Andina - Introducción a la Ingenieria en Computación
################


# Reemplazar por las funciones del ejercicio

def revertirCaracteres(texto):
    texto_cambiado = texto.swapcase()
    return texto_cambiado

def prueba():
    texto = str(input("Ingresar texto: "))
    resultado = revertirCaracteres(texto)
    print(resultado)

if __name__ == "__main__":
    prueba()

