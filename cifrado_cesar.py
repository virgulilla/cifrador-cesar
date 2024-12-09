from typing import *

ALFABETO = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ '
LONGITUD_ALFABETO = len(ALFABETO)

def creaCifrador(dist:int)->Callable:
    def cifrar(mensaje:str,d = dist)->str:
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
        return mensaje_cifrado
    return cifrar

def creaParCesar(dist:int)->Tuple[Callable,Callable]:
    def cifrar(mensaje:str,d = dist):
        pasos = 0
        punto_inicio = 0
        mensaje_cifrado=''
        for letra in mensaje.upper():
            if letra in ALFABETO:

                punto_inicio = ALFABETO.find(letra)
                pasos = punto_inicio + d
                if pasos > LONGITUD_ALFABETO:
                    pasos -= LONGITUD_ALFABETO
                mensaje_cifrado += ALFABETO[pasos]
        return mensaje_cifrado
    def decifrar(mensaje:str,d = dist*-1):
        pasos = 0
        punto_inicio = 0
        mensaje_cifrado=''
        for letra in mensaje.upper():
            if letra in ALFABETO:

                punto_inicio = ALFABETO.find(letra)
                pasos = punto_inicio + d
                if pasos > LONGITUD_ALFABETO:
                    pasos -= LONGITUD_ALFABETO
                mensaje_cifrado += ALFABETO[pasos]
        return mensaje_cifrado

    return cifrar,decifrar