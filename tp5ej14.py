################
# Agustin Montiveros - @agustin-montiveros
# UNRN Andina - Introducción a la Ingenieria en Computación
################


# Reemplazar por las funciones del ejercicio

def prueba_capicua(numero):
    capicua = list(str(numero))
    for i in range(len(capicua)):
        capicua[i] = int(capicua[i])
    print(capicua)
    capicua_reves= list(reversed(capicua))
    return capicua == capicua_reves



def prueba():
    numero = int(input("Ingresar un numero: "))
    resultado = prueba_capicua(numero)
    
    if resultado == True:
        print(resultado, ",el numero es capicua")
    else:
        print(resultado, ",el numero no es capicua")

if __name__ == "__main__":
    prueba()

