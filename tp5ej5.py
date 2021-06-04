################
# Agustin Montiveros - @agustin-montiveros
# UNRN Andina - Introducción a la Ingenieria en Computación
################


# Reemplazar por las funciones del ejercicio

def revertir_caracteres(texto):
    invertido = ""  #se crea una variable con un cadena string vacia
    for c in texto:  #por cada caracter en el texto introducido
        if c.isupper() == True:     #si el caracter es Mayuscula
            invertido = invertido + c.lower()  #se invierte ese caracter a Minuscula y se suma a la cadena string
        else:  #si el caracter no es Mayuscula, por ende es Minuscula
            invertido = invertido + c.upper()  #se invierte ese caracter a Mayuscula y se suma a la cadena string
    return invertido  

def prueba():
    texto = str(input("Ingresar texto: "))
    resultado = revertir_caracteres(texto)
    print(resultado)

if __name__ == "__main__":
    prueba()

