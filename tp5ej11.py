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
    print(nueva_lista)
    suma_lista= (sum(nueva_lista)) / len(nueva_lista)
    print("El promedio de los datos seleccionados es: ", suma_lista)
    
def lista_a(total_numeros):
    numeros=[]
    for n in range(total_numeros):
        valor = int(input("Ingresar valor:"))
        numeros.append(valor)
        print("La lista de valores ingresados es: ", numeros)
        
    

def prueba():
    total_numeros= int(input("Cuantos valores quiere ingresar: "))
    lista_a(total_numeros)
    lista=[]
    datos(lista)

if __name__ == "__main__":
    prueba()

