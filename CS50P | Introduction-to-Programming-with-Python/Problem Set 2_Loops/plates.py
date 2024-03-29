def main():

    plate =input("Plates: ")

    if is_valid(plate):

        print("Valid")

    else:

        print("Invalid") 

def is_valid(s):


#todas las placas deben de empezar con almenos 2 letras

    if s[0].isalpha() == False and s[1].isalpha == False:

    # 0 es el primer caracter, si este no es letra devuelve Falso

    # 1 es el segundo caracter, si este no es letra devuelve Falso

        return False

#pueden contener un max de 6 carac. y un min 2 carac.

    if len(s) < 2 or len(s) > 6: #len = obtiene el número de elementos de un caractere

    #si s es menor a 2 o s es mayor a 6

    #el resultado será False

        return False
#el primer número utilizado no puede ser "0"

    i = 0 #se crea nueva variable para ver el primer caracter

    # While es un bloque de código que se repite

    # mientra la condición sea verdadera

    #i tiene que ser menor a s:

    while i < len(s):

        #si s tiene como primer caracter a i y no es una letra

        #devuelve Falso

        if s[i].isalpha() == False:

            #si s tiene como primer caracter a 0, devuelve False

            if s[i] == "0":

                return False

            else:

                #rompe el bucle si la condición es Verdadera

                break

        #si no lo es seguimos intentando

        i += 1

#no se pueden usar números en medio de una placa

#ejem: AAA222 si, AAA22A no

    # for imprime todas las letras de la cadena s

    # range convierte a s en una secuencia de números , "Hola" =0,1,2,3

    #len = obtiene el número de elementos de s , "Hola" = 4

    for i in range(len(s)):

        #si s[i] encuentra un digito devuelve True y continua con

        # la siguiente linea de codigo

        if s[i].isdigit():

            #despues de cumplir la linea 11

            #si s[i:] encuentra la posición del primer digito

            #y siguen siendo digitos, retornara Falso

            # s[i:] no son digitos

            if not s[i:].isdigit():

                return False

#no se perminten puntos, espacios ni signos de puntuación

#no se permite : ".", " ", "?"," "

    #for imprime todas las letras de la cadena

    #imprime uno por uno

    # imprime los caracter s y verifica si contiene algo de c

    for c in s:

        # si c contiene ., " ", ?, !, devuelve falso

        if c in [".", " ","?","!"]:

            return False

    #si no se cumple ninguna de las condiciones dadas

    #Retorna verdadero

    return True

main()
