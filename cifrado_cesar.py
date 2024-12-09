from typing import *

ALFABETO = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ '
LONGITUD_ALFABETO = len(ALFABETO)

def cifrar(mensaje:str,d:int)->str:
    pasos = 0
    punto_inicio = 0
    mensaje_cifrado=''
    for letra in mensaje.upper():
        if letra in ALFABETO:

            punto_inicio = ALFABETO.find(letra)
            pasos = punto_inicio + d
            # print(pasos)
            # while pasos > LONGITUD_ALFABETO:
            #     pasos -= LONGITUD_ALFABETO
            pasos = pasos % LONGITUD_ALFABETO
            mensaje_cifrado += ALFABETO[pasos]
        else:
            mensaje_cifrado += letra    
    return mensaje_cifrado

def creaCifrador(dist:int)->Callable:
    def cifrador(mensaje: str) -> str:
        return cifrar(mensaje, dist)
    return cifrador

def creaParCesar(dist:int)->Tuple[Callable,Callable]:
    def cifrador(mensaje: str) -> str:
        return cifrar(mensaje, dist)
    
    def descifrador(mensaje: str) -> str:
        return cifrar(mensaje, -dist)

    return cifrador, descifrador