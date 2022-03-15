import collections

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'




def cesar_function(mensaje, corrimiento):
    print('Se hara un cesar al mensaje: ' + mensaje + '\ncon corrimiento: ' + str(corrimiento))
    mensaje = mensaje.lower()
    abc = collections.deque(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'])
    abclist=list(abc)
    abc.rotate(-(corrimiento))
    abcShiftedlist=list(abc)
    for indice, letra in enumerate(mensaje):
        if letra.isalpha():
            indiceReemplazo = abclist.index(letra)
            letrareemplazo = abcShiftedlist[indiceReemplazo]
            mensaje = mensaje[:indice] + letrareemplazo + mensaje[indice+1:]
    return mensaje


print('\n' + "Bienvenido" + '\n' + '\n' + "Este es el programa de encriptamiento Cesar" + '\n')
while True:
    while True:
        #main program
        while True:
            texto = input( '\n' + "Ingresa el mensaje a encriptar:" + '\n')
            textoVal = texto != '' and all(chr.isalpha() or chr.isspace() for chr in texto)
            if textoVal :
                break                
            else:
                print(f"{bcolors.WARNING}El valor a ingresar debe tener solo letras!{bcolors.ENDC}")

        while True:
            try:
                corrimiento = int(input('\n' + "Ingrese los digitos de corrimiento Cesar" + '\n'))
            except ValueError:
                print(f"{bcolors.WARNING}El valor a ingresar debe ser un numero entero!{bcolors.ENDC}")
                continue
            else:
                break
        mensaje = cesar_function(texto, corrimiento)
        print('\n' + "Su mensaje encriptado es: " + '\n' + mensaje)

        break



