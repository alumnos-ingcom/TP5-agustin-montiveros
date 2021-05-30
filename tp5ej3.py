################
# Agustin Montiveros - @agustin-montiveros
# UNRN Andina - Introducción a la Ingenieria en Computación
################


# Reemplazar por las funciones del ejercicio


def tribonacci(n):
    a= 0
    b= 0
    c= 1
    d= 0
    while a < n:       
        print(a, end=",")
        d = a + b + c
        a = b
        b = c
        c = d
    

def prueba():
        n= int(input("Ingrese el numero limite de fibonacci: "))
        print(tribonacci(n))
        pass
    
    
if __name__ == "__main__":
    prueba()

