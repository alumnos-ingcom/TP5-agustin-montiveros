################
# Agustin Montiveros - @agustin-montiveros
# UNRN Andina - Introducción a la Ingenieria en Computación
################


# Reemplazar por las funciones del ejercicio



def digitos(numero):
    a=str(numero)
    dig_lista = []
    for i in range(0,len(a)):
        dig_lista.append((numero//10**i)%10)

    return dig_lista

def factorial(n):  
    factor = 1
    for num in range(2, n + 1):
        factor = factor * num
    return factor



def factorion():
    limite = 1499999
    for numero in range(0,limite):
        digits_fact_sum =0
        digits_num = digitos(numero)
             
        for digit in digits_num:
            digits_fact_sum =digits_fact_sum+ factorial(digit)        

        if digits_fact_sum == numero:
            print("Factorion:", numero)

    print("No hay mas")
    
def prueba():
    factorion()
    
if __name__ == "__main__":
    prueba()
     
