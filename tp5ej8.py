################
# Agustin Montiveros - @agustin-montiveros
# UNRN Andina - Introducción a la Ingenieria en Computación
################


# Reemplazar por las funciones del ejercicio




def codificar(texto):
    x= texto
    ajuste = int(input("Ingresar cantidad de posiciones a ajustar: "))
    for i in range(len(texto)):
        codificado = ord(texto[i])
        mensaje = print(codificado + ajuste)
    return mensaje

def descodificar(texto):
    mensaje = texto
    for i in range(len(mensaje)):
       desco= print(chr(ord(mensaje[i])))
    return desco
    
def prueba():
    texto = list(input("Ingresar mensaje: "))
    resultado = codificar(texto)

    
    resultadoDes = descodificar(texto)
    print(resultadoDes)
if __name__ == "__main__":
    prueba()