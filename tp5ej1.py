################
# Agustin Montiveros - @agustin-montiveros
# UNRN Andina - Introducción a la Ingenieria en Computación
################


# Reemplazar por las funciones del ejercicio

def par_o_impar(numero):
    for i in range(numero): #aca ponemos un contador con el numero ingresado como limite
        mitad = numero / 2  #aca obtenemos la mitad del numero ingresado
        cero = mitad - int(mitad) #al pasar a entero descartamos la parte decimal, y hacemos la resta   
        if cero == 0:   #si la resta da 0, es par, si da otro numero es impar.
            return True
        else:
            return False
        
    
    


def prueba():
    numero = int(input("Insertar numero: "))
    resultado = par_o_impar(numero)
    print("El numero es par?: ", resultado)
        
        

if __name__ == "__main__":
    prueba()

