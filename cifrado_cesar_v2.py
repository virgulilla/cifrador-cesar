from typing import Callable, Tuple

ALFABETO = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ '
LONGITUD_ALFABETO = len(ALFABETO)

def desplazar(letra: str, dist: int) -> str:
    if letra in ALFABETO:
        nueva_pos = (ALFABETO.find(letra) + dist) % LONGITUD_ALFABETO
        return ALFABETO[nueva_pos]
    return letra

def creaCifrador(dist: int) -> Callable:
    return lambda mensaje: ''.join(desplazar(letra, dist) for letra in mensaje.upper())

def creaParCesar(dist: int) -> Tuple[Callable, Callable]:
    cifrar = creaCifrador(dist)
    descifrar = creaCifrador(-dist)
    return cifrar, descifrar 