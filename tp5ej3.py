################
# Agustin Montiveros - @agustin-montiveros
# UNRN Andina - Introducción a la Ingenieria en Computación
################


# Reemplazar por las funciones del ejercicio


def tribonacci(numero):  # n = numero para la explicacion
    lista = [1,1,1] #los primeros 3 numeros de la lista son 1, dado que segun la formula a(n): a(0)=a(1)=a(2)=1.
    if numero > 3: #Si el numero ingresado es mayor a 3, porque segun la formula a(n): a(0)=a(1)=a(2)=1. 
        for i in range(numero-3): #el "-3" es para que nos cuente los 3 primeros "1"
            valor_a= sum(lista[-3:]) #se suma los ultimos 3 numeros de la lista
            lista.append(valor_a) #se agrega el resultado de la suma de los 3 ultimos numeros de la lista a su ultimo lugar
        return lista
    else:
        return lista[:numero] #si numero no es mayor a 3, retornamos la lista original desde el principio hasta el numero ingresado
            

def prueba():
        numero= int(input("Ingrese el numero limite de fibonacci: "))
        resultado = tribonacci(numero)
        print(resultado)

    
    
if __name__ == "__main__":
    prueba()

