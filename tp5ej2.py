################
# Agustin Montiveros - @agustin-montiveros
# UNRN Andina - Introducción a la Ingenieria en Computación
################


# Reemplazar por las funciones del ejercicio

def fibonacci(n):
    a= 0
    b= 1
    while a < n:       
        print(a, end=",")
        a, b = b, a+b
    

def prueba():
        n= int(input("Ingrese el numero limite de fibonacci: "))
        print(fibonacci(n))
        pass

if __name__ == "__main__":
    prueba()

