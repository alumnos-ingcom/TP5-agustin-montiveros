################
# Agustin Montiveros - @agustin-montiveros
# UNRN Andina - Introducción a la Ingenieria en Computación
################


# Reemplazar por las funciones del ejercicio

def parentesisParejos(texto):
    lista = []
    parentesis = {'{': '}', '(': ')', '[': ']'}
    
    for a in texto:
        if a in parentesis:
            lista.append(a)
        elif len(lista) == 0 or a != parentesis[lista.pop()]:
            return False       
    return len(lista) == 0

def prueba():
    texto = "()"
    resultado = parentesisParejos(texto)
    print("La cadena con parentesis '()' esta balanceada? ", resultado)
    texto = "[]"
    resultado = parentesisParejos(texto)
    print("La cadena con parentesis '[]' esta balanceada? ", resultado)
    texto = "[][]"
    resultado = parentesisParejos(texto)
    print("La cadena con parentesis '[][]' esta balanceada? ", resultado)
    texto = "[[][]]"
    resultado = parentesisParejos(texto)
    print("La cadena con parentesis '[[][]]' esta balanceada? ", resultado)
    texto = "]["
    resultado = parentesisParejos(texto)
    print("La cadena con parentesis '][' esta balanceada? ", resultado)
    texto = "][]["
    resultado = parentesisParejos(texto)
    print("La cadena con parentesis '][][' esta balanceada? ", resultado)
    texto = "[]][[]"
    resultado = parentesisParejos(texto)
    print("La cadena con parentesis '[]][[]' esta balanceada? ", resultado)
    texto = str(input("Ingresar cadena de texto con parentesis: "))
    resultado = parentesisParejos(texto)
    print("La cadena con parentesis esta balanceada? ", resultado)

if __name__ == "__main__":
    prueba()
