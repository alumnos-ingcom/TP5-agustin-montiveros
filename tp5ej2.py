################
# Agustin Montiveros - @agustin-montiveros
# UNRN Andina - Introducción a la Ingenieria en Computación
################


# Reemplazar por las funciones del ejercicio

def fibonacci(numero):
    primer_valor = 0
    segundo_valor = 1
    while primer_valor < numero:       
        secuencia = print(primer_valor, end=",")
        primer_valor, segundo_valor = segundo_valor, primer_valor+segundo_valor
    return secuencia
    

def prueba():
        numero= int(input("Ingrese el numero limite de fibonacci: "))
        resultado = fibonacci(numero)



if __name__ == "__main__":
    prueba()

