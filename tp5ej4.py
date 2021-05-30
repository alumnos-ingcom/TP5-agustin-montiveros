################
# Agustin Montiveros - @agustin-montiveros
# UNRN Andina - Introducción a la Ingenieria en Computación
################


# Reemplazar por las funciones del ejercicio

def numeroPerfecto(numero):
    numeroGuardado = 0
    for i in range(1, numero):
        if numero % i == 0:
            numeroGuardado = numeroGuardado + i
    return numeroGuardado == numero


def prueba():
    numero = int(input("Ingrese un numero: "))
    resultado = numeroPerfecto(numero)
    print("Es un numero perfecto? ", resultado)



if __name__ == "__main__":
    prueba()

