################
# Agustin Montiveros - @agustin-montiveros
# UNRN Andina - Introducción a la Ingenieria en Computación
################


# Reemplazar por las funciones del ejercic

def tbinario(numero):
    resto = []
    base = 2
    while numero // base > 2:
        resto_guardado= numero % 2
        resto.append(resto_guardado)
        numero = int(numero / 2)
    else:
        resto_guardado= numero % 2
        resto.append(resto_guardado)
        print(resto)
        if numero // base == 1:
            resto.append(1)
            print(resto)
        elif numero // base == 0:
            resto.append(0)
            print(resto)
            
    lista_final = list(reversed(resto))
    print("El numero ingresado en binario es :", lista_final)


def binario_a_numero(cadena):
    texto = cadena
    texto_c = list(texto)
    n = 0
    lista = []
    for i in range(len(texto)):
        resultado = pow(2, i)
        lista.append(resultado)
        
    lista_guardado = []
    for a in texto_c:
        total = int(int(lista[n]) * int(a))
        lista_guardado.append(total)
        total = sum(lista_guardado)
        n = n+1
        
    print("El numero binario a decimal es: ", total)
    
        
    


def prueba():
    numero = int(input("Ingresar numero a convertir: "))
    tbinario(numero)
    cadena = input("Ingresar numero binario: ")
    binario_a_numero(cadena)


if __name__ == "__main__":
    prueba()

