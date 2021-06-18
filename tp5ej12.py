################
# Agustin Montiveros - @agustin-montiveros
# UNRN Andina - Introducción a la Ingenieria en Computación
################


# Reemplazar por las funciones del ejercicio

def listas(lista_a, lista_b):
    num = 0
    if len(lista_a) > len(lista_b):
        print("No son iguales, la primera lista es mas grande")
    elif len(lista_a) < len(lista_b):
        print("No son iguales, la segunda lista es mas grande")
    elif len(lista_a) == len(lista_b):

        for n in range(len(lista_a)):
            for a in range(len(lista_b)):
                
                if lista_a[n] == lista_b[a]:
                    num = num + 1
                    if num == len(lista_b):
                        print(True)
    
    
                    
                    




def prueba():
    lista_aa= input("Introducir primera lista: ")
    lista_bb= input("Introducir segunda lista: ")
    lista_a = list(lista_aa)
    lista_b = list(lista_bb)
    listas(lista_a, lista_b)
    

if __name__ == "__main__":
    prueba()

