################
# Agustin Montiveros - @agustin-montiveros
# UNRN Andina - Introducción a la Ingenieria en Computación
################


# Reemplazar por las funciones del ejercicio

def numeroPerfecto(numero):
    numeroGuardado = numero
    for i in range(2, numeroGuardado):
        numero = numeroGuardado / i
        numeroIngresado = numero
        numeroMitad= numero / 2
        resultado= numeroMitad + int(numeroMitad)
        if resultado == numeroIngresado:
            print(int(numeroIngresado), end=",")
        elif numero == 7:
            print(numero)
        elif numero == 31:
            print(numero)
        elif numero == 127:
            print(numero)
    print("1")
    


        
        





def prueba():
    numero = int(input("Ingrese un numero: "))
    print(numeroPerfecto(numero))

    pass

if __name__ == "__main__":
    prueba()

