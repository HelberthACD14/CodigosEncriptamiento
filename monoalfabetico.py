import collections
from email.policy import default

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

def clavecodificacion(abc, clave): 
    clavebase = []
    for i in clave:
        if i not in clavebase and i.isalpha():
            clavebase.append(i)
    alist = []
    xlong = len(clavebase)
    abcmatriz = []
    abcmatriz.append(list(clavebase))
    for letter in abc:
        if letter not in clavebase:
            alist.append(letter)
        if len(alist)==xlong:
            abcmatriz.append(list(alist))
            alist= []
    abcmatriz.append(list(alist))
    abccifrado =[]
    ylong = len(abcmatriz)

    for x in range(xlong):
        for y in range(ylong):
            try:
                abccifrado.append(abcmatriz[y][x]) 
            except:
                default
    
    return abccifrado



def monocifrado_function(mensaje, clave):
    print('Se hara un cifrado al mensaje: ' + mensaje + '\ncon clave: ' + clave)
    mensaje = mensaje.lower()
    abc = collections.deque(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'])
    abclist=list(abc)
    abccifrado = clavecodificacion(abclist, clave)
    for indice, letra in enumerate(mensaje):
        if letra.isalpha():
            indiceReemplazo = abclist.index(letra)
            letrareemplazo = abccifrado[indiceReemplazo]
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
            clave = input('\n' + "Ingrese la contraseña de codificacion:" + '\n')
            claveVal = texto != '' and all(chr.isalpha() or chr.isspace() for chr in clave)
            if claveVal :
                break                
            else:
                print(f"{bcolors.WARNING}El valor a ingresar debe tener solo letras!{bcolors.ENDC}")
        mensaje = monocifrado_function(texto, clave)
        print('\n' + "Su mensaje encriptado es: " + '\n' + mensaje)

        break