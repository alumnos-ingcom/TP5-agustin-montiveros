################
# Agustin Montiveros - @agustin-montiveros
# UNRN Andina - Introducción a la Ingenieria en Computación
################


# Reemplazar por las funciones del ejercicio
# 
def datos(lista):
    rango_p= int(input("Cuantos numeros desea promediar: "))
    limite_a = rango_p - rango_p
    limite_b = rango_p
    promedios = []
    for n in range(len(lista)):
        nueva_lista = lista[limite_a:limite_b]
        print("Estos son los datos seleccionados: ", nueva_lista)
        suma_lista =(sum(nueva_lista)) / len(nueva_lista)
        promedios.append(suma_lista)
        print("Lista de promedios acumulados: ", promedios)
        limite_a = limite_a+1
        limite_b = limite_b+1
        
    
def lista_a(total_numeros):
    numeros=[]
    for n in range(total_numeros):
        valor = int(input("Ingresar valor:"))
        numeros.append(valor)
    return numeros
        
    

def prueba():
    total_numeros= int(input("Cuantos valores quiere ingresar: "))
    lista_variable = lista_a(total_numeros)
    lista= lista_variable
    datos(lista)

if __name__ == "__main__":
    prueba()

