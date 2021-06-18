################
# Agustin Montiveros - @agustin-montiveros
# UNRN Andina - Introducción a la Ingenieria en Computación
################


# Reemplazar por las funciones del ejercicio
# 
def datos(lista):
    limite_a = int(input("Ingresar la posicion del primer dato que quiere promediar: "))
    limite_b = int(input("Ingresar la posicion del ultimo dato que quiere promediar: "))
    nueva_lista = lista[limite_a:limite_b]
    rango = limite_b - limite_a
    print("Estos son los datos seleccionados: ", nueva_lista)
    while len(nueva_lista) == rango:
        suma_lista= (sum(nueva_lista)) / len(nueva_lista)
        imprimir = print("El promedio de los datos seleccionados es: ", suma_lista)
        return imprimir
    
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

