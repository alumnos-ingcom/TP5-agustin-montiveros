################
# Agustin Montiveros - @agustin-montiveros
# UNRN Andina - Introducción a la Ingenieria en Computación
################


# Reemplazar por las funciones del ejercicio

def distancia_entre_numeros(numero, numero_dos):
    if numero > numero_dos:
        distancia= numero - numero_dos
        return distancia
    elif numero < numero_dos:
        distancia = numero_dos - numero
        return distancia

def prueba():
    numero = int(input("Ingresar primer numero: "))
    numero_dos = int(input("Ingresar segundo numero: "))
    resultado = distancia_entre_numeros(numero, numero_dos)
    print("La distancia entre los numeros es de: ", resultado)

if __name__ == "__main__":
    prueba()

